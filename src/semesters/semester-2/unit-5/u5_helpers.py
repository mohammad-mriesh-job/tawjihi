"""Shared helpers for the unit-5 generators (u5.py and u5_exams_5_10.py)."""
from qb import *

R = Rational
P = pi
ig = integrate
C = r'+C'
def A(tex, F_):
    """antiderivative option: displayed LaTeX (must end with +C) and the antiderivative F"""
    assert tex.rstrip().endswith('+C'), tex
    return O(tex, F_, 'anti')
def ode_ok(Yx, rhs, x0, y0):
    """explicit solution y=Y(x) satisfies y'=rhs(x,y) and y(x0)=y0"""
    return same(diff(Yx, x) - rhs.subs(y, Yx), 0) and same(Yx.subs(x, x0), y0)
def ode_ok_rel(Fxy, rhs, x0, y0):
    """implicit solution F(x,y)=0 satisfies y'=rhs and passes (x0,y0)"""
    dydx = -diff(Fxy, x)/diff(Fxy, y)
    if not same(Fxy.subs({x: x0, y: y0}), 0):
        return False
    return same(dydx - rhs, 0) or same(simplify((dydx - rhs).subs(y, solve(Fxy, y)[-1])), 0)

def region(f_, g_, a_, b_, xlim, ylim, labels=(), fill='#9cc3ef'):
    import numpy as np
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        xs = np.linspace(xlim[0], xlim[1], 400)
        ff = lambdify(x, f_, 'numpy'); gg = lambdify(x, g_, 'numpy')
        ax.plot(xs, ff(xs) + 0*xs, color='#1f5fbf', lw=1.8)
        if g_ != 0:
            ax.plot(xs, gg(xs) + 0*xs, color='#d04a1a', lw=1.8)
        xr = np.linspace(float(a_), float(b_), 200)
        ax.fill_between(xr, ff(xr) + 0*xr, gg(xr) + 0*xr, color=fill, alpha=0.8)
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

Cc = Symbol('C')
def ode_gen_ok(Fxy, rhs, pt=None):
    """general implicit solution F(x, y, C) = 0 of y' = rhs (optionally through pt)"""
    dydx = -diff(Fxy, x)/diff(Fxy, y)
    if not same(dydx - rhs, 0):
        return False
    return pt is None or same(Fxy.subs({x: pt[0], y: pt[1]}), 0)
