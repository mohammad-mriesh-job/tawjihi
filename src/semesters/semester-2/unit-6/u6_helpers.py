"""Shared helpers for the unit-6 generators (u6.py and u6_exams_4_8.py)."""
from qb import *

R = Rational
P = pi
V = lambda *c_: Matrix(c_)
T3 = lambda m_: Tuple(*list(m_))
def vt(*c_):
    return r'\langle ' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + r'\rangle'
def vec_opt(*c_):
    return O(vt(*c_), Tuple(*[sympify(q_) for q_ in c_]), 'vec')
def pt_opt(*c_):
    return O('(' + ',\,'.join(latex(sympify(q_)) for q_ in c_) + ')', Tuple(*[sympify(q_) for q_ in c_]), 'tuple')
def line_opt(p_, d_):
    return O(r'\vec{\mathbf{r}}=' + vt(*p_) + '+t' + vt(*d_), Tuple(Tuple(*p_), Tuple(*d_)), 'line')
def par(u_, v_): return Matrix(u_).cross(Matrix(v_)) == zeros(3, 1)
def on_line(pt_, ln):
    p0, d0 = Matrix(ln[0]), Matrix(ln[1])
    return par(Matrix(pt_) - p0, d0)
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
va, vb, vc = symbols('a b c')     # stand-ins for the vectors a, b, c in ratio problems
def vtex(expr):
    """LaTeX for a combination of the vector symbols a, b, c, written like the book: 4/3 a + b"""
    expr = expand(expr)
    out = ''
    for sym_, name in ((va, 'a'), (vb, 'b'), (vc, 'c')):
        cf = expr.coeff(sym_)
        if cf == 0:
            continue
        sign = '-' if cf < 0 else ('+' if out else '')
        mag = abs(cf)
        coef = '' if mag == 1 else latex(mag)
        out += f'{sign}{coef}' + r'\vec{\mathbf{' + name + '}}'
    return out
def vopt(expr):
    return O(vtex(expr), expr)
def ijk(*c_):
    """LaTeX of a vector written with the unit vectors: 5i - 6j + 9k (zero components left out)"""
    out = ''
    for cf, u_ in zip(c_, 'ijk'):
        cf = sympify(cf)
        if cf == 0:
            continue
        sign = '-' if cf < 0 else ('+' if out else '')
        out += sign + ('' if abs(cf) == 1 else latex(abs(cf))) + r'\hat{' + u_ + '}'
    return out
def ijk_opt(*c_):
    return O(ijk(*c_), Tuple(*[sympify(q_) for q_ in c_]), 'ijk')
def pair_opt(tex, *vals):
    """an answer made of two values, e.g. '-3,\\ 6' (both solutions of a quadratic)"""
    return O(tex, FiniteSet(*vals), 'set')
def solve_k(expr, target):
    """k in a vector identity expr(k) = target written with the symbols a, b (both coefficients must agree)"""
    d_ = expand(expr - target)
    sols = [s_ for s_ in solve(d_.coeff(va), k) if simplify(d_.coeff(vb).subs(k, s_)) == 0]
    assert len(sols) == 1, sols
    return sols[0]


# ---------- figures for exams 4-8
def plane_pts(origin, a2, b2, pts):
    """2-D drawing positions of points given as combinations of the vector symbols a, b (so the drawing is
    exactly the configuration of the question)"""
    out = {}
    for nm, e_ in pts.items():
        e_ = expand(sympify(e_))
        ca, cb = float(e_.coeff(va)), float(e_.coeff(vb))
        out[nm] = (origin[0] + ca*a2[0] + cb*b2[0], origin[1] + ca*a2[1] + cb*b2[1])
    return out


def poly_fig(points, edges, arrows, labels, dashed=(), thick=()):
    """vector diagram: points {name: (x, y)}, edges [(P, Q)] plain sides, arrows [(P, Q, label, (dx, dy))]
    sides that carry a vector (arrowhead in the middle), labels {name: (dx, dy)} label offsets,
    dashed / thick extra segments"""
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        for a1, b1 in edges:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=1.6)
        for a1, b1 in thick:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=2.6)
        for a1, b1 in dashed:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#d04a1a', lw=1.4, ls='--')
        for a1, b1, lab, off in arrows:
            (x1, y1), (x2, y2) = points[a1], points[b1]
            ax.plot([x1, x2], [y1, y2], color='#1f5fbf', lw=1.6)
            ax.annotate('', xy=(x1 + 0.6*(x2 - x1), y1 + 0.6*(y2 - y1)), xytext=(x1 + 0.45*(x2 - x1), y1 + 0.45*(y2 - y1)),
                        arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
            ax.text((x1 + x2)/2 + off[0], (y1 + y2)/2 + off[1], lab, fontsize=12, color='#1f5fbf')
        for nm, (px, py) in points.items():
            ax.plot(px, py, 'o', color='#222', ms=3.5)
            d_ = labels.get(nm, (0.12, 0.12))
            ax.text(px + d_[0], py + d_[1], f'${nm}$', fontsize=13)
        ax.margins(0.1)
    return draw


def iso_box(dx, dy, dz, marks=(), segs=()):
    """Cuboid drawn like the ministry's figure (2026 #41): O at the back (its three edges dashed), x toward the
    lower left, y toward the lower right, z up; vertices E(dx,0,0) F(dx,dy,0) G(0,dy,0) D(0,0,dz) A(dx,0,dz)
    B(dx,dy,dz) C(0,dy,dz). marks: [(name, (x, y, z), (dx, dy))] extra points with their label offsets;
    segs: [((x, y, z), (x, y, z))] extra segments, dashed red."""
    import numpy as np
    def proj(p_):
        x_, y_, z_ = p_
        return np.array([-0.7*x_ + y_, -0.5*x_ - 0.25*y_ + z_], dtype=float)
    vtx = {'O': (0, 0, 0), 'E': (dx, 0, 0), 'F': (dx, dy, 0), 'G': (0, dy, 0),
           'D': (0, 0, dz), 'A': (dx, 0, dz), 'B': (dx, dy, dz), 'C': (0, dy, dz)}
    # label directions chosen away from the edges and the axes meeting at each vertex
    side = {'O': (0.45, -1), 'E': (-1, 0.2), 'F': (0, -1), 'G': (1, 0.6), 'D': (-1, 0.35), 'A': (-1, 0.3),
            'B': (-0.25, 1), 'C': (1, 0.3)}
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        sp = max(dx, dy, dz)
        seen = []
        for e in ('OE', 'OG', 'OD', 'EF', 'FG', 'EA', 'FB', 'GC', 'DA', 'AB', 'BC', 'CD'):
            p1, p2 = proj(vtx[e[0]]), proj(vtx[e[1]])
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], ls='--' if 'O' in e else '-', color='#555', lw=1.3)
        for v_, lab in (('E', 'x'), ('G', 'y'), ('D', 'z')):
            p1 = proj(vtx[v_]); u_ = p1/np.linalg.norm(p1); p2 = p1 + 0.35*sp*u_
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#1f5fbf', lw=1.2)
            ax.annotate('', xy=p2, xytext=p2 - 0.1*sp*u_, arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.2))
            ax.text(*(p2 + 0.09*sp*u_), f'${lab}$', color='#1f5fbf', fontsize=12, ha='center', va='center')
            seen.append(p2 + 0.09*sp*u_)
        for p_, q_ in segs:
            a_, b_ = proj(p_), proj(q_)
            ax.plot([a_[0], b_[0]], [a_[1], b_[1]], color='#d04a1a', lw=1.4, ls='--')
        for k_, p_ in vtx.items():
            q_ = proj(p_); off = np.array(side[k_], dtype=float)
            off = off/np.linalg.norm(off)*0.085*sp
            ax.plot(*q_, 'o', color='#222', ms=3)
            ax.text(*(q_ + off), f'${k_}$', fontsize=12, ha='center', va='center')
            seen += [q_, q_ + off]
        for k_, p_, off in marks:
            q_ = proj(p_); lab = q_ + np.array(off)*sp
            ax.plot(*q_, 'o', color='#d04a1a', ms=4)
            ax.text(*lab, f'${k_}$', fontsize=12, color='#d04a1a', ha='center', va='center')
            seen.append(lab)
        xs, ys = [s_[0] for s_ in seen], [s_[1] for s_ in seen]
        pad = 0.07*sp      # labels are not part of autoscaling: fit the limits to them so nothing is clipped
        ax.set_xlim(min(xs) - pad, max(xs) + pad); ax.set_ylim(min(ys) - pad, max(ys) + pad)
    return draw


def sign_panels(angles):
    """four small panels (1)-(4): the vectors u and v drawn from one point, with the angle between them marked
    (a right-angle box for 90 degrees)"""
    import numpy as np
    def draw(fig, ax):
        ax.axis('off'); ax.set_aspect('equal')
        L = 1.7
        for i, th in enumerate(angles):
            cx, cy = (i % 2)*5.8, -(i // 2)*3.1
            t_ = np.radians(th)
            for (ang_, lab) in ((0.0, 'u'), (t_, 'v')):
                end = (cx + L*np.cos(ang_), cy + L*np.sin(ang_))
                ax.annotate('', xy=end, xytext=(cx, cy), arrowprops=dict(arrowstyle='-|>', color='#1f5fbf', lw=1.6))
                ax.text(cx + (L + 0.32)*np.cos(ang_), cy + (L + 0.32)*np.sin(ang_), r'$\vec{\mathbf{' + lab + '}}$',
                        fontsize=12, color='#1f5fbf', ha='center', va='center')
            if th == 90:
                s_ = 0.28
                ax.plot([cx + s_, cx + s_, cx], [cy, cy + s_, cy + s_], color='#d04a1a', lw=1.2)
            else:
                arc = np.linspace(0, t_, 60)
                ax.plot(cx + 0.5*np.cos(arc), cy + 0.5*np.sin(arc), color='#d04a1a', lw=1.2)
                ax.text(cx + 0.95*np.cos(t_/2), cy + 0.95*np.sin(t_/2), f'${th}^\\circ$', fontsize=11,
                        color='#d04a1a', ha='center', va='center')
            ax.plot(cx, cy, 'o', color='#222', ms=3)
            ax.text(cx, cy - 0.6, f'$({i + 1})$', fontsize=12, ha='center', va='center')
        ax.set_xlim(-2.4, 8.1); ax.set_ylim(-4.0, 2.3)
    return draw
