"""Semester-1 mock papers 6-10 (m6q1..m10q30), same layout as papers 1-5:
U1 items 1-4, U2 items 5-10, U3 items 11-22, U4 items 23-30.
Every paper covers the semester-1 item patterns of the ministry paper of 2 July 2026 with a different structure
each time, plus lesson patterns the first five papers do not use. Region items (item 30, and every region option)
are checked by sampling: each option is a predicate, the shaded figure is drawn from the correct predicate, and the
distractors must differ from it inside the plane or on its boundary (dashed vs solid lines)."""
import cmath
import math
from s1_helpers import *

A_, B_, C_, D_ = symbols('A B C D')
h_ = Symbol('h')


# ------------------------------------------------------------------ algebra helpers
def solve_pf(expr, form, unknowns):
    """constants making `form` identical to `expr` (None if the form cannot represent it)."""
    num = numer(together(expr - form))
    sol = solve(Poly(expand(num), x).all_coeffs(), unknowns, dict=True)
    return sol[0] if sol else None


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
def fig_tangent(fx, pts, xr, yr, flabel, llabel):
    """curve f and its tangent line through the two marked lattice points pts."""
    def draw(fig, ax):
        axes_style(ax, (xr[0] - 0.5, xr[1] + 0.5), (yr[0] - 0.5, yr[1] + 0.8), grid=True)
        ax.set_xticks(range(xr[0], xr[1] + 1)); ax.set_yticks(range(yr[0], yr[1] + 1)); ax.tick_params(labelsize=8)
        xs = np.linspace(xr[0] - 0.4, xr[1] + 0.4, 300)
        ax.plot(xs, fx(xs), color='#1f5fbf', lw=2)
        (x1, y1), (x2, y2) = pts
        m_ = (y2 - y1) / (x2 - x1)
        lx = np.linspace(xr[0] - 0.4, xr[1] + 0.4, 2)
        ax.plot(lx, y1 + m_*(lx - x1), color='#d04a1a', lw=1.6)
        for px, py in pts:
            ax.plot(px, py, 'o', color='black', ms=4, zorder=5)
            ax.text(px + 0.12, py - 0.45, f'$({px},\\,{py})$', fontsize=9)
        ax.text(*flabel, r'$f(x)$', color='#1f5fbf', fontsize=12)
        ax.text(*llabel, r'$L$', color='#d04a1a', fontsize=12)
        ax.set_ylim(yr[0] - 0.5, yr[1] + 0.8)
    return draw


def fig_dgraph(pts, xr, yr, label_pos):
    """graph of the derivative f'(x) (piecewise linear through lattice points)."""
    def draw(fig, ax):
        axes_style(ax, (xr[0] - 0.5, xr[1] + 0.5), (yr[0] - 0.5, yr[1] + 0.8), grid=True)
        ax.set_xticks(range(xr[0], xr[1] + 1)); ax.set_yticks(range(yr[0], yr[1] + 1)); ax.tick_params(labelsize=8)
        ax.plot(*zip(*pts), color='#1f5fbf', lw=2)
        ax.text(*label_pos, r"$y=f'(x)$", color='#1f5fbf', fontsize=12)
    return draw


def fig_argand(points, lim):
    """points z_k in the complex plane, labelled with their coordinates."""
    def draw(fig, ax):
        complex_axes(ax, lim)
        for (px, py), name, txt, off in points:
            ax.plot([0, px], [0, py], color='#9aa5b1', lw=1, ls='--')
            ax.plot(px, py, 'o', color='#1f5fbf', ms=5, zorder=5)
            ax.text(px + off[0], py + off[1], f'${name}$ {txt}', fontsize=9)
    return draw


def _sketch(fig, ax):
    ax.set_aspect('equal'); ax.axis('off')


def fig_cone():
    """inverted cone tank with the water level (m6q22)."""
    def draw(fig, ax):
        _sketch(fig, ax)
        ax.plot([-1.5, 0, 1.5], [3, 0, 3], color='#333333', lw=1.6)
        ax.add_patch(__import__('matplotlib.patches', fromlist=['Ellipse']).Ellipse((0, 3), 3, 0.5, fill=False, color='#333333', lw=1.4))
        ax.fill([-1, 0, 1], [2, 0, 2], color='#9cc3ef', alpha=0.85)
        ax.add_patch(__import__('matplotlib.patches', fromlist=['Ellipse']).Ellipse((0, 2), 2, 0.34, color='#7fb0e6'))
        ax.annotate('', (1.95, 0), (1.95, 3), arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
        ax.text(2.05, 1.45, r'$6\ \mathrm{m}$', fontsize=10)
        ax.plot([0, 1.5], [3, 3], color='#d04a1a', lw=1.2); ax.text(0.5, 3.38, r'$3\ \mathrm{m}$', fontsize=10, color='#d04a1a')
        ax.plot([0, 0], [0, 2], color='#1f5fbf', lw=1, ls='--'); ax.text(-0.42, 0.9, r'$h$', fontsize=11, color='#1f5fbf')
        ax.plot([0, 1], [2, 2], color='#1f5fbf', lw=1); ax.text(0.4, 2.12, r'$r$', fontsize=11, color='#1f5fbf')
        ax.set_xlim(-1.9, 2.8); ax.set_ylim(-0.3, 3.6)
    return draw


def fig_kite():
    """kite on a straight string at a fixed height (m7q22)."""
    def draw(fig, ax):
        _sketch(fig, ax)
        ax.plot([-0.3, 9.3], [0, 0], color='#333333', lw=1.4)
        ax.plot([0, 8], [0.25, 6], color='#555555', lw=1.2)
        ax.fill([8, 8.45, 8, 7.55], [6.55, 6, 5.3, 6], color='#d04a1a')
        ax.plot([0, 0], [0, 0.25], color='#333333', lw=3)
        ax.plot([8, 8], [0, 5.3], color='#1f5fbf', lw=1, ls='--')
        ax.text(8.2, 2.7, r'$60\ \mathrm{m}$', fontsize=10, color='#1f5fbf')
        ax.text(3.6, -0.65, r'$x$', fontsize=11); ax.text(3.2, 3.2, r'$\ell$', fontsize=12)
        ax.annotate('', (8.9, -0.35), (7.3, -0.35), arrowprops=dict(arrowstyle='->', color='#333333', lw=1))
        ax.text(7.4, -1.05, r'$2\ \mathrm{m/s}$', fontsize=9)
        ax.set_xlim(-0.6, 9.6); ax.set_ylim(-1.3, 7)
    return draw


def fig_ladder():
    """ladder against a wall, angle with the ground (m8q22)."""
    def draw(fig, ax):
        _sketch(fig, ax)
        ax.plot([0, 0], [0, 9], color='#333333', lw=2); ax.plot([0, 7.5], [0, 0], color='#333333', lw=2)
        ax.plot([6, 0], [0, 8], color='#8a5a2b', lw=3)
        ax.text(3.3, 4.3, r'$10\ \mathrm{m}$', fontsize=10)
        ax.add_patch(__import__('matplotlib.patches', fromlist=['Arc']).Arc((6, 0), 2.2, 2.2, theta1=126.87, theta2=180, color='#d04a1a', lw=1.2))
        ax.text(4.35, 0.35, r'$\theta$', fontsize=12, color='#d04a1a')
        ax.text(2.8, -0.85, r'$x$', fontsize=11)
        ax.annotate('', (7.4, 0.35), (6.1, 0.35), arrowprops=dict(arrowstyle='->', color='#333333', lw=1))
        ax.set_xlim(-0.6, 8); ax.set_ylim(-1.2, 9.3)
    return draw


def fig_trough():
    """water trough with isosceles-triangle ends (m10q22)."""
    def draw(fig, ax):
        _sketch(fig, ax)
        dx, dy = 3.2, 1.2
        A, B, C = (0, 1), (2, 1), (1, 0)
        for p_, q_ in [(A, B), (B, C), (C, A)]:
            ax.plot([p_[0], q_[0]], [p_[1], q_[1]], color='#333333', lw=1.5)
            ax.plot([p_[0] + dx, q_[0] + dx], [p_[1] + dy, q_[1] + dy], color='#333333', lw=1.0)
        for p_ in (A, B, C):
            ax.plot([p_[0], p_[0] + dx], [p_[1], p_[1] + dy], color='#333333', lw=1.0)
        ax.fill([0.5, 1.5, 1], [0.5, 0.5, 0], color='#9cc3ef', alpha=0.9)
        ax.text(0.75, 1.1, r'$2\ \mathrm{m}$', fontsize=9)
        ax.plot([2.25, 2.25], [0, 1], color='#1f5fbf', lw=0.8, ls='--'); ax.text(2.33, 0.4, r'$1\ \mathrm{m}$', fontsize=9, color='#1f5fbf')
        ax.text(1.75 + dx / 2, 0.15 + dy / 2, r'$4\ \mathrm{m}$', fontsize=9)
        ax.text(1.05, 0.18, r'$h$', fontsize=9, color='#1f5fbf')
        ax.set_xlim(-0.3, 5.6); ax.set_ylim(-0.3, 2.5)
    return draw


def tan_point_value(pts, x0):
    (x1, y1), (x2, y2) = pts
    m_ = R(y2 - y1, x2 - x1)
    return y1 + m_*(x0 - x1), m_


# ================================================================== PAPER 6
TP6 = [(0, 1), (4, 5)]                       # tangent to f at x=2 passes through these lattice points
f6_16 = lambda s_: -0.5*(s_ - 2)**2 + (s_ - 2) + 3
R6 = both(disk(1, 2, strict=True), sector(-1, -math.pi/4, math.pi/4))
PR6 = [('arc', 1 + 0j, 2, True, (-math.pi/2, math.pi/2)), ('seg', -1 + 0j, 1 + 2j, False), ('seg', -1 + 0j, 1 - 2j, False), ('open', -1 + 0j)]
P6 = [
# ---------------- unit 1
Q('m6q1', U1[1], 'easy',
  F(r"إذا كان $x=4$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ مجموعة حلّ المعادلة هي:", (r'x^{3}-2x^{2}', x**3-2*x**2), (r'7x+4', 7*x+4)),
  [O(st('4', '-1'), S_(4, -1), 'set'), O(st('-4', '1'), S_(-4, 1), 'set'), O(st('4', '1'), S_(4, 1), 'set'), O(st('-4', '-1'), S_(-4, -1), 'set')],
  r"$x^3-2x^2-7x-4=0$ ، وبالقسمة التركيبية على $(x-4)$: $1,\ -2,\ -7,\ -4 \to 1,\ 2,\ 1,\ 0$" "\n"
  r"$x^2+2x+1=(x+1)^2=0 \Rightarrow x=-1$ (حلّ مكرّر) ، فمجموعة الحل $\{4,\ -1\}$",
  truth=lambda: roots(x**3-2*x**2-7*x-4), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
Q('m6q2', U1[2], 'medium',
  F(r"إذا كان: $«0»=\dfrac{A}{x}+\dfrac{B}{x+1}+\dfrac{C}{(x+1)^{2}}$ ، فإنّ قيمة $A+B+C$ هي:", (r'\frac{2x^{2}+5x+1}{x(x+1)^{2}}', (2*x**2+5*x+1)/(x*(x+1)**2))),
  [O('4', 4), O('0', 0), O('2', 2), O('-2', -2)],
  r"$2x^2+5x+1=A(x+1)^2+Bx(x+1)+Cx$" "\n" r"عند $x=0$: $A=1$ ، وعند $x=-1$: $-2=-C \Rightarrow C=2$ ، ومعامل $x^2$: $2=A+B \Rightarrow B=1$" "\n" r"$A+B+C=4$",
  truth=lambda: (lambda s_: s_[A_]+s_[B_]+s_[C_])(solve_pf((2*x**2+5*x+1)/(x*(x+1)**2), A_/x+B_/(x+1)+C_/(x+1)**2, [A_, B_, C_])),
  tag='تجزئة: عامل خطي مكرر'),
Q('m6q3', U1[1], 'medium',
  F(r"إذا كان باقي قسمة الاقتران: $f(x)=«0»$ على $(2x-1)$ يساوي $3$ ، فإنّ قيمة الثابت $k$ هي:", (r'x^{3}+kx^{2}-x+2', x**3+k*x**2-x+2)),
  [O(r'\frac{11}{2}', R(11, 2)), O(r'\frac{5}{2}', R(5, 2)), O(r'\frac{11}{8}', R(11, 8)), O(r'\frac{5}{8}', R(5, 8))],
  r"صفر المقسوم عليه: $2x-1=0 \Rightarrow x=\frac12$ ، والباقي $f\left(\frac12\right)=\frac18+\frac k4-\frac12+2=\frac{13}{8}+\frac k4$" "\n"
  r"$\frac{13}{8}+\frac k4=3 \Rightarrow \frac k4=\frac{11}{8} \Rightarrow k=\frac{11}{2}$",
  truth=lambda: solve(rem(x**3+k*x**2-x+2, R(1, 2))-3, k)[0], tag='نظرية الباقي: القسمة على (ax−b)'),
Q('m6q4', U1[1], 'medium',
  r"إذا كان باقي قسمة كثير الحدود $f(x)$ على $(x-3)$ يساوي $5$ ، فإنّ باقي قسمة $f(2x+1)$ على $(x-1)$ يساوي:",
  [O('5', 5), O('11', 11), O('3', 3), O('1', 1)],
  r"نظرية الباقي: $f(3)=5$ ، وباقي قسمة $g(x)=f(2x+1)$ على $(x-1)$ هو $g(1)=f(2(1)+1)=f(3)=5$",
  truth=lambda: expand((X-3)*(a*X+b)+5).subs(X, 2*1+1), tag='نظرية الباقي لاقتران مركب'),
# ---------------- unit 2
Q('m6q5', U2[2], 'medium',
  r"إذا كان $\tan\theta=-\frac{4}{3}$ ، حيث $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\tan\frac{\theta}{2}$ تساوي:",
  [O('2', 2), O('-2', -2), O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2))],
  r"في الربع الثاني: $\sin\theta=\frac45$ ، $\cos\theta=-\frac35$ ، و $\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$ فالظل موجب" "\n"
  r"$\tan\frac{\theta}{2}=\dfrac{\sin\theta}{1+\cos\theta}=\dfrac{\frac45}{\frac25}=2$",
  truth=tan((pi-atan(R(4, 3)))/2), tag='نصف الزاوية مع تحديد الربع'),
Q('m6q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(\frac{\pi}{6}+x)+\cos(\frac{\pi}{3}+x)', sin(pi/6+x)+cos(pi/3+x))),
  [O(r'\cos x', cos(x)), O(r'\sin x', sin(x)), O(r'\sqrt{3}\cos x', sqrt(3)*cos(x)), O(r'\sqrt{3}\sin x', sqrt(3)*sin(x))],
  r"$\sin\left(\frac{\pi}{6}+x\right)=\frac12\cos x+\frac{\sqrt3}{2}\sin x$ ، $\cos\left(\frac{\pi}{3}+x\right)=\frac12\cos x-\frac{\sqrt3}{2}\sin x$" "\n" r"بالجمع: $\cos x$",
  truth=sin(pi/6+x)+cos(pi/3+x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
Q('m6q7', U2[1], 'medium',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\sin x}{1-\cos x}-\cot x', sin(x)/(1-cos(x))-cot(x))),
  [O(r'\csc x', csc(x)), O(r'\sec x', sec(x)), O(r'2\csc x', 2*csc(x)), O(r'2\sec x', 2*sec(x))],
  r"$\dfrac{\sin x}{1-\cos x}-\dfrac{\cos x}{\sin x}=\dfrac{\sin^2x-\cos x+\cos^2x}{\sin x(1-\cos x)}=\dfrac{1-\cos x}{\sin x(1-\cos x)}=\csc x$",
  truth=sin(x)/(1-cos(x))-cot(x), tag='المتطابقات الأساسية'),
Q('m6q8', U2[2], 'medium',
  r"إذا كان: $\tan x+\cot x=4$ ، فإنّ قيمة $\sin 2x$ هي:",
  [O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{1}{4}', R(1, 4)), O('2', 2), O(r'\frac{1}{8}', R(1, 8))],
  r"$\tan x+\cot x=\dfrac{\sin^2x+\cos^2x}{\sin x\cos x}=\dfrac{1}{\sin x\cos x}=\dfrac{2}{\sin2x}$" "\n" r"$\dfrac{2}{\sin2x}=4 \Rightarrow \sin2x=\frac12$",
  truth=(lambda t_: simplify(2*t_/(1+t_**2)))(2+sqrt(3)), tag='ضعف الزاوية بمعلومية علاقة'),
Q('m6q9', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'\cos 2x+5\cos x+3', cos(2*x)+5*cos(x)+3)),
  [O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'),
   O(st(r'\frac{5\pi}{6}', r'\frac{7\pi}{6}'), S_(5*P/6, 7*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set')],
  r"$\cos2x=2\cos^2x-1$: $2\cos^2x+5\cos x+2=0 \Rightarrow (2\cos x+1)(\cos x+2)=0$" "\n"
  r"$\cos x=-2$ مرفوض، و $\cos x=-\frac12 \Rightarrow x=\frac{2\pi}{3},\ \frac{4\pi}{3}$",
  truth=lambda: sols(cos(2*x)+5*cos(x)+3, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
Q('m6q10', U2[3], 'hard',
  F(r"حلول المعادلة: $«0»=3$ في الفترة $(0,\,\pi)$ هي:", (r'2\sin x+\csc x', 2*sin(x)+csc(x))),
  [O(st(r'\frac{\pi}{6}', r'\frac{\pi}{2}', r'\frac{5\pi}{6}'), S_(P/6, P/2, 5*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'),
   O(st(r'\frac{\pi}{3}', r'\frac{\pi}{2}', r'\frac{2\pi}{3}'), S_(P/3, P/2, 2*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set')],
  r"نضرب في $\sin x\ne0$: $2\sin^2x-3\sin x+1=0 \Rightarrow (2\sin x-1)(\sin x-1)=0$" "\n"
  r"$\sin x=\frac12 \Rightarrow x=\frac{\pi}{6},\ \frac{5\pi}{6}$ ، و $\sin x=1 \Rightarrow x=\frac{\pi}{2}$",
  truth=lambda: sols(2*sin(x)+csc(x)-3, 0, pi, closed_lo=False), tag='معادلة فيها مقلوب نسبة'),
# ---------------- unit 3
Q('m6q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{3}\right)$ تساوي:", (r'\sec x-2\tan x', sec(x)-2*tan(x))),
  [O(r'2\sqrt{3}-8', 2*sqrt(3)-8), O(r'2\sqrt{3}+8', 2*sqrt(3)+8), O(r'-2\sqrt{3}-8', -2*sqrt(3)-8), O(r'8-2\sqrt{3}', 8-2*sqrt(3))],
  r"$f'(x)=\sec x\tan x-2\sec^2x$ ، و $\sec\frac{\pi}{3}=2$ ، $\tan\frac{\pi}{3}=\sqrt3$" "\n" r"$f'\left(\frac{\pi}{3}\right)=2\sqrt3-2(4)=2\sqrt3-8$",
  truth=Dx(sec(x)-2*tan(x)).subs(x, pi/3), tag='مشتقات الاقترانات المثلثية'),
Q('m6q12', U3[1], 'medium',
  F(r"النقطة الواقعة على منحنى الاقتران: $y=«0»$ ، حيث $x>0$ ، والتي يكون العمودي على المماس عندها موازيًا للمستقيم $x+2y=3$ هي:", (r'3\ln x-x', 3*log(x)-x)),
  [O(r'(1,\ -1)', Tuple(1, -1), 'tuple'), O(r'(1,\ 1)', Tuple(1, 1), 'tuple'),
   O(r'(6,\ 3\ln 6-6)', Tuple(6, 3*log(6)-6), 'tuple'), O(r'(6,\ 6-3\ln 6)', Tuple(6, 6-3*log(6)), 'tuple')],
  r"ميل المستقيم $-\frac12$ ، فميل العمودي $-\frac12$ وميل المماس $2$" "\n" r"$y'=\dfrac3x-1=2 \Rightarrow x=1$ ، و $y=3\ln1-1=-1$",
  truth=lambda: (lambda x0: Tuple(x0, 3*log(x0)-x0))(solve(Dx(3*log(x)-x)-2, x)[0]), tag='عمودي يوازي مستقيمًا معلومًا'),
Q('m6q13', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(1)=-1$ ، فإنّ قيمة الثابت $k$ هي:", (r'x^{3}-kx\ln x', x**3-k*x*log(x))),
  [O('4', 4), O('-4', -4), O('2', 2), O('-2', -2)],
  r"$f'(x)=3x^2-k(\ln x+1)$ ، إذن $f'(1)=3-k=-1 \Rightarrow k=4$",
  truth=lambda: solve(Dx(x**3-k*x*log(x)).subs(x, 1)+1, k)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
Q('m6q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''(x)+f'(x)-2f(x)$ يساوي:", (r'e^{2x}+3e^{x}', exp(2*x)+3*exp(x))),
  [O(r'4e^{2x}', 4*exp(2*x)), O(r'-4e^{2x}', -4*exp(2*x)), O(r'4e^{x}', 4*exp(x)), O(r'-4e^{x}', -4*exp(x))],
  r"$f'(x)=2e^{2x}+3e^x$ ، $f''(x)=4e^{2x}+3e^x$" "\n" r"$f''+f'-2f=(4+2-2)e^{2x}+(3+3-6)e^x=4e^{2x}$",
  truth=diff(exp(2*x)+3*exp(x), x, 2)+Dx(exp(2*x)+3*exp(x))-2*(exp(2*x)+3*exp(x)), tag='المشتقات العليا وتراكيبها'),
Q('m6q15', U3[2], 'medium',
  F(r"النقطة الواقعة على منحنى الاقتران: $f(x)=«0»$ ، والتي يكون المماس عندها أفقيًّا هي:", (r'(x^{2}+1)e^{x}', (x**2+1)*exp(x))),
  [O(r'(-1,\ \frac{2}{e})', Tuple(-1, 2/E), 'tuple'), O(r'(-1,\ 2e)', Tuple(-1, 2*E), 'tuple'), O(r'(1,\ \frac{2}{e})', Tuple(1, 2/E), 'tuple'), O(r'(1,\ 2e)', Tuple(1, 2*E), 'tuple')],
  r"$f'(x)=2xe^x+(x^2+1)e^x=e^x(x+1)^2$ ، و $e^x\ne0$ ، إذن $f'(x)=0 \Rightarrow x=-1$" "\n" r"$f(-1)=2e^{-1}=\dfrac2e$",
  truth=lambda: (lambda x0: Tuple(x0, (x0**2+1)*exp(x0)))(solve(Dx((x**2+1)*exp(x)), x)[0]), tag='نقاط المماس الأفقي'),
Q('m6q16', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنى الاقتران $f(x)$ ، والمستقيم $L$ المماس له عند $x=2$ ، والمارّ بالنقطتين المُبيّنتين. إذا كان: $h(x)=x^{2}f(x)$ ، فإنّ $h'(2)$ تساوي:",
  [O('16', 16), O('12', 12), O('4', 4), O('7', 7)],
  r"ميل $L$: $\dfrac{5-1}{4-0}=1$ ، فـ $f'(2)=1$ ، ونقطة التماس على $L$: $f(2)=2+1=3$" "\n"
  r"$h'(x)=2xf(x)+x^2f'(x) \Rightarrow h'(2)=2(2)(3)+4(1)=16$",
  truth=lambda: (lambda v_m: 2*2*v_m[0]+4*v_m[1])(tan_point_value(TP6, 2)),
  figure=figure('m6q16', fig_tangent(f6_16, TP6, (0, 5), (0, 5), (4.6, 1.2), (4.3, 5.5))), tag='المشتقة من التمثيل البياني'),
Q('m6q17', U3[3], 'medium',
  F(r"تتناقص كتلة مادة مُشعّة وفق الاقتران: $M(t)=«0»$ ، حيث $M$ الكتلة بالغرامات بعد $t$ سنة. معدّل تغيّر كتلة المادة عندما $t=5$ هو:", (r'80\cdot2^{-\frac{t}{5}}', 80*2**(-t/5))),
  [O(r'-8\ln 2', -8*log(2), units='g/year'), O(r'8\ln 2', 8*log(2), units='g/year'), O(r'-\frac{8}{\ln 2}', -8/log(2), units='g/year'), O(r'\frac{8}{\ln 2}', 8/log(2), units='g/year')],
  r"$M'(t)=80\cdot2^{-\frac t5}\ln2\cdot\left(-\frac15\right)=-16\ln2\cdot2^{-\frac t5}$" "\n" r"$M'(5)=-16\ln2\cdot\frac12=-8\ln2\ \text{g/year}$",
  truth=diff(80*2**(-t/5), t).subs(t, 5), tag='معدل التغير في سياق حياتي'),
Q('m6q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>1$ ، فإنّ $f'(e)$ تساوي:", (r'\log_{2}(\ln x)', log(log(x), 2))),
  [O(r'\frac{1}{e\ln 2}', 1/(E*log(2))), O(r'\frac{e}{\ln 2}', E/log(2)), O(r'\frac{\ln 2}{e}', log(2)/E), O(r'e\ln 2', E*log(2))],
  r"$f'(x)=\dfrac{1}{\ln x\cdot\ln2}\cdot\dfrac1x$ ، و $\ln e=1$ ، إذن $f'(e)=\dfrac{1}{e\ln2}$",
  truth=Dx(log(log(x), 2)).subs(x, E), tag='مشتقة اللوغاريتم لأساس غير e'),
Q('m6q19', U3[3], 'easy',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، حيث $t>0$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=2$ هي:", (r't+\frac{1}{t}', t+1/t), (r't-\frac{1}{t}', t-1/t)),
  [O(r'\frac{5}{3}', R(5, 3)), O(r'-\frac{5}{3}', -R(5, 3)), O(r'\frac{3}{5}', R(3, 5)), O(r'-\frac{3}{5}', -R(3, 5))],
  r"$\dfrac{dx}{dt}=1-\dfrac1{t^2}=\dfrac34$ ، $\dfrac{dy}{dt}=1+\dfrac1{t^2}=\dfrac54$ عندما $t=2$" "\n" r"$\dfrac{dy}{dx}=\dfrac{5/4}{3/4}=\dfrac53$",
  truth=(diff(t-1/t, t)/diff(t+1/t, t)).subs(t, 2), tag='مشتقة المعادلات الوسيطية'),
Q('m6q20', U3[4], 'hard',
  F(r"إذا كان: $«0»=y+1$ ، فإنّ $\dfrac{dy}{dx}$ عندما $x=0$ هي:", (r'xe^{y}', x*exp(y))),
  [O(r'\frac{1}{e}', 1/E), O(r'-\frac{1}{e}', -1/E), O('e', E), O('-e', -E)],
  r"عندما $x=0$: $0=y+1 \Rightarrow y=-1$" "\n" r"باشتقاق الطرفين: $e^y+xe^y\dfrac{dy}{dx}=\dfrac{dy}{dx}$ ، وعند $(0,-1)$: $e^{-1}+0=\dfrac{dy}{dx}$ ، أي $\dfrac{dy}{dx}=\dfrac1e$",
  truth=imp(x*exp(y)-y-1, (0, -1)), tag='الاشتقاق الضمني عند نقطة'),
Q('m6q21', U3[4], 'hard',
  F(r"المقطع $x$ للمماس لمنحنى العلاقة: $«0»=6xy$ عند النقطة $(3,\,3)$ هو:", (r'x^{3}+y^{3}', x**3+y**3)),
  [O('6', 6), O('-6', -6), O('3', 3), O('-3', -3)],
  r"$3x^2+3y^2y'=6y+6xy'$ ، وعند $(3,3)$: $27+27y'=18+18y' \Rightarrow y'=-1$" "\n" r"المماس: $y-3=-(x-3)$ ، وعند $y=0$: $x=6$",
  truth=lambda: tangent_x_intercept(x**3+y**3-6*x*y, (3, 3)), tag='مماس منحنى علاقة ضمنية'),
Q('m6q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي خزّانًا على شكل مخروط دائري قائم رأسه إلى الأسفل، ارتفاعه $6\ \text{m}$ ونصف قطر قاعدته $3\ \text{m}$. يُضَخّ إليه الماء بمعدّل $200\ \text{L/min}$ ، فإنّ معدّل ارتفاع سطح الماء عندما يكون عمق الماء $4\ \text{m}$ هو:",
  [O(r'\frac{1}{20\pi}', 1/(20*pi), units='m/min'), O(r'\frac{1}{80\pi}', 1/(80*pi), units='m/min'), O(r'\frac{50}{\pi}', 50/pi, units='m/min'), O(r'\frac{25}{2\pi}', 25/(2*pi), units='m/min')],
  r"بالتشابه: $\dfrac rh=\dfrac36 \Rightarrow r=\dfrac h2$ ، و $V=\dfrac13\pi r^2h=\dfrac{\pi h^3}{12}$" "\n"
  r"$200\ \text{L/min}=0.2\ \text{m}^3/\text{min}$ ، و $\dfrac{dV}{dt}=\dfrac{\pi h^2}{4}\dfrac{dh}{dt} \Rightarrow 0.2=4\pi\dfrac{dh}{dt} \Rightarrow \dfrac{dh}{dt}=\dfrac{1}{20\pi}$",
  truth=R(2, 10)/diff(pi*(h_/2)**2*h_/3, h_).subs(h_, 4), figure=figure('m6q22', fig_cone(), 3.0, 3.2), tag='معدلات مرتبطة مع تحويل الوحدات'),
# ---------------- unit 4
Q('m6q23', U4[1], 'medium',
  r"الصورة المثلثية للعدد المُركَّب $z=(1-i)(\sqrt{3}+i)$ هي:",
  [O(trig(r'2\sqrt{2}', r'-\frac{\pi}{12}'), pol(2*sqrt(2), -P/12)), O(trig(r'2\sqrt{2}', r'\frac{\pi}{12}'), pol(2*sqrt(2), P/12)),
   O(trig(r'2\sqrt{2}', r'\frac{5\pi}{12}'), pol(2*sqrt(2), 5*P/12)), O(trig(r'2\sqrt{2}', r'-\frac{5\pi}{12}'), pol(2*sqrt(2), -5*P/12))],
  r"$|1-i|=\sqrt2$ ، $\text{Arg}(1-i)=-\frac{\pi}{4}$ ، $|\sqrt3+i|=2$ ، $\text{Arg}(\sqrt3+i)=\frac{\pi}{6}$" "\n"
  r"عند الضرب نضرب المقاييس ونجمع السعات: $|z|=2\sqrt2$ ، $\text{Arg}(z)=-\frac{\pi}{4}+\frac{\pi}{6}=-\frac{\pi}{12}$",
  truth=expand((1-I)*(sqrt(3)+I)), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
Q('m6q24', U4[2], 'medium',
  r"ناتج $z^{2}w$ هو:",
  [O('17+7i', 17+7*I), O('17-7i', 17-7*I), O('-7+7i', -7+7*I), O('-7-7i', -7-7*I)],
  r"$z^2=(3+2i)^2=9+12i+4i^2=5+12i$" "\n" r"$z^2w=(5+12i)(1-i)=5-5i+12i-12i^2=17+7i$",
  truth=expand((3+2*I)**2*(1-I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=3+2i$ ، $w=1-i$", 24, 25)),
Q('m6q25', U4[2], 'medium',
  r"ناتج $\dfrac{\bar{z}}{w}$ في الصورة القياسية هو:",
  [O(r'\frac{5+i}{2}', (5+I)/2), O(r'\frac{5-i}{2}', (5-I)/2), O(r'\frac{1+5i}{2}', (1+5*I)/2), O(r'\frac{1-5i}{2}', (1-5*I)/2)],
  r"$\bar z=3-2i$ ، $\dfrac{3-2i}{1-i}\cdot\dfrac{1+i}{1+i}=\dfrac{3+3i-2i-2i^2}{2}=\dfrac{5+i}{2}$",
  truth=(3-2*I)/(1-I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
Q('m6q26', U4[1], 'medium',
  r"قيم الثابت الحقيقي $a$ التي تجعل العدد $z=(a+2i)^{2}$ عددًا تخيّليًّا بحتًا هي:",
  [O(r'\pm 2', S_(2, -2), 'set'), O(r'\pm 4', S_(4, -4), 'set'), O(r'\pm 1', S_(1, -1), 'set'), O(r'\pm\sqrt{2}', S_(sqrt(2), -sqrt(2)), 'set')],
  r"$z=a^2+4ai+4i^2=(a^2-4)+4ai$" "\n" r"تخيّلي بحت: $a^2-4=0 \Rightarrow a=\pm2$ ، والجزء التخيلي $4a=\pm8\ne0$ ✔",
  truth=lambda: FiniteSet(*[r_ for r_ in solve(re(expand((X+2*I)**2)), X) if im(expand((X+2*I)**2)).subs(X, r_) != 0]),
  tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
Q('m6q27', U4[2], 'hard',
  r"إذا كان العدد $1-i$ أحد جذور المعادلة: $z^{3}+az+4=0$ ، حيث $a$ عدد حقيقي، فإنّ قيمة $a$ هي:",
  [O('-2', -2), O('2', 2), O('-4', -4), O('4', 4)],
  r"$(1-i)^2=-2i$ ، $(1-i)^3=-2i(1-i)=-2-2i$" "\n" r"$-2-2i+a(1-i)+4=0 \Rightarrow (2+a)+(-2-a)i=0 \Rightarrow a=-2$",
  truth=lambda: (lambda e_: solve([re(e_), im(e_)], X)[X])(expand((1-I)**3+X*(1-I)+4)), tag='معادلة كثير حدود بجذر مركب'),
Q('m6q28', U4[2], 'hard',
  r"إذا كان: $z_1=-2i$ ، $z_2=-1+i$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{3\pi}{4}', 3*P/4), O(r'\frac{5\pi}{4}', 5*P/4), O(r'\frac{\pi}{4}', P/4), O(r'\frac{\pi}{2}', P/2)],
  r"$\text{Arg}(z_1)=-\frac{\pi}{2}$ ، $\text{Arg}(z_2)=\frac{3\pi}{4}$ ، والفرق $\frac{3\pi}{4}+\frac{\pi}{2}=\frac{5\pi}{4}>\pi$" "\n" r"فالزاوية الصغرى $2\pi-\frac{5\pi}{4}=\frac{3\pi}{4}$",
  truth=smaller_angle(-2*I, -1+I), tag='الزاوية بين عددين مركبين'),
Q('m6q29', U4[3], 'medium',
  r"إذا كان: $|z-3+4i|=2$ ، فإنّ أكبر قيمة للمقدار $|z|$ هي:",
  [O('7', 7), O('5', 5), O('3', 3), O('2', 2)],
  r"المحل دائرة مركزها $(3,-4)$ ونصف قطرها $2$ ، وبُعد مركزها عن الأصل $\sqrt{9+16}=5$" "\n" r"أبعد نقطة عن الأصل على امتداد القطر المارّ بالأصل: $|z|_{\max}=5+2=7$",
  truth=Abs(3-4*I)+2, tag='القيمة العظمى والصغرى للمقياس على محل هندسي'),
IndexQ('m6q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z-1|<2$ ، $-\frac{\pi}{4}\le\text{Arg}(z+1)\le\frac{\pi}{4}$', R6),
   T(r'$|z-1|\le2$ ، $-\frac{\pi}{4}\le\text{Arg}(z+1)\le\frac{\pi}{4}$', both(disk(1, 2), sector(-1, -math.pi/4, math.pi/4))),
   T(r'$|z-1|<2$ ، $-\frac{\pi}{4}\le\text{Arg}(z-1)\le\frac{\pi}{4}$', both(disk(1, 2, strict=True), sector(1, -math.pi/4, math.pi/4))),
   T(r'$|z-1|\le2$ ، $-\frac{\pi}{4}\le\text{Arg}(z-1)\le\frac{\pi}{4}$', both(disk(1, 2), sector(1, -math.pi/4, math.pi/4)))],
  r"القوس جزء من دائرة مركزها $(1,0)$ ونصف قطرها $2$ ، وهو متقطّع: $|z-1|<2$" "\n"
  r"والقطعتان تبدآن من النقطة $(-1,0)$ (العدد $-1$) بزاويتي $\pm\frac{\pi}{4}$ ، وتمرّان بالنقطتين $(1,\pm2)$: $-\frac{\pi}{4}\le\text{Arg}(z+1)\le\frac{\pi}{4}$",
  truth=region_truth(R6, PR6, 4), figure=figure('m6q30', fig_region2(R6, PR6, 4), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 7
TP7 = [(1, 4), (5, 2)]                       # tangent to f at x=3
f7_16 = lambda s_: 3 - 0.5*(s_ - 3) + 0.3*(s_ - 3)**2
R7 = both(closer(0, 4), sector(0, 0, math.pi/3))
PR7 = [('seg', 0j, 2 + 0j, False), ('seg', 2 + 0j, 2 + 2*math.sqrt(3)*1j, True), ('seg', 0j, 2 + 2*math.sqrt(3)*1j, False),
       ('line', 2 - 4.9j, 2 + 4.9j), ('open', 0j)]
P7 = [
# ---------------- unit 1
Q('m7q1', U1[1], 'medium',
  F(r"إذا كان $x=\frac{2}{3}$ حلًّا للمعادلة: $«0»=0$ ، فإنّ الحلّين الآخرين لها هما:", (r'3x^{3}-2x^{2}-6x+4', 3*x**3-2*x**2-6*x+4)),
  [O(st(r'\sqrt{2}', r'-\sqrt{2}'), S_(sqrt(2), -sqrt(2)), 'set'), O(st('2', '-2'), S_(2, -2), 'set'),
   O(st(r'1+\sqrt{2}', r'1-\sqrt{2}'), S_(1+sqrt(2), 1-sqrt(2)), 'set'), O(st(r'\sqrt{3}', r'-\sqrt{3}'), S_(sqrt(3), -sqrt(3)), 'set')],
  r"بالقسمة التركيبية على $\left(x-\frac23\right)$: $3,\ -2,\ -6,\ 4 \to 3,\ 0,\ -6,\ 0$ ، فالناتج $3x^2-6$" "\n" r"$3x^2-6=0 \Rightarrow x^2=2 \Rightarrow x=\pm\sqrt2$",
  truth=lambda: other_roots(3*x**3-2*x**2-6*x+4, R(2, 3)), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
Q('m7q2', U1[2], 'medium',
  F(r"أيّ الآتية يُمثّل تجزئة المقدار النسبي: $«0»$ إلى كسور جزئية؟", (r'\frac{x^{2}+3x+2}{x(x+1)(x-2)}', (x**2+3*x+2)/(x*(x+1)*(x-2)))),
  [O(r'-\frac{1}{x}+\frac{2}{x-2}', -1/x+2/(x-2)), O(r'\frac{1}{x}+\frac{2}{x-2}', 1/x+2/(x-2)),
   O(r'-\frac{1}{x}-\frac{2}{x-2}', -1/x-2/(x-2)), O(r'\frac{1}{x}-\frac{2}{x-2}', 1/x-2/(x-2))],
  r"نبسّط أولًا: $x^2+3x+2=(x+1)(x+2)$ ، فالمقدار $\dfrac{x+2}{x(x-2)}$ (حيث $x\ne-1$)" "\n"
  r"$x+2=A(x-2)+Bx$: عند $x=0$: $A=-1$ ، وعند $x=2$: $B=2$",
  truth=(x**2+3*x+2)/(x*(x+1)*(x-2)), tag='تجزئة: تبسيط المقدار أولًا'),
Q('m7q3', U1[1], 'hard',
  F(r"إذا كان باقي قسمة الاقتران: $f(x)=«0»$ على $«1»$ يساوي $7$ ، فإنّ قيمة الثابت $a$ هي:", (r'x^{3}+ax^{2}+bx+3', x**3+a*x**2+b*x+3), (r'x^{2}+x-2', x**2+x-2)),
  [O('3', 3), O('-3', -3), O('6', 6), O('-6', -6)],
  r"$x^2+x-2=(x-1)(x+2)$ ، والباقي الثابت $7$ يعني $f(1)=7$ و $f(-2)=7$" "\n"
  r"$f(1)=4+a+b=7 \Rightarrow a+b=3$ ، $f(-2)=-5+4a-2b=7 \Rightarrow 2a-b=6$ ، بالجمع: $3a=9 \Rightarrow a=3$",
  truth=lambda: solve([rem(x**3+a*x**2+b*x+3, 1)-7, rem(x**3+a*x**2+b*x+3, -2)-7], [a, b])[a], tag='باقي القسمة على مقدار تربيعي'),
Q('m7q4', U1[2], 'hard',
  F(r"إذا كان: $«0»=\dfrac{A}{x}+\dfrac{B}{x+1}+\dfrac{C}{x+3}$ ، فإنّ قيمة $A+B+C$ هي:", (r'\frac{x^{2}+2x+3}{x(x+1)(x+3)}', (x**2+2*x+3)/(x*(x+1)*(x+3)))),
  [O('1', 1), O('3', 3), O('-1', -1), O('-3', -3)],
  r"$x^2+2x+3=A(x+1)(x+3)+Bx(x+3)+Cx(x+1)$" "\n" r"عند $x=0$: $A=1$ ، عند $x=-1$: $2=-2B \Rightarrow B=-1$ ، عند $x=-3$: $6=6C \Rightarrow C=1$ ، فالمجموع $1$",
  truth=lambda: (lambda s_: s_[A_]+s_[B_]+s_[C_])(solve_pf((x**2+2*x+3)/(x*(x+1)*(x+3)), A_/x+B_/(x+1)+C_/(x+3), [A_, B_, C_])),
  tag='إيجاد ثوابت في التجزئة'),
# ---------------- unit 2
Q('m7q5', U2[2], 'medium',
  r"إذا كان $\sin\theta=-\frac{24}{25}$ ، حيث $\frac{3\pi}{2}<\theta<2\pi$ ، فإنّ قيمة $\cos\frac{\theta}{2}$ تساوي:",
  [O(r'-\frac{4}{5}', -R(4, 5)), O(r'\frac{4}{5}', R(4, 5)), O(r'-\frac{3}{5}', -R(3, 5)), O(r'\frac{3}{5}', R(3, 5))],
  r"في الربع الرابع $\cos\theta=\frac{7}{25}$ ، و $\frac{3\pi}{4}<\frac{\theta}{2}<\pi$ (الربع الثاني) فجيب التمام سالب" "\n"
  r"$\cos\frac{\theta}{2}=-\sqrt{\dfrac{1+\frac{7}{25}}{2}}=-\sqrt{\dfrac{16}{25}}=-\dfrac45$",
  truth=cos((2*pi-asin(R(24, 25)))/2), tag='نصف الزاوية مع تحديد الربع'),
Q('m7q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(x+\frac{\pi}{3})+\sin(x-\frac{\pi}{3})', sin(x+pi/3)+sin(x-pi/3))),
  [O(r'\sin x', sin(x)), O(r'2\sin x', 2*sin(x)), O(r'\cos x', cos(x)), O(r'2\cos x', 2*cos(x))],
  r"$\sin x\cos\frac{\pi}{3}+\cos x\sin\frac{\pi}{3}+\sin x\cos\frac{\pi}{3}-\cos x\sin\frac{\pi}{3}=2\sin x\cdot\frac12=\sin x$",
  truth=sin(x+pi/3)+sin(x-pi/3), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
Q('m7q7', U2[2], 'medium',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{1+\tan^{2}x}{\tan x}', (1+tan(x)**2)/tan(x))),
  [O(r'2\csc 2x', 2*csc(2*x)), O(r'\csc 2x', csc(2*x)), O(r'2\sec 2x', 2*sec(2*x)), O(r'\sec 2x', sec(2*x))],
  r"$\dfrac{\sec^2x}{\tan x}=\dfrac{1}{\cos^2x}\cdot\dfrac{\cos x}{\sin x}=\dfrac{1}{\sin x\cos x}=\dfrac{2}{\sin2x}=2\csc2x$",
  truth=(1+tan(x)**2)/tan(x), tag='المتطابقات الأساسية'),
Q('m7q8', U2[2], 'hard',
  r"قيمة المقدار: $\cos20^\circ\cos40^\circ\cos80^\circ$ هي:",
  [O(r'\frac{1}{8}', R(1, 8)), O(r'\frac{1}{4}', R(1, 4)), O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{1}{16}', R(1, 16))],
  r"نضرب ونقسم على $\sin20^\circ$ ونستعمل $2\sin A\cos A=\sin2A$ ثلاث مرات:" "\n"
  r"$\dfrac{8\sin20^\circ\cos20^\circ\cos40^\circ\cos80^\circ}{8\sin20^\circ}=\dfrac{\sin160^\circ}{8\sin20^\circ}=\dfrac18$",
  truth=cos(deg(20))*cos(deg(40))*cos(deg(80)), tag='قيم دقيقة بمتطابقات ضعف الزاوية'),
Q('m7q9', U2[3], 'easy',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\sin^{2}x-3\cos x', 2*sin(x)**2-3*cos(x))),
  [O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set'),
   O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set'), O(st(r'\frac{5\pi}{6}', r'\frac{7\pi}{6}'), S_(5*P/6, 7*P/6), 'set')],
  r"$2(1-\cos^2x)-3\cos x=0 \Rightarrow 2\cos^2x+3\cos x-2=0 \Rightarrow (2\cos x-1)(\cos x+2)=0$" "\n" r"$\cos x=-2$ مرفوض، $\cos x=\frac12 \Rightarrow x=\frac{\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*sin(x)**2-3*cos(x), 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
Q('m7q10', U2[3], 'hard',
  F(r"حلول المعادلة: $«0»=-\frac{\sqrt{3}}{2}$ في الفترة $\left(\frac{\pi}{2},\,\pi\right)$ هي:", (r'\cos^{2}2x-\sin^{2}2x', cos(2*x)**2-sin(2*x)**2)),
  [O(st(r'\frac{17\pi}{24}', r'\frac{19\pi}{24}'), S_(17*P/24, 19*P/24), 'set'), O(st(r'\frac{5\pi}{24}', r'\frac{7\pi}{24}'), S_(5*P/24, 7*P/24), 'set'),
   O(st(r'\frac{17\pi}{12}', r'\frac{19\pi}{12}'), S_(17*P/12, 19*P/12), 'set'), O(st(r'\frac{5\pi}{12}', r'\frac{7\pi}{12}'), S_(5*P/12, 7*P/12), 'set')],
  r"$\cos^22x-\sin^22x=\cos4x=-\frac{\sqrt3}{2}$ ، و $\frac{\pi}{2}<x<\pi \Rightarrow 2\pi<4x<4\pi$" "\n"
  r"$4x=2\pi+\frac{5\pi}{6}=\frac{17\pi}{6}$ أو $4x=2\pi+\frac{7\pi}{6}=\frac{19\pi}{6}$ ، إذن $x=\frac{17\pi}{24},\ \frac{19\pi}{24}$",
  truth=lambda: sols(cos(4*x)+sqrt(3)/2, pi/2, pi, closed_lo=False), tag='معادلة بزاوية مضاعفة في فترة'),
# ---------------- unit 3
Q('m7q11', U3[1], 'medium',
  F(r"معادلة المماس لمنحنى الاقتران: $f(x)=«0»$ عند $x=1$ هي:", (r'e^{x}+e\ln x', exp(x)+E*log(x))),
  [O('y=2ex-e', 2*E*x-E, 'eq'), O('y=2ex+e', 2*E*x+E, 'eq'), O('y=ex-e', E*x-E, 'eq'), O('y=ex+e', E*x+E, 'eq')],
  r"$f(1)=e+e\ln1=e$ ، $f'(x)=e^x+\dfrac ex \Rightarrow f'(1)=2e$" "\n" r"المماس: $y-e=2e(x-1) \Rightarrow y=2ex-e$",
  truth=(lambda f_: f_.subs(x, 1)+Dx(f_).subs(x, 1)*(x-1))(exp(x)+E*log(x)), tag='معادلة المماس ومقاطعه'),
Q('m7q12', U3[1], 'easy',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t\ge0$ الزمن بالثواني، و $s$ الموقع بالأمتار. سرعة الجُسيم المتجهة في اللحظة التي ينعدم فيها تسارعه هي:", (r't^{3}-9t^{2}+15t', t**3-9*t**2+15*t)),
  [O('-12', -12, units='m/s'), O('12', 12, units='m/s'), O('15', 15, units='m/s'), O('-15', -15, units='m/s')],
  r"$v(t)=3t^2-18t+15$ ، $a(t)=6t-18=0 \Rightarrow t=3$" "\n" r"$v(3)=27-54+15=-12\ \text{m/s}$",
  truth=lambda: diff(t**3-9*t**2+15*t, t).subs(t, solve(diff(t**3-9*t**2+15*t, t, 2), t)[0]), tag='الحركة: السرعة والتسارع'),
Q('m7q13', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>0$ ، وكان: $f'(e)=3$ ، فإنّ قيمة الثابت $a$ هي:", (r'(x+a)\ln x', (x+a)*log(x))),
  [O('e', E), O('-e', -E), O('2e', 2*E), O('-2e', -2*E)],
  r"$f'(x)=\ln x+\dfrac{x+a}{x}$ ، إذن $f'(e)=1+\dfrac{e+a}{e}=2+\dfrac ae=3 \Rightarrow a=e$",
  truth=lambda: solve(Dx((x+a)*log(x)).subs(x, E)-3, a)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
Q('m7q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f^{(20)}(0)$ تساوي:", (r'xe^{-x}', x*exp(-x))),
  [O('-20', -20), O('20', 20), O('-21', -21), O('21', 21)],
  r"$f'(x)=(1-x)e^{-x}$ ، $f''(x)=(x-2)e^{-x}$ ، $f'''(x)=(3-x)e^{-x}$ ، فالنمط: $f^{(n)}(x)=(-1)^n(x-n)e^{-x}$" "\n" r"$f^{(20)}(0)=(+1)(0-20)e^0=-20$",
  truth=diff(x*exp(-x), x, 20).subs(x, 0), tag='المشتقات العليا: إيجاد نمط'),
Q('m7q15', U3[2], 'medium',
  r"إذا كان: $f(1)=2,\ f'(1)=-1,\ g(1)=3,\ g'(1)=4$ ، وكان: $h(x)=\dfrac{xf(x)}{g(x)}$ ، فإنّ $h'(1)$ تساوي:",
  [O(r'-\frac{5}{9}', -R(5, 9)), O(r'\frac{5}{9}', R(5, 9)), O(r'-\frac{11}{9}', -R(11, 9)), O(r'\frac{11}{9}', R(11, 9))],
  r"البسط $u=xf(x)$: $u(1)=2$ ، $u'(x)=f(x)+xf'(x) \Rightarrow u'(1)=2-1=1$" "\n" r"$h'(1)=\dfrac{u'(1)g(1)-u(1)g'(1)}{g(1)^2}=\dfrac{3-8}{9}=-\dfrac59$",
  truth=diff(x*(2-(x-1))/(3+4*(x-1)), x).subs(x, 1), tag='مشتقة الضرب والقسمة من قيم معطاة'),
Q('m7q16', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنى الاقتران $f(x)$ ، والمستقيم $L$ المماس له عند $x=3$ ، والمارّ بالنقطتين المُبيّنتين. إذا كان: $h(x)=\dfrac{f(x)}{x-1}$ ، فإنّ $h'(3)$ تساوي:",
  [O('-1', -1), O('1', 1), O('-2', -2), O('2', 2)],
  r"ميل $L$: $\dfrac{2-4}{5-1}=-\dfrac12=f'(3)$ ، و $f(3)$ هي قيمة $L$ عند $x=3$: $4-\frac12(2)=3$" "\n"
  r"$h'(3)=\dfrac{f'(3)(3-1)-f(3)(1)}{(3-1)^2}=\dfrac{-1-3}{4}=-1$",
  truth=lambda: (lambda v_m: (v_m[1]*2-v_m[0])/4)(tan_point_value(TP7, 3)),
  figure=figure('m7q16', fig_tangent(f7_16, TP7, (0, 6), (0, 6), (5.3, 4.7), (0.3, 4.75))), tag='المشتقة من التمثيل البياني'),
Q('m7q17', U3[3], 'easy',
  F(r"يُعطى عدد مستخدمي تطبيق إلكتروني (بالآلاف) بعد $t$ شهر من إطلاقه بالاقتران: $U(t)=«0»$. معدّل تغيّر عدد المستخدمين (ألف مستخدم/شهر) عندما $t=4$ هو:", (r'\frac{60t}{t+2}', 60*t/(t+2))),
  [O(r'\frac{10}{3}', R(10, 3)), O('10', 10), O('40', 40), O(r'\frac{5}{3}', R(5, 3))],
  r"$U'(t)=\dfrac{60(t+2)-60t}{(t+2)^2}=\dfrac{120}{(t+2)^2}$ ، إذن $U'(4)=\dfrac{120}{36}=\dfrac{10}{3}$",
  truth=diff(60*t/(t+2), t).subs(t, 4), tag='معدل التغير في سياق حياتي'),
Q('m7q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'\log_{2}\sqrt{x+3}', log(sqrt(x+3), 2))),
  [O(r'\frac{1}{8\ln 2}', 1/(8*log(2))), O(r'\frac{1}{4\ln 2}', 1/(4*log(2))), O(r'\frac{\ln 2}{8}', log(2)/8), O(r'\frac{\ln 2}{4}', log(2)/4)],
  r"$f(x)=\frac12\log_2(x+3)$ ، $f'(x)=\dfrac{1}{2(x+3)\ln2}$ ، إذن $f'(1)=\dfrac{1}{8\ln2}$",
  truth=Dx(log(sqrt(x+3), 2)).subs(x, 1), tag='مشتقة اللوغاريتم لأساس غير e'),
Q('m7q19', U3[3], 'easy',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، حيث $0<t<\frac{\pi}{2}$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\frac{\pi}{6}$ هي:", (r'\sec t', sec(t)), (r'\tan t', tan(t))),
  [O('2', 2), O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2)],
  r"$\dfrac{dy}{dx}=\dfrac{\sec^2t}{\sec t\tan t}=\dfrac{\sec t}{\tan t}=\dfrac{1}{\sin t}=\csc t$ ، وعند $t=\frac{\pi}{6}$: $\csc\frac{\pi}{6}=2$",
  truth=(diff(tan(t), t)/diff(sec(t), t)).subs(t, pi/6), tag='مشتقة المعادلات الوسيطية'),
Q('m7q20', U3[4], 'medium',
  F(r"إذا كان: $«0»=2$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(2,\,1)$ تساوي:", (r'\ln y+xy', log(y)+x*y)),
  [O(r'-\frac{1}{3}', -R(1, 3)), O(r'\frac{1}{3}', R(1, 3)), O('-1', -1), O('1', 1)],
  r"$\dfrac{y'}{y}+y+xy'=0$ ، وعند $(2,1)$: $y'+1+2y'=0 \Rightarrow y'=-\dfrac13$",
  truth=imp(log(y)+x*y-2, (2, 1)), tag='الاشتقاق الضمني عند نقطة'),
Q('m7q21', U3[4], 'hard',
  F(r"المقطع $x$ للمماس لمنحنى العلاقة: $«0»=6$ عند النقطة $(1,\,2)$ هو:", (r'y^{3}-xy', y**3-x*y)),
  [O('-10', -10), O('10', 10), O('12', 12), O('-12', -12)],
  r"$3y^2y'-y-xy'=0$ ، وعند $(1,2)$: $12y'-2-y'=0 \Rightarrow y'=\dfrac{2}{11}$" "\n" r"المماس: $y-2=\frac{2}{11}(x-1)$ ، وعند $y=0$: $x-1=-11 \Rightarrow x=-10$",
  truth=lambda: tangent_x_intercept(y**3-x*y-6, (1, 2)), tag='مماس منحنى علاقة ضمنية'),
Q('m7q22', U3[5], 'medium',
  r"يُبيّن الشكل الآتي طائرة ورقية تطير على ارتفاع ثابت $60\ \text{m}$ ، وتتحرّك أفقيًّا مبتعدةً عن الشخص الذي يمسك خيطها بسرعة $2\ \text{m/s}$. إذا بقي الخيط مشدودًا مستقيمًا، فإنّ معدّل تغيّر طول الخيط عندما يكون طوله $100\ \text{m}$ هو:",
  [D('1.6', 'm/s'), D('1.2', 'm/s'), D('2.5', 'm/s'), D('2', 'm/s')],
  r"$\ell^2=x^2+60^2$ ، وعندما $\ell=100$: $x=80$" "\n" r"$2\ell\dfrac{d\ell}{dt}=2x\dfrac{dx}{dt} \Rightarrow 100\dfrac{d\ell}{dt}=80(2) \Rightarrow \dfrac{d\ell}{dt}=1.6\ \text{m/s}$",
  truth=R(80, 100)*2, figure=figure('m7q22', fig_kite(), 3.8, 2.6), tag='معدلات مرتبطة: نظرية فيثاغورس'),
# ---------------- unit 4
Q('m7q23', U4[1], 'easy',
  r"إذا كان: $|z|=6$ ، و $\text{Arg}(z)=-\frac{3\pi}{4}$ ، فإنّ الصورة القياسية للعدد المُركَّب $z$ هي:",
  [O(r'-3\sqrt{2}-3\sqrt{2}i', -3*sqrt(2)-3*sqrt(2)*I), O(r'3\sqrt{2}-3\sqrt{2}i', 3*sqrt(2)-3*sqrt(2)*I),
   O(r'-3\sqrt{2}+3\sqrt{2}i', -3*sqrt(2)+3*sqrt(2)*I), O(r'3\sqrt{2}+3\sqrt{2}i', 3*sqrt(2)+3*sqrt(2)*I)],
  r"$z=6\left(\cos\left(-\frac{3\pi}{4}\right)+i\sin\left(-\frac{3\pi}{4}\right)\right)=6\left(-\frac{\sqrt2}{2}-\frac{\sqrt2}{2}i\right)=-3\sqrt2-3\sqrt2i$",
  truth=expand(pol(6, -3*P/4)), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
Q('m7q24', U4[2], 'easy',
  r"ناتج $3z-iw$ هو:",
  [O('9+4i', 9+4*I), O('3+4i', 3+4*I), O('9+2i', 9+2*I), O('3+2i', 3+2*I)],
  r"$3z=6+3i$ ، $iw=i(-1+3i)=-i+3i^2=-3-i$" "\n" r"$3z-iw=6+3i+3+i=9+4i$",
  truth=expand(3*(2+I)-I*(-1+3*I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=2+i$ ، $w=-1+3i$", 24, 25)),
Q('m7q25', U4[2], 'medium',
  r"ناتج $\dfrac{w}{z}$ في الصورة القياسية هو:",
  [O(r'\frac{1+7i}{5}', (1+7*I)/5), O(r'\frac{1-7i}{5}', (1-7*I)/5), O(r'\frac{-1+7i}{5}', (-1+7*I)/5), O(r'\frac{-1-7i}{5}', (-1-7*I)/5)],
  r"$\dfrac{-1+3i}{2+i}\cdot\dfrac{2-i}{2-i}=\dfrac{-2+i+6i-3i^2}{5}=\dfrac{1+7i}{5}$",
  truth=(-1+3*I)/(2+I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
Q('m7q26', U4[1], 'medium',
  r"قيم الثابت الحقيقي $a$ التي تجعل العدد $z=\dfrac{a+i}{a-i}$ عددًا تخيّليًّا بحتًا هي:",
  [O(r'\pm 1', S_(1, -1), 'set'), O('1', S_(1), 'set'), O(r'\pm 2', S_(2, -2), 'set'), O('0', S_(0), 'set')],
  r"$z=\dfrac{(a+i)(a+i)}{(a-i)(a+i)}=\dfrac{a^2-1+2ai}{a^2+1}$" "\n" r"تخيّلي بحت: $a^2-1=0 \Rightarrow a=\pm1$ ، والجزء التخيلي $\frac{2a}{a^2+1}\ne0$ ✔",
  truth=lambda: FiniteSet(*[r_ for r_ in solve(re(expand((X+I)**2)), X) if im(expand((X+I)**2)).subs(X, r_) != 0]),
  tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
Q('m7q27', U4[2], 'hard',
  r"إذا كان العدد المُركَّب $\dfrac{5}{2-i}$ أحد جذري المعادلة: $z^{2}+bz+c=0$ ، حيث $b,\ c$ عددان حقيقيان، فإنّ قيمة $b+c$ هي:",
  [O('1', 1), O('9', 9), O('-1', -1), O('-9', -9)],
  r"$\dfrac{5}{2-i}=\dfrac{5(2+i)}{5}=2+i$ ، والجذر الآخر المرافق $2-i$" "\n" r"المجموع $4=-b \Rightarrow b=-4$ ، والضرب $(2+i)(2-i)=5=c$ ، إذن $b+c=1$",
  truth=lambda: (lambda r_: -2*re(r_)+re(r_)**2+im(r_)**2)(expand(simplify(5/(2-I)))), tag='معادلة تربيعية بمعلومية جذر مركب'),
Q('m7q28', U4[2], 'hard',
  r"إذا كان: $z_1=4\left(\cos\left(-\frac{3\pi}{4}\right)+i\sin\left(-\frac{3\pi}{4}\right)\right)$ ، $z_2=2\left(\cos\frac{\pi}{2}+i\sin\frac{\pi}{2}\right)$ ، فإنّ الصورة القياسية لناتج $\dfrac{z_1}{z_2}$ هي:",
  [O(r'-\sqrt{2}+\sqrt{2}i', -sqrt(2)+sqrt(2)*I), O(r'\sqrt{2}-\sqrt{2}i', sqrt(2)-sqrt(2)*I), O(r'-\sqrt{2}-\sqrt{2}i', -sqrt(2)-sqrt(2)*I), O(r'\sqrt{2}+\sqrt{2}i', sqrt(2)+sqrt(2)*I)],
  r"نقسم المقياسين ونطرح السعتين: $\dfrac42=2$ ، $-\frac{3\pi}{4}-\frac{\pi}{2}=-\frac{5\pi}{4}$ ، وهي تكافئ $\frac{3\pi}{4}$" "\n"
  r"$2\left(\cos\frac{3\pi}{4}+i\sin\frac{3\pi}{4}\right)=-\sqrt2+\sqrt2i$",
  truth=expand(pol(4, -3*P/4)/pol(2, P/2)), tag='الضرب والقسمة بالصورة المثلثية'),
Q('m7q29', U4[3], 'medium',
  r"النقطة التي يقطع عندها المحل الهندسي: $\text{Arg}(z+2)=\frac{\pi}{4}$ المحور التخيلي تُمثّل العدد:",
  [O('2i', 2*I), O('-2i', -2*I), O('2', 2), O('-2', -2)],
  r"المحل شعاع يبدأ بالنقطة $(-2,0)$ ويصنع زاوية $\frac{\pi}{4}$ ، فنقاطه $(-2+s,\ s)$ حيث $s>0$" "\n" r"على المحور التخيلي: $-2+s=0 \Rightarrow s=2$ ، فالنقطة $(0,2)$ أي العدد $2i$",
  truth=(lambda s_: -2+s_+s_*I)(2), tag='المحل الهندسي: الشعاع'),
IndexQ('m7q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي (الخط الرأسي المتقطّع هو العمود المنصّف للقطعة الواصلة بين نقطة الأصل والنقطة $(4,0)$) هو:",
  [T(r'$|z|<|z-4|$ ، $0\le\text{Arg}(z)\le\frac{\pi}{3}$', R7),
   T(r'$|z|\le|z-4|$ ، $0\le\text{Arg}(z)\le\frac{\pi}{3}$', both(nearer(0, 4), sector(0, 0, math.pi/3))),
   T(r'$|z|<|z+4|$ ، $0\le\text{Arg}(z)\le\frac{\pi}{3}$', both(closer(0, -4), sector(0, 0, math.pi/3))),
   T(r'$|z|\le|z+4|$ ، $0\le\text{Arg}(z)\le\frac{\pi}{3}$', both(nearer(0, -4), sector(0, 0, math.pi/3)))],
  r"المنطقة على يسار العمود المنصّف $x=2$ ، (الخط متقطّع، لا ينتمي إلى المنطقة)، أي أقرب إلى الأصل منها إلى $4$: $|z|<|z-4|$" "\n"
  r"ومحصورة بين شعاعين من الأصل بزاويتي $0$ و $\frac{\pi}{3}$ (يمرّ بالنقطة $(2,\,2\sqrt3)$): $0\le\text{Arg}(z)\le\frac{\pi}{3}$",
  truth=region_truth(R7, PR7, 5), figure=figure('m7q30', fig_region2(R7, PR7, 5, marks=[(4 + 0j, '$4$')]), 3.4, 3.4),
  tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 8
D8 = [(0, 1), (2, 3), (5, 0)]                # graph of f'(x)
d8, _ = pw(D8)
S8 = 2*t**3-15*t**2+36*t
R8 = both(disk(1 + 1j, 2), closer(2, 2j))
_r2 = math.sqrt(2)
PR8 = [('arc', 1 + 1j, 2, False, (-3*math.pi/4, math.pi/4)), ('seg', complex(1 - _r2, 1 - _r2), complex(1 + _r2, 1 + _r2), True),
       ('line', -3.9 - 3.9j, 3.9 + 3.9j)]
P8 = [
# ---------------- unit 1
Q('m8q1', U1[1], 'medium',
  F(r"إذا كان كلٌّ من $(x-1)$ و $(x+2)$ عاملًا من عوامل الاقتران: $f(x)=«0»$ ، فإنّ صفري الاقتران الآخرين هما:", (r'x^{4}-x^{3}-6x^{2}+2x+4', x**4-x**3-6*x**2+2*x+4)),
  [O(st(r'1+\sqrt{3}', r'1-\sqrt{3}'), S_(1+sqrt(3), 1-sqrt(3)), 'set'), O(st(r'-1+\sqrt{3}', r'-1-\sqrt{3}'), S_(-1+sqrt(3), -1-sqrt(3)), 'set'),
   O(st(r'1+\sqrt{2}', r'1-\sqrt{2}'), S_(1+sqrt(2), 1-sqrt(2)), 'set'), O(st(r'-1+\sqrt{2}', r'-1-\sqrt{2}'), S_(-1+sqrt(2), -1-sqrt(2)), 'set')],
  r"القسمة التركيبية على $(x-1)$: $1,\ -1,\ -6,\ 2,\ 4 \to 1,\ 0,\ -6,\ -4,\ 0$ ، ثم على $(x+2)$: $1,\ 0,\ -6,\ -4 \to 1,\ -2,\ -2,\ 0$" "\n"
  r"$x^2-2x-2=0 \Rightarrow x=\dfrac{2\pm\sqrt{4+8}}{2}=1\pm\sqrt3$",
  truth=lambda: FiniteSet(*[r_ for r_ in solve(x**4-x**3-6*x**2+2*x+4, x) if r_ not in (1, -2)]), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
Q('m8q2', U1[2], 'medium',
  F(r"أيّ الآتية يُمثّل تجزئة المقدار النسبي: $«0»$ إلى كسور جزئية؟", (r'\frac{3x+2}{x^{2}(x+1)}', (3*x+2)/(x**2*(x+1)))),
  [O(r'\frac{1}{x}+\frac{2}{x^{2}}-\frac{1}{x+1}', 1/x+2/x**2-1/(x+1)), O(r'\frac{1}{x}+\frac{2}{x^{2}}+\frac{1}{x+1}', 1/x+2/x**2+1/(x+1)),
   O(r'-\frac{1}{x}+\frac{2}{x^{2}}-\frac{1}{x+1}', -1/x+2/x**2-1/(x+1)), O(r'-\frac{1}{x}+\frac{2}{x^{2}}+\frac{1}{x+1}', -1/x+2/x**2+1/(x+1))],
  r"$3x+2=Ax(x+1)+B(x+1)+Cx^2$: عند $x=0$: $B=2$ ، عند $x=-1$: $-1=C$ ، ومعامل $x^2$: $0=A+C \Rightarrow A=1$",
  truth=(3*x+2)/(x**2*(x+1)), tag='تجزئة: عامل خطي مكرر'),
Q('m8q3', U1[1], 'easy',
  r"إذا كان: $f(x)=(x-1)(x+2)\,q(x)+3x-1$ ، حيث $q(x)$ كثير حدود، فإنّ باقي قسمة $f(x)$ على $(x+2)$ هو:",
  [O('-7', -7), O('7', 7), O('5', 5), O('-5', -5)],
  r"نظرية الباقي: الباقي $f(-2)=(-3)(0)\,q(-2)+3(-2)-1=-7$ (الحدّ الأول يساوي صفرًا مهما كان $q$)",
  truth=expand((x-1)*(x+2)*(a*x+b)+3*x-1).subs(x, -2), tag='الباقي من صورة خوارزمية القسمة'),
Q('m8q4', U1[1], 'hard',
  r"صفيحة كرتون مستطيلة الشكل بُعداها $10\ \text{cm}$ و $8\ \text{cm}$ ، قُصّ من كل ركن من أركانها مربع طول ضلعه $x\ \text{cm}$ ، ثم ثُنيت الأجزاء البارزة لتكوين صندوق مفتوح من الأعلى حجمه $48\ \text{cm}^3$. القيم الممكنة لـ $x$ هي:",
  [O(st('1', '2'), S_(1, 2), 'set'), O(st('1', '2', '6'), S_(1, 2, 6), 'set'), O(st('2', '6'), S_(2, 6), 'set'), O(st('1'), S_(1), 'set')],
  r"$V=x(10-2x)(8-2x)=48 \Rightarrow 4x^3-36x^2+80x-48=0 \Rightarrow x^3-9x^2+20x-12=0$" "\n"
  r"$x=1$ حلّ، والقسمة تعطي $x^2-8x+12=(x-2)(x-6)$. ويجب أن يكون $0<x<4$ (لأن $8-2x>0$) ، فنرفض $6$: $x=1,\ x=2$",
  truth=lambda: FiniteSet(*[r_ for r_ in solve(x*(10-2*x)*(8-2*x)-48, x) if 0 < r_ < 4]), tag='تطبيق حياتي على نظرية العوامل'),
# ---------------- unit 2
Q('m8q5', U2[2], 'medium',
  r"إذا كان $\tan\theta=-2\sqrt{2}$ ، حيث $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\cos\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{\sqrt{3}}{3}', sqrt(3)/3), O(r'-\frac{\sqrt{3}}{3}', -sqrt(3)/3), O(r'\frac{\sqrt{6}}{3}', sqrt(6)/3), O(r'-\frac{\sqrt{6}}{3}', -sqrt(6)/3)],
  r"$\sec^2\theta=1+8=9$ ، وفي الربع الثاني $\cos\theta=-\frac13$ ، و $\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$ فجيب التمام موجب" "\n"
  r"$\cos\frac{\theta}{2}=\sqrt{\dfrac{1-\frac13}{2}}=\sqrt{\dfrac13}=\dfrac{\sqrt3}{3}$",
  truth=cos((pi-atan(2*sqrt(2)))/2), tag='نصف الزاوية مع تحديد الربع'),
Q('m8q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'(1-\tan x)\tan(x+\frac{\pi}{4})', (1-tan(x))*tan(x+pi/4))),
  [O(r'1+\tan x', 1+tan(x)), O(r'1-\tan x', 1-tan(x)), O(r'\tan x-1', tan(x)-1), O(r'-1-\tan x', -1-tan(x))],
  r"$\tan\left(x+\frac{\pi}{4}\right)=\dfrac{\tan x+1}{1-\tan x}$ ، فبالضرب في $(1-\tan x)$ يبقى $1+\tan x$",
  truth=(1-tan(x))*tan(x+pi/4), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
Q('m8q7', U2[2], 'medium',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'(\sec x-\cos x)(\csc x-\sin x)', (sec(x)-cos(x))*(csc(x)-sin(x)))),
  [O(r'\frac{1}{2}\sin 2x', sin(2*x)/2), O(r'\sin 2x', sin(2*x)), O(r'\frac{1}{2}\cos 2x', cos(2*x)/2), O(r'\cos 2x', cos(2*x))],
  r"$\sec x-\cos x=\dfrac{1-\cos^2x}{\cos x}=\dfrac{\sin^2x}{\cos x}$ ، $\csc x-\sin x=\dfrac{\cos^2x}{\sin x}$" "\n" r"حاصل الضرب: $\sin x\cos x=\frac12\sin2x$",
  truth=(sec(x)-cos(x))*(csc(x)-sin(x)), tag='المتطابقات الأساسية'),
Q('m8q8', U2[2], 'medium',
  r"قيمة المقدار: $\cos^{4}\frac{\pi}{12}-\sin^{4}\frac{\pi}{12}$ هي:",
  [O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{\sqrt{3}}{2}', -sqrt(3)/2), O(r'-\frac{1}{2}', -R(1, 2))],
  r"$\cos^4x-\sin^4x=(\cos^2x-\sin^2x)(\cos^2x+\sin^2x)=\cos2x$" "\n" r"عند $x=\frac{\pi}{12}$: $\cos\frac{\pi}{6}=\frac{\sqrt3}{2}$",
  truth=cos(pi/12)**4-sin(pi/12)**4, tag='قيم دقيقة بمتطابقات ضعف الزاوية'),
Q('m8q9', U2[3], 'easy',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\sin^{2}x+7\sin x+3', 2*sin(x)**2+7*sin(x)+3)),
  [O(st(r'\frac{7\pi}{6}', r'\frac{11\pi}{6}'), S_(7*P/6, 11*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'),
   O(st(r'\frac{4\pi}{3}', r'\frac{5\pi}{3}'), S_(4*P/3, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set')],
  r"$(2\sin x+1)(\sin x+3)=0$ ، $\sin x=-3$ مرفوض" "\n" r"$\sin x=-\frac12$ في الربعين الثالث والرابع: $x=\frac{7\pi}{6},\ \frac{11\pi}{6}$",
  truth=lambda: sols(2*sin(x)**2+7*sin(x)+3, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
Q('m8q10', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=2\cos x$ في الفترة $\left(\frac{\pi}{2},\,\frac{3\pi}{2}\right)$ هي:", (r'\sec x', sec(x))),
  [O(st(r'\frac{3\pi}{4}', r'\frac{5\pi}{4}'), S_(3*P/4, 5*P/4), 'set'), O(st(r'\frac{\pi}{4}', r'\frac{7\pi}{4}'), S_(P/4, 7*P/4), 'set'),
   O(st(r'\frac{\pi}{4}', r'\frac{3\pi}{4}', r'\frac{5\pi}{4}', r'\frac{7\pi}{4}'), S_(P/4, 3*P/4, 5*P/4, 7*P/4), 'set'), O(st(r'\frac{3\pi}{4}'), S_(3*P/4), 'set')],
  r"$\dfrac{1}{\cos x}=2\cos x \Rightarrow \cos^2x=\frac12 \Rightarrow \cos x=\pm\frac{\sqrt2}{2}$" "\n"
  r"في الفترة $\left(\frac{\pi}{2},\frac{3\pi}{2}\right)$ جيب التمام سالب: $\cos x=-\frac{\sqrt2}{2} \Rightarrow x=\frac{3\pi}{4},\ \frac{5\pi}{4}$",
  truth=lambda: sols(1-2*cos(x)**2, pi/2, 3*pi/2, closed_lo=False), tag='معادلة فيها مقلوب نسبة'),
# ---------------- unit 3
Q('m8q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{3}\right)$ تساوي:", (r'2\sin x+\sec x', 2*sin(x)+sec(x))),
  [O(r'1+2\sqrt{3}', 1+2*sqrt(3)), O(r'1-2\sqrt{3}', 1-2*sqrt(3)), O(r'-1+2\sqrt{3}', -1+2*sqrt(3)), O(r'-1-2\sqrt{3}', -1-2*sqrt(3))],
  r"$f'(x)=2\cos x+\sec x\tan x \Rightarrow f'\left(\frac{\pi}{3}\right)=2\cdot\frac12+2\sqrt3=1+2\sqrt3$",
  truth=Dx(2*sin(x)+sec(x)).subs(x, pi/3), tag='مشتقات الاقترانات المثلثية'),
Q('m8q12', U3[1], 'easy',
  r"الأزمنة التي يكون فيها الجُسيم في حالة سكون لحظي هي:",
  [O(st('2', '3', var='t'), S_(2, 3), 'set'), O(st('2', var='t'), S_(2), 'set'), O(st(r'\frac{5}{2}', var='t'), S_(R(5, 2)), 'set'), O(st('0', '2', '3', var='t'), S_(0, 2, 3), 'set')],
  r"$v(t)=6t^2-30t+36=6(t^2-5t+6)=6(t-2)(t-3)=0 \Rightarrow t=2,\ t=3$",
  truth=lambda: FiniteSet(*solve(diff(S8, t), t)), tag='الحركة: اتجاه الحركة والسكون',
  lead=shared(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=" + M(r'2t^{3}-15t^{2}+36t', S8) + r"$ ، حيث $t\ge0$ الزمن بالثواني، و $s$ الموقع بالأمتار", 12, 13)),
Q('m8q13', U3[1], 'hard',
  r"المسافة الكلية التي يقطعها الجُسيم في الفترة الزمنية $[0,\,4]$ هي:",
  [O('34', 34, units='m'), O('32', 32, units='m'), O('30', 30, units='m'), O('28', 28, units='m')],
  r"$s(0)=0$ ، $s(2)=28$ ، $s(3)=27$ ، $s(4)=32$ (الجُسيم يغيّر اتجاهه عند $t=2$ و $t=3$)" "\n" r"المسافة $=|28-0|+|27-28|+|32-27|=28+1+5=34\ \text{m}$",
  truth=sum(Abs(S8.subs(t, b_)-S8.subs(t, a_)) for a_, b_ in [(0, 2), (2, 3), (3, 4)]), tag='الحركة: المسافة الكلية والإزاحة'),
Q('m8q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $a$ ثابت، وكان: $f'\left(\frac{\pi}{6}\right)=2$ ، فإنّ قيمة $a$ هي:", (r'a\sin x\cos x', a*sin(x)*cos(x))),
  [O('4', 4), O('-4', -4), O('8', 8), O('-8', -8)],
  r"$f'(x)=a(\cos^2x-\sin^2x)=a\cos2x$ ، إذن $f'\left(\frac{\pi}{6}\right)=a\cos\frac{\pi}{3}=\frac a2=2 \Rightarrow a=4$",
  truth=lambda: solve(Dx(a*sin(x)*cos(x)).subs(x, pi/6)-2, a)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
Q('m8q15', U3[2], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>0$ ، فإنّ $f^{(5)}(1)$ تساوي:", (r'x\ln x', x*log(x))),
  [O('-6', -6), O('6', 6), O('-24', -24), O('24', 24)],
  r"$f'(x)=\ln x+1$ ، $f''(x)=x^{-1}$ ، $f'''(x)=-x^{-2}$ ، $f^{(4)}(x)=2x^{-3}$ ، $f^{(5)}(x)=-6x^{-4}$" "\n" r"$f^{(5)}(1)=-6$",
  truth=diff(x*log(x), x, 5).subs(x, 1), tag='المشتقات العليا: إيجاد نمط'),
Q('m8q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنى المشتقة الأولى $f'(x)$ للاقتران $f(x)$. إذا كان: $h(x)=f(x^{2})$ ، فإنّ $h'(2)$ تساوي:",
  [O('4', 4), O('-4', -4), O('1', 1), O('-1', -1)],
  r"قاعدة السلسلة: $h'(x)=f'(x^2)\cdot2x \Rightarrow h'(2)=4f'(4)$" "\n" r"من الشكل: $f'(4)=1$ (القطعة من $(2,3)$ إلى $(5,0)$ ميلها $-1$) ، إذن $h'(2)=4$",
  truth=lambda: 2*2*d8(4), figure=figure('m8q16', fig_dgraph(D8, (0, 5), (0, 3), (3.4, 2.2))), tag='المشتقة من التمثيل البياني'),
Q('m8q17', U3[3], 'easy',
  F(r"يُعطى طول نبتة (بالسنتيمترات) بعد $t$ أسبوع من زراعتها بالاقتران: $h(t)=«0»$. معدّل نمو النبتة عندما $t=5$ هو:", (r'30-25e^{-0.2t}', 30-25*exp(-R(1, 5)*t))),
  [O(r'\frac{5}{e}', 5/E, units='cm/week'), O(r'-\frac{5}{e}', -5/E, units='cm/week'), O(r'\frac{25}{e}', 25/E, units='cm/week'), O(r'-\frac{25}{e}', -25/E, units='cm/week')],
  r"$h'(t)=-25e^{-0.2t}\cdot(-0.2)=5e^{-0.2t}$ ، إذن $h'(5)=5e^{-1}=\dfrac5e$",
  truth=diff(30-25*exp(-R(1, 5)*t), t).subs(t, 5), tag='معدل التغير في سياق حياتي'),
Q('m8q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>0$ ، فإنّ $f'(1)$ تساوي:", (r'\log_{3}\left(\frac{x}{x+2}\right)', log(x/(x+2), 3))),
  [O(r'\frac{2}{3\ln 3}', 2/(3*log(3))), O(r'\frac{4}{3\ln 3}', 4/(3*log(3))), O(r'\frac{2\ln 3}{3}', 2*log(3)/3), O(r'\frac{4\ln 3}{3}', 4*log(3)/3)],
  r"$f(x)=\log_3x-\log_3(x+2)$ ، $f'(x)=\dfrac{1}{x\ln3}-\dfrac{1}{(x+2)\ln3}$" "\n" r"$f'(1)=\dfrac{1}{\ln3}\left(1-\dfrac13\right)=\dfrac{2}{3\ln3}$",
  truth=Dx(log(x/(x+2), 3)).subs(x, 1), tag='مشتقة اللوغاريتم لأساس غير e'),
Q('m8q19', U3[3], 'medium',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، فإنّ النقطة التي يكون عندها المماس رأسيًّا هي:", (r't^{2}-4t', t**2-4*t), (r't^{3}-3t', t**3-3*t)),
  [O(r'(-4,\ 2)', Tuple(-4, 2), 'tuple'), O(r'(-4,\ -2)', Tuple(-4, -2), 'tuple'), O(r'(4,\ 2)', Tuple(4, 2), 'tuple'), O(r'(4,\ -2)', Tuple(4, -2), 'tuple')],
  r"المماس رأسي عندما $\dfrac{dx}{dt}=0$ و $\dfrac{dy}{dt}\ne0$: $2t-4=0 \Rightarrow t=2$ ، و $\dfrac{dy}{dt}=3(4)-3=9\ne0$" "\n" r"النقطة: $x=4-8=-4$ ، $y=8-6=2$",
  truth=lambda: (lambda t0: Tuple((t**2-4*t).subs(t, t0), (t**3-3*t).subs(t, t0)))(solve(diff(t**2-4*t, t), t)[0]), tag='مماس رأسي لمنحنى وسيطي'),
Q('m8q20', U3[4], 'medium',
  F(r"إذا كان: $«0»=5$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(2,\,1)$ تساوي:", (r'x^{2}y+e^{y-1}', x**2*y+exp(y-1))),
  [O(r'-\frac{4}{5}', -R(4, 5)), O(r'\frac{4}{5}', R(4, 5)), O('-1', -1), O('1', 1)],
  r"$2xy+x^2y'+e^{y-1}y'=0$ ، وعند $(2,1)$: $4+4y'+y'=0 \Rightarrow y'=-\dfrac45$",
  truth=imp(x**2*y+exp(y-1)-5, (2, 1)), tag='الاشتقاق الضمني عند نقطة'),
Q('m8q21', U3[4], 'hard',
  F(r"المقطع $y$ للعمودي على المماس لمنحنى العلاقة: $«0»=21$ عند النقطة $(3,\,2)$ هو:", (r'x^{2}+3y^{2}', x**2+3*y**2)),
  [O('-4', -4), O('4', 4), O(r'\frac{7}{2}', R(7, 2)), O(r'-\frac{7}{2}', -R(7, 2))],
  r"$2x+6yy'=0 \Rightarrow y'=-\dfrac{x}{3y}=-\dfrac36=-\dfrac12$ ، فميل العمودي $2$" "\n" r"العمودي: $y-2=2(x-3)$ ، وعند $x=0$: $y=-4$",
  truth=lambda: 2+(-1/imp(x**2+3*y**2-21, (3, 2)))*(0-3), tag='معادلة العمودي على المماس'),
Q('m8q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي سُلّمًا طوله $10\ \text{m}$ يستند طرفه العلوي إلى جدار رأسي، وطرفه السفلي على أرض أفقية. إذا انزلق طرفه السفلي مبتعدًا عن الجدار بمعدّل $1\ \text{m/s}$ ، فإنّ معدّل تغيّر قياس الزاوية $\theta$ بين السُّلّم والأرض عندما يكون طرفه السفلي على بُعد $6\ \text{m}$ من الجدار هو:",
  [O(r'-\frac{1}{8}', -R(1, 8), units='rad/s'), O(r'\frac{1}{8}', R(1, 8), units='rad/s'), O(r'-\frac{1}{6}', -R(1, 6), units='rad/s'), O(r'\frac{1}{6}', R(1, 6), units='rad/s')],
  r"$x=10\cos\theta \Rightarrow \dfrac{dx}{dt}=-10\sin\theta\dfrac{d\theta}{dt}$ ، وعندما $x=6$: ارتفاع الطرف العلوي $8$ و $\sin\theta=\frac{8}{10}$" "\n"
  r"$1=-10\cdot\frac{8}{10}\cdot\dfrac{d\theta}{dt} \Rightarrow \dfrac{d\theta}{dt}=-\dfrac18\ \text{rad/s}$",
  truth=1/(-10*R(8, 10)), figure=figure('m8q22', fig_ladder(), 3.0, 3.0), tag='معدلات مرتبطة: معدل تغير زاوية'),
# ---------------- unit 4
Q('m8q23', U4[1], 'medium',
  r"إذا كان: $z=-1-\sqrt{3}\,i$ ، فإنّ الصورة المثلثية للعدد $z^{2}$ هي:",
  [O(trig('4', r'\frac{2\pi}{3}'), pol(4, 2*P/3)), O(trig('4', r'-\frac{2\pi}{3}'), pol(4, -2*P/3)), O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3)), O(trig('4', r'-\frac{\pi}{3}'), pol(4, -P/3))],
  r"$|z|=2$ ، $\text{Arg}(z)=-\frac{2\pi}{3}$ ، فـ $|z^2|=4$ وسعته $-\frac{4\pi}{3}$ ، وبإضافة $2\pi$ تصبح السعة الرئيسة $\frac{2\pi}{3}$" "\n" r"(تحقّق: $z^2=1+2\sqrt3i-3=-2+2\sqrt3i$)",
  truth=expand((-1-sqrt(3)*I)**2), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
Q('m8q24', U4[2], 'easy',
  r"ناتج $z^{2}+w$ هو:",
  [O('-1+3i', -1+3*I), O('7+3i', 7+3*I), O('-1+5i', -1+5*I), O('7+5i', 7+5*I)],
  r"$z^2=(1+2i)^2=1+4i+4i^2=-3+4i$ ، إذن $z^2+w=-3+4i+2-i=-1+3i$",
  truth=expand((1+2*I)**2+(2-I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=1+2i$ ، $w=2-i$", 24, 25)),
Q('m8q25', U4[2], 'medium',
  r"ناتج $z\,\bar{w}$ هو:",
  [O('5i', 5*I), O('-5i', -5*I), O('5', 5), O('-5', -5)],
  r"$\bar w=2+i$ ، $z\bar w=(1+2i)(2+i)=2+i+4i+2i^2=5i$",
  truth=expand((1+2*I)*(2+I)), tag='العمليات على الأعداد المركبة (نص مشترك)'),
Q('m8q26', U4[1], 'medium',
  r"إذا كان: $z=a+(a-1)i$ ، حيث $a$ عدد حقيقي، وكان: $|z|=5$ ، فإنّ قيم $a$ الممكنة هي:",
  [O(r'4,\ -3', S_(4, -3), 'set'), O(r'-4,\ 3', S_(-4, 3), 'set'), O(r'4,\ 3', S_(4, 3), 'set'), O(r'-4,\ -3', S_(-4, -3), 'set')],
  r"$a^2+(a-1)^2=25 \Rightarrow 2a^2-2a-24=0 \Rightarrow a^2-a-12=0 \Rightarrow (a-4)(a+3)=0$" "\n" r"$a=4$ أو $a=-3$",
  truth=lambda: FiniteSet(*solve(X**2+(X-1)**2-25, X)), tag='إيجاد ثابت بمعلومية المقياس'),
Q('m8q27', U4[2], 'hard',
  r"مجموعة حلّ المعادلة: $z^{2}+(1-i)z-i=0$ هي:",
  [O(r'\{-1,\ i\}', S_(-1, I), 'set'), O(r'\{1,\ -i\}', S_(1, -I), 'set'), O(r'\{-1,\ -i\}', S_(-1, -I), 'set'), O(r'\{1,\ i\}', S_(1, I), 'set')],
  r"نحلّل: $z^2+z-iz-i=z(z+1)-i(z+1)=(z+1)(z-i)=0$" "\n" r"$z=-1$ أو $z=i$",
  truth=lambda: FiniteSet(*solve(z**2+(1-I)*z-I, z)), tag='معادلة تربيعية بمعاملات مركبة'),
Q('m8q28', U4[2], 'hard',
  r"يُبيّن الشكل الآتي النقطتين $A$ و $B$ اللتين تُمثّلان العددين المُركَّبين $z_1$ و $z_2$ على الترتيب. السعة الرئيسة للعدد $\dfrac{z_1}{z_2}$ هي:",
  [O(r'-\frac{\pi}{2}', -P/2), O(r'\frac{\pi}{2}', P/2), O(r'\frac{3\pi}{2}', 3*P/2), O(r'-\frac{3\pi}{2}', -3*P/2)],
  r"من الشكل: $z_1=-1+i$ وسعته $\frac{3\pi}{4}$ ، $z_2=-2-2i$ وسعته $-\frac{3\pi}{4}$" "\n"
  r"$\text{Arg}\left(\dfrac{z_1}{z_2}\right)=\frac{3\pi}{4}-\left(-\frac{3\pi}{4}\right)=\frac{3\pi}{2}$ ، وليست رئيسة، فنطرح $2\pi$: $-\frac{\pi}{2}$",
  truth=arg(expand(simplify((-1+I)/(-2-2*I)))),
  figure=figure('m8q28', fig_argand([((-1, 1), 'A', r'$(-1,\,1)$', (-1.6, 0.25)), ((-2, -2), 'B', r'$(-2,\,-2)$', (0.15, -0.45))], 3), 3.4, 3.4),
  tag='السعة الرئيسة'),
Q('m8q29', U4[3], 'medium',
  r"المعادلة الديكارتية للمحل الهندسي: $|z-2+i|=3$ هي:",
  [O('x^{2}+y^{2}-4x+2y-4=0', x**2+y**2-4*x+2*y-4, 'rel'), O('x^{2}+y^{2}+4x-2y-4=0', x**2+y**2+4*x-2*y-4, 'rel'),
   O('x^{2}+y^{2}-4x-2y-4=0', x**2+y**2-4*x-2*y-4, 'rel'), O('x^{2}+y^{2}+4x+2y-4=0', x**2+y**2+4*x+2*y-4, 'rel')],
  r"$|(x-2)+(y+1)i|=3 \Rightarrow (x-2)^2+(y+1)^2=9$" "\n" r"$x^2-4x+4+y^2+2y+1-9=0 \Rightarrow x^2+y^2-4x+2y-4=0$",
  truth=expand((x-2)**2+(y+1)**2-9), tag='المعادلة الديكارتية لمحل هندسي'),
IndexQ('m8q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي (المستقيم المنقّط هو العمود المنصّف للقطعة الواصلة بين النقطتين اللتين تُمثّلان العددين $2$ و $2i$) هو:",
  [T(r'$|z-1-i|\le2$ ، $|z-2|<|z-2i|$', R8),
   T(r'$|z-1-i|\le2$ ، $|z-2|\le|z-2i|$', both(disk(1 + 1j, 2), nearer(2, 2j))),
   T(r'$|z+1+i|\le2$ ، $|z-2|<|z-2i|$', both(disk(-1 - 1j, 2), closer(2, 2j))),
   T(r'$|z+1+i|\le2$ ، $|z-2|\le|z-2i|$', both(disk(-1 - 1j, 2), nearer(2, 2j)))],
  r"الدائرة مركزها $(1,1)$ أي العدد $1+i$ ونصف قطرها $2$: $|z-1-i|\le2$" "\n"
  r"العمود المنصّف هو المستقيم $y=x$ ، والقطعة عليه متقطّعة، والمنطقة تحته أي في جهة النقطة $2$: $|z-2|<|z-2i|$",
  truth=region_truth(R8, PR8, 4), figure=figure('m8q30', fig_region2(R8, PR8, 4, marks=[(2 + 0j, '$2$'), (2j, '$2i$')]), 3.4, 3.4),
  tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 9
TP9 = [(1, 2), (5, 4)]                       # tangent to f at x=3
f9_16 = lambda s_: 3 + 0.5*(s_ - 3) + 0.35*(s_ - 3)**2
PF9 = (x**2+1)/((x-2)**2*(x**2+4))
R9 = both(outside(1, 1, strict=True), disk(1, 3), sector(1, -math.pi/2, math.pi/2))
PR9 = [('arc', 1 + 0j, 3, False, (-math.pi/2, math.pi/2)), ('arc', 1 + 0j, 1, True, (-math.pi/2, math.pi/2)),
       ('seg', 1 + 1j, 1 + 3j, False), ('seg', 1 - 1j, 1 - 3j, False), ('open', 1 + 1j), ('open', 1 - 1j)]
P9 = [
# ---------------- unit 1
Q('m9q1', U1[1], 'easy',
  F(r"مجموعة حلّ المعادلة: $«0»=«1»$ هي:", (r'2x^{3}+4', 2*x**3+4), (r'x^{2}+8x', x**2+8*x)),
  [O(r'\{\frac{1}{2},\ 2,\ -2\}', S_(R(1, 2), 2, -2), 'set'), O(r'\{-\frac{1}{2},\ 2,\ -2\}', S_(-R(1, 2), 2, -2), 'set'),
   O(r'\{\frac{1}{2},\ 4,\ -4\}', S_(R(1, 2), 4, -4), 'set'), O(r'\{-\frac{1}{2},\ 4,\ -4\}', S_(-R(1, 2), 4, -4), 'set')],
  r"$2x^3-x^2-8x+4=0$ ، بالتجميع: $x^2(2x-1)-4(2x-1)=(2x-1)(x^2-4)=0$" "\n" r"$x=\frac12$ أو $x=\pm2$",
  truth=lambda: roots(2*x**3-x**2-8*x+4), tag='الأصفار النسبية وحل المعادلة'),
Q('m9q2', U1[2], 'hard',
  F(r"المقدار: $«0»$ يساوي:", (r'\frac{2x^{2}+x}{x^{2}-1}', (2*x**2+x)/(x**2-1))),
  [O(r'2+\frac{3}{2(x-1)}-\frac{1}{2(x+1)}', 2+R(3, 2)/(x-1)-R(1, 2)/(x+1)), O(r'2+\frac{3}{2(x-1)}+\frac{1}{2(x+1)}', 2+R(3, 2)/(x-1)+R(1, 2)/(x+1)),
   O(r'\frac{3}{2(x-1)}-\frac{1}{2(x+1)}', R(3, 2)/(x-1)-R(1, 2)/(x+1)), O(r'\frac{3}{2(x-1)}+\frac{1}{2(x+1)}', R(3, 2)/(x-1)+R(1, 2)/(x+1))],
  r"كسر غير فعلي: بالقسمة $\dfrac{2x^2+x}{x^2-1}=2+\dfrac{x+2}{x^2-1}$" "\n"
  r"$x+2=A(x+1)+B(x-1)$: عند $x=1$: $A=\frac32$ ، عند $x=-1$: $B=-\frac12$",
  truth=(2*x**2+x)/(x**2-1), tag='تجزئة: كسر غير فعلي'),
Q('m9q3', U1[1], 'medium',
  F(r"إذا كان باقي قسمة الاقتران: $f(x)=«0»$ على $(x^{2}-1)$ هو $(2x+3)$ ، فإنّ قيمة $ab$ هي:", (r'x^{3}+ax^{2}+bx-1', x**3+a*x**2+b*x-1)),
  [O('4', 4), O('-4', -4), O('3', 3), O('-3', -3)],
  r"$f(x)=(x-1)(x+1)q(x)+2x+3$ ، إذن $f(1)=5$ و $f(-1)=1$" "\n" r"$a+b=5$ ، $a-b-2=1 \Rightarrow a-b=3$ ، فـ $a=4$ ، $b=1$ ، و $ab=4$",
  truth=lambda: (lambda s_: s_[a]*s_[b])(solve([rem(x**3+a*x**2+b*x-1, 1)-5, rem(x**3+a*x**2+b*x-1, -1)-1], [a, b])), tag='باقي القسمة على مقدار تربيعي'),
IndexQ('m9q4', U1[2], 'hard',
  F(r"الصورة الصحيحة لتجزئة المقدار النسبي: $«0»$ إلى كسور جزئية (حيث $A,\ B,\ C,\ D$ ثوابت) هي:", (r'\frac{x^{2}+1}{(x-2)^{2}(x^{2}+4)}', PF9)),
  [O(r'\frac{A}{x-2}+\frac{B}{(x-2)^{2}}+\frac{Cx+D}{x^{2}+4}', A_/(x-2)+B_/(x-2)**2+(C_*x+D_)/(x**2+4)),
   O(r'\frac{A}{x-2}+\frac{B}{(x-2)^{2}}+\frac{C}{x^{2}+4}', A_/(x-2)+B_/(x-2)**2+C_/(x**2+4)),
   O(r'\frac{A}{(x-2)^{2}}+\frac{Bx+C}{x^{2}+4}', A_/(x-2)**2+(B_*x+C_)/(x**2+4)),
   O(r'\frac{A}{x-2}+\frac{Bx+C}{x^{2}+4}', A_/(x-2)+(B_*x+C_)/(x**2+4))],
  r"العامل الخطي المكرر $(x-2)^2$ يحتاج حدّين: $\dfrac{A}{x-2}+\dfrac{B}{(x-2)^2}$" "\n" r"والعامل التربيعي الذي لا يتحلّل $x^2+4$ يحتاج بسطًا خطيًّا: $\dfrac{Cx+D}{x^2+4}$",
  truth=lambda vals: only(vals, lambda form_: solve_pf(PF9, form_, sorted(form_.free_symbols - {x}, key=str)) is not None),
  tag='تجزئة: الصورة الصحيحة للتجزئة'),
# ---------------- unit 2
Q('m9q5', U2[2], 'medium',
  r"إذا كان $\cos\theta=\frac{12}{13}$ ، حيث $\frac{3\pi}{2}<\theta<2\pi$ ، فإنّ قيمة $\tan\frac{\theta}{2}$ تساوي:",
  [O(r'-\frac{1}{5}', -R(1, 5)), O(r'\frac{1}{5}', R(1, 5)), O('-5', -5), O('5', 5)],
  r"في الربع الرابع $\sin\theta=-\frac{5}{13}$ ، و $\frac{3\pi}{4}<\frac{\theta}{2}<\pi$ فالظل سالب" "\n" r"$\tan\frac{\theta}{2}=\dfrac{\sin\theta}{1+\cos\theta}=\dfrac{-\frac{5}{13}}{\frac{25}{13}}=-\dfrac15$",
  truth=tan((2*pi-acos(R(12, 13)))/2), tag='نصف الزاوية مع تحديد الربع'),
Q('m9q6', U2[1], 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(x+y)-2\cos x\sin y', sin(x+y)-2*cos(x)*sin(y))),
  [O(r'\sin(x-y)', sin(x-y)), O(r'\sin(x+y)', sin(x+y)), O(r'\cos(x-y)', cos(x-y)), O(r'\cos(x+y)', cos(x+y))],
  r"$\sin x\cos y+\cos x\sin y-2\cos x\sin y=\sin x\cos y-\cos x\sin y=\sin(x-y)$",
  truth=sin(x+y)-2*cos(x)*sin(y), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
Q('m9q7', U2[1], 'easy',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\sec^{2}x-1}{\sec^{2}x}', (sec(x)**2-1)/sec(x)**2)),
  [O(r'\sin^{2}x', sin(x)**2), O(r'\cos^{2}x', cos(x)**2), O(r'\tan^{2}x', tan(x)**2), O(r'\cot^{2}x', cot(x)**2)],
  r"$\sec^2x-1=\tan^2x$ ، إذن $\dfrac{\tan^2x}{\sec^2x}=\dfrac{\sin^2x}{\cos^2x}\cdot\cos^2x=\sin^2x$",
  truth=(sec(x)**2-1)/sec(x)**2, tag='المتطابقات الأساسية'),
Q('m9q8', U2[2], 'medium',
  r"المقدار: $\sin10^\circ+\sin50^\circ$ يساوي:",
  [T(r'$\cos20^\circ$', cos(deg(20))), T(r'$\sin20^\circ$', sin(deg(20))), T(r'$\cos40^\circ$', cos(deg(40))), T(r'$\sin40^\circ$', sin(deg(40)))],
  r"$\sin A+\sin B=2\sin\dfrac{A+B}{2}\cos\dfrac{A-B}{2}=2\sin30^\circ\cos(-20^\circ)=2\cdot\frac12\cos20^\circ=\cos20^\circ$",
  truth=sin(deg(10))+sin(deg(50)), tag='تحويل المجموع إلى ضرب'),
Q('m9q9', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\tan^{2}x+3\sec x', 2*tan(x)**2+3*sec(x))),
  [O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'),
   O(st(r'\frac{5\pi}{6}', r'\frac{7\pi}{6}'), S_(5*P/6, 7*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set')],
  r"$\tan^2x=\sec^2x-1$: $2\sec^2x+3\sec x-2=0 \Rightarrow (2\sec x-1)(\sec x+2)=0$" "\n"
  r"$\sec x=\frac12$ مرفوض لأن $|\sec x|\ge1$ ، و $\sec x=-2 \Rightarrow \cos x=-\frac12 \Rightarrow x=\frac{2\pi}{3},\ \frac{4\pi}{3}$",
  truth=lambda: sols(2*sin(x)**2+3*cos(x), 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
Q('m9q10', U2[3], 'hard',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,\pi]$ هي:", (r'\sin 3x+\sin x', sin(3*x)+sin(x))),
  [O(st('0', r'\frac{\pi}{2}', r'\pi'), S_(0, P/2, P), 'set'), O(st(r'\frac{\pi}{2}'), S_(P/2), 'set'), O(st('0', r'\pi'), S_(0, P), 'set'),
   O(st('0', r'\frac{\pi}{4}', r'\frac{\pi}{2}', r'\frac{3\pi}{4}', r'\pi'), S_(0, P/4, P/2, 3*P/4, P), 'set')],
  r"$\sin3x+\sin x=2\sin2x\cos x=0$" "\n" r"$\sin2x=0 \Rightarrow x=0,\ \frac{\pi}{2},\ \pi$ ، و $\cos x=0 \Rightarrow x=\frac{\pi}{2}$ ، فمجموعة الحل $\{0,\ \frac{\pi}{2},\ \pi\}$",
  truth=lambda: sols(sin(3*x)+sin(x), 0, pi, closed_hi=True), tag='معادلة بتحويل المجموع إلى ضرب'),
# ---------------- unit 3
Q('m9q11', U3[1], 'easy',
  F(r"إذا كان: $y=«0»$ ، فإنّ $y''+y$ يساوي:", (r'4\sin x-3\cos x', 4*sin(x)-3*cos(x))),
  [O('0', 0), O(r'8\sin x-6\cos x', 8*sin(x)-6*cos(x)), O(r'-8\sin x+6\cos x', -8*sin(x)+6*cos(x)), O(r'2\cos x', 2*cos(x))],
  r"$y'=4\cos x+3\sin x$ ، $y''=-4\sin x+3\cos x=-y$ ، إذن $y''+y=0$",
  truth=diff(4*sin(x)-3*cos(x), x, 2)+4*sin(x)-3*cos(x), tag='مشتقات الاقترانات المثلثية'),
Q('m9q12', U3[1], 'medium',
  r"معادلة المماس لمنحنى الاقتران: $y=e^{x}$ ، والمارّ بالنقطة $(1,\,0)$ ، هي:",
  [O('y=e^{2}x-e^{2}', E**2*x-E**2, 'eq'), O('y=e^{2}x+e^{2}', E**2*x+E**2, 'eq'), O('y=ex-e', E*x-E, 'eq'), O('y=ex+e', E*x+E, 'eq')],
  r"المماس عند $x=a$: $y-e^a=e^a(x-a)$ ، ويمرّ بـ $(1,0)$: $-e^a=e^a(1-a) \Rightarrow -1=1-a \Rightarrow a=2$" "\n" r"$y-e^2=e^2(x-2) \Rightarrow y=e^2x-e^2$",
  truth=lambda: (lambda a0: exp(a0)+exp(a0)*(x-a0))(solve(-1-(1-a), a)[0]), tag='مماس من نقطة خارج المنحنى'),
Q('m9q13', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $k$ ثابت، وكان: $f''(0)=5$ ، فإنّ قيمة $k$ هي:", (r'e^{x}(x^{2}+k)', exp(x)*(x**2+k))),
  [O('3', 3), O('-3', -3), O('5', 5), O('-5', -5)],
  r"$f'(x)=e^x(x^2+2x+k)$ ، $f''(x)=e^x(x^2+4x+k+2)$ ، إذن $f''(0)=k+2=5 \Rightarrow k=3$",
  truth=lambda: solve(diff(exp(x)*(x**2+k), x, 2).subs(x, 0)-5, k)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
Q('m9q14', U3[2], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''(x)+2f'(x)+2f(x)$ يساوي:", (r'e^{-x}\cos x', exp(-x)*cos(x))),
  [O('0', 0), O(r'2e^{-x}\sin x', 2*exp(-x)*sin(x)), O(r'-4e^{-x}\cos x', -4*exp(-x)*cos(x)), O(r'4e^{-x}\sin x', 4*exp(-x)*sin(x))],
  r"$f'(x)=-e^{-x}\cos x-e^{-x}\sin x$ ، $f''(x)=2e^{-x}\sin x$" "\n" r"$2e^{-x}\sin x-2e^{-x}\cos x-2e^{-x}\sin x+2e^{-x}\cos x=0$",
  truth=(lambda f_: diff(f_, x, 2)+2*Dx(f_)+2*f_)(exp(-x)*cos(x)), tag='المشتقات العليا وتراكيبها'),
Q('m9q15', U3[2], 'medium',
  F(r"النقاط الواقعة على منحنى الاقتران: $f(x)=«0»$ ، والتي يكون المماس عندها أفقيًّا هي:", (r'\frac{x^{2}+3}{x-1}', (x**2+3)/(x-1))),
  [O(r'(3,\ 6),\ (-1,\ -2)', FiniteSet(Tuple(3, 6), Tuple(-1, -2)), 'tset'), O(r'(3,\ 6)', FiniteSet(Tuple(3, 6)), 'tset'),
   O(r'(-3,\ -3),\ (1,\ 2)', FiniteSet(Tuple(-3, -3), Tuple(1, 2)), 'tset'), O(r'(-1,\ 2),\ (3,\ -6)', FiniteSet(Tuple(-1, 2), Tuple(3, -6)), 'tset')],
  r"$f'(x)=\dfrac{2x(x-1)-(x^2+3)}{(x-1)^2}=\dfrac{x^2-2x-3}{(x-1)^2}=0 \Rightarrow (x-3)(x+1)=0$" "\n" r"$f(3)=\frac{12}{2}=6$ ، $f(-1)=\frac{4}{-2}=-2$",
  truth=lambda: FiniteSet(*[Tuple(r_, ((x**2+3)/(x-1)).subs(x, r_)) for r_ in solve(Dx((x**2+3)/(x-1)), x)]), tag='نقاط المماس الأفقي'),
Q('m9q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنى الاقتران $f(x)$ ، والمستقيم $L$ المماس له عند $x=3$ ، والمارّ بالنقطتين المُبيّنتين. إذا كان: $h(x)=\ln f(x)$ ، فإنّ $h'(3)$ تساوي:",
  [O(r'\frac{1}{6}', R(1, 6)), O(r'\frac{1}{3}', R(1, 3)), O(r'\frac{1}{2}', R(1, 2)), O('6', 6)],
  r"ميل $L$: $\dfrac{4-2}{5-1}=\dfrac12=f'(3)$ ، و $f(3)=2+\frac12(2)=3$" "\n" r"$h'(x)=\dfrac{f'(x)}{f(x)} \Rightarrow h'(3)=\dfrac{1/2}{3}=\dfrac16$",
  truth=lambda: (lambda v_m: v_m[1]/v_m[0])(tan_point_value(TP9, 3)),
  figure=figure('m9q16', fig_tangent(f9_16, TP9, (0, 5), (0, 6), (0.3, 5.0), (4.6, 3.3))), tag='المشتقة من التمثيل البياني'),
Q('m9q17', U3[3], 'medium',
  F(r"تُعطى درجة الحرارة (بالسيليسيوس) في مدينة بعد $t$ ساعة من منتصف الليل بالاقتران: $T(t)=«0»$. معدّل تغيّر درجة الحرارة في المدينة عند الساعة الرابعة صباحًا هو:", (r'20-6\cos\frac{\pi t}{12}', 20-6*cos(pi*t/12))),
  [O(r'\frac{\sqrt{3}\pi}{4}', sqrt(3)*pi/4, units='°C/h'), O(r'-\frac{\sqrt{3}\pi}{4}', -sqrt(3)*pi/4, units='°C/h'), O(r'\frac{\pi}{4}', pi/4, units='°C/h'), O(r'-\frac{\pi}{4}', -pi/4, units='°C/h')],
  r"$T'(t)=6\sin\dfrac{\pi t}{12}\cdot\dfrac{\pi}{12}=\dfrac{\pi}{2}\sin\dfrac{\pi t}{12}$" "\n" r"عند $t=4$: $\dfrac{\pi}{2}\sin\dfrac{\pi}{3}=\dfrac{\pi}{2}\cdot\dfrac{\sqrt3}{2}=\dfrac{\sqrt3\pi}{4}$",
  truth=diff(20-6*cos(pi*t/12), t).subs(t, 4), tag='معدل التغير في سياق حياتي'),
Q('m9q18', U3[3], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $0<x<\pi$ ، فإنّ $f'\left(\frac{\pi}{6}\right)$ تساوي:", (r'\log_{2}(\sin x)', log(sin(x), 2))),
  [O(r'\frac{\sqrt{3}}{\ln 2}', sqrt(3)/log(2)), O(r'\sqrt{3}\ln 2', sqrt(3)*log(2)), O(r'\frac{1}{\sqrt{3}\ln 2}', 1/(sqrt(3)*log(2))), O(r'\frac{\ln 2}{\sqrt{3}}', log(2)/sqrt(3))],
  r"$f'(x)=\dfrac{\cos x}{\sin x\ln2}=\dfrac{\cot x}{\ln2}$ ، و $\cot\frac{\pi}{6}=\sqrt3$ ، إذن $f'\left(\frac{\pi}{6}\right)=\dfrac{\sqrt3}{\ln2}$",
  truth=Dx(log(sin(x), 2)).subs(x, pi/6), tag='مشتقة اللوغاريتم لأساس غير e'),
Q('m9q19', U3[3], 'hard',
  F(r"معادلة المماس لمنحنى المعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ عندما $t=\frac{\pi}{4}$ هي:", (r'2\cos t', 2*cos(t)), (r'3\sin t', 3*sin(t))),
  [O(r'y=-\frac{3}{2}x+3\sqrt{2}', -R(3, 2)*x+3*sqrt(2), 'eq'), O(r'y=-\frac{3}{2}x+\frac{3\sqrt{2}}{2}', -R(3, 2)*x+3*sqrt(2)/2, 'eq'),
   O(r'y=-\frac{2}{3}x+3\sqrt{2}', -R(2, 3)*x+3*sqrt(2), 'eq'), O(r'y=-\frac{2}{3}x+\frac{3\sqrt{2}}{2}', -R(2, 3)*x+3*sqrt(2)/2, 'eq')],
  r"النقطة: $\left(\sqrt2,\ \frac{3\sqrt2}{2}\right)$ ، والميل $\dfrac{3\cos t}{-2\sin t}=-\dfrac32$ عند $t=\frac{\pi}{4}$" "\n"
  r"$y-\frac{3\sqrt2}{2}=-\frac32(x-\sqrt2) \Rightarrow y=-\frac32x+\frac{3\sqrt2}{2}+\frac{3\sqrt2}{2}=-\frac32x+3\sqrt2$",
  truth=(lambda m_, p_: p_[1]+m_*(x-p_[0]))((diff(3*sin(t), t)/diff(2*cos(t), t)).subs(t, pi/4), (2*cos(pi/4), 3*sin(pi/4))),
  tag='مماس منحنى وسيطي'),
Q('m9q20', U3[4], 'medium',
  F(r"إذا كان: $«0»=x^{2}y$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(1,\,1)$ تساوي:", (r'e^{x-y}', exp(x-y))),
  [O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2)), O('-1', -1), O('1', 1)],
  r"$e^{x-y}(1-y')=2xy+x^2y'$ ، وعند $(1,1)$: $1-y'=2+y' \Rightarrow y'=-\dfrac12$",
  truth=imp(exp(x-y)-x**2*y, (1, 1)), tag='الاشتقاق الضمني عند نقطة'),
Q('m9q21', U3[4], 'hard',
  F(r"المقطع $y$ للمماس لمنحنى العلاقة: $«0»=3$ عند النقطة $(1,\,2)$ هو:", (r'xy^{2}-x^{2}', x*y**2-x**2)),
  [O(r'\frac{5}{2}', R(5, 2)), O(r'-\frac{5}{2}', -R(5, 2)), O('5', 5), O('-5', -5)],
  r"$y^2+2xyy'-2x=0$ ، وعند $(1,2)$: $4+4y'-2=0 \Rightarrow y'=-\dfrac12$" "\n" r"المماس: $y-2=-\frac12(x-1)$ ، وعند $x=0$: $y=2+\frac12=\frac52$",
  truth=lambda: 2+imp(x*y**2-x**2-3, (1, 2))*(0-1), tag='مماس منحنى علاقة ضمنية'),
Q('m9q22', U3[5], 'medium',
  r"تتمدّد كرة بحيث تزداد مساحة سطحها بمعدّل $16\pi\ \text{cm}^2/\text{s}$. معدّل تزايد حجمها في اللحظة التي يكون فيها نصف قطرها $3\ \text{cm}$ هو:",
  [O(r'24\pi', 24*pi, units='cm^3/s'), O(r'36\pi', 36*pi, units='cm^3/s'), O(r'16\pi', 16*pi, units='cm^3/s'), O(r'48\pi', 48*pi, units='cm^3/s')],
  r"$A=4\pi r^2 \Rightarrow 16\pi=8\pi(3)\dfrac{dr}{dt} \Rightarrow \dfrac{dr}{dt}=\dfrac23$" "\n" r"$V=\frac43\pi r^3 \Rightarrow \dfrac{dV}{dt}=4\pi r^2\dfrac{dr}{dt}=36\pi\cdot\dfrac23=24\pi\ \text{cm}^3/\text{s}$",
  truth=4*pi*9*(16*pi/(8*pi*3)), tag='معدلات مرتبطة: كرة'),
# ---------------- unit 4
Q('m9q23', U4[1], 'medium',
  r"إذا كان: $z=a+ai$ ، حيث $a<0$ ، وكان: $|z|=4$ ، فإنّ الصورة المثلثية للعدد المُركَّب $z$ هي:",
  [O(trig('4', r'-\frac{3\pi}{4}'), pol(4, -3*P/4)), O(trig('4', r'\frac{3\pi}{4}'), pol(4, 3*P/4)), O(trig('4', r'\frac{\pi}{4}'), pol(4, P/4)), O(trig('4', r'-\frac{\pi}{4}'), pol(4, -P/4))],
  r"$a^2+a^2=16 \Rightarrow a=-2\sqrt2$ (لأن $a<0$) ، فـ $z=-2\sqrt2-2\sqrt2i$ في الربع الثالث" "\n" r"زاوية الإسناد $\frac{\pi}{4}$ ، و $\text{Arg}(z)=-\pi+\frac{\pi}{4}=-\frac{3\pi}{4}$",
  truth=lambda: (lambda a0: a0+a0*I)([r_ for r_ in solve(2*a**2-16, a) if r_ < 0][0]), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
Q('m9q24', U4[2], 'easy',
  r"ناتج $z^{4}+\bar{w}$ هو:",
  [O('-1-4i', -1-4*I), O('-1+4i', -1+4*I), O('7-4i', 7-4*I), O('7+4i', 7+4*I)],
  r"$z^2=(1-i)^2=-2i$ ، $z^4=(-2i)^2=-4$ ، $\bar w=3-4i$ ، إذن $z^4+\bar w=-1-4i$",
  truth=expand((1-I)**4+(3-4*I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=1-i$ ، $w=3+4i$", 24, 25)),
Q('m9q25', U4[2], 'easy',
  r"ناتج $\dfrac{w}{\bar{z}}$ في الصورة القياسية هو:",
  [O(r'\frac{7+i}{2}', (7+I)/2), O(r'\frac{7-i}{2}', (7-I)/2), O(r'\frac{-1+7i}{2}', (-1+7*I)/2), O(r'\frac{-1-7i}{2}', (-1-7*I)/2)],
  r"$\bar z=1+i$ ، $\dfrac{3+4i}{1+i}\cdot\dfrac{1-i}{1-i}=\dfrac{3-3i+4i-4i^2}{2}=\dfrac{7+i}{2}$",
  truth=(3+4*I)/(1+I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
Q('m9q26', U4[1], 'medium',
  r"قيمة الثابت الحقيقي $a$ التي تجعل العدد $z=\dfrac{3+ai}{2-i}$ عددًا حقيقيًّا هي:",
  [O(r'-\frac{3}{2}', -R(3, 2)), O('6', 6), O(r'\frac{3}{2}', R(3, 2)), O('-6', -6)],
  r"$z=\dfrac{(3+ai)(2+i)}{5}=\dfrac{(6-a)+(3+2a)i}{5}$" "\n" r"حقيقي: الجزء التخيلي صفر: $3+2a=0 \Rightarrow a=-\dfrac32$",
  truth=lambda: solve(im(expand((3+X*I)*(2+I))), X)[0], tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
Q('m9q27', U4[2], 'medium',
  r"المعادلة التربيعية ذات المعاملات الحقيقية التي أحد جذريها العدد المُركَّب $\dfrac{7+i}{1-i}$ هي:",
  [O('x^{2}-6x+25=0', x**2-6*x+25, 'rel'), O('x^{2}+6x+25=0', x**2+6*x+25, 'rel'), O('x^{2}-6x-7=0', x**2-6*x-7, 'rel'), O('x^{2}+6x-7=0', x**2+6*x-7, 'rel')],
  r"$\dfrac{7+i}{1-i}\cdot\dfrac{1+i}{1+i}=\dfrac{7+8i+i^2}{2}=3+4i$ ، والجذر الآخر $3-4i$" "\n" r"المجموع $6$ ، والضرب $9+16=25$: $x^2-6x+25=0$",
  truth=lambda: (lambda r_: expand(x**2-2*re(r_)*x+re(r_)**2+im(r_)**2))(expand(simplify((7+I)/(1-I)))), tag='معادلة تربيعية بمعلومية جذر مركب'),
Q('m9q28', U4[2], 'hard',
  r"إذا كان: $z_1=-\sqrt{3}+i$ ، $z_2=-1-i$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{5\pi}{12}', 5*P/12), O(r'\frac{19\pi}{12}', 19*P/12), O(r'\frac{7\pi}{12}', 7*P/12), O(r'\frac{\pi}{12}', P/12)],
  r"$\text{Arg}(z_1)=\frac{5\pi}{6}$ ، $\text{Arg}(z_2)=-\frac{3\pi}{4}$ ، والفرق $\frac{5\pi}{6}+\frac{3\pi}{4}=\frac{19\pi}{12}>\pi$" "\n" r"فالزاوية الصغرى $2\pi-\frac{19\pi}{12}=\frac{5\pi}{12}$",
  truth=smaller_angle(-sqrt(3)+I, -1-I), tag='الزاوية بين عددين مركبين'),
Q('m9q29', U4[3], 'medium',
  r"الأعداد المُركَّبة $z$ التي تُحقّق المعادلتين: $|z|=5$ و $|z-6|=|z|$ معًا هي:",
  [O(r'3+4i,\ 3-4i', S_(3+4*I, 3-4*I), 'set'), O(r'4+3i,\ 4-3i', S_(4+3*I, 4-3*I), 'set'), O(r'-3+4i,\ -3-4i', S_(-3+4*I, -3-4*I), 'set'), O(r'-4+3i,\ -4-3i', S_(-4+3*I, -4-3*I), 'set')],
  r"$|z-6|=|z|$ هو العمود المنصّف للقطعة من $0$ إلى $6$ ، أي المستقيم $x=3$" "\n" r"وعلى الدائرة $x^2+y^2=25$: $9+y^2=25 \Rightarrow y=\pm4$ ، فالعددان $3\pm4i$",
  truth=lambda: FiniteSet(*[3+r_*I for r_ in solve(9+Y**2-25, Y)]), tag='تقاطع محلين هندسيين'),
IndexQ('m9q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي (الخط المتقطّع لا ينتمي إلى المنطقة) هو:",
  [T(r'$1<|z-1|\le3$ ، $-\frac{\pi}{2}\le\text{Arg}(z-1)\le\frac{\pi}{2}$', R9),
   T(r'$1\le|z-1|<3$ ، $-\frac{\pi}{2}\le\text{Arg}(z-1)\le\frac{\pi}{2}$', both(outside(1, 1), disk(1, 3, strict=True), sector(1, -math.pi/2, math.pi/2))),
   T(r'$1<|z+1|\le3$ ، $-\frac{\pi}{2}\le\text{Arg}(z+1)\le\frac{\pi}{2}$', both(outside(-1, 1, strict=True), disk(-1, 3), sector(-1, -math.pi/2, math.pi/2))),
   T(r'$1\le|z+1|<3$ ، $-\frac{\pi}{2}\le\text{Arg}(z+1)\le\frac{\pi}{2}$', both(outside(-1, 1), disk(-1, 3, strict=True), sector(-1, -math.pi/2, math.pi/2)))],
  r"الدائرتان مركزهما $(1,0)$ أي العدد $1$ ، نصفا قطريهما $1$ (متقطّعة: $<$) و $3$ (متصلة: $\le$): $1<|z-1|\le3$" "\n"
  r"والمنطقة على يمين المستقيم الرأسي المارّ بالمركز: الزوايا من $-\frac{\pi}{2}$ إلى $\frac{\pi}{2}$ مقيسة من المركز: $-\frac{\pi}{2}\le\text{Arg}(z-1)\le\frac{\pi}{2}$",
  truth=region_truth(R9, PR9, 5), figure=figure('m9q30', fig_region2(R9, PR9, 5), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 10
F10, G10 = [(0, 1), (2, 3), (6, 1)], [(0, 4), (3, 1), (6, 4)]
f10, fs10 = pw(F10)
g10, gs10 = pw(G10)
CURVE10 = x**2+x*y+y**2-3
R10 = both(disk(1 + 1j, 3, strict=True), sector(-1 + 1j, 0, 3*math.pi/4))
_s10 = math.sqrt(7) - math.sqrt(2)            # where the 3pi/4 ray from -1+i meets the circle
_q10 = complex(-1 - _s10/math.sqrt(2), 1 + _s10/math.sqrt(2))
PR10 = [('arc', 1 + 1j, 3, True, (0.0, cmath.phase(_q10 - (1 + 1j)))), ('seg', -1 + 1j, 4 + 1j, False), ('seg', -1 + 1j, _q10, False), ('open', -1 + 1j)]
P10 = [
# ---------------- unit 1
Q('m10q1', U1[1], 'medium',
  F(r"إذا كان $x=-\frac{1}{2}$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ الحلّين الآخرين لها هما:", (r'4x^{3}+1', 4*x**3+1), (r'6x^{2}+2x', 6*x**2+2*x)),
  [O(st(r'\frac{2+\sqrt{2}}{2}', r'\frac{2-\sqrt{2}}{2}'), S_((2+sqrt(2))/2, (2-sqrt(2))/2), 'set'), O(st(r'\frac{-2+\sqrt{2}}{2}', r'\frac{-2-\sqrt{2}}{2}'), S_((-2+sqrt(2))/2, (-2-sqrt(2))/2), 'set'),
   O(st(r'2+\sqrt{2}', r'2-\sqrt{2}'), S_(2+sqrt(2), 2-sqrt(2)), 'set'), O(st(r'-2+\sqrt{2}', r'-2-\sqrt{2}'), S_(-2+sqrt(2), -2-sqrt(2)), 'set')],
  r"$4x^3-6x^2-2x+1=0$ ، وبالقسمة التركيبية على $\left(x+\frac12\right)$: $4,\ -6,\ -2,\ 1 \to 4,\ -8,\ 2,\ 0$" "\n"
  r"$4x^2-8x+2=0 \Rightarrow 2x^2-4x+1=0 \Rightarrow x=\dfrac{4\pm\sqrt{8}}{4}=\dfrac{2\pm\sqrt2}{2}$",
  truth=lambda: other_roots(4*x**3-6*x**2-2*x+1, -R(1, 2)), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
Q('m10q2', U1[2], 'medium',
  F(r"إذا كان: $«0»=\dfrac{A}{x-1}+\dfrac{Bx+C}{x^{2}+2}$ ، فإنّ قيمة $C$ هي:", (r'\frac{3x^{2}-2x+5}{(x-1)(x^{2}+2)}', (3*x**2-2*x+5)/((x-1)*(x**2+2)))),
  [O('-1', -1), O('1', 1), O('2', 2), O('-2', -2)],
  r"$3x^2-2x+5=A(x^2+2)+(Bx+C)(x-1)$ ، عند $x=1$: $6=3A \Rightarrow A=2$" "\n" r"معامل $x^2$: $3=A+B \Rightarrow B=1$ ، الحد الثابت: $5=2A-C \Rightarrow C=-1$",
  truth=lambda: solve_pf((3*x**2-2*x+5)/((x-1)*(x**2+2)), A_/(x-1)+(B_*x+C_)/(x**2+2), [A_, B_, C_])[C_], tag='تجزئة: عامل تربيعي غير قابل للتحليل'),
Q('m10q3', U1[1], 'hard',
  r"إذا كان باقي قسمة $x^{n}+3$ على $(x+1)$ يساوي $2$ ، حيث $n$ عدد صحيح موجب، فإنّ باقي قسمة $x^{n+1}+3$ على $(x+1)$ يساوي:",
  [O('4', 4), O('2', 2), O('3', 3), O('1', 1)],
  r"الباقي الأول $(-1)^n+3=2 \Rightarrow (-1)^n=-1$ ، أي $n$ فردي" "\n" r"فيكون $n+1$ زوجيًّا، والباقي الثاني $(-1)^{n+1}+3=1+3=4$",
  truth=lambda: (lambda vals_: vals_.pop() if len(vals_) == 1 else None)({(-1)**(n_+1)+3 for n_ in range(1, 40) if (-1)**n_+3 == 2}),
  tag='نظرية الباقي وإيجاد ثابت'),
Q('m10q4', U1[2], 'medium',
  F(r"إذا كان: $«0»=\dfrac{A}{x-1}+\dfrac{B}{(x-1)^{2}}+\dfrac{C}{(x-1)^{3}}$ ، فإنّ قيمة $A+B+C$ هي:", (r'\frac{x+1}{(x-1)^{3}}', (x+1)/(x-1)**3)),
  [O('3', 3), O('2', 2), O('4', 4), O('1', 1)],
  r"$x+1=A(x-1)^2+B(x-1)+C$ ، ونكتب البسط بدلالة $(x-1)$: $x+1=(x-1)+2$" "\n" r"إذن $A=0$ ، $B=1$ ، $C=2$ ، و $A+B+C=3$",
  truth=lambda: (lambda s_: s_[A_]+s_[B_]+s_[C_])(solve_pf((x+1)/(x-1)**3, A_/(x-1)+B_/(x-1)**2+C_/(x-1)**3, [A_, B_, C_])),
  tag='تجزئة: عامل خطي مكرر'),
# ---------------- unit 2
Q('m10q5', U2[2], 'hard',
  r"إذا كان $\tan\theta=\frac{3}{4}$ ، و $\sin\theta<0$ ، حيث $0<\theta<2\pi$ ، فإنّ قيمة $\sin\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{3\sqrt{10}}{10}', 3*sqrt(10)/10), O(r'-\frac{3\sqrt{10}}{10}', -3*sqrt(10)/10), O(r'\frac{\sqrt{10}}{10}', sqrt(10)/10), O(r'-\frac{\sqrt{10}}{10}', -sqrt(10)/10)],
  r"الظل موجب والجيب سالب، إذن $\theta$ في الربع الثالث: $\pi<\theta<\frac{3\pi}{2}$ ، و $\cos\theta=-\frac45$" "\n"
  r"$\frac{\pi}{2}<\frac{\theta}{2}<\frac{3\pi}{4}$ فالجيب موجب: $\sin\frac{\theta}{2}=\sqrt{\dfrac{1+\frac45}{2}}=\sqrt{\dfrac{9}{10}}=\dfrac{3\sqrt{10}}{10}$",
  truth=sin((pi+atan(R(3, 4)))/2), tag='نصف الزاوية مع تحديد الربع'),
Q('m10q6', U2[1], 'medium',
  F(r"إذا كان $\tan A$ و $\tan B$ جذري المعادلة: $«0»=0$ ، فإنّ قيمة $\tan(A+B)$ هي:", (r'x^{2}-5x+6', x**2-5*x+6)),
  [O('-1', -1), O('1', 1), O(r'\frac{5}{7}', R(5, 7)), O(r'-\frac{5}{7}', -R(5, 7))],
  r"مجموع الجذرين $\tan A+\tan B=5$ ، وحاصل ضربهما $\tan A\tan B=6$ (أو: الجذران $2$ و $3$)" "\n" r"$\tan(A+B)=\dfrac{\tan A+\tan B}{1-\tan A\tan B}=\dfrac{5}{1-6}=-1$",
  truth=(lambda r_: (r_[0]+r_[1])/(1-r_[0]*r_[1]))(solve(x**2-5*x+6, x)), tag='المجموع والفرق: جذور معادلة'),
Q('m10q7', U2[1], 'hard',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\sin 3x}{\sin x}-\frac{\cos 3x}{\cos x}', sin(3*x)/sin(x)-cos(3*x)/cos(x))),
  [O('2', 2), O('1', 1), O(r'2\cos 2x', 2*cos(2*x)), O(r'4\cos^{2}x-1', 4*cos(x)**2-1)],
  r"بتوحيد المقامات: $\dfrac{\sin3x\cos x-\cos3x\sin x}{\sin x\cos x}=\dfrac{\sin(3x-x)}{\frac12\sin2x}=\dfrac{\sin2x}{\frac12\sin2x}=2$",
  truth=sin(3*x)/sin(x)-cos(3*x)/cos(x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
Q('m10q8', U2[1], 'hard',
  r"إذا كان: $\sin A+\sin B=1$ ، و $\cos A+\cos B=\frac{1}{2}$ ، فإنّ قيمة $\cos(A-B)$ هي:",
  [O(r'-\frac{3}{8}', -R(3, 8)), O(r'\frac{3}{8}', R(3, 8)), O(r'-\frac{1}{4}', -R(1, 4)), O(r'\frac{1}{4}', R(1, 4))],
  r"بتربيع المعادلتين وجمعهما: $(\sin^2A+\cos^2A)+(\sin^2B+\cos^2B)+2(\cos A\cos B+\sin A\sin B)=1+\frac14$" "\n"
  r"$2+2\cos(A-B)=\frac54 \Rightarrow \cos(A-B)=-\frac38$",
  truth=(1+R(1, 4)-2)/2, tag='المجموع والفرق بالتربيع'),
Q('m10q9', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=3$ في الفترة $[0,\,2\pi)$ هي:", (r'\sin^{2}x-3\cos x', sin(x)**2-3*cos(x))),
  [O(r'x=\pi', S_(P), 'set'), O('x=0', S_(0), 'set'), O(r'x=\frac{\pi}{2}', S_(P/2), 'set'), O(r'x=\frac{3\pi}{2}', S_(3*P/2), 'set')],
  r"$1-\cos^2x-3\cos x-3=0 \Rightarrow \cos^2x+3\cos x+2=0 \Rightarrow (\cos x+1)(\cos x+2)=0$" "\n" r"$\cos x=-2$ مرفوض، و $\cos x=-1 \Rightarrow x=\pi$",
  truth=lambda: sols(sin(x)**2-3*cos(x)-3, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
Q('m10q10', U2[3], 'hard',
  F(r"حلول المعادلة: $«0»=-2$ في الفترة $(\pi,\,2\pi)$ هي:", (r'\csc 2x', csc(2*x))),
  [O(st(r'\frac{19\pi}{12}', r'\frac{23\pi}{12}'), S_(19*P/12, 23*P/12), 'set'), O(st(r'\frac{7\pi}{12}', r'\frac{11\pi}{12}'), S_(7*P/12, 11*P/12), 'set'),
   O(st(r'\frac{19\pi}{6}', r'\frac{23\pi}{6}'), S_(19*P/6, 23*P/6), 'set'), O(st(r'\frac{7\pi}{6}', r'\frac{11\pi}{6}'), S_(7*P/6, 11*P/6), 'set')],
  r"$\sin2x=-\frac12$ ، و $\pi<x<2\pi \Rightarrow 2\pi<2x<4\pi$" "\n" r"$2x=2\pi+\frac{7\pi}{6}=\frac{19\pi}{6}$ أو $2x=2\pi+\frac{11\pi}{6}=\frac{23\pi}{6}$ ، إذن $x=\frac{19\pi}{12},\ \frac{23\pi}{12}$",
  truth=lambda: sols(sin(2*x)+R(1, 2), pi, 2*pi, closed_lo=False), tag='معادلة فيها مقلوب نسبة وزاوية مضاعفة'),
# ---------------- unit 3
Q('m10q11', U3[1], 'medium',
  F(r"قياس الزاوية التي يصنعها المماس لمنحنى الاقتران: $f(x)=«0»$ عند $x=0$ مع الاتجاه الموجب لمحور $x$ هو:", (r'\tan x-2x', tan(x)-2*x)),
  [O(r'\frac{3\pi}{4}', 3*P/4), O(r'\frac{\pi}{4}', P/4), O(r'-\frac{\pi}{4}', -P/4), O(r'\frac{2\pi}{3}', 2*P/3)],
  r"ميل المماس $f'(0)=\sec^20-2=-1$ ، وميل المستقيم يساوي ظل الزاوية التي يصنعها مع الاتجاه الموجب لمحور $x$ ($0\le\alpha<\pi$)" "\n" r"$\tan\alpha=-1 \Rightarrow \alpha=\frac{3\pi}{4}$",
  truth=(lambda m_: atan(m_) + (pi if m_ < 0 else 0))(Dx(tan(x)-2*x).subs(x, 0)), tag='زاوية ميل المماس'),
Q('m10q12', U3[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t\ge0$ الزمن بالثواني، و $s$ الموقع بالأمتار. موقع الجُسيم في اللحظة التي يكون فيها في حالة سكون لحظي هو:", (r'e^{2t}-4e^{t}', exp(2*t)-4*exp(t))),
  [O('-4', -4, units='m'), O('4', 4, units='m'), O('-3', -3, units='m'), O('3', 3, units='m')],
  r"$v(t)=2e^{2t}-4e^t=2e^t(e^t-2)=0 \Rightarrow e^t=2 \Rightarrow t=\ln2$" "\n" r"$s(\ln2)=e^{2\ln2}-4e^{\ln2}=4-8=-4\ \text{m}$",
  truth=lambda: (exp(2*t)-4*exp(t)).subs(t, solve(diff(exp(2*t)-4*exp(t), t), t)[0]), tag='الحركة: السرعة والتسارع'),
Q('m10q13', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $k>0$ ، وكان: $f'(1)=0$ ، فإنّ قيمة $k$ هي:", (r'\frac{x}{x^{2}+k}', x/(x**2+k))),
  [O('1', 1), O('2', 2), O('3', 3), O(r'\frac{1}{2}', R(1, 2))],
  r"$f'(x)=\dfrac{(x^2+k)-x(2x)}{(x^2+k)^2}=\dfrac{k-x^2}{(x^2+k)^2}$ ، إذن $f'(1)=0 \Rightarrow k-1=0 \Rightarrow k=1$",
  truth=lambda: [r_ for r_ in solve(Dx(x/(x**2+k)).subs(x, 1), k) if r_ > 0][0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
Q('m10q14', U3[2], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>0$ ، فإنّ $f''(e)$ تساوي:", (r'\frac{\ln x}{x}', log(x)/x)),
  [O(r'-\frac{1}{e^{3}}', -1/E**3), O(r'\frac{1}{e^{3}}', 1/E**3), O(r'-\frac{3}{e^{3}}', -3/E**3), O(r'\frac{3}{e^{3}}', 3/E**3)],
  r"$f'(x)=\dfrac{1-\ln x}{x^2}$ ، $f''(x)=\dfrac{-\frac1x\cdot x^2-(1-\ln x)(2x)}{x^4}=\dfrac{2\ln x-3}{x^3}$" "\n" r"$f''(e)=\dfrac{2-3}{e^3}=-\dfrac{1}{e^3}$",
  truth=diff(log(x)/x, x, 2).subs(x, E), tag='المشتقات العليا'),
Q('m10q15', U3[2], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ المشتقة الرابعة $f^{(4)}(x)$ تساوي:", (r'e^{x}\sin x', exp(x)*sin(x))),
  [O(r'-4e^{x}\sin x', -4*exp(x)*sin(x)), O(r'4e^{x}\sin x', 4*exp(x)*sin(x)), O(r'-4e^{x}\cos x', -4*exp(x)*cos(x)), O(r'4e^{x}\cos x', 4*exp(x)*cos(x))],
  r"$f'(x)=e^x(\sin x+\cos x)$ ، $f''(x)=2e^x\cos x$ ، $f'''(x)=2e^x(\cos x-\sin x)$" "\n" r"$f^{(4)}(x)=2e^x(\cos x-\sin x-\sin x-\cos x)=-4e^x\sin x$",
  truth=diff(exp(x)*sin(x), x, 4), tag='المشتقات العليا: إيجاد نمط'),
Q('m10q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=g\big(f(x)\big)$ ، فإنّ $h'(4)$ تساوي:",
  [O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2)), O('2', 2), O('-1', -1)],
  r"من الشكل: $f(4)=2$ ، $f'(4)=-\frac12$ (ميل القطعة من $(2,3)$ إلى $(6,1)$) ، $g'(2)=-1$ (ميل القطعة من $(0,4)$ إلى $(3,1)$)" "\n"
  r"$h'(4)=g'\big(f(4)\big)\cdot f'(4)=g'(2)\cdot\left(-\frac12\right)=\frac12$",
  truth=lambda: gs10(f10(4))*fs10(4), figure=figure('m10q16', draw_two(F10, G10, 6, 4, (0.6, 2.4), (4.7, 3.6))), tag='المشتقة من التمثيل البياني'),
Q('m10q17', U3[3], 'medium',
  F(r"يتسرّب الماء من خزّان، ويُعطى حجم الماء المتبقّي فيه (باللتر) بعد $t$ دقيقة بالاقتران: $V(t)=«0»$ ، حيث $0\le t\le40$. معدّل تغيّر حجم الماء في الخزّان عندما $t=10$ هو:", (r'500\left(1-\frac{t}{40}\right)^{2}', 500*(1-t/40)**2)),
  [O(r'-\frac{75}{4}', -R(75, 4), units='L/min'), O(r'\frac{75}{4}', R(75, 4), units='L/min'), O('-25', -25, units='L/min'), O('25', 25, units='L/min')],
  r"$V'(t)=500\cdot2\left(1-\frac{t}{40}\right)\cdot\left(-\frac{1}{40}\right)=-25\left(1-\frac{t}{40}\right)$" "\n" r"$V'(10)=-25\cdot\frac34=-\frac{75}{4}\ \text{L/min}$",
  truth=diff(500*(1-t/40)**2, t).subs(t, 10), tag='معدل التغير في سياق حياتي'),
Q('m10q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(0)$ تساوي:", (r'\log_{4}(e^{2x}+1)', log(exp(2*x)+1, 4))),
  [O(r'\frac{1}{\ln 4}', 1/log(4)), O(r'\frac{2}{\ln 4}', 2/log(4)), O(r'\frac{\ln 4}{2}', log(4)/2), O(r'\ln 4', log(4))],
  r"$f'(x)=\dfrac{2e^{2x}}{(e^{2x}+1)\ln4}$ ، إذن $f'(0)=\dfrac{2}{2\ln4}=\dfrac{1}{\ln4}$",
  truth=Dx(log(exp(2*x)+1, 4)).subs(x, 0), tag='مشتقة اللوغاريتم لأساس غير e'),
Q('m10q19', U3[3], 'hard',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، حيث $t>0$ ، فإنّ $\dfrac{d^{2}y}{dx^{2}}$ عندما $t=1$ تساوي:", (r't^{2}', t**2), (r't^{3}-6t', t**3-6*t)),
  [O(r'\frac{9}{4}', R(9, 4)), O(r'\frac{9}{2}', R(9, 2)), O(r'-\frac{3}{4}', -R(3, 4)), O(r'-\frac{3}{2}', -R(3, 2))],
  r"$\dfrac{dy}{dx}=\dfrac{3t^2-6}{2t}=\dfrac32t-\dfrac3t$ ، و $\dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)=\dfrac32+\dfrac{3}{t^2}=\dfrac92$ عند $t=1$" "\n"
  r"$\dfrac{d^2y}{dx^2}=\dfrac{9/2}{dx/dt}=\dfrac94$",
  truth=(lambda dydx: (diff(dydx, t)/diff(t**2, t)).subs(t, 1))(diff(t**3-6*t, t)/diff(t**2, t)), tag='المشتقة الثانية للمعادلات الوسيطية'),
Q('m10q20', U3[4], 'easy',
  r"ميل المماس لمنحنى العلاقة عند النقطة $(1,\,1)$ هو:",
  [O('-1', -1), O('1', 1), O('-3', -3), O('3', 3)],
  r"$2x+y+xy'+2yy'=0 \Rightarrow y'=-\dfrac{2x+y}{x+2y}$ ، وعند $(1,1)$: $y'=-\dfrac33=-1$",
  truth=imp(CURVE10, (1, 1)), tag='الاشتقاق الضمني عند نقطة',
  lead=shared(r"إذا كانت العلاقة: $" + M(r'x^{2}+xy+y^{2}', x**2+x*y+y**2) + r"=3$", 20, 21)),
Q('m10q21', U3[4], 'hard',
  r"النقاط الواقعة على منحنى العلاقة، والتي يكون المماس عندها أفقيًّا، هي:",
  [O(r'(1,\ -2),\ (-1,\ 2)', FiniteSet(Tuple(1, -2), Tuple(-1, 2)), 'tset'), O(r'(-2,\ 1),\ (2,\ -1)', FiniteSet(Tuple(-2, 1), Tuple(2, -1)), 'tset'),
   O(r'(1,\ 2),\ (-1,\ -2)', FiniteSet(Tuple(1, 2), Tuple(-1, -2)), 'tset'), O(r'(2,\ 1),\ (-2,\ -1)', FiniteSet(Tuple(2, 1), Tuple(-2, -1)), 'tset')],
  r"المماس أفقي عندما $y'=0$ ، أي $2x+y=0 \Rightarrow y=-2x$ (والمقام $x+2y\ne0$)" "\n" r"بالتعويض: $x^2-2x^2+4x^2=3 \Rightarrow x^2=1 \Rightarrow x=\pm1$ ، فالنقطتان $(1,-2)$ و $(-1,2)$",
  truth=lambda: FiniteSet(*[Tuple(s_[x], s_[y]) for s_ in solve([2*x+y, CURVE10], [x, y], dict=True)]), tag='مماس أفقي لمنحنى ضمني'),
Q('m10q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي حوض ماء طوله $4\ \text{m}$ ، ومقطعه العرضي مثلث متطابق الضلعين رأسه إلى الأسفل، طول قاعدته (في الأعلى) $2\ \text{m}$ وارتفاعه $1\ \text{m}$. يُضَخّ إليه الماء بمعدّل $400\ \text{L/min}$ ، فإنّ معدّل ارتفاع سطح الماء عندما يكون عمق الماء $0.5\ \text{m}$ هو:",
  [D('0.1', 'm/min'), D('100', 'm/min'), D('0.05', 'm/min'), D('0.2', 'm/min')],
  r"بالتشابه: عرض سطح الماء $w=2h$ ، فالحجم $V=\frac12(2h)(h)(4)=4h^2$" "\n"
  r"$400\ \text{L/min}=0.4\ \text{m}^3/\text{min}$ ، و $\dfrac{dV}{dt}=8h\dfrac{dh}{dt} \Rightarrow 0.4=4\dfrac{dh}{dt} \Rightarrow \dfrac{dh}{dt}=0.1\ \text{m/min}$",
  truth=R(4, 10)/diff(4*h_**2, h_).subs(h_, R(1, 2)), figure=figure('m10q22', fig_trough(), 3.8, 2.6), tag='معدلات مرتبطة مع تحويل الوحدات'),
# ---------------- unit 4
Q('m10q23', U4[1], 'medium',
  r"إذا كان: $\bar{z}=\dfrac{2i}{1+i}$ ، فإنّ الصورة المثلثية للعدد المُركَّب $z$ هي:",
  [O(trig(r'\sqrt{2}', r'-\frac{\pi}{4}'), pol(sqrt(2), -P/4)), O(trig(r'\sqrt{2}', r'\frac{\pi}{4}'), pol(sqrt(2), P/4)), O(trig(r'\sqrt{2}', r'\frac{3\pi}{4}'), pol(sqrt(2), 3*P/4)), O(trig(r'\sqrt{2}', r'-\frac{3\pi}{4}'), pol(sqrt(2), -3*P/4))],
  r"$\bar z=\dfrac{2i(1-i)}{2}=i-i^2=1+i$ ، إذن $z=1-i$" "\n" r"$|z|=\sqrt2$ ، و $z$ في الربع الرابع: $\text{Arg}(z)=-\frac{\pi}{4}$",
  truth=conjugate(expand(simplify(2*I/(1+I)))), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
Q('m10q24', U4[2], 'easy',
  r"ناتج $z\bar{w}$ هو:",
  [O('-4+7i', -4+7*I), O('-4-7i', -4-7*I), O('8+7i', 8+7*I), O('8-7i', 8-7*I)],
  r"$\bar w=1+2i$ ، $z\bar w=(2+3i)(1+2i)=2+4i+3i+6i^2=-4+7i$",
  truth=expand((2+3*I)*(1+2*I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=2+3i$ ، $w=1-2i$", 24, 25)),
Q('m10q25', U4[2], 'medium',
  r"ناتج $\dfrac{z^{2}}{w}$ في الصورة القياسية هو:",
  [O(r'\frac{-29+2i}{5}', (-29+2*I)/5), O(r'\frac{-29-2i}{5}', (-29-2*I)/5), O(r'\frac{19+2i}{5}', (19+2*I)/5), O(r'\frac{19-2i}{5}', (19-2*I)/5)],
  r"$z^2=4+12i+9i^2=-5+12i$" "\n" r"$\dfrac{-5+12i}{1-2i}\cdot\dfrac{1+2i}{1+2i}=\dfrac{-5-10i+12i+24i^2}{5}=\dfrac{-29+2i}{5}$",
  truth=(2+3*I)**2/(1-2*I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
Q('m10q26', U4[1], 'medium',
  r"قيم الثابت الحقيقي $a$ التي تجعل العدد $z=(a+i)(2-ai)$ عددًا حقيقيًّا هي:",
  [O(r'\pm\sqrt{2}', S_(sqrt(2), -sqrt(2)), 'set'), O(r'\pm 2', S_(2, -2), 'set'), O(r'\sqrt{2}', S_(sqrt(2)), 'set'), O('0', S_(0), 'set')],
  r"$z=2a-a^2i+2i-ai^2=3a+(2-a^2)i$" "\n" r"حقيقي: $2-a^2=0 \Rightarrow a=\pm\sqrt2$",
  truth=lambda: FiniteSet(*solve(im(expand((X+I)*(2-X*I))), X)), tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
Q('m10q27', U4[2], 'hard',
  r"إذا كان العدد $1+2i$ أحد جذور المعادلة: $z^{3}+az^{2}+bz-15=0$ ، حيث $a,\ b$ عددان حقيقيان، فإنّ قيمة $a+b$ هي:",
  [O('6', 6), O('-6', -6), O('16', 16), O('-16', -16)],
  r"المرافق $1-2i$ جذر أيضًا، و $(z-1-2i)(z-1+2i)=z^2-2z+5$" "\n"
  r"الجذر الثالث $c$: $5\cdot(-c)=-15 \Rightarrow c=3$ ، و $(z^2-2z+5)(z-3)=z^3-5z^2+11z-15$ ، إذن $a=-5$ ، $b=11$ ، $a+b=6$",
  truth=lambda: (lambda e_: (lambda s_: s_[X]+s_[Y])(solve([re(e_), im(e_)], [X, Y])))(expand((1+2*I)**3+X*(1+2*I)**2+Y*(1+2*I)-15)),
  tag='معادلة كثير حدود بجذر مركب'),
Q('m10q28', U4[2], 'medium',
  r"يُبيّن الشكل الآتي النقطتين $A$ و $B$ اللتين تُمثّلان العددين المُركَّبين $z_1$ و $z_2$ على الترتيب. قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{\pi}{2}', P/2), O(r'\frac{3\pi}{2}', 3*P/2), O(r'\frac{\pi}{6}', P/6), O(r'\frac{5\pi}{6}', 5*P/6)],
  r"$\text{Arg}(z_1)=\text{Arg}(-1+\sqrt3i)=\frac{2\pi}{3}$ ، $\text{Arg}(z_2)=\text{Arg}(-\sqrt3-i)=-\frac{5\pi}{6}$" "\n"
  r"الفرق $\frac{2\pi}{3}+\frac{5\pi}{6}=\frac{3\pi}{2}>\pi$ ، فالزاوية الصغرى $2\pi-\frac{3\pi}{2}=\frac{\pi}{2}$",
  truth=smaller_angle(-1+sqrt(3)*I, -sqrt(3)-I),
  figure=figure('m10q28', fig_argand([((-1, math.sqrt(3)), 'A', r'$(-1,\,\sqrt{3})$', (-1.9, 0.25)), ((-math.sqrt(3), -1), 'B', r'$(-\sqrt{3},\,-1)$', (-0.6, -0.55))], 3), 3.4, 3.4),
  tag='الزاوية بين عددين مركبين'),
Q('m10q29', U4[3], 'hard',
  r"العدد المُركَّب $z$ الواقع على الدائرة $|z-3-4i|=2$ ، والأقرب إلى نقطة الأصل، هو:",
  [O(r'\frac{9}{5}+\frac{12}{5}i', R(9, 5)+R(12, 5)*I), O(r'\frac{21}{5}+\frac{28}{5}i', R(21, 5)+R(28, 5)*I), O('1+4i', 1+4*I), O('3+2i', 3+2*I)],
  r"المركز $3+4i$ على بُعد $5$ من الأصل، وأقرب نقطة تقع على القطعة الواصلة بين الأصل والمركز على بُعد $5-2=3$ من الأصل" "\n"
  r"$z=\dfrac35(3+4i)=\dfrac95+\dfrac{12}{5}i$",
  truth=(3+4*I)*(1-2/Abs(3+4*I)), tag='القيمة العظمى والصغرى للمقياس على محل هندسي'),
IndexQ('m10q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي (الخط المتقطّع لا ينتمي إلى المنطقة) هو:",
  [T(r'$|z-1-i|<3$ ، $0\le\text{Arg}(z+1-i)\le\frac{3\pi}{4}$', R10),
   T(r'$|z-1-i|\le3$ ، $0\le\text{Arg}(z+1-i)\le\frac{3\pi}{4}$', both(disk(1 + 1j, 3), sector(-1 + 1j, 0, 3*math.pi/4))),
   T(r'$|z-1-i|<3$ ، $0\le\text{Arg}(z-1+i)\le\frac{3\pi}{4}$', both(disk(1 + 1j, 3, strict=True), sector(1 - 1j, 0, 3*math.pi/4))),
   T(r'$|z-1-i|\le3$ ، $0\le\text{Arg}(z-1+i)\le\frac{3\pi}{4}$', both(disk(1 + 1j, 3), sector(1 - 1j, 0, 3*math.pi/4)))],
  r"القوس المتقطّع من دائرة مركزها $(1,1)$ أي العدد $1+i$ ونصف قطرها $3$ ، ولا ينتمي إلى المنطقة: $|z-1-i|<3$" "\n"
  r"والقطعتان المتصلتان تبدآن من النقطة $(-1,1)$ أي العدد $-1+i$ بزاويتي $0$ و $\frac{3\pi}{4}$: $0\le\text{Arg}(z+1-i)\le\frac{3\pi}{4}$",
  truth=region_truth(R10, PR10, 5), figure=figure('m10q30', fig_region2(R10, PR10, 5), 3.4, 3.4),
  tag='منطقة في المستوى المركب من الشكل'),
]
