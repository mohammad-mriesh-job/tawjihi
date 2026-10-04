"""Question-bank framework (v2).

Every question is verified three ways before it is written to the app:
  1. truth   - the answer is computed independently with sympy and must match the
               value of the correct option ONLY (no other option may match).
  2. options - the LaTeX shown to the student for each option is parsed back with
               sympy and must equal the value that was checked in (1). A typo in an
               option's text therefore fails the build.
  3. stems   - formulas inside the question text are written with M(tex, expr): the
               displayed LaTeX is parsed and must equal the expression the truth was
               computed from.
Antiderivative options ("... + C") are checked by differentiating.
Descriptive (Arabic text) options are allowed only with an explicit `manual` reason.
The correct option is always written first; the app shuffles options at runtime.
"""
import json, os, random, re as _re
from sympy import *
from sympy.parsing.latex import parse_latex

x, y, t, z, k, a, b, c, u, n, m, p, s, v, w = symbols('x y t z k a b c u n m p s v w')
th = Symbol('theta')
HERE = os.path.dirname(os.path.abspath(__file__))
TS_DIR = os.path.join(HERE, '..', 'src', 'data', 'units')
FIG_DIR = os.path.join(HERE, '..', 'public', 'fig')


# ----------------------------------------------------------------------------- equality
def same(p_, q_):
    seq = (FiniteSet, Tuple, tuple, list)
    if isinstance(p_, seq) or isinstance(q_, seq):
        if not (isinstance(p_, seq) and isinstance(q_, seq)):
            return False
        if isinstance(p_, FiniteSet) or isinstance(q_, FiniteSet):
            pl, ql = list(FiniteSet(*p_)), list(FiniteSet(*q_))
            if len(pl) != len(ql):
                return False
            used = set()
            for e in pl:
                hit = next((j for j, f in enumerate(ql) if j not in used and same(e, f)), None)
                if hit is None:
                    return False
                used.add(hit)
            return True
        pl, ql = list(p_), list(q_)
        return len(pl) == len(ql) and all(same(i, j) for i, j in zip(pl, ql))
    if isinstance(p_, str) or isinstance(q_, str):
        return p_ == q_
    d = sympify(p_) - sympify(q_)
    fs = sorted(d.free_symbols, key=str)
    if not fs:
        return abs(complex(N(d, 40))) < 1e-10
    rnd = random.Random(7)
    good = 0
    for _ in range(40):
        sub = {sy: Rational(rnd.randint(13, 89), 41) for sy in fs}
        try:
            val = complex(N(d.subs(sub), 40))
        except (TypeError, ValueError, ZeroDivisionError):
            continue
        if val != val:  # nan
            continue
        if abs(val) > 1e-8:
            return False
        good += 1
        if good >= 6:
            return True
    return good >= 3


# ----------------------------------------------------------------------------- LaTeX parsing
_SYM = {'e': E, 'pi': pi, 'i': I}


def _prep(s):
    s = s.replace('$', '').strip()
    s = s.replace(r'\dfrac', r'\frac').replace(r'\tfrac', r'\frac').replace(r'\displaystyle', '')
    s = _re.sub(r'\\text\{[^}]*\}', '', s)
    s = s.replace(r'\%', '')
    s = s.replace(r'\,', ' ').replace(r'\ ', ' ').replace(r'\!', '').replace(r'\;', ' ')
    s = s.replace(r'\left', '').replace(r'\right', '')
    s = _re.sub(r'\\ln\s*\|([^|]+)\|', r'\\ln(\1)', s)       # ln|u| -> ln(u)  (same derivative)
    s = _re.sub(r'(?<![a-zA-Z\\])([xyzt])\(', r'\1\\cdot(', s)   # x(x-1): product, not a function call
    s = _re.sub(r'\\pi\s*\(', r'\\pi\\cdot(', s)                   # \pi(e-1): product
    s = _re.sub(r'\\vec\{\\mathbf\{([a-z])\}\}', r'\1', s)     # vector symbols a, b, c -> scalars stand-ins
    s = s.replace(r'\hat{i}', 'IHAT').replace(r'\hat{j}', 'JHAT').replace(r'\hat{k}', 'KHAT')
    return s.strip()


def parse_tex(s, sym=None):
    s = _prep(s)
    e = parse_latex(s)
    rep = dict(_SYM)
    if sym:
        rep.update(sym)
    e = e.xreplace({Symbol(k_): v_ for k_, v_ in rep.items()})
    return e


def _split_top(s, sep=','):
    out, depth, cur = [], 0, ''
    for ch in s:
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return [o.strip() for o in out]


# ----------------------------------------------------------------------------- options
class O:
    """An option: LaTeX (without $) and the sympy value it denotes.
    kind: 'expr' (default), 'anti' (+C antiderivative), 'tuple', 'set', 'vec', 'text'."""

    def __init__(self, tex, val, kind=None, sym=None, units=''):
        self.tex, self.val, self.sym, self.units = tex, val, sym, units
        if kind is None:
            kind = 'anti' if _re.search(r'\+\s*C\s*$', tex) else 'expr'
        self.kind = kind

    def display(self):
        if self.kind == 'text':
            return self.tex
        u_ = (r'\ ' + _re.sub(r'([A-Za-z/]+)', r'\\text{\1}', self.units)) if self.units else ''
        return f'${self.tex}{u_}$'

    def parsed(self):
        s = self.tex
        if self.kind == 'anti':
            return diff(parse_tex(_re.sub(r'\+\s*C\s*$', '', s), self.sym), x)
        if self.kind == 'tuple':
            inner = _prep(s)
            inner = inner[inner.index('(') + 1: inner.rindex(')')]
            return Tuple(*[parse_tex(q_, self.sym) for q_ in _split_top(inner)])
        if self.kind == 'vec':
            inner = _prep(s[s.index(r'\langle') + 7: s.rindex(r'\rangle')])
            return Tuple(*[parse_tex(q_, self.sym) for q_ in _split_top(inner)])
        if self.kind == 'set':  # "x=a,\ x=b"  or  "a,\ b"  or "\pm a"
            st = _prep(s)
            if st.startswith(r'\pm'):
                e = parse_tex(st[3:], self.sym)
                return FiniteSet(e, -e)
            if st.startswith(r'\{') and st.endswith(r'\}'):
                st = st[2:-2]
            parts = _split_top(st)
            vals = [parse_tex(q_.split('=')[-1], self.sym) for q_ in parts]
            return FiniteSet(*vals)
        if self.kind == 'line':  # r = <p> + t<d>  ->  Tuple(Tuple(p), Tuple(d))
            grp = _re.findall(r'\\langle(.*?)\\rangle', s)
            assert len(grp) == 2, s
            return Tuple(*[Tuple(*[parse_tex(q_, self.sym) for q_ in _split_top(_prep(g_))]) for g_ in grp])
        if self.kind == 'tset':  # "(a,b),\ (c,d)" -> FiniteSet of Tuples
            parts = _split_top(_prep(s))
            return FiniteSet(*[Tuple(*[parse_tex(q_, self.sym) for q_ in _split_top(pt.strip()[1:-1])]) for pt in parts])
        if self.kind == 'pairs':  # "A=2,\ B=3" -> Tuple(2,3)
            parts = _split_top(_prep(s))
            return Tuple(*[parse_tex(q_.split('=')[-1], self.sym) for q_ in parts])
        if self.kind == 'eq':  # "y = expr"
            return parse_tex(s.split('=', 1)[1], self.sym)
        if self.kind == 'rel':  # "L = R"  ->  L - R
            l_, r_ = s.split('=', 1)
            return parse_tex(l_, self.sym) - parse_tex(r_, self.sym)
        return parse_tex(s, self.sym)


def T(text, val=None):
    """Descriptive option (Arabic text, may embed $math$). Not parsed."""
    return O(text, val, kind='text')


def D(dec, units=''):
    """Decimal option shown exactly as written, e.g. D('0.8413')."""
    return O(dec, Rational(dec), units=units)


def M(tex, expr, sym=None):
    """Formula for a question stem: returns the LaTeX after asserting it parses to expr."""
    got = parse_tex(tex, sym)
    if not same(got, expr):
        raise AssertionError(f'stem formula mismatch: {tex!r} parsed as {got}, expected {expr}')
    return tex


# ----------------------------------------------------------------------------- figures
def figure(qid, draw, w_=4.2, h_=3.2):
    """Render a matplotlib figure to public/fig/<qid>.svg and return its public path."""
    import matplotlib
    matplotlib.use('svg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 11, 'mathtext.fontset': 'cm', 'svg.fonttype': 'path'})
    os.makedirs(FIG_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(w_, h_))
    draw(fig, ax)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, f'{qid}.svg'), transparent=False, facecolor='white')
    plt.close(fig)
    return f'fig/{qid}.svg'


def axes_style(ax, xlim, ylim, xlabel='x', ylabel='y', grid=False, ticks=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
    ax.plot(1, 0, '>k', transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, '^k', transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.set_xlabel(f'${xlabel}$', loc='right'); ax.set_ylabel(f'${ylabel}$', loc='top', rotation=0)
    if grid:
        ax.grid(True, color='#dddddd', lw=0.6)
    if not ticks:
        ax.set_xticks([]); ax.set_yticks([])


# ----------------------------------------------------------------------------- questions
class Q:
    def __init__(self, id, lesson, diff, text, opts, solution, truth=None, manual=None, figure=None, tag=None, lead=None, group=None):
        self.id, self.lesson, self.diff, self.text = id, lesson, diff, text
        self.opts, self.solution, self.truth, self.manual, self.figure = opts, solution, truth, manual, figure
        self.tag, self.lead, self.group = tag, lead, group


def verify(q):
    assert q.diff in ('easy', 'medium', 'hard'), q.id
    assert len(q.opts) == 4, f'{q.id}: need 4 options'
    shown = [o.display() for o in q.opts]
    assert len(set(shown)) == 4, f'{q.id}: duplicate option text'
    # (2) displayed option text must denote the stated value
    for j, o in enumerate(q.opts):
        if o.kind == 'text':
            continue
        try:
            got = o.parsed()
        except Exception as err:
            raise AssertionError(f'{q.id} option {j} {o.tex!r}: cannot parse ({type(err).__name__}: {err})')
        target = diff(o.val, x) if o.kind == 'anti' else o.val
        if not same(got, target):
            raise AssertionError(f'{q.id} option {j} {o.tex!r}: displays {got} but value is {target}')
    # (1) truth must match the first option only
    if q.truth is None:
        assert q.manual, f'{q.id}: no computed truth and no manual justification'
        return 'manual'
    if callable(q.truth) and q.truth.__code__.co_argcount == 1:
        tr = q.truth([o.val for o in q.opts])     # property check over the options' own values
    else:
        tr = q.truth() if callable(q.truth) else q.truth
    if getattr(q, 'index_truth', False):
        assert tr == 0, f'{q.id}: index truth says option {tr}'
        return 'checked'
    vals = []
    for o in q.opts:
        if o.kind == 'anti':
            vals.append(diff(o.val, x))
        else:
            vals.append(o.val)
    ok = [vv is not None and same(tr, vv) for vv in vals]
    if not ok[0]:
        raise AssertionError(f'{q.id}: truth {tr} does not match the correct option {vals[0]}')
    if sum(ok) != 1:
        raise AssertionError(f'{q.id}: truth {tr} matches several options {ok}')
    return 'checked'


def only(vals, ok):
    """index of the single value satisfying ok(v) (for IndexQ truths)."""
    hits = [i for i, v_ in enumerate(vals) if ok(v_)]
    assert len(hits) == 1, f'property holds for options {hits}'
    return hits[0]


def IndexQ(*args, **kw):
    """Question whose truth is computed as the index of the option satisfying a property."""
    q_ = Q(*args, **kw)
    q_.index_truth = True
    return q_


def build(meta, exams, fname):
    stats = {'checked': 0, 'manual': 0}
    ids, out = set(), []
    lesson_ids = {l['id'] for l in meta['lessons']}
    for ex in exams:
        qs = []
        for q in ex['questions']:
            assert q.id not in ids, q.id
            assert q.lesson in lesson_ids, q.id
            ids.add(q.id)
            stats[verify(q)] += 1
            d_ = dict(id=q.id, lesson=q.lesson, difficulty=q.diff, text=q.text,
                      options=[o.display() for o in q.opts], answer=0, solution=q.solution)
            if q.figure:
                d_['figure'] = q.figure
            qs.append(d_)
        out.append(dict(id=ex['id'], title=ex['title'], questions=qs))
    body = json.dumps(dict(meta, exams=out), ensure_ascii=False, indent=2)
    ts = ("// Generated by question-bank/" + fname + ".py (verified). Do not edit by hand.\n"
          "import type { Unit } from '../types';\n\n"
          f"const unit: Unit = {body};\n\nexport default unit;\n")
    open(os.path.join(TS_DIR, f'{fname}.ts'), 'w').write(ts)
    print(f"{fname}: {len(ids)} questions, {stats['checked']} computed+parsed, {stats['manual']} manual")


# ----------------------------------------------------------------------------- helpers
def numsols(expr, lo, hi, closed_lo=True, closed_hi=False, var=None):
    """All real roots of expr on the interval via dense sampling + refinement (floats)."""
    import math
    var = var or sorted(expr.free_symbols, key=str)[0]
    f = lambdify(var, expr, 'math')
    lo, hi = float(lo), float(hi)
    N_ = 60000
    xs = [lo + (hi - lo) * i / N_ for i in range(N_ + 1)]

    def val(v_):
        try:
            return f(v_)
        except (ZeroDivisionError, ValueError, OverflowError):
            return float('nan')
    ys = [val(v_) for v_ in xs]
    cands = []
    for i in range(N_):
        y0, y1 = ys[i], ys[i + 1]
        if math.isnan(y0) or math.isnan(y1):
            continue
        if y0 == 0:
            cands.append(xs[i])
        elif y0 * y1 < 0 and abs(y0 - y1) < 1e3:
            cands.append((xs[i] + xs[i + 1]) / 2)
    for i in range(1, N_):
        a0, a1, a2 = abs(ys[i - 1]), abs(ys[i]), abs(ys[i + 1])
        if a1 <= a0 and a1 <= a2 and a1 < 1e-3:
            cands.append(xs[i])
    if not math.isnan(ys[-1]) and abs(ys[-1]) < 1e-12:
        cands.append(hi)
    roots = []
    for c0 in cands:
        try:
            r = float(nsolve(expr, var, c0, tol=1e-25, prec=40, verify=False))
        except Exception:
            continue
        if abs(val(r)) > 1e-9:
            continue
        inside = (r > lo + 1e-9 or (closed_lo and abs(r - lo) < 1e-9)) and (r < hi - 1e-9 or (closed_hi and abs(r - hi) < 1e-9))
        if inside and all(abs(r - q_) > 1e-6 for q_ in roots):
            roots.append(r)
    return FiniteSet(*[nsimplify(r_, [pi], tolerance=1e-9) for r_ in sorted(roots)])


def F(tpl, *items):
    """Question stem with checked formulas: «0», «1», ... are replaced by the LaTeX of each
    (tex, expr[, sym]) item after asserting the LaTeX parses to expr."""
    for i, it in enumerate(items):
        tex, expr = it[0], it[1]
        sym = it[2] if len(it) > 2 else None
        M(tex, expr, sym)
        assert f'«{i}»' in tpl, f'placeholder «{i}» missing'
        tpl = tpl.replace(f'«{i}»', tex)
    return tpl


MOCK_DIR = os.path.join(HERE, '..', 'src', 'data', 'mocks')


def build_mock(meta, exams, fname, seed=2026):
    """Mock papers: options keep a FIXED order (like a printed paper) with the correct answer
    placed so that a/b/c/d are used equally often in every paper."""
    os.makedirs(MOCK_DIR, exist_ok=True)
    stats = {'checked': 0, 'manual': 0}
    ids, out = set(), []
    rnd = random.Random(seed)
    for ex in exams:
        qs = ex['questions']
        targets = ([0, 1, 2, 3] * ((len(qs) + 3) // 4))[:len(qs)]
        rnd.shuffle(targets)
        # avoid long runs of the same letter
        for i in range(2, len(targets)):
            if targets[i] == targets[i - 1] == targets[i - 2]:
                j = next(j for j in range(len(targets)) if targets[j] != targets[i] and j not in (i - 1, i - 2))
                targets[i], targets[j] = targets[j], targets[i]
        items = []
        for q, tgt in zip(qs, targets):
            assert q.id not in ids, q.id
            assert q.tag, f'{q.id}: mock questions need a tag (pattern)'
            ids.add(q.id)
            stats[verify(q)] += 1
            shown = [o.display() for o in q.opts]
            order = shown[1:]
            order.insert(tgt, shown[0])
            d_ = dict(id=q.id, lesson=q.lesson, difficulty=q.diff, tag=q.tag, text=q.text,
                      options=order, answer=tgt, solution=q.solution)
            if q.figure:
                d_['figure'] = q.figure
            if q.lead:
                d_['lead'] = q.lead
            if getattr(q, 'pattern', None):
                d_['pattern'] = q.pattern
            if getattr(q, 'group', None):
                d_['group'] = q.group
            items.append(d_)
        counts = [sum(1 for it in items if it['answer'] == k_) for k_ in range(4)]
        out.append(dict(ex, questions=items, answerSpread=counts))
    body = json.dumps(dict(meta, exams=out), ensure_ascii=False, indent=2)
    ts = ("// Generated by question-bank/mock_" + fname + ".py (verified). Do not edit by hand.\n"
          "import type { MockSet } from '../types';\n\n"
          f"const mocks: MockSet = {body};\n\nexport default mocks;\n")
    open(os.path.join(MOCK_DIR, f'{fname}.ts'), 'w').write(ts)
    print(f"{fname}: {len(ids)} questions in {len(exams)} papers, {stats['checked']} computed+parsed, {stats['manual']} manual")
