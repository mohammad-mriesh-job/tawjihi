"""Shared helpers for the unit-7 generators (u7.py and u7_exams_4_8.py)."""
from qb import *

R = Rational

def Phi4(z0):
    """standard normal CDF rounded to 4 decimals, exactly as printed in the ministry table"""
    z0 = nsimplify(z0)
    val = N((1 + erf(z0/sqrt(2)))/2, 30)
    return R(str(round(float(val), 4)))
def Ph(z0):
    z0 = nsimplify(z0)
    return Phi4(z0) if z0 >= 0 else 1 - Phi4(-z0)
def ztable(*zs):
    zs = sorted({nsimplify(q_) for q_ in zs})
    head = ' & '.join(f'{float(q_):g}' for q_ in zs)
    row = ' & '.join(f'{float(Phi4(q_)):.4f}' for q_ in zs)
    return ("\n" r"يمكنك الاستفادة من الجدول الآتي الذي يُمثّل بعضًا من قيم جدول التوزيع الطبيعي المعياري:" "\n"
            r"$$\begin{array}{|c|" + 'c|'*len(zs) + r"}\hline z & " + head + r"\\ \hline P(Z<z) & " + row + r"\\ \hline\end{array}$$")
def binom(n_, p_, k_): return binomial(n_, k_)*p_**k_*(1-p_)**(n_-k_)
def geo(p_, k_): return (1-p_)**(k_-1)*p_
def r4(v_): return R(str(round(float(v_), 4)))

def bell(a_, b_, labels):
    import numpy as np
    def draw(fig, ax):
        xs = np.linspace(-3.6, 3.6, 400)
        ys = np.exp(-xs**2/2)/np.sqrt(2*np.pi)
        ax.plot(xs, ys, color='#1f5fbf', lw=1.8)
        xr = np.linspace(a_, b_, 200)
        ax.fill_between(xr, np.exp(-xr**2/2)/np.sqrt(2*np.pi), color='#9cc3ef', alpha=0.9)
        ax.axhline(0, color='black', lw=0.8)
        for xv in (a_, b_):
            ax.plot([xv, xv], [0, np.exp(-xv**2/2)/np.sqrt(2*np.pi)], color='#1f5fbf', lw=1, ls='--')
        ax.set_yticks([]); ax.set_xticks(labels); ax.set_xticklabels([f'{q_:g}' for q_ in labels])
        for side in ('top', 'right', 'left'):
            ax.spines[side].set_visible(False)
        ax.text(3.4, -0.05, '$z$', fontsize=12)
        ax.set_ylim(-0.02, 0.45)
    return draw

def zclosest(target, zs):
    """the table entry z whose P(Z<z) is closest to target (how the student reads a table that lacks the exact value)"""
    best = sorted(zs, key=lambda z_: abs(Phi4(z_) - nsimplify(target)))
    assert abs(Phi4(best[0]) - nsimplify(target)) < abs(Phi4(best[1]) - nsimplify(target)), 'two entries equally close'
    return nsimplify(best[0])


EMP_PARTS = {(-3, -2): R(235, 10000), (-2, -1): R(135, 1000), (-1, 0): R(34, 100), (0, 1): R(34, 100),
             (1, 2): R(135, 1000), (2, 3): R(235, 10000)}
def emp(a_, b_):
    """probability between mu + a sigma and mu + b sigma by the empirical rule figure (a, b whole numbers)"""
    return sum((v_ for (lo, hi), v_ in EMP_PARTS.items() if a_ <= lo and hi <= b_), R(0)) + \
        (R(15, 10000) if a_ <= -3 and b_ >= 3 else 0)


def pair_opt(tex, *vals):
    """an answer made of two values, e.g. 'p=0.2,\ p=0.8'"""
    return O(tex, FiniteSet(*vals), 'set')


def _curve(ax, xs):
    import numpy as np
    return np.exp(-xs**2/2)/np.sqrt(2*np.pi)


def emp_fig(fig, ax):
    """the ministry's empirical-rule reference figure: the percentages between mu + k sigma"""
    import numpy as np
    xs = np.linspace(-3.6, 3.6, 400)
    ax.plot(xs, _curve(ax, xs), color='#1f5fbf', lw=1.8)
    ax.axhline(0, color='black', lw=0.8)
    for k_ in (-3, -2, -1, 0, 1, 2, 3):
        ax.plot([k_, k_], [0, float(_curve(ax, np.array(k_)))], color='#555', lw=0.9, ls='--')
    for x_, y_, t_ in ((0.5, 0.17, '34%'), (-0.5, 0.17, '34%'), (1.5, 0.055, '13.5%'), (-1.5, 0.055, '13.5%'),
                       (2.5, 0.03, '2.35%'), (-2.5, 0.03, '2.35%'), (3.35, 0.012, '0.15%'), (-3.35, 0.012, '0.15%')):
        ax.text(x_, y_, t_, ha='center', fontsize=9)
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_xticklabels([r'$\mu-3\sigma$', r'$\mu-2\sigma$', r'$\mu-\sigma$', r'$\mu$', r'$\mu+\sigma$', r'$\mu+2\sigma$', r'$\mu+3\sigma$'], fontsize=9)
    ax.set_yticks([])
    for side in ('top', 'right', 'left'):
        ax.spines[side].set_visible(False)
    ax.set_ylim(-0.01, 0.43); ax.set_xlim(-3.7, 3.7)


def tails_fig(lo_lab, mid_lab, hi_lab, pct):
    """normal curve with both tails beyond mu -/+ 2 sigma shaded and labelled with their percentage; the axis shows the
    two values (the mean is not written, only marked)"""
    import numpy as np
    def draw(fig, ax):
        xs = np.linspace(-3.6, 3.6, 400)
        ax.plot(xs, _curve(ax, xs), color='#1f5fbf', lw=1.8)
        ax.axhline(0, color='black', lw=0.8)
        for a_, b_ in ((-3.6, -2), (2, 3.6)):
            xr = np.linspace(a_, b_, 100)
            ax.fill_between(xr, _curve(ax, xr), color='#9cc3ef', alpha=0.9)
        ax.plot([0, 0], [0, float(_curve(ax, np.array(0)))], color='#555', lw=0.9, ls='--')
        for x_, side in ((-2.45, -1), (2.45, 1)):
            ax.annotate(pct, xy=(x_, 0.012), xytext=(x_ + 0.9*side, 0.12), ha='center', fontsize=10,
                        arrowprops=dict(arrowstyle='->', color='#333', lw=0.9))
        ax.set_xticks([-2, 0, 2]); ax.set_xticklabels([lo_lab, mid_lab, hi_lab])
        ax.set_yticks([])
        for side in ('top', 'right', 'left'):
            ax.spines[side].set_visible(False)
        ax.set_ylim(-0.01, 0.43); ax.set_xlim(-3.7, 3.7)
    return draw


def tails_emp_fig(lo_lab, mid_lab, hi_lab, pct):
    """2025 #23 as the ministry prints it, in one figure: on top the item's curve with both tails marked (tails_fig),
    below it the empirical-rule figure given as a note (emp_fig)"""
    def draw(fig, ax):
        ax.remove()
        top, bottom = fig.subplots(2, 1)
        tails_fig(lo_lab, mid_lab, hi_lab, pct)(fig, top)
        top.text(3.55, -0.045, '$X$', fontsize=12)
        emp_fig(fig, bottom)
    return draw
