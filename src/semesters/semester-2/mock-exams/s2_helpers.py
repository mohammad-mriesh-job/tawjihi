"""Shared helpers for the semester-2 mock papers (s2_papers_*.py): lesson ids, solvers, option builders,
figure drawers and paper notes."""
from qb import *
import numpy as np

R = Rational
P = pi
U5 = {i: f'u5-l{i}' for i in range(1, 7)}
U6 = {1: 'u6-l1', 2: 'u6-l2', 3: 'u6-l3'}
U7 = {1: 'u7-l1', 2: 'u7-l2'}
ig = integrate
yp = Symbol('yp')
Cc = Symbol('C')

# ------------------------------------------------------------------ helpers (integration)
def A(tex, F_):
    assert tex.rstrip().endswith('+C'), tex
    return O(tex, F_, 'anti')
def ode_ok(Yx, rhs, x0, y0):
    return same(diff(Yx, x) - rhs.subs(y, Yx), 0) and same(Yx.subs(x, x0), y0)
def ode_rel_ok(Fxy, rhs, pt=None):
    """implicit (possibly general, with C) solution F(x,y)=0 of y'=rhs"""
    dydx = -diff(Fxy, x)/diff(Fxy, y)
    if not same(dydx - rhs, 0):
        return False
    return pt is None or same(Fxy.subs({x: pt[0], y: pt[1]}), 0)

def region(f_, g_, a_, b_, xlim, ylim, labels=()):
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        xs = np.linspace(xlim[0], xlim[1], 400)
        ff = lambdify(x, f_, 'numpy'); gg = lambdify(x, g_, 'numpy')
        with np.errstate(all='ignore'):
            ax.plot(xs, ff(xs) + 0*xs, color='#1f5fbf', lw=1.8)
            if g_ != 0:
                ax.plot(xs, gg(xs) + 0*xs, color='#d04a1a', lw=1.8)
            xr = np.linspace(float(a_), float(b_), 200)
            ax.fill_between(xr, ff(xr) + 0*xr, gg(xr) + 0*xr, color='#9cc3ef', alpha=0.85)
        for (tx_, ty_, s_, col) in labels:
            ax.text(tx_, ty_, s_, color=col, fontsize=11)
    return draw

def vt_graph(pts, tmax, vmin, vmax):
    def draw(fig, ax):
        axes_style(ax, (-0.4, tmax + 0.8), (vmin - 0.8, vmax + 1), xlabel=r't\,(\mathrm{s})', ylabel=r'v\,(\mathrm{m/s})', grid=True)
        ax.set_xticks(range(0, tmax + 1)); ax.set_yticks(range(vmin, vmax + 1))
        tx_, vy_ = zip(*pts)
        ax.plot(tx_, vy_, color='#1f5fbf', lw=2)
    return draw
def pw_integral(pts, a_, b_, absolute=False):
    tt = symbols('tt')
    tot = 0
    for (t1, v1), (t2, v2) in zip(pts, pts[1:]):
        seg = R(v1) + R(v2 - v1, t2 - t1)*(tt - t1)
        lo, hi = max(a_, t1), min(b_, t2)
        if lo < hi:
            tot += ig(Abs(seg) if absolute else seg, (tt, lo, hi))
    return tot

# ------------------------------------------------------------------ helpers (vectors)
V = lambda *c_: Matrix(c_)
T3 = lambda m_: Tuple(*list(m_))
def vt(*c_): return r'\langle ' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + r'\rangle'
def vec_opt(*c_): return O(vt(*c_), Tuple(*[sympify(q_) for q_ in c_]), 'vec')
def pt_opt(*c_): return O('(' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + ')', Tuple(*[sympify(q_) for q_ in c_]), 'tuple')
def line_opt(p_, d_): return O(r'\vec{\mathbf{r}}=' + vt(*p_) + '+t' + vt(*d_), Tuple(Tuple(*p_), Tuple(*d_)), 'line')
def par(u_, v_): return Matrix(u_).cross(Matrix(v_)) == zeros(3, 1)
def on_line(pt_, ln): return par(Matrix(pt_) - Matrix(ln[0]), Matrix(ln[1]))
def classify(a1, d1, a2, d2):
    a1, d1, a2, d2 = map(Matrix, (a1, d1, a2, d2))
    if par(d1, d2):
        return 'coincident' if par(a2 - a1, d1) else 'parallel'
    s_, t_ = symbols('s_ t_')
    return 'intersect' if solve(list(a1 + t_*d1 - a2 - s_*d2), [t_, s_], dict=True) else 'skew'
def inter(a1, d1, a2, d2):
    a1, d1, a2, d2 = map(Matrix, (a1, d1, a2, d2))
    s_, t_ = symbols('s_ t_')
    sol = solve(list(a1 + t_*d1 - a2 - s_*d2), [t_, s_], dict=True)[0]
    return T3(a1 + sol[t_]*d1)
REL = [('متوازيان', 'parallel'), ('متقاطعان', 'intersect'), ('متخالفان', 'skew'), ('منطبقان', 'coincident')]
def rel_opts(first):
    order = [r_ for r_ in REL if r_[1] == first] + [r_ for r_ in REL if r_[1] != first]
    return [T(t_, v_) for t_, v_ in order]
def ang(u_, v_):
    u_, v_ = Matrix(u_), Matrix(v_)
    return acos(u_.dot(v_)/(u_.norm()*v_.norm()))
va, vb, vc = symbols('a b c')
def vtex(expr):
    expr = expand(expr); out = ''
    for sym_, name in ((va, 'a'), (vb, 'b'), (vc, 'c')):
        cf = expr.coeff(sym_)
        if cf == 0:
            continue
        sign = '-' if cf < 0 else ('+' if out else '')
        mag = abs(cf)
        out += f'{sign}{"" if mag == 1 else latex(mag)}' + r'\vec{\mathbf{' + name + '}}'
    return out
def vopt(expr): return O(vtex(expr), expr)

def fig_box(dx, dy, dz):
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        proj = lambda x_, y_, z_: (y_ - 0.55*x_, z_ - 0.35*x_)
        vtx = {'O': (0, 0, 0), 'P': (dx, 0, 0), 'Q': (dx, dy, 0), 'R': (0, dy, 0), 'S': (0, 0, dz), 'T': (dx, 0, dz), 'U': (dx, dy, dz), 'V': (0, dy, dz)}
        for e in ['OP', 'PQ', 'QR', 'RO', 'OS', 'PT', 'QU', 'RV', 'ST', 'TU', 'UV', 'VS']:
            a1, a2 = proj(*vtx[e[0]]), proj(*vtx[e[1]])
            ax.plot([a1[0], a2[0]], [a1[1], a2[1]], ls='--' if e in ('OP', 'RO', 'OS') else '-', color='#555', lw=1.3)
        for start, end, lab in [((dx, 0, 0), (dx*1.6, 0, 0), 'x'), ((0, dy, 0), (0, dy*1.35, 0), 'y'), ((0, 0, dz), (0, 0, dz*1.5), 'z')]:
            a1, a2 = proj(*start), proj(*end)
            ax.plot([a1[0], a2[0]], [a1[1], a2[1]], color='#1f5fbf', lw=1.2)
            ax.annotate('', xy=a2, xytext=(a1[0] + 0.8*(a2[0] - a1[0]), a1[1] + 0.8*(a2[1] - a1[1])),
                        arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.2), annotation_clip=False)
            ax.text(a2[0] + 0.1, a2[1] + 0.1, f'${lab}$', color='#1f5fbf', fontsize=12)
            ax.plot([a2[0] - 0.3, a2[0] + 0.5], [a2[1] - 0.3, a2[1] + 0.5], alpha=0)
        for k_, p_ in vtx.items():
            q_ = proj(*p_); ax.plot(*q_, 'o', color='#222', ms=3); ax.text(q_[0] + 0.12, q_[1] + 0.12, f'${k_}$', fontsize=12)
        ax.autoscale(); ax.margins(0.08)
    return draw

def fig_poly(points, edges, arrows, labels, extra_dashed=()):
    """generic vector diagram: points {name:(x,y)}, edges [(A,B)], arrows [(A,B,label,(dx,dy))]"""
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        for a1, b1 in edges:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=1.6)
        for a1, b1 in extra_dashed:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#888', lw=1.2, ls='--')
        for a1, b1, lab, off in arrows:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=1.6)
            ax.annotate('', xy=(x1 + 0.6*(x2 - x1), y1 + 0.6*(y2 - y1)), xytext=(x1 + 0.45*(x2 - x1), y1 + 0.45*(y2 - y1)), arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
            ax.text((x1 + x2)/2 + off[0], (y1 + y2)/2 + off[1], lab, fontsize=12, color='#1f5fbf')
        for nm, (px, py) in points.items():
            ax.plot(px, py, 'o', color='#222', ms=3.5)
            d_ = labels.get(nm, (0.12, 0.12))
            ax.text(px + d_[0], py + d_[1], f'${nm}$', fontsize=13)
        ax.margins(0.1)
    return draw

# ------------------------------------------------------------------ helpers (statistics)
def Phi4(z0):
    z0 = nsimplify(z0)
    return R(str(round(float(N((1 + erf(z0/sqrt(2)))/2, 30)), 4)))
def Ph(z0):
    z0 = nsimplify(z0)
    return Phi4(z0) if z0 >= 0 else 1 - Phi4(-z0)
def ztable_lead(items, *zs):
    zs = sorted({nsimplify(q_) for q_ in zs})
    head = ' & '.join(f'{float(q_):g}' for q_ in zs)
    row = ' & '.join(f'{float(Phi4(q_)):.4f}' for q_ in zs)
    nums = ' و '.join(f'({i_})' for i_ in items)
    return (rf"❖ يمكنك الاستفادة من الجدول الآتي الذي يُمثّل بعضًا من قيم جدول التوزيع الطبيعي المعياري للإجابة عن الفقرات {nums} الآتية:"
            r"$$\begin{array}{|c|" + 'c|'*len(zs) + r"}\hline z & " + head + r"\\ \hline P(Z<z) & " + row + r"\\ \hline\end{array}$$")
def binom(n_, p_, k_): return binomial(n_, k_)*p_**k_*(1-p_)**(n_-k_)
def geo(p_, k_): return (1-p_)**(k_-1)*p_
def r4(v_): return R(str(round(float(v_), 4)))
def bell(intervals, ticks):
    def draw(fig, ax):
        xs = np.linspace(-3.6, 3.6, 400); f_ = lambda u_: np.exp(-u_**2/2)/np.sqrt(2*np.pi)
        ax.plot(xs, f_(xs), color='#1f5fbf', lw=1.8)
        for a_, b_ in intervals:
            xr = np.linspace(a_, b_, 200); ax.fill_between(xr, f_(xr), color='#9cc3ef', alpha=0.9)
        for xv in ticks:
            ax.plot([xv, xv], [0, f_(xv)], color='#1f5fbf', lw=1, ls='--')
        ax.axhline(0, color='black', lw=0.8); ax.set_yticks([])
        ax.set_xticks(ticks); ax.set_xticklabels([f'{q_:g}' for q_ in ticks])
        for side in ('top', 'right', 'left'):
            ax.spines[side].set_visible(False)
        ax.text(3.4, -0.05, '$Z$', fontsize=12); ax.set_ylim(-0.02, 0.45)
    return draw
def shared(stem, a_, b_): return rf"❖ {stem} ، فاعتمد ذلك للإجابة عن الفقرتين ({a_}) و ({b_}) الآتيتين:"

# ------------------------------------------------------------------ helpers added for papers 6-10
def ztable_note(items, *zs):
    """the ❖ table note shared by the normal-distribution items (2026 #48-50), with the dual form for two items"""
    zs = sorted({nsimplify(q_) for q_ in zs})
    head = ' & '.join(f'{float(q_):g}' for q_ in zs)
    row = ' & '.join(f'{float(Phi4(q_)):.4f}' for q_ in zs)
    if len(items) == 2:
        target = f'الفقرتين ({items[0]}) و ({items[1]}) الآتيتين'
    else:
        target = 'الفقرات ' + ' و '.join(f'({i_})' for i_ in items) + ' الآتية'
    return (rf"❖ يمكنك الاستفادة من الجدول الآتي الذي يُمثّل بعضًا من قيم جدول التوزيع الطبيعي المعياري للإجابة عن {target}:"
            r"$$\begin{array}{|c|" + 'c|'*len(zs) + r"}\hline z & " + head + r"\\ \hline P(Z<z) & " + row + r"\\ \hline\end{array}$$")
