"""Shared helpers for the semester-1 mock papers (s1_papers_*.py): lesson ids, solvers, figure drawers, paper notes."""
from qb import *
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
