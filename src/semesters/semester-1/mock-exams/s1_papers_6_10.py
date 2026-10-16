"""Semester-1 mock papers 6-10 (m6q1..m10q30), same layout as papers 1-5:
U1 items 1-4, U2 items 5-10, U3 items 11-22, U4 items 23-30.
Every item is modelled on a named official ministry item (the comment above each Q gives it: 2026 = paper of
2 July 2026, gen 2008; 2025/2024 = summer paper 1; 2025s/2024s = supplementary; 2026r = 2026 repeaters; 2023 =
summer paper 1): same skill, same stem structure, same kind of function and numbers, same option grid -- new
function and numbers. Region items are checked by sampling: each option is a predicate, the shaded figure is drawn
from the correct predicate, and the distractors must differ from it inside the plane or on its boundary."""
import cmath
import math
from s1_helpers import *

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


# ================================================================== PAPER 6
# Each item names the official item it is modelled on (2026 = 2 July 2026 paper, gen 2008; 2025/2024 = summer
# paper 1; 2025s/2024s = supplementary; 2026r = 2026 repeaters). Same skill, same stem structure, same kind of
# function and numbers, same option grid -- new function and numbers.
F6, G6 = [(0, 5), (4, 1), (6, 3)], [(0, 0), (2, 4), (6, 2)]
_q6 = complex(1 - (math.sqrt(2) + math.sqrt(34))/2/math.sqrt(2), -1 + (math.sqrt(2) + math.sqrt(34))/2/math.sqrt(2))
R6 = both(disk(-1j, 3), sector(1 - 1j, 0, 3*math.pi/4, hi_open=True))
PR6 = [('arc', -1j, 3, False, (0.0, cmath.phase(_q6 + 1j))), ('seg', 1 - 1j, 3 - 1j, False), ('seg', 1 - 1j, _q6, True), ('open', 1 - 1j)]
P6 = [
# ---------------- unit 1
# 2026 #1: one root given, equation not set to zero, options = signs of the other two roots
Q('m6q1', U1[1], 'easy',
  F(r"إذا كان $x=2$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ لها حلَّين آخرين هما:", (r'x^{3}+24', x**3+24), (r'3x^{2}+10x', 3*x**2+10*x)),
  [O(st('4', '-3'), S_(4, -3), 'set'), O(st('-4', '3'), S_(-4, 3), 'set'), O(st('-4', '-3'), S_(-4, -3), 'set'), O(st('4', '3'), S_(4, 3), 'set')],
  r"$x^3-3x^2-10x+24=0$ ، وبالقسمة التركيبية على $(x-2)$: $1,\ -3,\ -10,\ 24 \to 1,\ -1,\ -12,\ 0$" "\n"
  r"$x^2-x-12=(x-4)(x+3)=0 \Rightarrow x=4,\ x=-3$",
  truth=lambda: other_roots(x**3-3*x**2-10*x+24, 2), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# 2026 #2: repeated linear factor, "which is the decomposition", options = numerators swapped x sign
Q('m6q2', U1[2], 'easy',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{4x-5}{(x-2)^{2}}', (4*x-5)/(x-2)**2)),
  [O(r'\frac{4}{x-2}+\frac{3}{(x-2)^{2}}', 4/(x-2)+3/(x-2)**2), O(r'\frac{3}{x-2}+\frac{4}{(x-2)^{2}}', 3/(x-2)+4/(x-2)**2),
   O(r'\frac{4}{x-2}-\frac{3}{(x-2)^{2}}', 4/(x-2)-3/(x-2)**2), O(r'\frac{3}{x-2}-\frac{4}{(x-2)^{2}}', 3/(x-2)-4/(x-2)**2)],
  r"$\dfrac{4x-5}{(x-2)^2}=\dfrac{A}{x-2}+\dfrac{B}{(x-2)^2} \Rightarrow 4x-5=A(x-2)+B$" "\n"
  r"معامل $x$: $A=4$ ، وعند $x=2$: $B=3$",
  truth=(4*x-5)/(x-2)**2, tag='تجزئة: عامل خطي مكرر'),
# 2026 #3: equal remainders on two linear divisors -> constant, options = sign x magnitude
Q('m6q3', U1[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x-2)$ مساويًا لباقي قسمته على $(x+1)$ ، فإنّ قيمة الثابت $p$ هي:", (r'x^{4}+x^{3}+px-20', x**4+x**3+p*x-20)),
  [O('-8', -8), O('8', 8), O('2', 2), O('-2', -2)],
  r"$f(2)=16+8+2p-20=4+2p$ ، $f(-1)=1-1-p-20=-20-p$" "\n" r"$4+2p=-20-p \Rightarrow 3p=-24 \Rightarrow p=-8$",
  truth=lambda: solve(rem(x**4+x**3+p*x-20, 2)-rem(x**4+x**3+p*x-20, -1), p)[0], tag='نظرية الباقي وإيجاد ثابت'),
# 2026 #2 (distinct linear factors version): which is the decomposition, options = numerators swapped x factor signs
Q('m6q4', U1[2], 'easy',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{5x+1}{(x-1)(x+2)}', (5*x+1)/((x-1)*(x+2)))),
  [O(r'\frac{2}{x-1}+\frac{3}{x+2}', 2/(x-1)+3/(x+2)), O(r'\frac{3}{x-1}+\frac{2}{x+2}', 3/(x-1)+2/(x+2)),
   O(r'\frac{2}{x+1}+\frac{3}{x-2}', 2/(x+1)+3/(x-2)), O(r'\frac{3}{x+1}+\frac{2}{x-2}', 3/(x+1)+2/(x-2))],
  r"$5x+1=A(x+2)+B(x-1)$" "\n" r"عند $x=1$: $6=3A \Rightarrow A=2$ ، وعند $x=-2$: $-9=-3B \Rightarrow B=3$",
  truth=(5*x+1)/((x-1)*(x+2)), tag='تجزئة: عوامل خطية مختلفة'),
# ---------------- unit 2
# 2026 #4: tan(theta/2) from cos theta and a quadrant, options = sign x reciprocal
Q('m6q5', U2[2], 'medium',
  r"إذا كان: $\cos\theta=-\frac{1}{3}$ ، $\pi<\theta<\frac{3\pi}{2}$ ، فإنّ قيمة $\tan\frac{\theta}{2}$ تساوي:",
  [O(r'-\sqrt{2}', -sqrt(2)), O(r'\sqrt{2}', sqrt(2)), O(r'-\frac{1}{\sqrt{2}}', -1/sqrt(2)), O(r'\frac{1}{\sqrt{2}}', 1/sqrt(2))],
  r"$\frac{\pi}{2}<\frac{\theta}{2}<\frac{3\pi}{4}$ (الربع الثاني) فالظل سالب" "\n"
  r"$\tan\frac{\theta}{2}=-\sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}}=-\sqrt{\dfrac{4/3}{2/3}}=-\sqrt2$",
  truth=tan((pi+acos(R(1, 3)))/2), tag='نصف الزاوية مع تحديد الربع'),
# 2026 #5: simplest form with a sum identity, options = coefficient x sin/cos
Q('m6q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(x+\frac{\pi}{3})-\frac{\sqrt{3}}{2}\cos x', sin(x+pi/3)-sqrt(3)/2*cos(x))),
  [O(r'\frac{1}{2}\sin x', sin(x)/2), O(r'\frac{\sqrt{3}}{2}\sin x', sqrt(3)/2*sin(x)), O(r'\frac{1}{2}\cos x', cos(x)/2), O(r'\frac{\sqrt{3}}{2}\cos x', sqrt(3)/2*cos(x))],
  r"$\sin\left(x+\frac{\pi}{3}\right)=\frac12\sin x+\frac{\sqrt3}{2}\cos x$ ، وبطرح $\frac{\sqrt3}{2}\cos x$ يبقى $\frac12\sin x$",
  truth=sin(x+pi/3)-sqrt(3)/2*cos(x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #6: equivalent expression (one reciprocal ratio), options = csc/sec/2sin/2cos
Q('m6q7', U2[1], 'easy',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\sin x+\cos x\cot x', sin(x)+cos(x)*cot(x))),
  [O(r'\csc x', csc(x)), O(r'\sec x', sec(x)), O(r'2\sin x', 2*sin(x)), O(r'2\cos x', 2*cos(x))],
  r"$\sin x+\cos x\cdot\dfrac{\cos x}{\sin x}=\dfrac{\sin^2x+\cos^2x}{\sin x}=\dfrac{1}{\sin x}=\csc x$",
  truth=sin(x)+cos(x)*cot(x), tag='المتطابقات الأساسية'),
# 2026 #4 sibling (double angle from one ratio and a quadrant), options = sign x sin/cos value
Q('m6q8', U2[2], 'easy',
  r"إذا كان: $\sin\theta=\frac{3}{5}$ ، $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\sin 2\theta$ تساوي:",
  [O(r'-\frac{24}{25}', -R(24, 25)), O(r'\frac{24}{25}', R(24, 25)), O(r'-\frac{7}{25}', -R(7, 25)), O(r'\frac{7}{25}', R(7, 25))],
  r"في الربع الثاني: $\cos\theta=-\frac45$" "\n" r"$\sin2\theta=2\sin\theta\cos\theta=2\left(\frac35\right)\left(-\frac45\right)=-\frac{24}{25}$",
  truth=sin(2*(pi-asin(R(3, 5)))), tag='ضعف الزاوية بمعلومية نسبة'),
# 2026 #7: quadratic in a trig ratio, one root rejected, single quadrantal answer
Q('m6q9', U2[3], 'easy',
  F(r"حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هو:", (r'\sin^{2}x+2\sin x-3', sin(x)**2+2*sin(x)-3)),
  [O(st(r'\frac{\pi}{2}'), S_(P/2), 'set'), O(st(r'\frac{3\pi}{2}'), S_(3*P/2), 'set'), O(st('0'), S_(0), 'set'), O(st(r'\pi'), S_(P), 'set')],
  r"$(\sin x+3)(\sin x-1)=0$ ، و $\sin x=-3$ مرفوض لأنّ $-1\le\sin x\le1$" "\n" r"$\sin x=1 \Rightarrow x=\frac{\pi}{2}$",
  truth=lambda: sols(sin(x)**2+2*sin(x)-3, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
# 2026 #8: reciprocal ratio -> double angle, interval (pi, 2pi); options = halved or not x shifted or not
Q('m6q10', U2[3], 'hard',
  F(r"حُلول المعادلة: $«0»=0$ في الفترة $(\pi,\,2\pi)$ هي:", (r'4\sin x-\sec x', 4*sin(x)-sec(x))),
  [O(st(r'\frac{13\pi}{12}', r'\frac{17\pi}{12}'), S_(13*P/12, 17*P/12), 'set'), O(st(r'\frac{\pi}{12}', r'\frac{5\pi}{12}'), S_(P/12, 5*P/12), 'set'),
   O(st(r'\frac{13\pi}{6}', r'\frac{17\pi}{6}'), S_(13*P/6, 17*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set')],
  r"نضرب في $\cos x\ne0$: $4\sin x\cos x=1 \Rightarrow 2\sin2x=1 \Rightarrow \sin2x=\frac12$" "\n"
  r"$x\in(\pi,2\pi) \Rightarrow 2x\in(2\pi,4\pi)$: $2x=\frac{13\pi}{6},\ \frac{17\pi}{6} \Rightarrow x=\frac{13\pi}{12},\ \frac{17\pi}{12}$",
  truth=lambda: sols(4*sin(x)-sec(x), pi, 2*pi, closed_lo=False), tag='معادلة فيها مقلوب نسبة وزاوية مضاعفة'),
# ---------------- unit 3
# 2026 #9: f'(x) x f(x) for a sin/cos sum collapses to a double angle; options = sign x sin/cos
Q('m6q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)\times f(x)$ هو:", (r'\sin x-\cos x', sin(x)-cos(x))),
  [O(r'-\cos 2x', -cos(2*x)), O(r'\cos 2x', cos(2*x)), O(r'-\sin 2x', -sin(2*x)), O(r'\sin 2x', sin(2*x))],
  r"$f'(x)=\cos x+\sin x$" "\n" r"$f'(x)f(x)=(\sin x+\cos x)(\sin x-\cos x)=\sin^2x-\cos^2x=-\cos2x$",
  truth=Dx(sin(x)-cos(x))*(sin(x)-cos(x)), tag='مشتقات الاقترانات المثلثية'),
# 2025 #5 / 2025s #5: slope of the normal to an exponential a^(linear); options = sign x slope/normal slope
Q('m6q12', U3[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ ميل العمودي على المماس لمنحنى الاقتران $f(x)$ عندما $x=1$ هو:", (r'3^{1-2x}', 3**(1-2*x))),
  [O(r'\frac{3}{2\ln 3}', 3/(2*log(3))), O(r'-\frac{3}{2\ln 3}', -3/(2*log(3))), O(r'-\frac{2\ln 3}{3}', -2*log(3)/3), O(r'\frac{2\ln 3}{3}', 2*log(3)/3)],
  r"$f'(x)=3^{1-2x}\ln3\cdot(-2)$ ، $f'(1)=3^{-1}\ln3\cdot(-2)=-\dfrac{2\ln3}{3}$ (ميل المماس)" "\n" r"ميل العمودي: $m_{\perp}=-\dfrac{1}{f'(1)}=\dfrac{3}{2\ln3}$",
  truth=-1/Dx(3**(1-2*x)).subs(x, 1), tag='معادلة العمودي على المماس'),
# 2026 #10: root times polynomial with a constant, f'(a) given -> constant; options = small integers
Q('m6q13', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(4)=22$ ، فإنّ قيمة الثابت $b$ هي:", (r'\sqrt{x}\,(x^{2}+b)', sqrt(x)*(x**2+b))),
  [O('8', 8), O('4', 4), O('16', 16), O('2', 2)],
  r"$f'(x)=\dfrac{1}{2\sqrt x}(x^2+b)+\sqrt x(2x)$" "\n" r"$f'(4)=\dfrac{16+b}{4}+2(8)=22 \Rightarrow \dfrac{16+b}{4}=6 \Rightarrow b=8$",
  truth=lambda: solve(Dx(sqrt(x)*(x**2+b)).subs(x, 4)-22, b)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2026 #11: combination of f'' and f' for a sum of exponentials; options = sign x exponent
Q('m6q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''(x)+3f'(x)$ هي:", (r'e^{x}+e^{-3x}', exp(x)+exp(-3*x))),
  [O(r'4e^{x}', 4*exp(x)), O(r'-4e^{x}', -4*exp(x)), O(r'4e^{-3x}', 4*exp(-3*x)), O(r'-4e^{-3x}', -4*exp(-3*x))],
  r"$f'(x)=e^x-3e^{-3x}$ ، $f''(x)=e^x+9e^{-3x}$" "\n" r"$f''+3f'=e^x+9e^{-3x}+3e^x-9e^{-3x}=4e^x$",
  truth=diff(exp(x)+exp(-3*x), x, 2)+3*Dx(exp(x)+exp(-3*x)), tag='المشتقات العليا وتراكيبها'),
# 2026 #12 (temperature after sunset): a cooling model in context, units in stem and options; sign x power slip
Q('m6q15', U3[3], 'medium',
  F(r"إذا أمكن التعبير عن درجة حرارة كوب من الشاي بعد سكبه بالاقتران: $T(t)=«0»$ ، حيث $t$ الزمن بالدقائق، و $T$ درجة الحرارة بالسيلسيوس، فإنّ معدّل تغيّر درجة حرارة الشاي عندما $t=1$ هو:", (r'20+\frac{60}{(t+1)^{2}}', 20+60/(t+1)**2)),
  [O('-15', -15, units='°C/min'), O('15', 15, units='°C/min'), O('-30', -30, units='°C/min'), O('30', 30, units='°C/min')],
  r"$T(t)=20+60(t+1)^{-2} \Rightarrow T'(t)=-120(t+1)^{-3}$" "\n" r"$T'(1)=-\dfrac{120}{8}=-15\ ^\circ\text{C/min}$",
  truth=diff(20+60/(t+1)**2, t).subs(t, 1), tag='معدل التغير في سياق حياتي'),
# 2026 #14 / 2024s #5: two piecewise-linear graphs, h built from f and g; options = sign x magnitude
Q('m6q16', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=f(x)\,g(x)$ ، فإنّ $h'(1)$ هي:",
  [O('6', 6), O('-6', -6), O('10', 10), O('-10', -10)],
  r"من الشكل: $f(1)=4$ ، $f'(1)=-1$ (ميل القطعة الأولى من $f$) ، $g(1)=2$ ، $g'(1)=2$" "\n" r"$h'(1)=f'(1)g(1)+f(1)g'(1)=(-1)(2)+(4)(2)=6$",
  truth=lambda: (lambda fv, fs, gv, gs: fs(1)*gv(1)+fv(1)*gs(1))(*pw(F6), *pw(G6)),
  figure=figure('m6q16', draw_two(F6, G6, 6, 5, (5.2, 1.5), (4.4, 3.3))), tag='المشتقة من التمثيل البياني'),
# 2026 #13: log base a of (c + ln x), f'(e); options = e vs 1/e x ln(a^n) right vs wrong
Q('m6q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(e)$ هي:", (r'\log_{2}(3+\ln x)', log(3+log(x), 2))),
  [O(r'\frac{1}{e\ln 16}', 1/(E*log(16))), O(r'\frac{1}{e\ln 8}', 1/(E*log(8))), O(r'\frac{e}{\ln 16}', E/log(16)), O(r'\frac{e}{\ln 8}', E/log(8))],
  r"$f'(x)=\dfrac{1}{(3+\ln x)\ln2}\cdot\dfrac1x$" "\n" r"$f'(e)=\dfrac{1}{(3+1)\ln2\cdot e}=\dfrac{1}{e\cdot4\ln2}=\dfrac{1}{e\ln16}$",
  truth=Dx(log(3+log(x), 2)).subs(x, E), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2025 #9 / 2026r #6: h = root of an expression in f, values f(a), f'(a) given; options = sign x missing 1/2
Q('m6q18', U3[3], 'medium',
  r"إذا كان: $h(x)=\sqrt{5+(f(x))^{3}}$ ، وكان: $f(2)=-1$ ، $f'(2)=4$ ، فإنّ $h'(2)$ هي:",
  [O('3', 3), O('-3', -3), O('6', 6), O('-6', -6)],
  r"$h'(x)=\dfrac{3(f(x))^2f'(x)}{2\sqrt{5+(f(x))^3}}$" "\n" r"$h'(2)=\dfrac{3(-1)^2(4)}{2\sqrt{5-1}}=\dfrac{12}{4}=3$",
  truth=(diff(sqrt(5+s**3), s)*4).subs(s, -1), tag='قاعدة السلسلة من قيم معطاة'),
# 2026 #15: parametric with sec/tan at a special t; options = reciprocal x factor 2
Q('m6q19', U3[3], 'medium',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، حيث: $-\frac{\pi}{2}<t<\frac{\pi}{2}$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\frac{\pi}{6}$ هو:", (r'1+2\tan t', 1+2*tan(t)), (r'\sec t', sec(t))),
  [O(r'\frac{1}{4}', R(1, 4)), O('4', 4), O(r'\frac{1}{2}', R(1, 2)), O('2', 2)],
  r"$\dfrac{dx}{dt}=2\sec^2t=2\cdot\dfrac43=\dfrac83$ ، $\dfrac{dy}{dt}=\sec t\tan t=\dfrac{2}{\sqrt3}\cdot\dfrac{1}{\sqrt3}=\dfrac23$" "\n"
  r"$\dfrac{dy}{dx}=\dfrac{2/3}{8/3}=\dfrac14$",
  truth=(diff(sec(t), t)/diff(1+2*tan(t), t)).subs(t, pi/6), tag='مشتقة المعادلات الوسيطية'),
# 2026 #16: a^x ln y = rational in x, y; point found from y = 1; options = unit fractions
Q('m6q20', U3[4], 'hard',
  F(r"إذا كان: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $y=1$ هو:", (r'5^{x}\ln y', 5**x*log(y)), (r'\frac{x}{y}-y+1', x/y-y+1)),
  [O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{1}{3}', R(1, 3)), O(r'\frac{1}{4}', R(1, 4)), O(r'\frac{1}{5}', R(1, 5))],
  r"عندما $y=1$: $5^x\ln1=x-1+1 \Rightarrow x=0$" "\n"
  r"$5^x\ln5\ln y+\dfrac{5^x}{y}\dfrac{dy}{dx}=\dfrac{y-x\frac{dy}{dx}}{y^2}-\dfrac{dy}{dx}$ ، وعند $(0,1)$: $\dfrac{dy}{dx}=1-\dfrac{dy}{dx} \Rightarrow \dfrac{dy}{dx}=\dfrac12$",
  truth=imp(5**x*log(y)-x/y+y-1, (0, 1)), tag='الاشتقاق الضمني عند نقطة'),
# 2026 #17: tangent to a root relation at a lattice point, y-intercept; options = integers from typical slips
Q('m6q21', U3[4], 'medium',
  F(r"إذا مثّل المستقيم $l$ مماسًّا لمنحنى العلاقة: $«0»=3$ عند النقطة $(8,\,1)$ ، فإنّ المقطع $y$ للمستقيم $l$ هو:", (r'\sqrt[3]{x}+\sqrt[3]{y}', x**R(1, 3)+y**R(1, 3))),
  [O('3', 3), O('12', 12), O('-1', -1), O('33', 33)],
  r"$\dfrac13x^{-\frac23}+\dfrac13y^{-\frac23}\dfrac{dy}{dx}=0 \Rightarrow \dfrac{dy}{dx}=-\left(\dfrac yx\right)^{\frac23}=-\left(\dfrac18\right)^{\frac23}=-\dfrac14$" "\n"
  r"$l$: $y-1=-\dfrac14(x-8)$ ، وعند $x=0$: $y=1+2=3$",
  truth=lambda: 1-8*imp(x**R(1, 3)+y**R(1, 3)-3, (8, 1)), tag='مماس منحنى علاقة ضمنية'),
# 2024s #12 (ripples): area rate given, rate of the circumference; options = factor 2 x pi slip
Q('m6q22', U3[5], 'medium',
  r"تنتشر بقعة زيت على سطح الماء على شكل دائرة، وتزداد مساحتها بمعدّل $24\ \text{cm}^2/\text{s}$ ، فإنّ معدّل تغيّر محيط البقعة عندما يكون طول نصف قطرها $4\ \text{cm}$ هو:",
  [O('6', 6, units='cm/s'), O('3', 3, units='cm/s'), O(r'\frac{6}{\pi}', 6/pi, units='cm/s'), O(r'\frac{3}{\pi}', 3/pi, units='cm/s')],
  r"$A=\pi r^2 \Rightarrow \dfrac{dA}{dt}=2\pi r\dfrac{dr}{dt} \Rightarrow 24=8\pi\dfrac{dr}{dt} \Rightarrow \dfrac{dr}{dt}=\dfrac{3}{\pi}$" "\n"
  r"$C=2\pi r \Rightarrow \dfrac{dC}{dt}=2\pi\cdot\dfrac{3}{\pi}=6\ \text{cm/s}$",
  truth=2*pi*(24/diff(pi*s**2, s).subs(s, 4)), tag='معدلات مرتبطة: دائرة'),
# ---------------- unit 4
# 2026 #19: z = a + bi with a sign condition and |z| given -> trigonometric form; options = quadrant x reference angle
Q('m6q23', U4[1], 'medium',
  r"إذا كان: $z=a+2i$ ، حيث $a<0$ ، وكان: $|z|=4$ ، فإنّ الصورة المثلثية للعدد المركّب $z$ هي:",
  [O(trig('4', r'\frac{5\pi}{6}'), pol(4, 5*P/6)), O(trig('4', r'\frac{\pi}{6}'), pol(4, P/6)),
   O(trig('4', r'\frac{2\pi}{3}'), pol(4, 2*P/3)), O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3))],
  r"$a^2+4=16 \Rightarrow a=-2\sqrt3$ (لأنّ $a<0$) ، فـ $z=-2\sqrt3+2i$ في الربع الثاني" "\n"
  r"زاوية الإسناد: $\tan\theta=\dfrac{2}{2\sqrt3}=\dfrac{1}{\sqrt3} \Rightarrow \theta=\frac{\pi}{6}$ ، و $\text{Arg}(z)=\pi-\frac{\pi}{6}=\frac{5\pi}{6}$",
  truth=lambda: [r_ for r_ in solve(X**2+4-16, X) if r_ < 0][0]+2*I, tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2026 #20-21: one shared stem, two operations; options = real part x imaginary part slips
Q('m6q24', U4[2], 'easy',
  r"ناتج $2z-iw$ هو:",
  [O('10-5i', 10-5*I), O('2-5i', 2-5*I), O('10-3i', 10-3*I), O('2-3i', 2-3*I)],
  r"$2z=6-4i$ ، $iw=i(1+4i)=i+4i^2=-4+i$" "\n" r"$2z-iw=6-4i+4-i=10-5i$",
  truth=expand(2*(3-2*I)-I*(1+4*I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=3-2i$ ، $w=1+4i$", 24, 25)),
# 2026 #21: second item of the shared stem (product zw); options = real part x imaginary part slips
Q('m6q25', U4[2], 'easy',
  r"ناتج $zw$ هو:",
  [O('11+10i', 11+10*I), O('-5+10i', -5+10*I), O('11+14i', 11+14*I), O('-5+14i', -5+14*I)],
  r"$zw=(3-2i)(1+4i)=3+12i-2i-8i^2=3+10i+8=11+10i$",
  truth=expand((3-2*I)*(1+4*I)), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2026r #19 / 2025 #19: equation in z and its conjugate; options = sign of each part
Q('m6q26', U4[1], 'easy',
  r"إذا كان $z$ عددًا مركّبًا، وكان: $z+2\bar{z}=9-2i$ ، فإنّ $z$ هو:",
  [O('3+2i', 3+2*I), O('3-2i', 3-2*I), O('-3+2i', -3+2*I), O('-3-2i', -3-2*I)],
  r"نفرض $z=a+bi$: $a+bi+2(a-bi)=3a-bi=9-2i$" "\n" r"$3a=9 \Rightarrow a=3$ ، $-b=-2 \Rightarrow b=2$ ، إذن $z=3+2i$",
  truth=lambda: (lambda s_: s_[X]+s_[Y]*I)(solve([re(expand(X+Y*I+2*(X-Y*I)-9+2*I)), im(expand(X+Y*I+2*(X-Y*I)-9+2*I))], [X, Y])),
  tag='معادلة فيها العدد ومرافقه'),
# 2026 #22: two values of a constant making a quotient real; options = +-k list
Q('m6q27', U4[2], 'medium',
  r"إذا كان: $z=\dfrac{a+8i}{2+ai}$ ، فإنّ القيمتين المُمكنتين للثابت $a$ اللتين تجعلان $z$ عددًا حقيقيًّا هما:",
  [O(r'\pm 4', S_(4, -4), 'set'), O(r'\pm 2', S_(2, -2), 'set'), O(r'\pm 8', S_(8, -8), 'set'), O(r'\pm 1', S_(1, -1), 'set')],
  r"نضرب في مرافق المقام: $(a+8i)(2-ai)=2a-a^2i+16i+8a=10a+(16-a^2)i$" "\n" r"حقيقي: $16-a^2=0 \Rightarrow a=\pm4$",
  truth=lambda: FiniteSet(*solve(im(expand((X+8*I)*(2-X*I))), X)), tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
# 2026 #23: quadratic with a given complex root; options = sign of the sum x sum/product swapped
Q('m6q28', U4[2], 'easy',
  r"المعادلة التربيعية التي أحد جذريها العدد المركّب $(2-3i)$ هي:",
  [O(r'x^{2}-4x+13=0', x**2-4*x+13, 'rel'), O(r'x^{2}+4x+13=0', x**2+4*x+13, 'rel'),
   O(r'x^{2}-13x+4=0', x**2-13*x+4, 'rel'), O(r'x^{2}+13x+4=0', x**2+13*x+4, 'rel')],
  r"الجذر الآخر هو المرافق $2+3i$ ، المجموع $4$ والضرب $(2-3i)(2+3i)=4+9=13$" "\n" r"$x^2-Sx+P=0 \Rightarrow x^2-4x+13=0$",
  truth=expand((x-(2-3*I))*(x-(2+3*I))), tag='معادلة تربيعية بمعلومية جذر مركب'),
# 2026 #24: smaller angle between two numbers in different quadrants (difference > pi)
Q('m6q29', U4[1], 'medium',
  r"إذا كان: $z_1=1+i\sqrt{3}$ ، $z_2=-\sqrt{3}-i$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{5\pi}{6}', 5*P/6), O(r'\frac{7\pi}{6}', 7*P/6), O(r'\frac{\pi}{2}', P/2), O(r'\frac{\pi}{6}', P/6)],
  r"$\text{Arg}(z_1)=\frac{\pi}{3}$ ، $\text{Arg}(z_2)=-\pi+\frac{\pi}{6}=-\frac{5\pi}{6}$" "\n"
  r"الفرق $\frac{\pi}{3}+\frac{5\pi}{6}=\frac{7\pi}{6}>\pi$ ، فالزاوية الصغرى $2\pi-\frac{7\pi}{6}=\frac{5\pi}{6}$",
  truth=smaller_angle(1+sqrt(3)*I, -sqrt(3)-I), tag='الزاوية بين عددين مركبين'),
# 2026 #25: disc (solid) cut by a wedge whose vertex is not the centre, one ray dashed; options = vertex sign x strictness
IndexQ('m6q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثِّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z+i|\le3$ ، $0\le\text{Arg}(z-1+i)<\frac{3\pi}{4}$', R6),
   T(r'$|z+i|\le3$ ، $0<\text{Arg}(z-1+i)\le\frac{3\pi}{4}$', both(disk(-1j, 3), sector(1 - 1j, 0, 3*math.pi/4, lo_open=True))),
   T(r'$|z+i|\le3$ ، $0\le\text{Arg}(z+1-i)<\frac{3\pi}{4}$', both(disk(-1j, 3), sector(-1 + 1j, 0, 3*math.pi/4, hi_open=True))),
   T(r'$|z+i|\le3$ ، $0<\text{Arg}(z+1-i)\le\frac{3\pi}{4}$', both(disk(-1j, 3), sector(-1 + 1j, 0, 3*math.pi/4, lo_open=True)))],
  r"الدائرة متصلة، مركزها $(0,-1)$ ونصف قطرها $3$: $|z+i|\le3$" "\n"
  r"الشعاعان يبدآن من $(1,-1)$ أي العدد $1-i$: $\text{Arg}(z-1+i)$ ؛ الأفقي متصل ($0\le$) والمائل بزاوية $\frac{3\pi}{4}$ متقطّع ($<\frac{3\pi}{4}$)",
  truth=region_truth(R6, PR6, 4), figure=figure('m6q30', fig_region2(R6, PR6, 4), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 7
F7, G7 = [(0, 1), (3, 4), (6, 1)], [(0, 5), (2, 1), (6, 3)]
C7 = -2 + 1j
R7 = both(outside(C7, 1), disk(C7, 3, strict=True))
PR7 = [('arc', C7, 3, True, (0.0, 2*math.pi)), ('arc', C7, 1, False, (0.0, 2*math.pi))]
N_ = Symbol('N')


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


def fig_drone():
    """drone rising vertically, watched from a point 40 m away (m7q22)."""
    def draw(fig, ax):
        _sketch(fig, ax)
        ax.plot([-0.5, 9.5], [0, 0], color='#333333', lw=1.4)
        ax.plot([0, 8], [0, 6], color='#555555', lw=1.2, ls='--')
        ax.plot([8, 8], [0, 5.75], color='#1f5fbf', lw=1.2)
        ax.plot([7.6, 7.6, 8], [0, 0.4, 0.4], color='#333333', lw=1)
        ax.plot([7.5, 8.5], [6.15, 6.15], color='#333333', lw=2); ax.plot(8, 6, 's', color='#d04a1a', ms=8)
        ax.annotate('', (8.6, 7.4), (8.6, 6.2), arrowprops=dict(arrowstyle='->', color='#333333', lw=1))
        ax.add_patch(__import__('matplotlib.patches', fromlist=['Arc']).Arc((0, 0), 2.6, 2.6, theta1=0, theta2=36.87, color='#d04a1a', lw=1.2))
        ax.text(1.45, 0.3, r'$\theta$', fontsize=12, color='#d04a1a')
        ax.text(3.6, -0.75, r'$40\ \mathrm{m}$', fontsize=10); ax.text(8.25, 2.7, r'$h$', fontsize=12, color='#1f5fbf')
        ax.plot(0, 0, 'o', color='#333333', ms=5); ax.text(-0.5, -0.75, r'$A$', fontsize=11)
        ax.set_xlim(-0.8, 9.8); ax.set_ylim(-1.1, 7.8)
    return draw


P7 = [
# ---------------- unit 1
# 2026 #1 with a fractional root (zero of 2x - 1), equation not set to zero; options = signs of the other two roots
Q('m7q1', U1[1], 'medium',
  F(r"إذا كان $x=\frac{1}{2}$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ لها حلَّين آخرين هما:", (r'2x^{3}+6', 2*x**3+6), (r'3x^{2}+11x', 3*x**2+11*x)),
  [O(st('3', '-2'), S_(3, -2), 'set'), O(st('-3', '2'), S_(-3, 2), 'set'), O(st('-3', '-2'), S_(-3, -2), 'set'), O(st('3', '2'), S_(3, 2), 'set')],
  r"$2x^3-3x^2-11x+6=0$ ، وبالقسمة التركيبية على $\left(x-\frac12\right)$: $2,\ -3,\ -11,\ 6 \to 2,\ -2,\ -12,\ 0$" "\n"
  r"$2x^2-2x-12=2(x-3)(x+2)=0 \Rightarrow x=3,\ x=-2$",
  truth=lambda: other_roots(2*x**3-3*x**2-11*x+6, R(1, 2)), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# 2026 #2 (irreducible quadratic factor version); options = A halved or not x sign of the linear numerator
Q('m7q2', U1[2], 'medium',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{3x^{2}+1}{(x-1)(x^{2}+1)}', (3*x**2+1)/((x-1)*(x**2+1)))),
  [O(r'\frac{2}{x-1}+\frac{x+1}{x^{2}+1}', 2/(x-1)+(x+1)/(x**2+1)), O(r'\frac{4}{x-1}+\frac{x+1}{x^{2}+1}', 4/(x-1)+(x+1)/(x**2+1)),
   O(r'\frac{2}{x-1}+\frac{x-1}{x^{2}+1}', 2/(x-1)+(x-1)/(x**2+1)), O(r'\frac{4}{x-1}+\frac{x-1}{x^{2}+1}', 4/(x-1)+(x-1)/(x**2+1))],
  r"$3x^2+1=A(x^2+1)+(Bx+C)(x-1)$" "\n" r"عند $x=1$: $4=2A \Rightarrow A=2$ ، معامل $x^2$: $3=A+B \Rightarrow B=1$ ، الحدّ الثابت: $1=A-C \Rightarrow C=1$",
  truth=(3*x**2+1)/((x-1)*(x**2+1)), tag='تجزئة: عامل تربيعي غير قابل للتحليل'),
# 2026 #3 extended to two constants (factor + remainder); options = sign of each constant
Q('m7q3', U1[1], 'medium',
  F(r"إذا كان $(x-2)$ أحد عوامل الاقتران: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x+1)$ يساوي $6$ ، فإنّ قيمتي الثابتين $a$ و $b$ هما:", (r'x^{3}+ax^{2}-4x+b', x**3+a*x**2-4*x+b)),
  [O(r'a=-1,\ b=4', Tuple(-1, 4), 'pairs'), O(r'a=1,\ b=-4', Tuple(1, -4), 'pairs'), O(r'a=-1,\ b=-4', Tuple(-1, -4), 'pairs'), O(r'a=1,\ b=4', Tuple(1, 4), 'pairs')],
  r"$f(2)=8+4a-8+b=0 \Rightarrow 4a+b=0$" "\n" r"$f(-1)=-1+a+4+b=6 \Rightarrow a+b=3$ ، بالطرح: $3a=-3 \Rightarrow a=-1$ ، $b=4$",
  truth=lambda: (lambda s_: Tuple(s_[a], s_[b]))(solve([rem(x**3+a*x**2-4*x+b, 2), rem(x**3+a*x**2-4*x+b, -1)-6], [a, b])),
  tag='نظرية العوامل وإيجاد ثابتين'),
# 2026 #3 (remainder theorem) with high powers of a negative number; options = the parity slips
Q('m7q4', U1[1], 'easy',
  F(r"باقي قسمة الاقتران: $f(x)=«0»$ على $(x+1)$ هو:", (r'x^{20}-3x^{9}+2', x**20-3*x**9+2)),
  [O('6', 6), O('4', 4), O('0', 0), O('-2', -2)],
  r"الباقي $f(-1)=(-1)^{20}-3(-1)^9+2=1+3+2=6$",
  truth=rem(x**20-3*x**9+2, -1), tag='نظرية الباقي: قوى عالية'),
# ---------------- unit 2
# 2026 #4 with cos(theta/2) from tan theta; options = sign x sin/cos of the half angle
Q('m7q5', U2[2], 'medium',
  r"إذا كان: $\tan\theta=\frac{3}{4}$ ، $\pi<\theta<\frac{3\pi}{2}$ ، فإنّ قيمة $\cos\frac{\theta}{2}$ تساوي:",
  [O(r'-\frac{1}{\sqrt{10}}', -1/sqrt(10)), O(r'\frac{1}{\sqrt{10}}', 1/sqrt(10)), O(r'-\frac{3}{\sqrt{10}}', -3/sqrt(10)), O(r'\frac{3}{\sqrt{10}}', 3/sqrt(10))],
  r"في الربع الثالث $\cos\theta=-\frac45$ ، و $\frac{\pi}{2}<\frac{\theta}{2}<\frac{3\pi}{4}$ فجيب التمام سالب" "\n"
  r"$\cos\frac{\theta}{2}=-\sqrt{\dfrac{1+\cos\theta}{2}}=-\sqrt{\dfrac{1/5}{2}}=-\dfrac{1}{\sqrt{10}}$",
  truth=cos((pi+atan(R(3, 4)))/2), tag='نصف الزاوية مع تحديد الربع'),
# 2026 #5 with a difference identity; options = coefficient x sin/cos
Q('m7q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x-\frac{\pi}{4})-\frac{\sqrt{2}}{2}\sin x', cos(x-pi/4)-sqrt(2)/2*sin(x))),
  [O(r'\frac{\sqrt{2}}{2}\cos x', sqrt(2)/2*cos(x)), O(r'\frac{\sqrt{2}}{2}\sin x', sqrt(2)/2*sin(x)), O(r'\sqrt{2}\cos x', sqrt(2)*cos(x)), O(r'\sqrt{2}\sin x', sqrt(2)*sin(x))],
  r"$\cos\left(x-\frac{\pi}{4}\right)=\cos x\cdot\frac{\sqrt2}{2}+\sin x\cdot\frac{\sqrt2}{2}$ ، وبطرح $\frac{\sqrt2}{2}\sin x$ يبقى $\frac{\sqrt2}{2}\cos x$",
  truth=cos(x-pi/4)-sqrt(2)/2*sin(x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #6 (equivalent expression)
Q('m7q7', U2[1], 'easy',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\sec x-\sin x\tan x', sec(x)-sin(x)*tan(x))),
  [O(r'\cos x', cos(x)), O(r'\sin x', sin(x)), O(r'\sec x', sec(x)), O(r'\csc x', csc(x))],
  r"$\dfrac{1}{\cos x}-\sin x\cdot\dfrac{\sin x}{\cos x}=\dfrac{1-\sin^2x}{\cos x}=\dfrac{\cos^2x}{\cos x}=\cos x$",
  truth=sec(x)-sin(x)*tan(x), tag='المتطابقات الأساسية'),
# 2026 #5 family: exact value from a difference of special angles; options = order of the surds x sign
Q('m7q8', U2[1], 'medium',
  r"قيمة $\sin\frac{\pi}{12}$ هي:",
  [O(r'\frac{\sqrt{6}-\sqrt{2}}{4}', (sqrt(6)-sqrt(2))/4), O(r'\frac{\sqrt{2}-\sqrt{6}}{4}', (sqrt(2)-sqrt(6))/4),
   O(r'\frac{\sqrt{6}+\sqrt{2}}{4}', (sqrt(6)+sqrt(2))/4), O(r'-\frac{\sqrt{6}+\sqrt{2}}{4}', -(sqrt(6)+sqrt(2))/4)],
  r"$\frac{\pi}{12}=\frac{\pi}{3}-\frac{\pi}{4}$" "\n" r"$\sin\frac{\pi}{3}\cos\frac{\pi}{4}-\cos\frac{\pi}{3}\sin\frac{\pi}{4}=\frac{\sqrt3}{2}\cdot\frac{\sqrt2}{2}-\frac12\cdot\frac{\sqrt2}{2}=\frac{\sqrt6-\sqrt2}{4}$",
  truth=sin(pi/12), tag='قيم دقيقة بمتطابقات المجموع والفرق'),
# 2026 #7 after a Pythagorean substitution (quadratic in cos x, three solutions); options = include 0 x sign of cos
Q('m7q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\sin^{2}x+3\cos x-3', 2*sin(x)**2+3*cos(x)-3)),
  [O(st('0', r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(0, P/3, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'),
   O(st('0', r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(0, 2*P/3, 4*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set')],
  r"$2(1-\cos^2x)+3\cos x-3=0 \Rightarrow 2\cos^2x-3\cos x+1=0 \Rightarrow (2\cos x-1)(\cos x-1)=0$" "\n"
  r"$\cos x=1 \Rightarrow x=0$ ، $\cos x=\frac12 \Rightarrow x=\frac{\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*sin(x)**2+3*cos(x)-3, 0, 2*pi), tag='معادلة تربيعية بعد استعمال متطابقة فيثاغورس'),
# 2026 #8: reciprocal ratio -> sin 2x; options = halved or not x second period or not
Q('m7q10', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\cos x-\csc x', 2*cos(x)-csc(x))),
  [O(st(r'\frac{\pi}{4}', r'\frac{5\pi}{4}'), S_(P/4, 5*P/4), 'set'), O(st(r'\frac{\pi}{2}', r'\frac{5\pi}{2}'), S_(P/2, 5*P/2), 'set'),
   O(st(r'\frac{\pi}{4}'), S_(P/4), 'set'), O(st(r'\frac{\pi}{2}'), S_(P/2), 'set')],
  r"نضرب في $\sin x\ne0$: $2\sin x\cos x=1 \Rightarrow \sin2x=1$" "\n"
  r"$0\le2x<4\pi$: $2x=\frac{\pi}{2},\ \frac{5\pi}{2} \Rightarrow x=\frac{\pi}{4},\ \frac{5\pi}{4}$",
  truth=lambda: sols(2*cos(x)-csc(x), 0, 2*pi), tag='معادلة فيها مقلوب نسبة وزاوية مضاعفة'),
# ---------------- unit 3
# 2025 #2 / 2026r #5: value of the derivative of a trig combination; options = sec^2 vs sec x sign of the cos term
Q('m7q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{3}\right)$ هي:", (r'2\tan x-4\cos x', 2*tan(x)-4*cos(x))),
  [O(r'8+2\sqrt{3}', 8+2*sqrt(3)), O(r'8-2\sqrt{3}', 8-2*sqrt(3)), O(r'4+2\sqrt{3}', 4+2*sqrt(3)), O(r'4-2\sqrt{3}', 4-2*sqrt(3))],
  r"$f'(x)=2\sec^2x+4\sin x$" "\n" r"$f'\left(\frac{\pi}{3}\right)=2(2)^2+4\cdot\frac{\sqrt3}{2}=8+2\sqrt3$",
  truth=Dx(2*tan(x)-4*cos(x)).subs(x, pi/3), tag='مشتقات الاقترانات المثلثية'),
# 2024 #6: x-coordinate where the tangent is parallel to a given line (exponential minus linear)
Q('m7q12', U3[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ الإحداثي $x$ للنقطة التي يكون عندها المماس موازيًا للمستقيم الذي معادلته: $3x-y+1=0$ هو:", (r'e^{2x}-5x', exp(2*x)-5*x)),
  [O(r'\ln 2', log(2)), O(r'\frac{3}{2}\ln 2', R(3, 2)*log(2)), O('0', 0), O(r'\ln 4', log(4))],
  r"ميل المستقيم $3$ ، و $f'(x)=2e^{2x}-5$" "\n" r"$2e^{2x}-5=3 \Rightarrow e^{2x}=4 \Rightarrow 2x=\ln4 \Rightarrow x=\ln2$",
  truth=lambda: [r_ for r_ in solve(Dx(exp(2*x)-5*x)-3, x) if r_.is_real][0], tag='مماس يوازي مستقيمًا معلومًا'),
# 2025s #8: exponential growth model, rate given -> the initial constant N; options = slips with the 0.5
Q('m7q13', U3[1], 'medium',
  r"إذا كان الاقتران: $A(t)=Ne^{0.5t}$ يُمثّل عدد الخلايا البكتيرية بعد $t$ ساعة في مجتمع بكتيري، وكان معدّل نموّ المجتمع بعد $4$ ساعات هو $(300e^{2})$ خلية لكلّ ساعة، فإنّ قيمة الثابت $N$ هي:",
  [O('600', 600), O('300', 300), O('150', 150), O('6000', 6000)],
  r"$A'(t)=0.5Ne^{0.5t}$ ، و $A'(4)=0.5Ne^{2}=300e^2 \Rightarrow N=600$",
  truth=lambda: solve(diff(N_*exp(t/2), t).subs(t, 4)-300*E**2, N_)[0], tag='معدل التغير في سياق حياتي'),
# 2024s #7: third derivative of a polynomial plus a reciprocal; options = sign x keeping a constant
Q('m7q14', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، $x\ne0$ ، فإنّ $f'''(x)$ هي:", (r'3x^{2}-\frac{2}{x}', 3*x**2-2/x)),
  [O(r'\frac{12}{x^{4}}', 12/x**4), O(r'-\frac{12}{x^{4}}', -12/x**4), O(r'6+\frac{12}{x^{4}}', 6+12/x**4), O(r'6-\frac{12}{x^{4}}', 6-12/x**4)],
  r"$f'(x)=6x+2x^{-2}$ ، $f''(x)=6-4x^{-3}$ ، $f'''(x)=12x^{-4}=\dfrac{12}{x^4}$",
  truth=diff(3*x**2-2/x, x, 3), tag='المشتقات العليا'),
# 2026r #3 / 2025 #3: two graphs, h a quotient of f and g; options = numerator order x slope sign
Q('m7q15', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=\dfrac{f(x)}{g(x)}$ ، فإنّ $h'(1)$ هي:",
  [O(r'\frac{7}{9}', R(7, 9)), O(r'-\frac{7}{9}', -R(7, 9)), O(r'-\frac{1}{9}', -R(1, 9)), O(r'\frac{1}{9}', R(1, 9))],
  r"من الشكل: $f(1)=2$ ، $f'(1)=1$ ، $g(1)=3$ ، $g'(1)=-2$" "\n" r"$h'(1)=\dfrac{f'(1)g(1)-f(1)g'(1)}{(g(1))^2}=\dfrac{3+4}{9}=\dfrac79$",
  truth=lambda: (lambda fv, fs, gv, gs: (fs(1)*gv(1)-fv(1)*gs(1))/gv(1)**2)(*pw(F7), *pw(G7)),
  figure=figure('m7q15', draw_two(F7, G7, 6, 5, (4.5, 3.0), (5.5, 3.2))), tag='المشتقة من التمثيل البياني'),
# 2025 #8: product of an exponential composite and a root composite at 0; options = chain-factor slips
Q('m7q16', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(0)$ هو:", (r'3e^{x^{2}}\sqrt{2x+1}', 3*exp(x**2)*sqrt(2*x+1))),
  [O('3', 3), O(r'\frac{3}{2}', R(3, 2)), O('0', 0), O('6', 6)],
  r"$f'(x)=3\left[2xe^{x^2}\sqrt{2x+1}+e^{x^2}\cdot\dfrac{2}{2\sqrt{2x+1}}\right]$" "\n" r"$f'(0)=3\left[0+1\cdot1\right]=3$",
  truth=Dx(3*exp(x**2)*sqrt(2*x+1)).subs(x, 0), tag='مشتقة الضرب'),
# 2024s #11: log base a of a quadratic at a point; options = ln a missing / inverted x divided by u or not
Q('m7q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(3)$ هي:", (r'\log_{3}(x^{2}-5)', log(x**2-5, 3))),
  [O(r'\frac{3}{2\ln 3}', 3/(2*log(3))), O(r'\frac{6}{\ln 3}', 6/log(3)), O(r'\frac{3}{2}', R(3, 2)), O(r'\frac{3\ln 3}{2}', 3*log(3)/2)],
  r"$f'(x)=\dfrac{2x}{(x^2-5)\ln3}$ ، $f'(3)=\dfrac{6}{4\ln3}=\dfrac{3}{2\ln3}$",
  truth=Dx(log(x**2-5, 3)).subs(x, 3), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2025 #10: k^(trig x), f'(a) given as a logarithm -> k; options = k, its reciprocal, its square, negative
IndexQ('m7q18', U3[3], 'hard',
  r"إذا كان: $f(x)=k^{\tan x}$ ، حيث $k>0$ ، وكان: $f'\left(\frac{\pi}{4}\right)=\ln 16$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('2', 2), O('4', 4), O(r'\frac{1}{2}', R(1, 2)), O('-2', -2)],
  r"$f'(x)=k^{\tan x}\ln k\cdot\sec^2x$ ، $f'\left(\frac{\pi}{4}\right)=k\ln k\cdot2=2k\ln k$" "\n" r"$2k\ln k=\ln16=4\ln2 \Rightarrow k\ln k=2\ln2 \Rightarrow k=2$",
  truth=lambda vals: only(vals, lambda v_: sympify(v_).is_positive and simplify(Dx(v_**tan(x)).subs(x, pi/4)-log(16)) == 0),
  tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2026 #15 / 2023 #8: parametric (polynomial and log); options = reciprocal x missing chain factor
Q('m7q19', U3[3], 'easy',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=1$ هو:", (r't^{3}+1', t**3+1), (r'\ln(t^{2}+3)', log(t**2+3))),
  [O(r'\frac{1}{6}', R(1, 6)), O('6', 6), O(r'\frac{1}{12}', R(1, 12)), O('12', 12)],
  r"$\dfrac{dy}{dt}=\dfrac{2t}{t^2+3}=\dfrac12$ ، $\dfrac{dx}{dt}=3t^2=3$ عندما $t=1$" "\n" r"$\dfrac{dy}{dx}=\dfrac{1/2}{3}=\dfrac16$",
  truth=(diff(log(t**2+3), t)/diff(t**3+1, t)).subs(t, 1), tag='مشتقة المعادلات الوسيطية'),
# 2024 #9: y^2 and ln(xy) at a point; options = terms of d/dx ln(xy) dropped
Q('m7q20', U3[4], 'medium',
  F(r"إذا كانت: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(1,\,1)$ هي:", (r'y^{2}+\ln(xy)', y**2+log(x*y)), (r'2x-1', 2*x-1)),
  [O(r'\frac{1}{3}', R(1, 3)), O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{2}{3}', R(2, 3)), O('1', 1)],
  r"$\ln(xy)=\ln x+\ln y$ ، فالاشتقاق: $2y\dfrac{dy}{dx}+\dfrac1x+\dfrac1y\dfrac{dy}{dx}=2$" "\n" r"عند $(1,1)$: $2y'+1+y'=2 \Rightarrow y'=\dfrac13$",
  truth=imp(y**2+log(x*y)-2*x+1, (1, 1)), tag='الاشتقاق الضمني عند نقطة'),
# 2024 #10 / 2023 #10: variable base and exponent, logarithmic differentiation; options = factor y x factor 2
Q('m7q21', U3[4], 'hard',
  F(r"إذا كانت: $y=«0»$ ، $x>0$ ، فإنّ ميل المماس لمنحنى العلاقة عند أيّ نقطة تقع عليها هو:", (r'x^{\ln x}', x**log(x))),
  [O(r'\frac{2y\ln x}{x}', 2*x**log(x)*log(x)/x, sym={'y': x**log(x)}), O(r'\frac{2\ln x}{x}', 2*log(x)/x),
   O(r'\frac{y\ln x}{x}', x**log(x)*log(x)/x, sym={'y': x**log(x)}), O(r'\frac{\ln x}{x}', log(x)/x)],
  r"$\ln y=\ln x\cdot\ln x=(\ln x)^2$" "\n" r"$\dfrac1y\dfrac{dy}{dx}=\dfrac{2\ln x}{x} \Rightarrow \dfrac{dy}{dx}=\dfrac{2y\ln x}{x}$",
  truth=Dx(x**log(x)), tag='الاشتقاق اللوغاريتمي'),
# 2024 #11 / 2025 #12: angle of elevation of a rising object, with a figure; options = sign x missing cos^2
Q('m7q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي طائرة مُسيّرة ترتفع رأسيًّا بسرعة $15\ \text{m/min}$ ، ويرصدها شخص عند النقطة $A$ التي تبعد $40\ \text{m}$ عن نقطة إقلاعها. معدّل تغيّر زاوية الارتفاع $\theta$ عندما يكون ارتفاع الطائرة $30\ \text{m}$ هو:",
  [O(r'\frac{6}{25}', R(6, 25), units='rad/min'), O(r'\frac{3}{8}', R(3, 8), units='rad/min'), O(r'-\frac{6}{25}', -R(6, 25), units='rad/min'), O(r'-\frac{3}{8}', -R(3, 8), units='rad/min')],
  r"$\tan\theta=\dfrac{h}{40} \Rightarrow \sec^2\theta\dfrac{d\theta}{dt}=\dfrac{1}{40}\dfrac{dh}{dt}$" "\n"
  r"عندما $h=30$: الوتر $50$ ، $\cos\theta=\frac45$ ، $\dfrac{d\theta}{dt}=\dfrac{15}{40}\cdot\dfrac{16}{25}=\dfrac{6}{25}\ \text{rad/min}$",
  truth=(diff(atan(s/40), s)*15).subs(s, 30), figure=figure('m7q22', fig_drone(), 3.4, 2.8), tag='معدلات مرتبطة: معدل تغير زاوية'),
# ---------------- unit 4
# 2025 #18: trigonometric form of a number shown as a point; options = quadrant x reference angle
Q('m7q23', U4[1], 'easy',
  r"الصورة المثلثية للعدد المركّب $w$ المُمثَّل في المستوى المركّب الآتي هي:",
  [O(trig('4', r'\frac{2\pi}{3}'), pol(4, 2*P/3)), O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3)),
   O(trig('4', r'\frac{5\pi}{6}'), pol(4, 5*P/6)), O(trig('4', r'\frac{\pi}{6}'), pol(4, P/6))],
  r"$w=-2+2\sqrt3\,i$ ، $|w|=\sqrt{4+12}=4$ ، وهو في الربع الثاني" "\n" r"زاوية الإسناد $\tan\theta=\dfrac{2\sqrt3}{2}=\sqrt3 \Rightarrow \theta=\frac{\pi}{3}$ ، و $\text{Arg}(w)=\pi-\frac{\pi}{3}=\frac{2\pi}{3}$",
  truth=-2+2*sqrt(3)*I, figure=figure('m7q23', fig_point(-2, 2*math.sqrt(3), r'$-2$', r'$2\sqrt{3}$', 'w', 5), 3.0, 3.0),
  tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2025 #21-22 / 2025s #21-22: shared stem, Arg of a difference then a quotient
Q('m7q24', U4[1], 'easy',
  r"قيمة $\text{Arg}(z-w)$ هي:",
  [O(r'-\frac{\pi}{4}', -P/4), O(r'\frac{\pi}{4}', P/4), O(r'-\frac{3\pi}{4}', -3*P/4), O(r'\frac{3\pi}{4}', 3*P/4)],
  r"$z-w=(4-1)+(-1-2)i=3-3i$ في الربع الرابع، وزاوية الإسناد $\frac{\pi}{4}$ ، إذن $\text{Arg}(z-w)=-\frac{\pi}{4}$",
  truth=arg(3-3*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=4-i$ ، $w=1+2i$", 24, 25)),
# 2026r #21: second item of the shared stem (quotient z/w); options = i^2 slip x conjugate slip
Q('m7q25', U4[2], 'medium',
  r"ناتج $\dfrac{z}{w}$ هو:",
  [O(r'\frac{2}{5}-\frac{9}{5}i', R(2, 5)-R(9, 5)*I), O(r'\frac{6}{5}-\frac{9}{5}i', R(6, 5)-R(9, 5)*I),
   O(r'\frac{2}{5}+\frac{9}{5}i', R(2, 5)+R(9, 5)*I), O(r'\frac{6}{5}+\frac{7}{5}i', R(6, 5)+R(7, 5)*I)],
  r"$\dfrac{4-i}{1+2i}\cdot\dfrac{1-2i}{1-2i}=\dfrac{4-8i-i+2i^2}{1+4}=\dfrac{2-9i}{5}$",
  truth=(4-I)/(1+2*I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2025 #24 / 2025s #25: modulus of a product given -> two values of a constant
Q('m7q26', U4[1], 'medium',
  r"إذا كان: $z_1=8+pi$ ، $z_2=3+4i$ ، وكان: $|z_1z_2|=50$ ، فإنّ القيمتين المُمكنتين للثابت $p$ هما:",
  [O(r'\pm 6', S_(6, -6), 'set'), O(r'\pm 2', S_(2, -2), 'set'), O(r'\pm 8', S_(8, -8), 'set'), O(r'\pm 10', S_(10, -10), 'set')],
  r"$|z_1z_2|=|z_1||z_2|=5|z_1|=50 \Rightarrow |z_1|=10$" "\n" r"$64+p^2=100 \Rightarrow p^2=36 \Rightarrow p=\pm6$",
  truth=lambda: FiniteSet(*solve(5*sqrt(64+X**2)-50, X)), tag='إيجاد ثابت بمعلومية المقياس'),
# 2026r #24 / 2025s #24: a complex root of a quadratic with unknown real coefficients
Q('m7q27', U4[2], 'medium',
  r"إذا كان: $z=-2+ai$ ، $a>0$ أحد جذري المعادلة: $x^{2}+bx+13=0$ ، حيث $a$ و $b$ عددان حقيقيان، فإنّ قيمة $a+b$ هي:",
  [O('7', 7), O('-1', -1), O('13', 13), O('5', 5)],
  r"الجذر الآخر $-2-ai$ ، المجموع $-4=-b \Rightarrow b=4$" "\n" r"الضرب $4+a^2=13 \Rightarrow a=3$ ، إذن $a+b=7$",
  truth=lambda: (lambda s_: s_[X]+s_[Y])([d_ for d_ in solve([re(expand((-2+X*I)**2+Y*(-2+X*I)+13)), im(expand((-2+X*I)**2+Y*(-2+X*I)+13))], [X, Y], dict=True) if d_[X] > 0][0]),
  tag='معادلة تربيعية بمعلومية جذر مركب'),
# 2025 #20 / 2024s #23: Arg of an expression in z given -> constant; options = quadrant x sign of the shift
IndexQ('m7q28', U4[1], 'medium',
  r"إذا كان: $z=a-5i$ ، وكان: $\text{Arg}(z+3-2i)=-\frac{\pi}{4}$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('4', 4), O('-10', -10), O('10', 10), O('-4', -4)],
  r"$z+3-2i=(a+3)-7i$ ، والسعة $-\frac{\pi}{4}$ تعني الربع الرابع مع تساوي الجزأين في القيمة المطلقة" "\n" r"$a+3=7 \Rightarrow a=4$",
  truth=lambda vals: only(vals, lambda v_: simplify(arg(v_+3-7*I)+pi/4) == 0), tag='السعة الرئيسة'),
# 2023 #24: greatest Arg of points on a circle
Q('m7q29', U4[3], 'hard',
  r"القيمة العظمى لسعة الأعداد المركّبة $z$ التي تحقّق المعادلة: $|z-\sqrt{3}-i|=1$ هي:",
  [O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{6}', P/6), O('0', 0), O(r'\frac{\pi}{2}', P/2)],
  r"دائرة مركزها $(\sqrt3,1)$ ونصف قطرها $1$ ، وبُعد المركز عن الأصل $2$ وسعته $\frac{\pi}{6}$" "\n"
  r"المماس من الأصل يصنع مع الخط الواصل إلى المركز زاوية $\alpha$: $\sin\alpha=\frac12 \Rightarrow \alpha=\frac{\pi}{6}$ ، فالعظمى $\frac{\pi}{6}+\frac{\pi}{6}=\frac{\pi}{3}$",
  truth=atan2(1, sqrt(3))+asin(R(1, 2)), tag='القيمة العظمى للسعة على محل هندسي'),
# 2025 #25: annulus with one dashed circle; options = centre sign x which circle is strict
IndexQ('m7q30', U4[3], 'medium',
  r"متباينة المحل الهندسي (بدلالة $z$) التي تُمثِّل المنطقة المُظلَّلة في الشكل الآتي هي:",
  [T(r'$1\le|z+2-i|<3$', R7),
   T(r'$1<|z+2-i|\le3$', both(outside(C7, 1, strict=True), disk(C7, 3))),
   T(r'$1\le|z-2+i|<3$', both(outside(2 - 1j, 1), disk(2 - 1j, 3, strict=True))),
   T(r'$1<|z-2+i|\le3$', both(outside(2 - 1j, 1, strict=True), disk(2 - 1j, 3)))],
  r"المركز $(-2,1)$ أي $-2+i$ ، فنكتب $|z-(-2+i)|=|z+2-i|$" "\n" r"الدائرة الداخلية (نصف القطر $1$) متصلة: $1\le$ ، والخارجية (نصف القطر $3$) متقطّعة: $<3$",
  truth=region_truth(R7, PR7, 5), figure=figure('m7q30', fig_region2(R7, PR7, 5), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 8
F8 = [(0, 3), (2, 1), (5, 4)]                # graph of f for m8q16
A8, B8 = 3j, 4 + 1j                          # m8q29: the bisected segment
V8 = -1 + 2j                                 # m8q30: vertex of the wedge
R8 = sector(V8, -math.pi/2, math.pi/4, hi_open=True)
PR8 = [('seg', V8, V8 - 7j, False), ('seg', V8, V8 + 7*cmath.exp(1j*math.pi/4), True), ('open', V8)]


def bisector(p_, q_):
    return lambda z_: abs(abs(z_ - p_) - abs(z_ - q_)) < 1e-6


L8 = [('seg', complex(-1.5, -5), complex(3.5, 5), False)]   # y = 2x - 2


def fig_one(pts, xr, yr, label_pos, name='f(x)'):
    """graph of one piecewise-linear function on a grid."""
    def draw(fig, ax):
        axes_style(ax, (xr[0] - 0.5, xr[1] + 0.5), (yr[0] - 0.5, yr[1] + 0.8), grid=True)
        ax.set_xticks(range(xr[0], xr[1] + 1)); ax.set_yticks(range(yr[0], yr[1] + 1)); ax.tick_params(labelsize=8)
        ax.plot(*zip(*pts), color='#1f5fbf', lw=2)
        ax.text(*label_pos, f'${name}$', color='#1f5fbf', fontsize=12)
    return draw


def fig_cylinder():
    """upright cylindrical tank, diameter 4 m, height 6 m (m8q22)."""
    def draw(fig, ax):
        Ell = __import__('matplotlib.patches', fromlist=['Ellipse']).Ellipse
        _sketch(fig, ax)
        ax.plot([-2, -2], [0, 6], color='#333333', lw=1.6); ax.plot([2, 2], [0, 6], color='#333333', lw=1.6)
        ax.add_patch(Ell((0, 6), 4, 0.8, fill=False, color='#333333', lw=1.4))
        ax.fill_between([-2, 2], [0, 0], [3.5, 3.5], color='#9cc3ef', alpha=0.8)
        ax.add_patch(Ell((0, 3.5), 4, 0.8, color='#7fb0e6'))
        ax.add_patch(Ell((0, 0), 4, 0.8, color='#9cc3ef', ec='#333333', lw=1.4))
        ax.annotate('', (2.6, 0), (2.6, 6), arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
        ax.text(2.75, 2.9, r'$6\ \mathrm{m}$', fontsize=10)
        ax.annotate('', (-2, -0.9), (2, -0.9), arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
        ax.text(-0.45, -1.45, r'$4\ \mathrm{m}$', fontsize=10)
        ax.text(-0.25, 1.6, r'$h$', fontsize=12, color='#1f5fbf')
        ax.set_xlim(-2.6, 3.9); ax.set_ylim(-1.8, 6.8)
    return draw


def fig_bisector():
    """line l = perpendicular bisector of AB, A and B marked (2024 #25 / 2023 #25 style)."""
    def draw(fig, ax):
        complex_axes(ax, 5)
        ax.plot([-1.5, 3.5], [-5, 5], color=LINE, lw=1.8); ax.text(3.0, 4.6, r'$l$', fontsize=13, color=LINE)
        ax.plot([0, 4], [3, 1], color='#d04a1a', lw=1.1, ls=':')
        for (px, py), nm, off in [((0, 3), 'A', (0.2, 0.3)), ((4, 1), 'B', (0.15, 0.15))]:
            ax.plot(px, py, 'x', color='#d04a1a', ms=8, mew=1.6); ax.text(px + off[0], py + off[1], f'${nm}$', fontsize=11, color='#d04a1a')
        for mx, my in [(1, 2.5), (3, 1.5)]:            # equal-length ticks on the two halves
            ax.plot([mx - 0.1, mx + 0.1], [my - 0.2, my + 0.2], color='#d04a1a', lw=1.2)
    return draw


P8 = [
# ---------------- unit 1
# 2026 #1 phrased with a given factor; options = signs of the other two zeros
Q('m8q1', U1[1], 'easy',
  F(r"إذا كان $(x+3)$ أحد عوامل الاقتران: $f(x)=«0»$ ، فإنّ الصفرين الآخرين للاقتران $f(x)$ هما:", (r'x^{3}+2x^{2}-5x-6', x**3+2*x**2-5*x-6)),
  [O(st('2', '-1'), S_(2, -1), 'set'), O(st('-2', '1'), S_(-2, 1), 'set'), O(st('-2', '-1'), S_(-2, -1), 'set'), O(st('2', '1'), S_(2, 1), 'set')],
  r"القسمة التركيبية على $(x+3)$ (نعوّض $-3$): $1,\ 2,\ -5,\ -6 \to 1,\ -1,\ -2,\ 0$" "\n" r"$x^2-x-2=(x-2)(x+1) \Rightarrow x=2,\ x=-1$",
  truth=lambda: other_roots(x**3+2*x**2-5*x-6, -3), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# 2026 #2 (improper fraction): quotient kept or dropped x constants swapped
Q('m8q2', U1[2], 'medium',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{x^{2}+2x+3}{x^{2}-1}', (x**2+2*x+3)/(x**2-1))),
  [O(r'1+\frac{3}{x-1}-\frac{1}{x+1}', 1+3/(x-1)-1/(x+1)), O(r'\frac{3}{x-1}-\frac{1}{x+1}', 3/(x-1)-1/(x+1)),
   O(r'1-\frac{1}{x-1}+\frac{3}{x+1}', 1-1/(x-1)+3/(x+1)), O(r'-\frac{1}{x-1}+\frac{3}{x+1}', -1/(x-1)+3/(x+1))],
  r"الكسر غير فعلي: $\dfrac{x^2+2x+3}{x^2-1}=1+\dfrac{2x+4}{(x-1)(x+1)}$" "\n" r"$2x+4=A(x+1)+B(x-1)$: عند $x=1$: $A=3$ ، وعند $x=-1$: $B=-1$",
  truth=(x**2+2*x+3)/(x**2-1), tag='تجزئة: كسر غير فعلي'),
# 2026 #3: a relation between two remainders -> constant; options = sign x parity slip
Q('m8q3', U1[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x-1)$ يساوي مثلَي باقي قسمته على $(x+1)$ ، فإنّ قيمة الثابت $k$ هي:", (r'x^{3}+kx^{2}-4', x**3+k*x**2-4)),
  [O('7', 7), O('-7', -7), O('3', 3), O('-3', -3)],
  r"$f(1)=1+k-4=k-3$ ، $f(-1)=-1+k-4=k-5$" "\n" r"$k-3=2(k-5) \Rightarrow k-3=2k-10 \Rightarrow k=7$",
  truth=lambda: solve(rem(x**3+k*x**2-4, 1)-2*rem(x**3+k*x**2-4, -1), k)[0], tag='نظرية الباقي وإيجاد ثابت'),
# remainder theorem with a quadratic divisor from two given remainders (2026 #3 extension)
Q('m8q4', U1[1], 'hard',
  r"إذا كان باقي قسمة كثير الحدود $f(x)$ على $(x-1)$ يساوي $3$ ، وباقي قسمته على $(x+2)$ يساوي $-6$ ، فإنّ باقي قسمة $f(x)$ على $(x-1)(x+2)$ هو:",
  [O('3x', 3*x), O('-3x', -3*x), O('3x+6', 3*x+6), O('x+2', x+2)],
  r"الباقي من الدرجة الأولى على الأكثر: $r(x)=ax+b$ ، و $f(x)=(x-1)(x+2)q(x)+ax+b$" "\n"
  r"$f(1)=a+b=3$ ، $f(-2)=-2a+b=-6$ ، بالطرح: $3a=9 \Rightarrow a=3$ ، $b=0$ ، فالباقي $3x$",
  truth=lambda: (lambda s_: s_[a]*x+s_[b])(solve([a+b-3, -2*a+b+6], [a, b])), tag='باقي القسمة على مقدار تربيعي'),
# ---------------- unit 2
# 2026 #4 with sec theta given, asking sin(theta/2); options = sign x sin/cos half-angle formula
Q('m8q5', U2[2], 'medium',
  r"إذا كان: $\sec\theta=-3$ ، $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\sin\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{\sqrt{6}}{3}', sqrt(6)/3), O(r'-\frac{\sqrt{6}}{3}', -sqrt(6)/3), O(r'\frac{\sqrt{3}}{3}', sqrt(3)/3), O(r'-\frac{\sqrt{3}}{3}', -sqrt(3)/3)],
  r"$\cos\theta=-\frac13$ ، و $\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$ فالجيب موجب" "\n" r"$\sin\frac{\theta}{2}=\sqrt{\dfrac{1-\cos\theta}{2}}=\sqrt{\dfrac{4/3}{2}}=\sqrt{\dfrac23}=\dfrac{\sqrt6}{3}$",
  truth=sin(acos(-R(1, 3))/2), tag='نصف الزاوية مع تحديد الربع'),
# 2026 #5: simplest form (sum of two sines); options = coefficient x sin/cos
Q('m8q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(\frac{\pi}{6}-x)+\sin(\frac{\pi}{6}+x)', sin(pi/6-x)+sin(pi/6+x))),
  [O(r'\cos x', cos(x)), O(r'\sin x', sin(x)), O(r'\sqrt{3}\cos x', sqrt(3)*cos(x)), O(r'\sqrt{3}\sin x', sqrt(3)*sin(x))],
  r"$\sin\left(\frac{\pi}{6}\mp x\right)=\frac12\cos x\mp\frac{\sqrt3}{2}\sin x$ ، وبالجمع: $2\cdot\frac12\cos x=\cos x$",
  truth=sin(pi/6-x)+sin(pi/6+x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #6: equivalent expression (Pythagorean identities in a quotient)
Q('m8q7', U2[1], 'easy',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{1+\tan^{2}x}{1+\cot^{2}x}', (1+tan(x)**2)/(1+cot(x)**2))),
  [O(r'\tan^{2}x', tan(x)**2), O(r'\cot^{2}x', cot(x)**2), O(r'\sec^{2}x', sec(x)**2), O(r'\csc^{2}x', csc(x)**2)],
  r"$\dfrac{1+\tan^2x}{1+\cot^2x}=\dfrac{\sec^2x}{\csc^2x}=\dfrac{\sin^2x}{\cos^2x}=\tan^2x$",
  truth=(1+tan(x)**2)/(1+cot(x)**2), tag='المتطابقات الأساسية'),
# double angle from a squared relation (2026 #4 family); options = sign x 1 -/+ (1/2)^2
Q('m8q8', U2[2], 'medium',
  r"إذا كان: $\sin x-\cos x=\frac{1}{2}$ ، فإنّ قيمة $\sin 2x$ هي:",
  [O(r'\frac{3}{4}', R(3, 4)), O(r'-\frac{3}{4}', -R(3, 4)), O(r'\frac{5}{4}', R(5, 4)), O(r'-\frac{5}{4}', -R(5, 4))],
  r"بتربيع الطرفين: $\sin^2x-2\sin x\cos x+\cos^2x=\frac14$" "\n" r"$1-\sin2x=\frac14 \Rightarrow \sin2x=\frac34$",
  truth=(lambda xs: sin(2*xs))(nsolve(sin(x)-cos(x)-R(1, 2), x, 1)), tag='ضعف الزاوية بالتربيع'),
# 2026 #7: quadratic in cos with one solution rejected by an OPEN interval; options = single angles
Q('m8q9', U2[3], 'medium',
  F(r"حلّ المعادلة: $«0»=0$ في الفترة $(0,\,\pi)$ هو:", (r'2\cos^{2}x+\cos x-1', 2*cos(x)**2+cos(x)-1)),
  [O(st(r'\frac{\pi}{3}'), S_(P/3), 'set'), O(st(r'\pi'), S_(P), 'set'), O(st(r'\frac{2\pi}{3}'), S_(2*P/3), 'set'), O(st(r'\frac{\pi}{6}'), S_(P/6), 'set')],
  r"$(2\cos x-1)(\cos x+1)=0$" "\n" r"$\cos x=-1 \Rightarrow x=\pi$ خارج الفترة المفتوحة، و $\cos x=\frac12 \Rightarrow x=\frac{\pi}{3}$",
  truth=lambda: sols(2*cos(x)**2+cos(x)-1, 0, pi, closed_lo=False), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
# 2026 #8 family: double angle against a single angle, factor (do not divide by cos x)
Q('m8q10', U2[3], 'hard',
  F(r"حلول المعادلة: $«0»=«1»$ في الفترة $[0,\,\pi]$ هي:", (r'\sin 2x', sin(2*x)), (r'\cos x', cos(x))),
  [O(st(r'\frac{\pi}{6}', r'\frac{\pi}{2}', r'\frac{5\pi}{6}'), S_(P/6, P/2, 5*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'),
   O(st(r'\frac{\pi}{3}', r'\frac{\pi}{2}', r'\frac{2\pi}{3}'), S_(P/3, P/2, 2*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set')],
  r"$2\sin x\cos x-\cos x=0 \Rightarrow \cos x(2\sin x-1)=0$" "\n" r"$\cos x=0 \Rightarrow x=\frac{\pi}{2}$ ، $\sin x=\frac12 \Rightarrow x=\frac{\pi}{6},\ \frac{5\pi}{6}$",
  truth=lambda: sols(sin(2*x)-cos(x), 0, pi, closed_hi=True), tag='معادلة باستعمال متطابقة ضعف الزاوية'),
# ---------------- unit 3
# 2025s #2: sin/cos with a pi coefficient at a quadrantal angle; options = sign x which term survives
Q('m8q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(\pi)$ هي:", (r'2\cos x+\pi\sin x', 2*cos(x)+pi*sin(x))),
  [O(r'-\pi', -pi), O(r'\pi', pi), O('-2', -2), O('2', 2)],
  r"$f'(x)=-2\sin x+\pi\cos x$" "\n" r"$f'(\pi)=-2(0)+\pi(-1)=-\pi$",
  truth=Dx(2*cos(x)+pi*sin(x)).subs(x, pi), tag='مشتقات الاقترانات المثلثية'),
# 2026r #2: slope of the normal for ln plus reciprocal; options = sign x slope/normal slope
Q('m8q12', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، $x>0$ ، فإنّ ميل العمودي على المماس لمنحنى الاقتران $f(x)$ عندما $x=2$ هو:", (r'3\ln x-\frac{6}{x}', 3*log(x)-6/x)),
  [O(r'-\frac{1}{3}', -R(1, 3)), O(r'\frac{1}{3}', R(1, 3)), O('3', 3), O('-3', -3)],
  r"$f'(x)=\dfrac3x+\dfrac{6}{x^2}$ ، $f'(2)=\dfrac32+\dfrac64=3$ (ميل المماس)" "\n" r"ميل العمودي: $-\dfrac{1}{3}$",
  truth=-1/Dx(3*log(x)-6/x).subs(x, 2), tag='معادلة العمودي على المماس'),
# 2024s #4: velocity when the acceleration is zero; options = velocity sign x other quantities
Q('m8q13', U3[2], 'medium',
  F(r"إذا كان الاقتران: $s(t)=«0»$ ، $t\ge0$ يُمثّل موقع جُسيم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار و $t$ الزمن بالثواني، فإنّ سرعة الجُسيم المتجهة عندما يكون تسارعه صفرًا هي:", (r't^{3}-9t^{2}+15t', t**3-9*t**2+15*t)),
  [O('-12', -12, units='m/s'), O('12', 12, units='m/s'), O('-9', -9, units='m/s'), O('15', 15, units='m/s')],
  r"$v(t)=3t^2-18t+15$ ، $a(t)=6t-18=0 \Rightarrow t=3$" "\n" r"$v(3)=27-54+15=-12\ \text{m/s}$",
  truth=diff(t**3-9*t**2+15*t, t).subs(t, solve(diff(t**3-9*t**2+15*t, t, 2), t)[0]), tag='الحركة: السرعة والتسارع'),
# 2023 #5: f' given, a higher derivative asked; options = sign x one derivative too many
Q('m8q14', U3[2], 'medium',
  F(r"إذا كان: $f'(x)=«0»$ ، $x\ne0$ ، فإنّ $f'''(x)$ هي:", (r'\frac{x^{2}-4}{x^{2}}', (x**2-4)/x**2)),
  [O(r'-\frac{24}{x^{4}}', -24/x**4), O(r'\frac{24}{x^{4}}', 24/x**4), O(r'\frac{96}{x^{5}}', 96/x**5), O(r'-\frac{96}{x^{5}}', -96/x**5)],
  r"$f'(x)=1-4x^{-2}$ ، $f''(x)=8x^{-3}$ ، $f'''(x)=-24x^{-4}=-\dfrac{24}{x^4}$",
  truth=diff((x**2-4)/x**2, x, 2), tag='المشتقات العليا'),
# 2025s #4 (plant height): quotient model in context; options = sign x squared denominator
Q('m8q15', U3[2], 'medium',
  F(r"إذا أمكن التعبير عن ارتفاع نبتة بالاقتران: $h(t)=«0»$ ، حيث $h$ الارتفاع بالسنتيمترات، و $t$ الزمن بالأسابيع بعد زراعة البذور، فإنّ معدّل تغيّر ارتفاع النبتة بالنسبة إلى الزمن عندما $t=3$ هو:", (r'\frac{30t^{2}}{t^{2}+9}', 30*t**2/(t**2+9))),
  [O('5', 5, units='cm/week'), O('90', 90, units='cm/week'), O('-5', -5, units='cm/week'), O('-90', -90, units='cm/week')],
  r"$h'(t)=\dfrac{60t(t^2+9)-30t^2(2t)}{(t^2+9)^2}=\dfrac{540t}{(t^2+9)^2}$" "\n" r"$h'(3)=\dfrac{1620}{324}=5\ \text{cm/week}$",
  truth=diff(30*t**2/(t**2+9), t).subs(t, 3), tag='معدل التغير في سياق حياتي'),
# 2025s #3 / 2024 #4: one graph, h = exponential times f; options = sign x f -/+ f'
Q('m8q16', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنى الاقتران $f(x)$. إذا كان: $h(x)=e^{x}f(x)$ ، فإنّ $h'(1)$ هي:",
  [O('e', E), O('-e', -E), O('3e', 3*E), O('-3e', -3*E)],
  r"من الشكل: $f(1)=2$ ، $f'(1)=-1$ (ميل القطعة من $(0,3)$ إلى $(2,1)$)" "\n" r"$h'(x)=e^xf(x)+e^xf'(x) \Rightarrow h'(1)=e(2-1)=e$",
  truth=lambda: (lambda fv, fs: E*(fv(1)+fs(1)))(*pw(F8)),
  figure=figure('m8q16', fig_one(F8, (0, 5), (0, 4), (4.2, 2.3))), tag='المشتقة من التمثيل البياني'),
# 2025s #11: power of a logarithm to base a; options = ln a position x chain factor 2
Q('m8q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(8)$ هي:", (r'(\log_{3}(x+1))^{2}', log(x+1, 3)**2)),
  [O(r'\frac{4}{9\ln 3}', 4/(9*log(3))), O(r'\frac{4\ln 3}{9}', 4*log(3)/9), O(r'\frac{2}{9\ln 3}', 2/(9*log(3))), O(r'\frac{2\ln 3}{9}', 2*log(3)/9)],
  r"$f'(x)=2\log_3(x+1)\cdot\dfrac{1}{(x+1)\ln3}$ ، و $\log_39=2$" "\n" r"$f'(8)=2(2)\cdot\dfrac{1}{9\ln3}=\dfrac{4}{9\ln3}$",
  truth=Dx(log(x+1, 3)**2).subs(x, 8), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2025s #9: composite from tables of values; options = sign x evaluating g' at the wrong point
Q('m8q18', U3[3], 'medium',
  r"إذا كان: $h(x)=g(f(x))$ ، وكان: $f(3)=2$ ، $f'(3)=-4$ ، $g'(2)=\frac{1}{2}$ ، $g'(3)=7$ ، فإنّ $h'(3)$ هي:",
  [O('-2', -2), O('2', 2), O('-28', -28), O('28', 28)],
  r"$h'(x)=g'(f(x))\cdot f'(x)$" "\n" r"$h'(3)=g'(f(3))\cdot f'(3)=g'(2)\cdot(-4)=\frac12(-4)=-2$",
  truth=R(1, 2)*(-4), tag='قاعدة السلسلة من قيم معطاة'),
# 2026 #15: parametric (cos/sin) at a special angle; options = sign x reciprocal
Q('m8q19', U3[3], 'easy',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\frac{\pi}{3}$ هو:", (r'2\cos t', 2*cos(t)), (r'3\sin t', 3*sin(t))),
  [O(r'-\frac{\sqrt{3}}{2}', -sqrt(3)/2), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O(r'-\frac{2\sqrt{3}}{3}', -2*sqrt(3)/3), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3)],
  r"$\dfrac{dx}{dt}=-2\sin t=-\sqrt3$ ، $\dfrac{dy}{dt}=3\cos t=\dfrac32$" "\n" r"$\dfrac{dy}{dx}=\dfrac{3/2}{-\sqrt3}=-\dfrac{\sqrt3}{2}$",
  truth=(diff(3*sin(t), t)/diff(2*cos(t), t)).subs(t, pi/3), tag='مشتقة المعادلات الوسيطية'),
# 2023 #9 / 2026 #16: implicit with a trig term at a lattice point; options = sign of cos(pi) x moving a term
Q('m8q20', U3[4], 'hard',
  F(r"إذا كان: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(1,\,1)$ هي:", (r'x^{2}y+\sin(\pi y)', x**2*y+sin(pi*y)), (r'4x-3', 4*x-3)),
  [O(r'\frac{2}{1-\pi}', 2/(1-pi)), O(r'\frac{2}{1+\pi}', 2/(1+pi)), O(r'\frac{6}{1-\pi}', 6/(1-pi)), O(r'\frac{6}{1+\pi}', 6/(1+pi))],
  r"$2xy+x^2\dfrac{dy}{dx}+\pi\cos(\pi y)\dfrac{dy}{dx}=4$" "\n" r"عند $(1,1)$: $2+\dfrac{dy}{dx}-\pi\dfrac{dy}{dx}=4 \Rightarrow (1-\pi)\dfrac{dy}{dx}=2 \Rightarrow \dfrac{dy}{dx}=\dfrac{2}{1-\pi}$",
  truth=imp(x**2*y+sin(pi*y)-4*x+3, (1, 1)), tag='الاشتقاق الضمني عند نقطة'),
# 2026 #17: tangent to an implicit curve, x-intercept; options = slope slips
Q('m8q21', U3[4], 'medium',
  F(r"إذا مثّل المستقيم $l$ مماسًّا لمنحنى العلاقة: $«0»=1$ عند النقطة $(1,\,2)$ ، فإنّ المقطع $x$ للمستقيم $l$ هو:", (r'x^{2}+2xy-y^{2}', x**2+2*x*y-y**2)),
  [O(r'\frac{1}{3}', R(1, 3)), O('-1', -1), O('-5', -5), O(r'\frac{5}{3}', R(5, 3))],
  r"$2x+2y+2xy'-2yy'=0$ ، وعند $(1,2)$: $2+4+2y'-4y'=0 \Rightarrow y'=3$" "\n" r"$l$: $y-2=3(x-1)$ ، وعند $y=0$: $x-1=-\frac23 \Rightarrow x=\frac13$",
  truth=lambda: tangent_x_intercept(x**2+2*x*y-y**2-1, (1, 2)), tag='مماس منحنى علاقة ضمنية'),
# 2026 #18: cylinder with a figure, L/min -> m/min, draining; options = unit conversion x radius/diameter
Q('m8q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي خزّانًا أسطوانيًّا ارتفاعه $6\ \text{m}$ ، وطول قُطر قاعدته $4\ \text{m}$ ، يتسرّب منه الماء بمعدّل $400\ \text{L/min}$ ، فإنّ معدّل تغيّر ارتفاع الماء في الخزّان عند أيّ لحظة هو:",
  [O(r'-\frac{1}{10\pi}', -1/(10*pi), units='m/min'), O(r'-\frac{1}{40\pi}', -1/(40*pi), units='m/min'), O(r'-\frac{100}{\pi}', -100/pi, units='m/min'), O(r'-\frac{25}{\pi}', -25/pi, units='m/min')],
  r"$V=\pi r^2h=4\pi h$ (نصف القطر $2$) ، و $\dfrac{dV}{dt}=-400\ \text{L/min}=-0.4\ \text{m}^3/\text{min}$" "\n" r"$-0.4=4\pi\dfrac{dh}{dt} \Rightarrow \dfrac{dh}{dt}=-\dfrac{1}{10\pi}\ \text{m/min}$",
  truth=-R(4, 10)/diff(pi*2**2*s, s), figure=figure('m8q22', fig_cylinder(), 2.8, 3.2), tag='معدلات مرتبطة مع تحويل الوحدات'),
# ---------------- unit 4
# 2026r #18: trigonometric form of a product written as i-multiple; options = quadrant x reference angle
Q('m8q23', U4[1], 'medium',
  r"الصورة المثلثية للعدد المركّب $w=-2i(\sqrt{3}+i)$ هي:",
  [O(trig('4', r'-\frac{\pi}{3}'), pol(4, -P/3)), O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3)),
   O(trig('4', r'-\frac{\pi}{6}'), pol(4, -P/6)), O(trig('4', r'\frac{2\pi}{3}'), pol(4, 2*P/3))],
  r"$w=-2\sqrt3\,i-2i^2=2-2\sqrt3\,i$ ، $|w|=\sqrt{4+12}=4$ (الربع الرابع)" "\n" r"زاوية الإسناد $\frac{\pi}{3}$ ، و $\text{Arg}(w)=-\frac{\pi}{3}$",
  truth=expand(-2*I*(sqrt(3)+I)), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2026r #21-22: shared stem (conjugate and modulus of a product)
Q('m8q24', U4[2], 'easy',
  r"ناتج $\bar{z}+2w$ هو:",
  [O('9-7i', 9-7*I), O('9-5i', 9-5*I), O('9+5i', 9+5*I), O('9+7i', 9+7*I)],
  r"$\bar z=5-i$ ، $2w=4-6i$" "\n" r"$\bar z+2w=9-7i$",
  truth=conjugate(5+I)+2*(2-3*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=5+i$ ، $w=2-3i$", 24, 25)),
# 2026r #25: second item of the shared stem (|zw|); options = add vs multiply moduli
Q('m8q25', U4[1], 'easy',
  r"قيمة $|zw|$ هي:",
  [O(r'13\sqrt{2}', 13*sqrt(2)), O(r'\sqrt{39}', sqrt(39)), O(r'\sqrt{26}+\sqrt{13}', sqrt(26)+sqrt(13)), O('26', 26)],
  r"$|z|=\sqrt{26}$ ، $|w|=\sqrt{13}$ ، و $|zw|=|z||w|=\sqrt{338}=13\sqrt2$",
  truth=Abs(expand((5+I)*(2-3*I))), tag='المقياس والعمليات (نص مشترك)'),
# 2024 #22 / 2023 #21: equality with a quotient -> real constant; options = sign x answering b instead of a
Q('m8q26', U4[2], 'medium',
  r"إذا كان: $\dfrac{a+5i}{2+i}=b+3i$ ، حيث $a$ و $b$ ثابتان حقيقيان، فإنّ قيمة الثابت $a$ هي:",
  [O('-5', -5), O('5', 5), O('-1', -1), O('1', 1)],
  r"$a+5i=(b+3i)(2+i)=2b+bi+6i+3i^2=(2b-3)+(b+6)i$" "\n" r"$b+6=5 \Rightarrow b=-1$ ، و $a=2b-3=-5$",
  truth=lambda: solve([re(expand(X+5*I-(Y+3*I)*(2+I))), im(expand(X+5*I-(Y+3*I)*(2+I)))], [X, Y])[X], tag='معادلة فيها العدد ومرافقه'),
# 2023 #23 / 2024 #24: one square root of a complex number has a given form
Q('m8q27', U4[2], 'medium',
  r"إذا كان: $3+bi$ أحد الجذرين التربيعيين للعدد المركّب $5-12i$ ، فإنّ قيمة الثابت الحقيقي $b$ هي:",
  [O('-2', -2), O('2', 2), O('-4', -4), O('4', 4)],
  r"$(3+bi)^2=9-b^2+6bi=5-12i$" "\n" r"$6b=-12 \Rightarrow b=-2$ (وتحقّق $9-b^2=5$)",
  truth=lambda: [r_ for r_ in solve(im(expand((3+X*I)**2))+12, X) if (9-r_**2) == 5][0], tag='الجذور التربيعية للعدد المركب'),
# 2024 #20: Arg of a related number in terms of alpha (multiplication by i rotates by pi/2)
Q('m8q28', U4[1], 'medium',
  r"إذا كان: $\text{Arg}(2+3i)=\alpha$ ، فإنّ $\text{Arg}(-3+2i)$ هي:",
  [O(r'\alpha+\frac{\pi}{2}', atan(R(3, 2))+pi/2, sym={'alpha': atan(R(3, 2))}), O(r'\frac{\pi}{2}-\alpha', pi/2-atan(R(3, 2)), sym={'alpha': atan(R(3, 2))}),
   O(r'\pi-\alpha', pi-atan(R(3, 2)), sym={'alpha': atan(R(3, 2))}), O(r'\alpha-\frac{\pi}{2}', atan(R(3, 2))-pi/2, sym={'alpha': atan(R(3, 2))})],
  r"$-3+2i=i(2+3i)$ ، والضرب في $i$ يدوّر العدد بزاوية $\frac{\pi}{2}$ عكس عقارب الساعة" "\n" r"$\text{Arg}(-3+2i)=\alpha+\frac{\pi}{2}$ (وهي أقل من $\pi$ لأنّ $\alpha<\frac{\pi}{2}$)",
  truth=arg(-3+2*I), tag='السعة الرئيسة'),
# 2024 #25 / 2023 #25: perpendicular bisector shown with its two points; options = sign of A x sign of B
IndexQ('m8q29', U4[3], 'medium',
  r"معتمدًا الشكل الآتي، ما معادلة المستقيم $l$ المُمثَّل بيانيًّا (بدلالة $z$)؟",
  [T(r'$|z-3i|=|z-4-i|$', bisector(A8, B8)), T(r'$|z+3i|=|z+4+i|$', bisector(-A8, -B8)),
   T(r'$|z-3i|=|z+4+i|$', bisector(A8, -B8)), T(r'$|z+3i|=|z-4-i|$', bisector(-A8, B8))],
  r"$l$ عمود منصّف للقطعة $AB$ ، حيث $A(0,3)$ أي $3i$ ، و $B(4,1)$ أي $4+i$" "\n" r"$|z-3i|=|z-(4+i)|=|z-4-i|$",
  truth=region_truth(bisector(A8, B8), L8, 5), figure=figure('m8q29', fig_bisector(), 3.2, 3.2), tag='كتابة معادلة محل هندسي'),
# 2025s #23 / 2026r #23: a wedge from a point, one ray dashed; options = vertex sign x strictness
IndexQ('m8q30', U4[3], 'medium',
  r"متباينة المحل الهندسي (بدلالة $z$) التي تُمثِّل المنطقة المُظلَّلة في الشكل الآتي هي:",
  [T(r'$-\frac{\pi}{2}\le\text{Arg}(z+1-2i)<\frac{\pi}{4}$', R8),
   T(r'$-\frac{\pi}{2}<\text{Arg}(z+1-2i)\le\frac{\pi}{4}$', sector(V8, -math.pi/2, math.pi/4, lo_open=True)),
   T(r'$-\frac{\pi}{2}\le\text{Arg}(z-1+2i)<\frac{\pi}{4}$', sector(1 - 2j, -math.pi/2, math.pi/4, hi_open=True)),
   T(r'$-\frac{\pi}{2}<\text{Arg}(z-1+2i)\le\frac{\pi}{4}$', sector(1 - 2j, -math.pi/2, math.pi/4, lo_open=True))],
  r"رأس المنطقة $(-1,2)$ أي $-1+2i$ ، فنكتب $\text{Arg}(z+1-2i)$" "\n" r"الشعاع الرأسي إلى الأسفل ($-\frac{\pi}{2}$) متصل، والمائل ($\frac{\pi}{4}$) متقطّع",
  truth=region_truth(R8, PR8, 5), figure=figure('m8q30', fig_region2(R8, PR8, 5), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 9
F9, G9 = [(0, 1), (2, 5), (6, 3)], [(0, 5), (4, 1), (6, 3)]
_h9 = math.sqrt(3)
R9 = both(disk(2j, 2, strict=True), nearer(0, 2))
PR9 = [('arc', 2j, 2, True, (math.pi/3, 5*math.pi/3)), ('seg', complex(1, 2 - _h9), complex(1, 2 + _h9), False)]


def fig_square():
    """square z1 z2 z3 z4 in the complex plane; only z2 and z3 are given (2025 #23 style)."""
    def draw(fig, ax):
        complex_axes(ax, 7)
        ax.set_xticks([]); ax.set_yticks([])
        pts = {'z_1': (1, 6), 'z_2': (-2, 3), 'z_3': (1, 0), 'z_4': (4, 3)}
        order = ['z_1', 'z_2', 'z_3', 'z_4', 'z_1']
        ax.plot([pts[k_][0] for k_ in order], [pts[k_][1] for k_ in order], color='#555555', lw=1.6)
        offs = {'z_1': (0.2, 0.2), 'z_2': (-1.2, 0.1), 'z_3': (0.2, -0.75), 'z_4': (0.25, 0.1)}
        for k_, (px, py) in pts.items():
            ax.plot(px, py, 'o', color=LINE, ms=5, zorder=5)
            ax.text(px + offs[k_][0], py + offs[k_][1], f'${k_}$', fontsize=12)
        ax.set_xlim(-4.5, 6.5); ax.set_ylim(-1.5, 7.5)
    return draw


P9 = [
# ---------------- unit 1
# 2026 #1: one negative root given, equation not set to zero
Q('m9q1', U1[1], 'easy',
  F(r"إذا كان $x=-2$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ لها حلَّين آخرين هما:", (r'x^{3}', x**3), (r'2x^{2}+13x+10', 2*x**2+13*x+10)),
  [O(st('5', '-1'), S_(5, -1), 'set'), O(st('-5', '1'), S_(-5, 1), 'set'), O(st('-5', '-1'), S_(-5, -1), 'set'), O(st('5', '1'), S_(5, 1), 'set')],
  r"$x^3-2x^2-13x-10=0$ ، وبالقسمة التركيبية على $(x+2)$: $1,\ -2,\ -13,\ -10 \to 1,\ -4,\ -5,\ 0$" "\n" r"$x^2-4x-5=(x-5)(x+1)=0 \Rightarrow x=5,\ x=-1$",
  truth=lambda: other_roots(x**3-2*x**2-13*x-10, -2), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# 2026 #2 with a repeated factor and a distinct factor; options = B,C swapped x sign of A
Q('m9q2', U1[2], 'medium',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{2x^{2}-x+1}{x(x-1)^{2}}', (2*x**2-x+1)/(x*(x-1)**2))),
  [O(r'\frac{1}{x}+\frac{1}{x-1}+\frac{2}{(x-1)^{2}}', 1/x+1/(x-1)+2/(x-1)**2), O(r'\frac{1}{x}+\frac{2}{x-1}+\frac{1}{(x-1)^{2}}', 1/x+2/(x-1)+1/(x-1)**2),
   O(r'-\frac{1}{x}+\frac{1}{x-1}+\frac{2}{(x-1)^{2}}', -1/x+1/(x-1)+2/(x-1)**2), O(r'-\frac{1}{x}+\frac{2}{x-1}+\frac{1}{(x-1)^{2}}', -1/x+2/(x-1)+1/(x-1)**2)],
  r"$2x^2-x+1=A(x-1)^2+Bx(x-1)+Cx$" "\n" r"$x=0$: $A=1$ ، $x=1$: $C=2$ ، معامل $x^2$: $2=A+B \Rightarrow B=1$",
  truth=(2*x**2-x+1)/(x*(x-1)**2), tag='تجزئة: عامل خطي مكرر'),
# 2026 #3 with a divisor (ax + b); options = right zero x sign slips
Q('m9q3', U1[1], 'medium',
  F(r"إذا كان باقي قسمة الاقتران: $f(x)=«0»$ على $(2x+1)$ يساوي $3$ ، فإنّ قيمة الثابت $k$ هي:", (r'4x^{3}+kx^{2}-2x+1', 4*x**3+k*x**2-2*x+1)),
  [O('6', 6), O('10', 10), O(r'\frac{15}{2}', R(15, 2)), O('-6', -6)],
  r"صفر المقسوم عليه $x=-\frac12$" "\n" r"$f\left(-\frac12\right)=-\frac12+\frac k4+1+1=\frac32+\frac k4=3 \Rightarrow k=6$",
  truth=lambda: solve(rem(4*x**3+k*x**2-2*x+1, -R(1, 2))-3, k)[0], tag='نظرية الباقي: القسمة على (ax−b)'),
# 2026 #1 family: complete factorisation (find a zero by trial, then factor); options = sign patterns
Q('m9q4', U1[1], 'medium',
  F(r"التحليل الكامل للاقتران: $f(x)=«0»$ هو:", (r'x^{3}-7x-6', x**3-7*x-6)),
  [O('(x+1)(x+2)(x-3)', (x+1)*(x+2)*(x-3)), O('(x-1)(x-2)(x+3)', (x-1)*(x-2)*(x+3)),
   O('(x+1)(x-2)(x+3)', (x+1)*(x-2)*(x+3)), O('(x-1)(x+2)(x-3)', (x-1)*(x+2)*(x-3))],
  r"$f(-1)=-1+7-6=0$ ، فـ $(x+1)$ عامل، وبالقسمة: $x^2-x-6=(x-3)(x+2)$" "\n" r"$f(x)=(x+1)(x+2)(x-3)$",
  truth=x**3-7*x-6, tag='التحليل الكامل لكثير حدود'),
# ---------------- unit 2
# 2026 #4 from sin theta in the 4th quadrant; options = sign x reciprocal
Q('m9q5', U2[2], 'medium',
  r"إذا كان: $\sin\theta=-\frac{5}{13}$ ، $\frac{3\pi}{2}<\theta<2\pi$ ، فإنّ قيمة $\tan\frac{\theta}{2}$ تساوي:",
  [O(r'-\frac{1}{5}', -R(1, 5)), O(r'\frac{1}{5}', R(1, 5)), O('-5', -5), O('5', 5)],
  r"$\cos\theta=\frac{12}{13}$ ، و $\frac{3\pi}{4}<\frac{\theta}{2}<\pi$ فالظل سالب" "\n" r"$\tan\frac{\theta}{2}=\dfrac{\sin\theta}{1+\cos\theta}=\dfrac{-5/13}{25/13}=-\dfrac15$",
  truth=tan((2*pi-asin(R(5, 13)))/2), tag='نصف الزاوية مع تحديد الربع'),
# 2026 #5: simplest form; options = coefficient x sin/cos
Q('m9q6', U2[1], 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(x+\frac{\pi}{4})-\cos(x+\frac{\pi}{4})', sin(x+pi/4)-cos(x+pi/4))),
  [O(r'\sqrt{2}\sin x', sqrt(2)*sin(x)), O(r'\sqrt{2}\cos x', sqrt(2)*cos(x)), O(r'\frac{\sqrt{2}}{2}\sin x', sqrt(2)/2*sin(x)), O(r'\frac{\sqrt{2}}{2}\cos x', sqrt(2)/2*cos(x))],
  r"$\sin\left(x+\frac{\pi}{4}\right)=\frac{\sqrt2}{2}(\sin x+\cos x)$ ، $\cos\left(x+\frac{\pi}{4}\right)=\frac{\sqrt2}{2}(\cos x-\sin x)$" "\n" r"بالطرح: $\frac{\sqrt2}{2}(2\sin x)=\sqrt2\sin x$",
  truth=sin(x+pi/4)-cos(x+pi/4), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #6: equivalent expression (fraction minus a ratio)
Q('m9q7', U2[1], 'medium',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\cos x}{1-\sin x}-\tan x', cos(x)/(1-sin(x))-tan(x))),
  [O(r'\sec x', sec(x)), O(r'\csc x', csc(x)), O(r'2\sec x', 2*sec(x)), O(r'2\csc x', 2*csc(x))],
  r"$\dfrac{\cos x}{1-\sin x}-\dfrac{\sin x}{\cos x}=\dfrac{\cos^2x-\sin x+\sin^2x}{(1-\sin x)\cos x}=\dfrac{1-\sin x}{(1-\sin x)\cos x}=\dfrac{1}{\cos x}$",
  truth=cos(x)/(1-sin(x))-tan(x), tag='المتطابقات الأساسية'),
# sum-to-product exact value (2026 #5 family); options = surd slips
Q('m9q8', U2[2], 'medium',
  r"قيمة المقدار: $\cos\frac{5\pi}{12}+\cos\frac{\pi}{12}$ هي:",
  [O(r'\frac{\sqrt{6}}{2}', sqrt(6)/2), O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2), O(r'\frac{\sqrt{6}}{4}', sqrt(6)/4), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2)],
  r"$\cos A+\cos B=2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$" "\n" r"$=2\cos\frac{\pi}{4}\cos\frac{\pi}{6}=2\cdot\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}=\frac{\sqrt6}{2}$",
  truth=cos(5*pi/12)+cos(pi/12), tag='تحويل المجموع إلى ضرب'),
# 2026 #7 family: Pythagorean identity gives a perfect square in tan; options = second quadrant vs third x one solution
Q('m9q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'\sec^{2}x-2\tan x', sec(x)**2-2*tan(x))),
  [O(st(r'\frac{\pi}{4}', r'\frac{5\pi}{4}'), S_(P/4, 5*P/4), 'set'), O(st(r'\frac{\pi}{4}', r'\frac{3\pi}{4}'), S_(P/4, 3*P/4), 'set'),
   O(st(r'\frac{\pi}{4}'), S_(P/4), 'set'), O(st(r'\frac{3\pi}{4}', r'\frac{7\pi}{4}'), S_(3*P/4, 7*P/4), 'set')],
  r"$1+\tan^2x-2\tan x=0 \Rightarrow (\tan x-1)^2=0 \Rightarrow \tan x=1$" "\n" r"الظل موجب في الربعين الأول والثالث: $x=\frac{\pi}{4},\ \frac{5\pi}{4}$",
  truth=lambda: sols(sec(x)**2-2*tan(x), 0, 2*pi), tag='معادلة تربيعية بعد استعمال متطابقة فيثاغورس'),
# 2026 #8: double angle in the interval (pi, 2pi); options = shifted or not x halved or not
Q('m9q10', U2[3], 'hard',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $(\pi,\,2\pi)$ هي:", (r'2\cos 2x+1', 2*cos(2*x)+1)),
  [O(st(r'\frac{4\pi}{3}', r'\frac{5\pi}{3}'), S_(4*P/3, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set'),
   O(st(r'\frac{8\pi}{3}', r'\frac{10\pi}{3}'), S_(8*P/3, 10*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set')],
  r"$\cos2x=-\frac12$ ، و $2\pi<2x<4\pi$" "\n" r"$2x=2\pi+\frac{2\pi}{3}=\frac{8\pi}{3}$ أو $2x=2\pi+\frac{4\pi}{3}=\frac{10\pi}{3}$ ، إذن $x=\frac{4\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*cos(2*x)+1, pi, 2*pi, closed_lo=False), tag='معادلة بزاوية مضاعفة في فترة'),
# ---------------- unit 3
# 2025 #1 / 2025s #1: ln of a quotient with a power of e; options = constant kept x 1/(2x) vs 1/sqrt x
Q('m9q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، $x>0$ ، فإنّ $f'(x)$ هي:", (r'\ln(\frac{\sqrt{x}}{e^{3}})', log(sqrt(x)/E**3))),
  [O(r'\frac{1}{2x}', 1/(2*x)), O(r'\frac{1}{2x}-3', 1/(2*x)-3), O(r'\frac{1}{\sqrt{x}}', 1/sqrt(x)), O(r'\frac{1}{\sqrt{x}}-3', 1/sqrt(x)-3)],
  r"$f(x)=\ln\sqrt x-\ln e^3=\frac12\ln x-3$" "\n" r"$f'(x)=\dfrac{1}{2x}$",
  truth=Dx(log(sqrt(x)/E**3)), tag='مشتقة الاقتران اللوغاريتمي'),
# 2024s #6 / 2025s #6: tan/cot of a multiple of x at a point; options = chain factor pi x squared or not
Q('m9q12', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{1}{3}\right)$ هي:", (r'2\tan(\pi x)', 2*tan(pi*x))),
  [O(r'8\pi', 8*pi), O('8', 8), O(r'4\pi', 4*pi), O('4', 4)],
  r"$f'(x)=2\pi\sec^2(\pi x)$ ، و $\sec\frac{\pi}{3}=2$" "\n" r"$f'\left(\frac13\right)=2\pi(4)=8\pi$",
  truth=Dx(2*tan(pi*x)).subs(x, R(1, 3)), tag='مشتقات الاقترانات المثلثية'),
# 2025s #10 / 2025 #4: position at the first instant of momentary rest; options = positions at other instants
Q('m9q13', U3[1], 'medium',
  F(r"إذا كان الاقتران: $s(t)=«0»$ ، $t\ge0$ يُمثّل موقع جُسيم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار و $t$ الزمن بالثواني، فإنّ موقع الجُسيم عندما كان في حالة سكون لحظي أوّل مرة بعد انطلاقه هو:", (r'4+2\cos(\pi t)', 4+2*cos(pi*t))),
  [O('2', 2, units='m'), O('6', 6, units='m'), O('4', 4, units='m'), O('0', 0, units='m')],
  r"$v(t)=-2\pi\sin(\pi t)=0 \Rightarrow t=0,\ 1,\ 2,\ \dots$ ، وأوّل سكون بعد الانطلاق عند $t=1$" "\n" r"$s(1)=4+2\cos\pi=2\ \text{m}$",
  truth=(4+2*cos(pi*t)).subs(t, [r_ for r_ in solve(diff(4+2*cos(pi*t), t), t) if r_ > 0][0]), tag='الحركة: اتجاه الحركة والسكون'),
# 2026 #11: combination of derivatives of a trig sum; options = sign x sin/cos
Q('m9q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''(x)+2f'(x)$ هي:", (r'\sin 2x+\cos 2x', sin(2*x)+cos(2*x))),
  [O(r'-8\sin 2x', -8*sin(2*x)), O(r'8\sin 2x', 8*sin(2*x)), O(r'-8\cos 2x', -8*cos(2*x)), O(r'8\cos 2x', 8*cos(2*x))],
  r"$f'(x)=2\cos2x-2\sin2x$ ، $f''(x)=-4\sin2x-4\cos2x$" "\n" r"$f''+2f'=-4\sin2x-4\cos2x+4\cos2x-4\sin2x=-8\sin2x$",
  truth=diff(sin(2*x)+cos(2*x), x, 2)+2*Dx(sin(2*x)+cos(2*x)), tag='المشتقات العليا وتراكيبها'),
# 2026r #11: bacteria with a fractional exponent base, units in options; options = sign x missing square
Q('m9q15', U3[3], 'hard',
  F(r"إذا كان الاقتران: $N(t)=«0»$ ، $t\ge0$ يُمثّل عدد الخلايا البكتيرية بعد $t$ ساعة في مجتمع بكتيري، فإنّ معدّل نموّ المجتمع بعد ساعة واحدة (بالخلية لكلّ ساعة) هو:", (r'600(\frac{1}{4})^{\frac{1}{t+1}}', 600*R(1, 4)**(1/(t+1)))),
  [O(r'75\ln 4', 75*log(4)), O(r'-75\ln 4', -75*log(4)), O(r'150\ln 4', 150*log(4)), O(r'-150\ln 4', -150*log(4))],
  r"$N'(t)=600\left(\frac14\right)^{\frac{1}{t+1}}\ln\frac14\cdot\left(-\dfrac{1}{(t+1)^2}\right)$" "\n" r"$N'(1)=600\cdot\frac12\cdot(-\ln4)\cdot\left(-\frac14\right)=75\ln4$",
  truth=diff(600*R(1, 4)**(1/(t+1)), t).subs(t, 1), tag='معدل التغير في سياق حياتي'),
# 2026 #14 with a composite: h = f(g(x)) read from two graphs; options = sign x evaluating f' at x instead of g(x)
Q('m9q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=f(g(x))$ ، فإنّ $h'(1)$ هي:",
  [O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2)), O('-2', -2), O('2', 2)],
  r"من الشكل: $g(1)=4$ ، $g'(1)=-1$ ، و $f'(4)=-\frac12$ (ميل قطعة $f$ من $(2,5)$ إلى $(6,3)$)" "\n" r"$h'(1)=f'(g(1))\cdot g'(1)=f'(4)\cdot(-1)=\frac12$",
  truth=lambda: (lambda fv, fs, gv, gs: fs(gv(1))*gs(1))(*pw(F9), *pw(G9)),
  figure=figure('m9q16', draw_two(F9, G9, 6, 5, (2.6, 5.2), (4.6, 1.3))), tag='المشتقة من التمثيل البياني'),
# 2025 #11: log of a product of conjugate factors; options = ln 10 position x sign of the denominator
Q('m9q17', U3[3], 'medium',
  r"إذا كان: $f(x)=\log\big((2-x)(2+x)\big)$ ، $-2<x<2$ ، فإنّ $f'(x)$ هي:",
  [O(r'\frac{2x}{(x^{2}-4)\ln 10}', 2*x/((x**2-4)*log(10))), O(r'\frac{-2x}{(x^{2}-4)\ln 10}', -2*x/((x**2-4)*log(10))),
   O(r'\frac{2x\cdot\ln 10}{x^{2}-4}', 2*x*log(10)/(x**2-4)), O(r'\frac{-2x\cdot\ln 10}{x^{2}-4}', -2*x*log(10)/(x**2-4))],
  r"$f(x)=\log(4-x^2)$ ، $f'(x)=\dfrac{-2x}{(4-x^2)\ln10}=\dfrac{2x}{(x^2-4)\ln10}$",
  truth=Dx(log((2-x)*(2+x), 10)), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2024s #8: ln of a squared trig ratio at a special angle; options = sign x cot vs tan
Q('m9q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، $0<x<\frac{\pi}{2}$ ، فإنّ $f'\left(\frac{\pi}{6}\right)$ هي:", (r'\ln(\csc^{2}x)', log(csc(x)**2))),
  [O(r'-2\sqrt{3}', -2*sqrt(3)), O(r'2\sqrt{3}', 2*sqrt(3)), O(r'-\frac{2\sqrt{3}}{3}', -2*sqrt(3)/3), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3)],
  r"$f(x)=2\ln(\csc x)$ ، $f'(x)=2\cdot\dfrac{-\csc x\cot x}{\csc x}=-2\cot x$" "\n" r"$f'\left(\frac{\pi}{6}\right)=-2\sqrt3$",
  truth=Dx(log(csc(x)**2)).subs(x, pi/6), tag='قاعدة السلسلة مع اللوغاريتم'),
# 2023 #8: parametric derivative as a function of t; options = reciprocal x sign
Q('m9q19', U3[3], 'easy',
  F(r"إذا كان: $x=«0»$ ، $y=«1»$ ، $0<t<\frac{\pi}{2}$ ، فإنّ $\dfrac{dy}{dx}$ هي:", (r'\sec t', sec(t)), (r'\tan t', tan(t))),
  [O(r'\csc t', csc(t)), O(r'\sin t', sin(t)), O(r'-\csc t', -csc(t)), O(r'-\sin t', -sin(t))],
  r"$\dfrac{dy}{dx}=\dfrac{\sec^2t}{\sec t\tan t}=\dfrac{\sec t}{\tan t}=\dfrac{1/\cos t}{\sin t/\cos t}=\dfrac{1}{\sin t}=\csc t$",
  truth=diff(tan(t), t)/diff(sec(t), t), tag='مشتقة المعادلات الوسيطية'),
# 2026 #16: a^(xy) relation, point from x = 0; options = sign x ln a dropped
Q('m9q20', U3[4], 'hard',
  F(r"إذا كان: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $x=0$ هو:", (r'3^{xy}', 3**(x*y)), (r'x+y', x+y)),
  [O(r'\ln 3-1', log(3)-1), O(r'1-\ln 3', 1-log(3)), O(r'\ln 3+1', log(3)+1), O(r'-\ln 3-1', -log(3)-1)],
  r"عندما $x=0$: $3^0=0+y \Rightarrow y=1$" "\n" r"$3^{xy}\ln3\left(y+x\dfrac{dy}{dx}\right)=1+\dfrac{dy}{dx}$ ، وعند $(0,1)$: $\ln3=1+\dfrac{dy}{dx} \Rightarrow \dfrac{dy}{dx}=\ln3-1$",
  truth=imp(3**(x*y)-x-y, (0, 1)), tag='الاشتقاق الضمني عند نقطة'),
# 2026 #17: tangent to x y^2 = c at a lattice point, y-intercept; options = slope slips
Q('m9q21', U3[4], 'medium',
  F(r"إذا مثّل المستقيم $l$ مماسًّا لمنحنى العلاقة: $«0»=12$ عند النقطة $(3,\,2)$ ، فإنّ المقطع $y$ للمستقيم $l$ هو:", (r'xy^{2}', x*y**2)),
  [O('3', 3), O('9', 9), O('1', 1), O('11', 11)],
  r"$y^2+2xy\dfrac{dy}{dx}=0$ ، وعند $(3,2)$: $4+12\dfrac{dy}{dx}=0 \Rightarrow \dfrac{dy}{dx}=-\frac13$" "\n" r"$l$: $y-2=-\frac13(x-3)$ ، وعند $x=0$: $y=2+1=3$",
  truth=lambda: 2-3*imp(x*y**2-12, (3, 2)), tag='مماس منحنى علاقة ضمنية'),
# 2023 #11: two perpendicular roads, distance to a fixed station; options = sign x wrong side in the ratio
Q('m9q22', U3[5], 'medium',
  r"$l$ و $m$ طريقان مستقيمان متعامدان في النقطة $C$. تقع محطة شرطة على الطريق $m$ وتبعد $8\ \text{km}$ عن $C$. إذا تحرّكت سيارة على الطريق $l$ مبتعدةً عن $C$ بسرعة $60\ \text{km/h}$ ، فما معدّل تغيّر المسافة بين السيارة والمحطة عندما تكون السيارة على بُعد $6\ \text{km}$ من $C$ ؟",
  [O('36', 36, units='km/h'), O('-36', -36, units='km/h'), O('45', 45, units='km/h'), O('-45', -45, units='km/h')],
  r"$d^2=x^2+8^2 \Rightarrow 2d\dfrac{dd}{dt}=2x\dfrac{dx}{dt}$" "\n" r"عند $x=6$: $d=10$ ، $\dfrac{dd}{dt}=\dfrac{6}{10}(60)=36\ \text{km/h}$",
  truth=(diff(sqrt(s**2+64), s)*60).subs(s, 6), tag='معدلات مرتبطة: نظرية فيثاغورس'),
# ---------------- unit 4
# 2024 #23: power of a number given in a "minus" trig form; options = modulus power x sign of the angle
Q('m9q23', U4[2], 'medium',
  r"إذا كان: $z=2\cos\frac{\pi}{8}-2i\sin\frac{\pi}{8}$ ، فإنّ الصورة المثلثية للعدد $z^{4}$ هي:",
  [O(trig('16', r'-\frac{\pi}{2}'), pol(16, -P/2)), O(trig('16', r'\frac{\pi}{2}'), pol(16, P/2)),
   O(trig('8', r'-\frac{\pi}{2}'), pol(8, -P/2)), O(trig('8', r'\frac{\pi}{2}'), pol(8, P/2))],
  r"$z=2\left(\cos\left(-\frac{\pi}{8}\right)+i\sin\left(-\frac{\pi}{8}\right)\right)$" "\n" r"$z^4=2^4\left(\cos\left(-\frac{\pi}{2}\right)+i\sin\left(-\frac{\pi}{2}\right)\right)$ ، و $2^4=16$",
  truth=expand(pol(2, -pi/8)**4), tag='قوى العدد المركب', lead=NOTE_I(23, 30)),
# 2024 #21 + 2025 #22: shared stem (difference of squares; 1/z + w/5)
Q('m9q24', U4[2], 'medium',
  r"قيمة المقدار $z^{2}-w^{2}$ هي:",
  [O('-6-8i', -6-8*I), O('2-8i', 2-8*I), O('6+8i', 6+8*I), O('-2+8i', -2+8*I)],
  r"$z^2=1-4i+4i^2=-3-4i$ ، $w^2=4+4i+i^2=3+4i$" "\n" r"$z^2-w^2=-6-8i$",
  truth=expand((1-2*I)**2-(2+I)**2), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=1-2i$ ، $w=2+i$", 24, 25)),
# 2025 #22: second item of the shared stem (1/z + w/5); options = conjugate slips
Q('m9q25', U4[2], 'medium',
  r"ناتج $\dfrac{1}{z}+\dfrac{w}{5}$ هو:",
  [O(r'\frac{3}{5}+\frac{3}{5}i', R(3, 5)+R(3, 5)*I), O(r'\frac{3}{5}-\frac{1}{5}i', R(3, 5)-R(1, 5)*I), O(r'\frac{3}{5}+\frac{1}{5}i', R(3, 5)+R(1, 5)*I), O(r'\frac{3}{5}-\frac{3}{5}i', R(3, 5)-R(3, 5)*I)],
  r"$\dfrac1z=\dfrac{1}{1-2i}\cdot\dfrac{1+2i}{1+2i}=\dfrac{1+2i}{5}$" "\n" r"$\dfrac{1+2i}{5}+\dfrac{2+i}{5}=\dfrac{3+3i}{5}$",
  truth=1/(1-2*I)+(2+I)/5, tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2024s #21: modulus and an Arg range fix a constant
Q('m9q26', U4[1], 'medium',
  r"إذا كان: $z=2\sqrt{3}+ik$ ، حيث: $|z|=4$ ، و $-\frac{\pi}{2}<\text{Arg}(z)<0$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('-2', -2), O('2', 2), O('-4', -4), O('4', 4)],
  r"$12+k^2=16 \Rightarrow k=\pm2$" "\n" r"السعة بين $-\frac{\pi}{2}$ و $0$ تعني الربع الرابع، فالجزء التخيلي سالب: $k=-2$",
  truth=lambda: [r_ for r_ in solve(12+X**2-16, X) if r_ < 0][0], tag='إيجاد ثابت بمعلومية المقياس'),
# 2024s #20 / 2023 #19: equal complex numbers with a quadratic real part condition
Q('m9q27', U4[1], 'medium',
  r"قيمة $y$ الحقيقية التي تحقّق المعادلة: $2x+y+(x^{2}-4)i=5+5i$ ، حيث $x>0$ هي:",
  [O('-1', -1), O('1', 1), O('11', 11), O('-11', -11)],
  r"$x^2-4=5 \Rightarrow x=3$ (لأنّ $x>0$)" "\n" r"$2(3)+y=5 \Rightarrow y=-1$",
  truth=lambda: [5-2*r_ for r_ in solve(X**2-4-5, X) if r_ > 0][0], tag='تساوي عددين مركبين'),
# 2023 #22: quotient in trigonometric form; options = divide/multiply moduli x subtract/add arguments
Q('m9q28', U4[2], 'easy',
  r"إذا كان: $z_1=8\left(\cos\frac{5\pi}{6}+i\sin\frac{5\pi}{6}\right)$ ، $z_2=2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right)$ ، فإنّ $\dfrac{z_1}{z_2}$ هو:",
  [O(trig('4', r'\frac{7\pi}{12}'), pol(4, 7*P/12)), O(trig('4', r'\frac{13\pi}{12}'), pol(4, 13*P/12)),
   O(trig('16', r'\frac{7\pi}{12}'), pol(16, 7*P/12)), O(trig('16', r'\frac{13\pi}{12}'), pol(16, 13*P/12))],
  r"عند القسمة نقسم المقياسين ونطرح السعتين: $\frac82=4$ ، $\frac{5\pi}{6}-\frac{\pi}{4}=\frac{10\pi-3\pi}{12}=\frac{7\pi}{12}$",
  truth=expand(pol(8, 5*pi/6)/pol(2, pi/4)), tag='الضرب والقسمة بالصورة المثلثية'),
# 2025 #23: a square in the complex plane, rotation by i; options = rotation direction x wrong vertex
Q('m9q29', U4[2], 'hard',
  r"يظهر في المستوى المركّب الآتي مربّع رؤوسه الأعداد المركّبة $z_1,\ z_2,\ z_3,\ z_4$. إذا علمت أنّ: $z_2=-2+3i$ ، $z_3=1$ ، فإنّ $z_4$ هو:",
  [O('4+3i', 4+3*I), O('-2-3i', -2-3*I), O('1+6i', 1+6*I), O('3+3i', 3+3*I)],
  r"$\overrightarrow{z_3z_2}=z_2-z_3=-3+3i$ ، والضلع $\overrightarrow{z_3z_4}$ ناتج عن تدويره بزاوية $\frac{\pi}{2}$ مع عقارب الساعة (الضرب في $-i$)" "\n"
  r"$(-3+3i)(-i)=3i-3i^2=3+3i$ ، إذن $z_4=z_3+(3+3i)=4+3i$",
  truth=1+(-2+3*I-1)*(-I), figure=figure('m9q29', fig_square(), 3.0, 2.6), tag='تمثيل العمليات في المستوى المركب'),
# 2026 #25 family: disc cut by a perpendicular bisector; options = centre sign x which boundary is strict
IndexQ('m9q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثِّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z-2i|<2$ ، $|z|\le|z-2|$', R9),
   T(r'$|z-2i|\le2$ ، $|z|<|z-2|$', both(disk(2j, 2), closer(0, 2))),
   T(r'$|z+2i|<2$ ، $|z|\le|z-2|$', both(disk(-2j, 2, strict=True), nearer(0, 2))),
   T(r'$|z+2i|\le2$ ، $|z|<|z-2|$', both(disk(-2j, 2), closer(0, 2)))],
  r"الدائرة المتقطّعة مركزها $(0,2)$ ونصف قطرها $2$: $|z-2i|<2$" "\n"
  r"المستقيم المتصل $x=1$ هو العمود المنصّف للقطعة بين $0$ و $2$ ، والمنطقة في جهة الأصل: $|z|\le|z-2|$",
  truth=region_truth(R9, PR9, 5), figure=figure('m9q30', fig_region2(R9, PR9, 5), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]

# ================================================================== PAPER 10
F10, G10 = [(0, 2), (4, 4), (6, 1)], [(0, 1), (3, 4), (6, 1)]
C10 = -2 + 1j
R10 = disk(C10, 2)
PR10 = [('arc', C10, 2, False, (0.0, 2*math.pi))]
_cb = lambda e_: e_**R(1, 3)


def fig_isosceles():
    """isosceles triangle, equal sides 8 cm, vertex angle theta (m10q22)."""
    def draw(fig, ax):
        _sketch(fig, ax)
        th_ = math.pi/3
        A_, B_, C_ = (0, 0), (8, 0), (8*math.cos(th_), 8*math.sin(th_))
        ax.fill([A_[0], B_[0], C_[0]], [A_[1], B_[1], C_[1]], color='#dbe9f8')
        ax.plot([A_[0], B_[0], C_[0], A_[0]], [A_[1], B_[1], C_[1], A_[1]], color='#333333', lw=1.6)
        ax.add_patch(__import__('matplotlib.patches', fromlist=['Arc']).Arc(A_, 2.4, 2.4, theta1=0, theta2=60, color='#d04a1a', lw=1.2))
        ax.text(1.35, 0.45, r'$\theta$', fontsize=12, color='#d04a1a')
        ax.text(3.7, -0.75, r'$8\ \mathrm{cm}$', fontsize=10); ax.text(0.9, 3.7, r'$8\ \mathrm{cm}$', fontsize=10)
        ax.set_xlim(-0.8, 8.8); ax.set_ylim(-1.2, 7.6)
    return draw


P10 = [
# ---------------- unit 1
# 2026 #1: the other two roots are fractions/negatives; options = sign of each root
Q('m10q1', U1[1], 'medium',
  F(r"إذا كان $x=3$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ لها حلَّين آخرين هما:", (r'2x^{3}-3', 2*x**3-3), (r'3x^{2}+8x', 3*x**2+8*x)),
  [O(st(r'-\frac{1}{2}', '-1'), S_(-R(1, 2), -1), 'set'), O(st(r'\frac{1}{2}', '1'), S_(R(1, 2), 1), 'set'),
   O(st(r'\frac{1}{2}', '-1'), S_(R(1, 2), -1), 'set'), O(st(r'-\frac{1}{2}', '1'), S_(-R(1, 2), 1), 'set')],
  r"$2x^3-3x^2-8x-3=0$ ، وبالقسمة التركيبية على $(x-3)$: $2,\ -3,\ -8,\ -3 \to 2,\ 3,\ 1,\ 0$" "\n" r"$2x^2+3x+1=(2x+1)(x+1)=0 \Rightarrow x=-\frac12,\ x=-1$",
  truth=lambda: other_roots(2*x**3-3*x**2-8*x-3, 3), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# 2026 #2: repeated linear factor with a negative second constant; options = sign x constants swapped
Q('m10q2', U1[2], 'easy',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{5x+2}{(x+2)^{2}}', (5*x+2)/(x+2)**2)),
  [O(r'\frac{5}{x+2}-\frac{8}{(x+2)^{2}}', 5/(x+2)-8/(x+2)**2), O(r'\frac{5}{x+2}+\frac{8}{(x+2)^{2}}', 5/(x+2)+8/(x+2)**2),
   O(r'-\frac{8}{x+2}+\frac{5}{(x+2)^{2}}', -8/(x+2)+5/(x+2)**2), O(r'\frac{8}{x+2}+\frac{5}{(x+2)^{2}}', 8/(x+2)+5/(x+2)**2)],
  r"$5x+2=A(x+2)+B$: معامل $x$: $A=5$ ، وعند $x=-2$: $B=-8$",
  truth=(5*x+2)/(x+2)**2, tag='تجزئة: عامل خطي مكرر'),
# 2026 #3: equal remainders; options = sign x parity slip in f(-1)
Q('m10q3', U1[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x+1)$ مساويًا لباقي قسمته على $(x-3)$ ، فإنّ قيمة الثابت $p$ هي:", (r'x^{3}-2x^{2}+px+4', x**3-2*x**2+p*x+4)),
  [O('-3', -3), O('3', 3), O('-2', -2), O('2', 2)],
  r"$f(-1)=-1-2-p+4=1-p$ ، $f(3)=27-18+3p+4=13+3p$" "\n" r"$1-p=13+3p \Rightarrow -4p=12 \Rightarrow p=-3$",
  truth=lambda: solve(rem(x**3-2*x**2+p*x+4, -1)-rem(x**3-2*x**2+p*x+4, 3), p)[0], tag='نظرية الباقي وإيجاد ثابت'),
# factor theorem with (2x - 1) -> constant (2026 #3 family); options = the zero used
Q('m10q4', U1[1], 'medium',
  F(r"إذا كان $(2x-1)$ أحد عوامل الاقتران: $f(x)=«0»$ ، فإنّ قيمة الثابت $k$ هي:", (r'2x^{3}+kx^{2}-5x+2', 2*x**3+k*x**2-5*x+2)),
  [O('1', 1), O('-2', -2), O('-17', -17), O('-1', -1)],
  r"$(2x-1)$ عامل $\Leftrightarrow f\left(\frac12\right)=0$" "\n" r"$\frac14+\frac k4-\frac52+2=0 \Rightarrow \frac k4=\frac14 \Rightarrow k=1$",
  truth=lambda: solve(rem(2*x**3+k*x**2-5*x+2, R(1, 2)), k)[0], tag='نظرية العوامل وإيجاد ثابتين'),
# ---------------- unit 2
# 2026 #4 from tan theta in the 2nd quadrant, asking cos(theta/2); options = sign x sin/cos formula
Q('m10q5', U2[2], 'medium',
  r"إذا كان: $\tan\theta=-2\sqrt{2}$ ، $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\cos\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{1}{\sqrt{3}}', 1/sqrt(3)), O(r'-\frac{1}{\sqrt{3}}', -1/sqrt(3)), O(r'\frac{\sqrt{6}}{3}', sqrt(6)/3), O(r'-\frac{\sqrt{6}}{3}', -sqrt(6)/3)],
  r"$\sec^2\theta=1+8=9$ ، وفي الربع الثاني $\cos\theta=-\frac13$" "\n" r"$\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$: $\cos\frac{\theta}{2}=\sqrt{\dfrac{1-\frac13}{2}}=\sqrt{\dfrac13}=\dfrac{1}{\sqrt3}$",
  truth=cos((pi-atan(2*sqrt(2)))/2), tag='نصف الزاوية مع تحديد الربع'),
# 2026 #5: simplest form (difference of two cosines); options = coefficient x sin/cos
Q('m10q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x-\frac{\pi}{6})-\cos(x+\frac{\pi}{6})', cos(x-pi/6)-cos(x+pi/6))),
  [O(r'\sin x', sin(x)), O(r'\cos x', cos(x)), O(r'\sqrt{3}\sin x', sqrt(3)*sin(x)), O(r'\sqrt{3}\cos x', sqrt(3)*cos(x))],
  r"$\cos\left(x\mp\frac{\pi}{6}\right)=\frac{\sqrt3}{2}\cos x\pm\frac12\sin x$" "\n" r"بالطرح: $2\cdot\frac12\sin x=\sin x$",
  truth=cos(x-pi/6)-cos(x+pi/6), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #6: equivalent expression for tan + cot
Q('m10q7', U2[1], 'easy',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\tan x+\cot x', tan(x)+cot(x))),
  [O(r'\sec x\csc x', sec(x)*csc(x)), O(r'\sin x\cos x', sin(x)*cos(x)), O(r'\sec^{2}x', sec(x)**2), O(r'\csc^{2}x', csc(x)**2)],
  r"$\dfrac{\sin x}{\cos x}+\dfrac{\cos x}{\sin x}=\dfrac{\sin^2x+\cos^2x}{\sin x\cos x}=\dfrac{1}{\sin x\cos x}=\sec x\csc x$",
  truth=tan(x)+cot(x), tag='المتطابقات الأساسية'),
# product-to-sum exact value; options = sign x missing factor 2
Q('m10q8', U2[2], 'medium',
  r"قيمة المقدار: $2\sin\frac{5\pi}{12}\cos\frac{\pi}{12}$ هي:",
  [O(r'\frac{2+\sqrt{3}}{2}', (2+sqrt(3))/2), O(r'\frac{2-\sqrt{3}}{2}', (2-sqrt(3))/2), O(r'\frac{2+\sqrt{3}}{4}', (2+sqrt(3))/4), O(r'\frac{2-\sqrt{3}}{4}', (2-sqrt(3))/4)],
  r"$2\sin A\cos B=\sin(A+B)+\sin(A-B)$" "\n" r"$=\sin\frac{\pi}{2}+\sin\frac{\pi}{3}=1+\frac{\sqrt3}{2}=\frac{2+\sqrt3}{2}$",
  truth=2*sin(5*pi/12)*cos(pi/12), tag='تحويل الضرب إلى مجموع'),
# 2026 #7: quadratic in cos with one root rejected (|cos x| <= 1); options = sign x reference angle
Q('m10q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\cos^{2}x+3\cos x-2', 2*cos(x)**2+3*cos(x)-2)),
  [O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set'),
   O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set'), O(st(r'\frac{5\pi}{6}', r'\frac{7\pi}{6}'), S_(5*P/6, 7*P/6), 'set')],
  r"$(2\cos x-1)(\cos x+2)=0$ ، و $\cos x=-2$ مرفوض" "\n" r"$\cos x=\frac12$: الربعان الأول والرابع: $x=\frac{\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*cos(x)**2+3*cos(x)-2, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
# 2026 #8 family: tan 2x = 1 in [0, pi); options = halved or not x second solution
Q('m10q10', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,\pi)$ هي:", (r'\sin 2x-\cos 2x', sin(2*x)-cos(2*x))),
  [O(st(r'\frac{\pi}{8}', r'\frac{5\pi}{8}'), S_(P/8, 5*P/8), 'set'), O(st(r'\frac{\pi}{4}', r'\frac{5\pi}{4}'), S_(P/4, 5*P/4), 'set'),
   O(st(r'\frac{\pi}{8}'), S_(P/8), 'set'), O(st(r'\frac{\pi}{4}'), S_(P/4), 'set')],
  r"$\tan2x=1$ ، و $0\le2x<2\pi$: $2x=\frac{\pi}{4},\ \frac{5\pi}{4}$" "\n" r"$x=\frac{\pi}{8},\ \frac{5\pi}{8}$",
  truth=lambda: sols(sin(2*x)-cos(2*x), 0, pi), tag='معادلة بزاوية مضاعفة في فترة'),
# ---------------- unit 3
# 2024 #2: trig with a shifted angle plus a polynomial over pi; options = sign of sin(-pi/2) x sign of the result
Q('m10q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{2}\right)$ هي:", (r'3\cos(x-\pi)+\frac{x^{2}}{2\pi}', 3*cos(x-pi)+x**2/(2*pi))),
  [O(r'\frac{7}{2}', R(7, 2)), O(r'-\frac{5}{2}', -R(5, 2)), O(r'\frac{5}{2}', R(5, 2)), O(r'-\frac{7}{2}', -R(7, 2))],
  r"$f'(x)=-3\sin(x-\pi)+\dfrac{x}{\pi}$" "\n" r"$f'\left(\frac{\pi}{2}\right)=-3\sin\left(-\frac{\pi}{2}\right)+\frac12=3+\frac12=\frac72$",
  truth=Dx(3*cos(x-pi)+x**2/(2*pi)).subs(x, pi/2), tag='مشتقات الاقترانات المثلثية'),
# 2024s #10 / 2024 #7: a^(linear), f'(a) given -> a
Q('m10q12', U3[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(a)=6\ln 3$ ، فإنّ قيمة الثابت $a$ هي:", (r'3^{2x-1}', 3**(2*x-1))),
  [O('1', 1), O('0', 0), O('2', 2), O('-1', -1)],
  r"$f'(x)=3^{2x-1}\ln3\cdot2$" "\n" r"$2\ln3\cdot3^{2a-1}=6\ln3 \Rightarrow 3^{2a-1}=3 \Rightarrow 2a-1=1 \Rightarrow a=1$",
  truth=lambda: [r_ for r_ in solve(Dx(3**(2*x-1)).subs(x, X)-6*log(3), X) if r_.is_real][0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2024 #3: velocity when the particle returns to its starting position
Q('m10q13', U3[1], 'medium',
  F(r"يُمثّل الاقتران: $s(t)=«0»$ ، $t\ge0$ موقع جسم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار، و $t$ الزمن بالثواني، فإنّ سرعة الجسم المتجهة في اللحظة التي يعود فيها إلى موقعه الابتدائي هي:", (r't^{3}-6t^{2}+5', t**3-6*t**2+5)),
  [O('36', 36, units='m/s'), O('0', 0, units='m/s'), O('-12', -12, units='m/s'), O('-36', -36, units='m/s')],
  r"$s(0)=5$ ، و $t^3-6t^2+5=5 \Rightarrow t^2(t-6)=0 \Rightarrow t=6$ (بعد الانطلاق)" "\n" r"$v(t)=3t^2-12t \Rightarrow v(6)=108-72=36\ \text{m/s}$",
  truth=diff(t**3-6*t**2+5, t).subs(t, [r_ for r_ in solve(t**3-6*t**2, t) if r_ > 0][0]), tag='الحركة: السرعة والتسارع'),
# 2024 #5: second derivative of sec x plus a constant; options = one product-rule term missing x constant differentiated
Q('m10q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''\left(\frac{\pi}{3}\right)$ هي:", (r'\sec x-\pi^{2}', sec(x)-pi**2)),
  [O('14', 14), O('6', 6), O('8', 8), O(r'14-2\pi', 14-2*pi)],
  r"$f'(x)=\sec x\tan x$ ، $f''(x)=\sec x\tan^2x+\sec^3x$" "\n" r"$f''\left(\frac{\pi}{3}\right)=2(3)+8=14$",
  truth=diff(sec(x)-pi**2, x, 2).subs(x, pi/3), tag='المشتقات العليا'),
# 2025s #12: particle moving on a curve, dx/dt given -> dy/dt; options = sign x missing inner derivative
Q('m10q15', U3[5], 'medium',
  F(r"يتحرّك جُسيم على منحنى الاقتران: $f(x)=«0»$ ، $x\ge0$. إذا كان معدّل تغيّر الإحداثي $x$ هو $3\ \text{cm/s}$ ، فإنّ معدّل تغيّر الإحداثي $y$ عندما $x=4\ \text{cm}$ هو:", (r'\frac{12}{1+\sqrt{x}}', 12/(1+sqrt(x)))),
  [O('-1', -1, units='cm/s'), O('1', 1, units='cm/s'), O('-4', -4, units='cm/s'), O('4', 4, units='cm/s')],
  r"$\dfrac{dy}{dx}=-\dfrac{12}{(1+\sqrt x)^2}\cdot\dfrac{1}{2\sqrt x}$ ، وعند $x=4$: $-\dfrac{12}{9}\cdot\dfrac14=-\dfrac13$" "\n" r"$\dfrac{dy}{dt}=\dfrac{dy}{dx}\cdot\dfrac{dx}{dt}=-\dfrac13(3)=-1\ \text{cm/s}$",
  truth=(Dx(12/(1+sqrt(x)))*3).subs(x, 4), tag='معدلات مرتبطة: جسيم على منحنى'),
# 2025 #3: two graphs, u = f + c/g; options = sign x squared denominator
Q('m10q16', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $u(x)=f(x)+\dfrac{4}{g(x)}$ ، فإنّ $u'(2)$ هي:",
  [O(r'\frac{1}{18}', R(1, 18)), O(r'\frac{17}{18}', R(17, 18)), O(r'-\frac{5}{6}', -R(5, 6)), O(r'\frac{11}{6}', R(11, 6))],
  r"من الشكل: $f'(2)=\frac12$ ، $g(2)=3$ ، $g'(2)=1$" "\n" r"$u'(x)=f'(x)-\dfrac{4g'(x)}{(g(x))^2} \Rightarrow u'(2)=\frac12-\frac49=\frac{1}{18}$",
  truth=lambda: (lambda fv, fs, gv, gs: fs(2)-4*gs(2)/gv(2)**2)(*pw(F10), *pw(G10)),
  figure=figure('m10q16', draw_two(F10, G10, 6, 5, (4.4, 4.2), (1.0, 3.4))), tag='المشتقة من التمثيل البياني'),
# 2023 #1: exponential of a root; options = coefficient 2/3 vs 3/2 x root in the denominator or numerator
Q('m10q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، $x\ne0$ ، فإنّ $f'(x)$ هي:", (r'e^{\sqrt[3]{x^{2}}}', exp(_cb(x**2)))),
  [O(r'\frac{2}{3\sqrt[3]{x}}e^{\sqrt[3]{x^{2}}}', 2/(3*_cb(x))*exp(_cb(x**2))), O(r'\frac{3}{2\sqrt[3]{x}}e^{\sqrt[3]{x^{2}}}', 3/(2*_cb(x))*exp(_cb(x**2))),
   O(r'\frac{2\sqrt[3]{x}}{3}e^{\sqrt[3]{x^{2}}}', 2*_cb(x)/3*exp(_cb(x**2))), O(r'\frac{3\sqrt[3]{x}}{2}e^{\sqrt[3]{x^{2}}}', 3*_cb(x)/2*exp(_cb(x**2)))],
  r"$\left(x^{\frac23}\right)'=\frac23x^{-\frac13}=\dfrac{2}{3\sqrt[3]{x}}$" "\n" r"$f'(x)=e^{\sqrt[3]{x^2}}\cdot\dfrac{2}{3\sqrt[3]{x}}$",
  truth=Dx(exp(_cb(x**2))), tag='مشتقة الاقتران الأسي'),
# 2026r #7: trig of a power of x (chain rule); options = inner derivative kept x sign of cos
Q('m10q18', U3[3], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ هي:", (r'3x+\sin(\pi x^{2})', 3*x+sin(pi*x**2))),
  [O(r'3+2\pi x\cos(\pi x^{2})', 3+2*pi*x*cos(pi*x**2)), O(r'3-2\pi x\cos(\pi x^{2})', 3-2*pi*x*cos(pi*x**2)),
   O(r'3+\pi\cos(\pi x^{2})', 3+pi*cos(pi*x**2)), O(r'3-\pi\cos(\pi x^{2})', 3-pi*cos(pi*x**2))],
  r"$\left(\sin u\right)'=\cos u\cdot u'$ ، $u=\pi x^2 \Rightarrow u'=2\pi x$" "\n" r"$f'(x)=3+2\pi x\cos(\pi x^2)$",
  truth=Dx(3*x+sin(pi*x**2)), tag='قاعدة السلسلة مع الاقترانات المثلثية'),
# 2026 #15: parametric with exponentials at t = ln 2; options = reciprocal x missing chain factor 2
Q('m10q19', U3[3], 'medium',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\ln 2$ هو:", (r'e^{2t}', exp(2*t)), (r'e^{t}-t', exp(t)-t)),
  [O(r'\frac{1}{8}', R(1, 8)), O('8', 8), O(r'\frac{1}{4}', R(1, 4)), O('4', 4)],
  r"$\dfrac{dy}{dt}=e^t-1=2-1=1$ ، $\dfrac{dx}{dt}=2e^{2t}=2(4)=8$" "\n" r"$\dfrac{dy}{dx}=\dfrac18$",
  truth=(diff(exp(t)-t, t)/diff(exp(2*t), t)).subs(t, log(2)), tag='مشتقة المعادلات الوسيطية'),
# 2026 #16: x e^y + y = 2x - 1, point from y = 0; options = unit fractions / slips
Q('m10q20', U3[4], 'medium',
  F(r"إذا كان: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $y=0$ هو:", (r'xe^{y}+y', x*exp(y)+y), (r'2x-1', 2*x-1)),
  [O(r'\frac{1}{2}', R(1, 2)), O('1', 1), O(r'\frac{1}{3}', R(1, 3)), O('2', 2)],
  r"عندما $y=0$: $x+0=2x-1 \Rightarrow x=1$" "\n" r"$e^y+xe^y\dfrac{dy}{dx}+\dfrac{dy}{dx}=2$ ، وعند $(1,0)$: $1+2\dfrac{dy}{dx}=2 \Rightarrow \dfrac{dy}{dx}=\dfrac12$",
  truth=imp(x*exp(y)+y-2*x+1, (1, 0)), tag='الاشتقاق الضمني عند نقطة'),
# 2023 #10: d/dx (ln y) for a variable base and exponent; options = cot vs tan x sign
Q('m10q21', U3[4], 'medium',
  F(r"إذا كان: $y=«0»$ ، $0<x<\pi$ ، فإنّ $\dfrac{d}{dx}(\ln y)$ هي:", (r'(\sin x)^{x}', sin(x)**x)),
  [O(r'\ln(\sin x)+x\cot x', log(sin(x))+x*cot(x)), O(r'\ln(\sin x)-x\cot x', log(sin(x))-x*cot(x)),
   O(r'\ln(\sin x)+x\tan x', log(sin(x))+x*tan(x)), O(r'\ln(\sin x)-x\tan x', log(sin(x))-x*tan(x))],
  r"$\ln y=x\ln(\sin x)$" "\n" r"$\dfrac{d}{dx}(\ln y)=\ln(\sin x)+x\cdot\dfrac{\cos x}{\sin x}=\ln(\sin x)+x\cot x$",
  truth=Dx(x*log(sin(x))), tag='الاشتقاق اللوغاريتمي'),
# 2023 #12: isosceles triangle, angle rate -> area rate (with a figure); options = cos vs sin x factor 1/2
Q('m10q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي مثلّثًا متطابق الضلعين، طول كلٍّ من ضلعيه المتطابقين $8\ \text{cm}$ ، وقياس الزاوية بينهما $\theta$. إذا تغيّرت $\theta$ بمعدّل $\frac{\pi}{90}\ \text{rad/min}$ ، فإنّ معدّل تغيّر مساحة المثلث عندما $\theta=\frac{\pi}{6}$ هو:",
  [O(r'\frac{8\sqrt{3}\pi}{45}', 8*sqrt(3)*pi/45, units='cm^2/min'), O(r'\frac{8\pi}{45}', 8*pi/45, units='cm^2/min'),
   O(r'\frac{16\sqrt{3}\pi}{45}', 16*sqrt(3)*pi/45, units='cm^2/min'), O(r'\frac{16\pi}{45}', 16*pi/45, units='cm^2/min')],
  r"$A=\frac12(8)(8)\sin\theta=32\sin\theta \Rightarrow \dfrac{dA}{dt}=32\cos\theta\dfrac{d\theta}{dt}$" "\n" r"$\dfrac{dA}{dt}=32\cdot\dfrac{\sqrt3}{2}\cdot\dfrac{\pi}{90}=\dfrac{16\sqrt3\pi}{90}=\dfrac{8\sqrt3\pi}{45}$",
  truth=(diff(32*sin(s), s)*pi/90).subs(s, pi/6), figure=figure('m10q22', fig_isosceles(), 3.0, 2.6), tag='معدلات مرتبطة: معدل تغير زاوية'),
# ---------------- unit 4
# 2025s #20: modulus and Arg of the conjugate -> standard form; options = sign of the imaginary part x cos/sin swapped
Q('m10q23', U4[1], 'medium',
  r"إذا كان $z$ عددًا مركّبًا، وكان: $|z|=6$ ، $\text{Arg}(\bar{z})=-\frac{\pi}{6}$ ، فإنّ الصورة القياسية للعدد المركّب $z$ هي:",
  [O(r'3\sqrt{3}+3i', 3*sqrt(3)+3*I), O(r'3\sqrt{3}-3i', 3*sqrt(3)-3*I), O(r'3+3\sqrt{3}i', 3+3*sqrt(3)*I), O(r'3-3\sqrt{3}i', 3-3*sqrt(3)*I)],
  r"$\text{Arg}(z)=-\text{Arg}(\bar z)=\frac{\pi}{6}$" "\n" r"$z=6\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right)=6\left(\frac{\sqrt3}{2}+\frac12i\right)=3\sqrt3+3i$",
  truth=conjugate(pol(6, -pi/6)), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2025s #18-19: shared stem (quotient by a pure imaginary; modulus of a square)
Q('m10q24', U4[2], 'easy',
  r"ناتج $\dfrac{z}{w}$ بالصورة القياسية هو:",
  [O('-3+i', -3+I), O('3-i', 3-I), O('-3-i', -3-I), O('3+i', 3+I)],
  r"$\dfrac{2+6i}{-2i}\cdot\dfrac{i}{i}=\dfrac{2i+6i^2}{-2i^2}=\dfrac{-6+2i}{2}=-3+i$",
  truth=(2+6*I)/(-2*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=2+6i$ ، $w=-2i$", 24, 25)),
# 2025s #18: second item of the shared stem (|z^2|); options = |z|, a part of z^2, |z|^4
Q('m10q25', U4[1], 'easy',
  r"قيمة $|z^{2}|$ هي:",
  [O('40', 40), O(r'2\sqrt{10}', 2*sqrt(10)), O('32', 32), O('1600', 1600)],
  r"$|z^2|=|z|^2=2^2+6^2=40$",
  truth=Abs(expand((2+6*I)**2)), tag='المقياس والعمليات (نص مشترك)'),
# 2024 #18 / 2023 #18: power of i times a root of a negative number; options = sign x real/imaginary
Q('m10q26', U4[1], 'easy',
  r"قيمة $\left(i^{35}\times\sqrt{-18}\right)$ في أبسط صورة هي:",
  [O(r'3\sqrt{2}', 3*sqrt(2)), O(r'-3\sqrt{2}', -3*sqrt(2)), O(r'3\sqrt{2}i', 3*sqrt(2)*I), O(r'-3\sqrt{2}i', -3*sqrt(2)*I)],
  r"$i^{35}=i^{32}\cdot i^3=-i$ ، $\sqrt{-18}=3\sqrt2\,i$" "\n" r"$(-i)(3\sqrt2\,i)=-3\sqrt2\,i^2=3\sqrt2$",
  truth=expand(I**35*sqrt(-18)), tag='قوى i'),
# 2024s #24: cube of a complex number; options = i^2 and i^3 slips
Q('m10q27', U4[2], 'medium',
  r"ناتج $(1+2i)^{3}$ هو:",
  [O('-11-2i', -11-2*I), O('13+14i', 13+14*I), O('-11+14i', -11+14*I), O('13-2i', 13-2*I)],
  r"$(1+2i)^2=1+4i+4i^2=-3+4i$" "\n" r"$(-3+4i)(1+2i)=-3-6i+4i+8i^2=-11-2i$",
  truth=expand((1+2*I)**3), tag='قوى العدد المركب'),
# 2023 #20: modulus fixes a constant inside a fraction; options = small values
Q('m10q28', U4[1], 'medium',
  r"إذا كان: $z=\dfrac{4}{k}+\sqrt{5}\,i$ ، $k>0$ ، وكان: $|z|=3$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('2', 2), O('4', 4), O('1', 1), O(r'\frac{1}{2}', R(1, 2))],
  r"$\dfrac{16}{k^2}+5=9 \Rightarrow \dfrac{16}{k^2}=4 \Rightarrow k^2=4 \Rightarrow k=2$",
  truth=lambda: [r_ for r_ in solve(16/X**2+5-9, X) if r_ > 0][0], tag='إيجاد ثابت بمعلومية المقياس'),
# 2024s #19: conjugate read from a point in the complex plane; options = which signs change
Q('m10q29', U4[1], 'easy',
  r"معتمدًا المستوى المركّب الآتي الذي يُبيّن العدد المركّب $z$ ، فإنّ مرافق $z$ هو:",
  [O(r'\bar{z}=-2+i', -2+I, 'eq'), O(r'\bar{z}=2-i', 2-I, 'eq'), O(r'\bar{z}=2+i', 2+I, 'eq'), O(r'\bar{z}=-2-i', -2-I, 'eq')],
  r"من الشكل: $z=-2-i$" "\n" r"المرافق يغيّر إشارة الجزء التخيلي فقط: $\bar z=-2+i$",
  truth=conjugate(-2-I), figure=figure('m10q29', fig_point(-2, -1, r'$-2$', r'$-1$', 'z', 4), 3.0, 3.0), tag='المرافق من التمثيل البياني'),
# 2024s #25: a disc read from the figure; options = centre coordinates swapped x signs
IndexQ('m10q30', U4[3], 'easy',
  r"المتباينة (بدلالة $z$) التي تُمثِّل المحل الهندسي المُمثَّل بيانيًّا في الشكل الآتي هي:",
  [T(r'$|z+2-i|\le2$', R10), T(r'$|z-2+i|\le2$', disk(2 - 1j, 2)), T(r'$|z+1-2i|\le2$', disk(-1 + 2j, 2)), T(r'$|z-1+2i|\le2$', disk(1 - 2j, 2))],
  r"المركز $(-2,1)$ أي $-2+i$ ، ونصف القطر $2$ ، والدائرة متصلة والداخل مظلّل" "\n" r"$|z-(-2+i)|\le2 \Rightarrow |z+2-i|\le2$",
  truth=region_truth(R10, PR10, 5), figure=figure('m10q30', fig_region2(R10, PR10, 5, marks=[(C10, '')]), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]
