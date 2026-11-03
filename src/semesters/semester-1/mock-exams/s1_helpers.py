"""Shared helpers for the semester-1 mock papers (s1_papers_*.py): lesson ids, solvers, figure drawers, paper notes."""
from qb import *
import cmath
import math
import numpy as np

R = Rational
P = pi
X, Y = symbols('X Y', real=True)
U1 = {1: 'u1-l1', 2: 'u1-l2'}
U2 = {1: 'u2-l1', 2: 'u2-l2', 3: 'u2-l3'}
U3 = {i: f'u3-l{i}' for i in range(1, 6)}
U4 = {1: 'u4-l1', 2: 'u4-l2', 3: 'u4-l3'}

# ------------------------------------------------------------------ helpers
def roots(f): return FiniteSet(*solve(f, x))
def other_roots(f, r0): return FiniteSet(*[q for q in solve(f, x) if simplify(q - r0) != 0])
def rem(f, r0): return expand(f).subs(x, r0)
def st(*vals_tex, var='x'): return r',\ '.join(f'{var}=' + t_ for t_ in vals_tex)
S_ = lambda *v_: FiniteSet(*v_)
deg = lambda d_: d_*pi/180
def sols(expr, lo, hi, closed_lo=True, closed_hi=False): return numsols(expr, lo, hi, closed_lo, closed_hi)
Dx = lambda f_: diff(f_, x)
def imp(eq, pt, order=1): return idiff(eq, y, x, order).subs({x: pt[0], y: pt[1]})
pol = lambda r_, th_: r_*(cos(th_) + I*sin(th_))
def trig(r_tex, th_tex): return rf'{r_tex}\left(\cos({th_tex})+i\sin({th_tex})\right)'
def croots(poly): return FiniteSet(*[nsimplify(expand(r_)) for r_ in solve(poly, z)])
def ab(lst): return Tuple(*lst)

def pw(points):
    def val(x0):
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 <= x0 <= x2:
                return R(y1) + R(y2 - y1, x2 - x1)*(x0 - x1)
        raise ValueError
    def slope(x0):
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 < x0 < x2:
                return R(y2 - y1, x2 - x1)
        raise ValueError('corner or outside')
    return val, slope

def draw_two(fpts, gpts, xmax, ymax, flabel, glabel):
    def draw(fig, ax):
        axes_style(ax, (-0.6, xmax + 0.6), (-0.6, ymax + 0.8), grid=True)
        ax.set_xticks(range(0, xmax + 1)); ax.set_yticks(range(0, ymax + 1))
        fx, fy = zip(*fpts); gx, gy = zip(*gpts)
        ax.plot(fx, fy, color='#1f5fbf', lw=2); ax.plot(gx, gy, color='#d04a1a', lw=2)
        ax.text(*flabel, r'$f(x)$', color='#1f5fbf', fontsize=12)
        ax.text(*glabel, r'$g(x)$', color='#d04a1a', fontsize=12)
    return draw

def complex_axes(ax, lim):
    axes_style(ax, (-lim, lim), (-lim, lim), xlabel=r'\mathrm{Re}', ylabel=r'\mathrm{Im}', grid=True)
    ax.set_aspect('equal'); ax.set_xticks(range(-lim + 1, lim)); ax.set_yticks(range(-lim + 1, lim))
    ax.tick_params(labelsize=8)

FILL, LINE = '#9cc3ef', '#1f5fbf'

def fig_region(kind):
    """locus regions used in the papers (drawn exactly as described in each solution)"""
    def draw(fig, ax):
        if kind == 'halfdisk':          # |z-i|<=2 , 0<=Arg(z-i)<=pi
            complex_axes(ax, 4)
            th_ = np.linspace(0, np.pi, 100)
            ax.fill(np.r_[2*np.cos(th_)], np.r_[1 + 2*np.sin(th_)], color=FILL, alpha=0.8)
            ax.plot(2*np.cos(th_), 1 + 2*np.sin(th_), color=LINE, lw=1.8)
            ax.plot([-2, 2], [1, 1], color=LINE, lw=1.8)
            ax.plot(0, 1, 'o', mfc='white', mec=LINE, ms=5)
        elif kind == 'disk_right':      # |z|<=3 , |z-2|<=|z|  (x>=1)
            complex_axes(ax, 4)
            th_ = np.linspace(-np.arccos(1/3), np.arccos(1/3), 100)
            xs = np.r_[1, 3*np.cos(th_), 1]; ys = np.r_[-np.sqrt(8), 3*np.sin(th_), np.sqrt(8)]
            ax.fill(xs, ys, color=FILL, alpha=0.8)
            full = np.linspace(0, 2*np.pi, 200)
            ax.plot(3*np.cos(full), 3*np.sin(full), color=LINE, lw=1.4)
            ax.plot([1, 1], [-3.9, 3.9], color=LINE, lw=1.4)
            ax.plot(2, 0, 'x', color='#d04a1a', ms=7)
        elif kind == 'quarter_ring':    # 1<|z|<=3 , 0<=Arg z<=pi/2
            complex_axes(ax, 4)
            th_ = np.linspace(0, np.pi/2, 100)
            xs = np.r_[3*np.cos(th_), np.cos(th_[::-1])]; ys = np.r_[3*np.sin(th_), np.sin(th_[::-1])]
            ax.fill(xs, ys, color=FILL, alpha=0.8)
            ax.plot(3*np.cos(th_), 3*np.sin(th_), color=LINE, lw=1.8)
            ax.plot(np.cos(th_), np.sin(th_), color=LINE, lw=1.6, ls='--')
            ax.plot([1, 3], [0, 0], color=LINE, lw=1.8); ax.plot([0, 0], [1, 3], color=LINE, lw=1.8)
        elif kind == 'disk_left':       # |z-2i|<=2 , |z|<=|z-2| (x<=1)
            complex_axes(ax, 5)
            th_ = np.linspace(np.pi - np.arccos(-0.5), np.pi + np.arccos(-0.5), 10)
            t2 = np.linspace(np.arccos(0.5), 2*np.pi - np.arccos(0.5), 200)
            xs = 2*np.cos(t2); ys = 2 + 2*np.sin(t2)
            ax.fill(np.r_[xs, 1], np.r_[ys, 2 + 2*np.sin(np.arccos(0.5))], color=FILL, alpha=0.8)
            full = np.linspace(0, 2*np.pi, 200)
            ax.plot(2*np.cos(full), 2 + 2*np.sin(full), color=LINE, lw=1.4)
            ax.plot([1, 1], [-4.9, 4.9], color=LINE, lw=1.4)
            ax.plot(2, 0, 'x', color='#d04a1a', ms=7)
        elif kind == 'wedge':           # pi/6<=Arg(z+1-i)<=2pi/3
            complex_axes(ax, 5)
            v0 = np.array([-1, 1]); L_ = 7
            a1, a2 = np.pi/6, 2*np.pi/3
            pts = [v0, v0 + L_*np.array([np.cos(a1), np.sin(a1)]), v0 + L_*np.array([np.cos(a2), np.sin(a2)])]
            ax.fill([p_[0] for p_ in pts], [p_[1] for p_ in pts], color=FILL, alpha=0.8)
            for a_ in (a1, a2):
                e_ = v0 + L_*np.array([np.cos(a_), np.sin(a_)])
                ax.plot([v0[0], e_[0]], [v0[1], e_[1]], color=LINE, lw=1.8)
            ax.plot(*v0, 'o', mfc='white', mec=LINE, ms=5)
            ax.set_xlim(-5, 5); ax.set_ylim(-5, 5)
    return draw

NOTE_I = lambda a_, b_: rf"ملحوظة: في جميع الفقرات من ({a_}) إلى ({b_}) ، فإنّ $i=\sqrt{{-1}}$ حيثما وردت، و $\text{{Arg}}(z)$ هي السعة الرئيسة للعدد $z$."
def shared(stem, a_, b_):
    return rf"❖ {stem} ، فاعتمد ذلك للإجابة عن الفقرتين ({a_}) و ({b_}) الآتيتين:"


# ------------------------------------------------------------------ algebra helpers
def tangent_x_intercept(eq, pt):
    m_ = imp(eq, pt)
    return pt[0] - pt[1] / m_


def smaller_angle(z1, z2):
    return acos(re(expand(z1*conjugate(z2))) / (Abs(z1)*Abs(z2)))


# ------------------------------------------------------------------ regions in the complex plane
EPS = 1e-9


def arg_of(w):
    """principal argument in (-pi, pi]; None at 0 (Arg(0) is undefined)."""
    if abs(w) < EPS:
        return None
    a_ = cmath.phase(w)
    return math.pi if a_ <= -math.pi + 1e-12 else a_


def disk(c, r, strict=False):
    return (lambda z_: abs(z_ - c) < r - EPS) if strict else (lambda z_: abs(z_ - c) <= r + EPS)


def outside(c, r, strict=False):
    return (lambda z_: abs(z_ - c) > r + EPS) if strict else (lambda z_: abs(z_ - c) >= r - EPS)


def sector(c, lo, hi, lo_open=False, hi_open=False):
    def ok(z_):
        a_ = arg_of(z_ - c)
        if a_ is None:
            return False
        return (a_ > lo + EPS if lo_open else a_ >= lo - EPS) and (a_ < hi - EPS if hi_open else a_ <= hi + EPS)
    return ok


def nearer(p_, q_):
    """|z - p| <= |z - q|"""
    return lambda z_: abs(z_ - p_) <= abs(z_ - q_) + EPS


def closer(p_, q_):
    """|z - p| < |z - q| (dashed bisector, boundary not included)"""
    return lambda z_: abs(z_ - p_) < abs(z_ - q_) - EPS


def bisector(p_, q_):
    return lambda z_: abs(abs(z_ - p_) - abs(z_ - q_)) < 1e-6


def both(*preds):
    return lambda z_: all(f_(z_) for f_ in preds)


def region_points(prims, lim):
    pts = [complex(a_, b_) for a_ in np.linspace(-lim, lim, 161) for b_ in np.linspace(-lim, lim, 161)]
    for pr in prims:
        if pr[0] == 'arc':
            _, c_, r_, _, (t0, t1) = pr
            pts += [c_ + r_*cmath.exp(1j*t_) for t_ in np.linspace(t0, t1, 400)]
        elif pr[0] == 'seg':
            _, p1, p2, _ = pr
            pts += [p1 + (p2 - p1)*s_ for s_ in np.linspace(0, 1, 400)]
        elif pr[0] == 'open':
            pts.append(pr[1])
    return pts


def region_truth(true_pred, prims, lim):
    """IndexQ truth: the only option whose predicate gives the shaded region, also on the boundary."""
    pts = region_points(prims, lim)
    return lambda vals: only(vals, lambda pred: all(pred(z_) == true_pred(z_) for z_ in pts))


def fig_region2(pred, prims, lim, marks=()):
    """shade exactly the points where pred holds; draw the boundary pieces (dashed = not included)."""
    def draw(fig, ax):
        complex_axes(ax, lim)
        xs = np.linspace(-lim, lim, 520)
        X_, Y_ = np.meshgrid(xs, xs)
        mask = np.vectorize(lambda a_, b_: 1.0 if pred(complex(a_, b_)) else 0.0)(X_, Y_)
        ax.contourf(X_, Y_, mask, levels=[0.5, 1.5], colors=[FILL], alpha=0.8)
        for pr in prims:
            if pr[0] == 'arc':
                _, c_, r_, dashed, (t0, t1) = pr
                ts = np.linspace(t0, t1, 300)
                ax.plot(c_.real + r_*np.cos(ts), c_.imag + r_*np.sin(ts), color=LINE, lw=1.8, ls='--' if dashed else '-')
            elif pr[0] == 'seg':
                _, p1, p2, dashed = pr
                ax.plot([p1.real, p2.real], [p1.imag, p2.imag], color=LINE, lw=1.8, ls='--' if dashed else '-')
            elif pr[0] == 'line':        # reference line (not part of the region's boundary)
                _, p1, p2 = pr
                ax.plot([p1.real, p2.real], [p1.imag, p2.imag], color='#888888', lw=1.0, ls=':')
            elif pr[0] == 'open':
                ax.plot(pr[1].real, pr[1].imag, 'o', mfc='white', mec=LINE, ms=5, zorder=5)
        for p_, txt in marks:
            ax.plot(p_.real, p_.imag, 'x', color='#d04a1a', ms=7)
            ax.text(p_.real + 0.15, p_.imag + 0.2, txt, fontsize=9, color='#d04a1a')
        ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    return draw


# ------------------------------------------------------------------ other figures
def _sketch(fig, ax):
    ax.set_aspect('equal'); ax.axis('off')


def fig_point(px, py, xtxt, ytxt, name, lim):
    """one complex number as a point with dashed projections and its coordinates on the axes (2025 #18 style)."""
    def draw(fig, ax):
        complex_axes(ax, lim)
        ax.set_xticks([]); ax.set_yticks([])
        ax.plot([0, px], [0, py], color=LINE, lw=1.8)
        ax.plot([px, px], [0, py], color='#555555', lw=1, ls='--'); ax.plot([0, px], [py, py], color='#555555', lw=1, ls='--')
        ax.plot(px, py, 'o', color=LINE, ms=5, zorder=5)
        ax.text(px - 0.2, -0.75 if py > 0 else 0.35, xtxt, fontsize=10)
        ax.text(0.2 if px < 0 else -1.1, py - 0.15, ytxt, fontsize=10)
        ax.text(px + (0.25 if px > 0 else -0.7), py + 0.2, f'${name}$', fontsize=12, color=LINE)
    return draw


def fig_one(pts, xr, yr, label_pos, name='f(x)'):
    """graph of one piecewise-linear function on a grid."""
    def draw(fig, ax):
        axes_style(ax, (xr[0] - 0.5, xr[1] + 0.5), (yr[0] - 0.5, yr[1] + 0.8), grid=True)
        ax.set_xticks(range(xr[0], xr[1] + 1)); ax.set_yticks(range(yr[0], yr[1] + 1)); ax.tick_params(labelsize=8)
        ax.plot(*zip(*pts), color='#1f5fbf', lw=2)
        ax.text(*label_pos, f'${name}$', color='#1f5fbf', fontsize=12)
    return draw


def fig_tank(d_txt, h_txt=None, level=0.55):
    """upright cylindrical tank (2026 #18 style): the base diameter labelled below, the height on the right if given,
    water up to a level h."""
    def draw(fig, ax):
        from matplotlib.patches import Ellipse
        _sketch(fig, ax)
        H, wl = 6, 6*level
        ax.plot([-2, -2], [0, H], color='#333333', lw=1.6); ax.plot([2, 2], [0, H], color='#333333', lw=1.6)
        ax.add_patch(Ellipse((0, H), 4, 0.8, fill=False, color='#333333', lw=1.4))
        ax.fill_between([-2, 2], [0, 0], [wl, wl], color='#9cc3ef', alpha=0.8)
        ax.add_patch(Ellipse((0, wl), 4, 0.8, color='#7fb0e6'))
        ax.add_patch(Ellipse((0, 0), 4, 0.8, color='#9cc3ef', ec='#333333', lw=1.4))
        if h_txt:
            ax.annotate('', (2.6, 0), (2.6, H), arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
            ax.text(2.75, H/2 - 0.1, h_txt, fontsize=10)
        ax.annotate('', (-2, -0.9), (2, -0.9), arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
        ax.text(-0.45, -1.45, d_txt, fontsize=10)
        ax.text(-0.25, wl/2 - 0.2, r'$h$', fontsize=12, color='#1f5fbf')
        ax.set_xlim(-2.6, 3.9); ax.set_ylim(-1.8, H + 0.8)
    return draw
