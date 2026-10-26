"""Unit-5 exams 5-10 (imported by u5.py). Every item is a sibling of the official item named in the comment above
it (2026 = the 2008-generation paper, items 26-37; 2026r = 2026 repeaters paper 2; 2023-2025 = paper 2, items 1-13).
Each exam follows the 2026 order: special integrals and motion, substitution, partial fractions, parts,
areas and volumes, differential equations."""
from qb import *
from u5_helpers import *
import numpy as np

L = {i: f'u5-l{i}' for i in range(1, 7)}
ap = Symbol('a', positive=True)


def num(expr):
    """numerical value of a definite integral (used for integrands with |...| or roots of negatives)"""
    return expr.evalf(40)


def ode_t_ok(Nt, rhs, t0, n0):
    """explicit solution N(t) of N' = rhs(t) with N(t0) = n0"""
    return same(diff(Nt, t) - rhs, 0) and same(Nt.subs(t, t0), n0)


def shaded(f_, lo, hi, xlim, ylim, ticks, label):
    """shaded area under f from lo to hi; only the x ticks given as {value: label} are shown (no y values,
    so the figure does not give the answer away)"""
    def draw(fig, ax):
        axes_style(ax, xlim, ylim, grid=False)
        xs = np.linspace(xlim[0], xlim[1], 400)
        ff = lambdify(x, f_, 'numpy')
        with np.errstate(all='ignore'):
            ys = ff(xs) + 0*xs
            ys[ys > ylim[1] + 1] = np.nan
            ax.plot(xs, ys, color='#1f5fbf', lw=1.8)
            xr = np.linspace(float(lo), float(hi), 200)
            ax.fill_between(xr, ff(xr) + 0*xr, 0*xr, color='#9cc3ef', alpha=0.85)
        ax.plot([float(hi)] * 2, [0, float(f_.subs(x, hi))], color='#444', lw=1)
        ax.set_xticks([float(v_) for v_ in ticks]); ax.set_xticklabels(list(ticks.values()))
        ax.set_yticks([])
        ax.text(*label, color='#1f5fbf')
    return draw


# ============================================================== Exam 5
E5 = [
# 2026 #26: integral of cot(x/2); options = ln|sin| vs -ln|cos| x coefficient 2 vs 1/2
Q('u5e5q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cot\frac{x}{4}', cot(x/4))),
  [A(r'4\ln|\sin\frac{x}{4}|+C', 4*log(sin(x/4))), A(r'-4\ln|\cos\frac{x}{4}|+C', -4*log(cos(x/4))),
   A(r'\frac{1}{4}\ln|\sin\frac{x}{4}|+C', log(sin(x/4))/4), A(r'-\frac{1}{4}\ln|\cos\frac{x}{4}|+C', -log(cos(x/4))/4)],
  r"$\displaystyle\int\cot\frac x4\,dx=\int\frac{\cos\frac x4}{\sin\frac x4}dx=4\ln\left|\sin\frac x4\right|+C$",
  truth=cot(x/4)),
# 2026 #27: a^(linear) divided by ln a; options = exponent (extra 1/2 or not) x ln a vs (ln a)^2
Q('u5e5q2', L[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2^{2x+3}}{\ln 4}', 2**(2*x+3)/log(4))),
  [A(r'\frac{2^{2x+3}}{(\ln 4)^{2}}+C', 2**(2*x+3)/log(4)**2), A(r'\frac{2^{2x+3}}{\ln 4}+C', 2**(2*x+3)/log(4)),
   A(r'\frac{2^{2x+2}}{(\ln 4)^{2}}+C', 2**(2*x+2)/log(4)**2), A(r'\frac{2^{2x+2}}{\ln 4}+C', 2**(2*x+2)/log(4))],
  r"$\displaystyle\int2^{2x+3}dx=\frac{2^{2x+3}}{2\ln2}=\frac{2^{2x+3}}{\ln4}$ ، ثم نقسم على $\ln4$ الموجود في المقام: $\dfrac{2^{2x+3}}{(\ln4)^2}+C$",
  truth=2**(2*x+3)/log(4)),
# 2026 #28: integral of sin^2 over an interval = a pi; options = +-1/2, +-1/4 (power reduction, missing 1/2)
Q('u5e5q3', L[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{0}^{\pi/4}«0»\,dx=a\pi$ ، فإنّ قيمة الثابت $a$ هي:", (r'\sin^{2}2x', sin(2*x)**2)),
  [O(r'\frac{1}{8}', R(1, 8)), O(r'-\frac{1}{8}', -R(1, 8)), O(r'\frac{1}{4}', R(1, 4)), O(r'-\frac{1}{4}', -R(1, 4))],
  r"$\sin^22x=\dfrac{1-\cos4x}{2}$ ، و $\displaystyle\int_0^{\pi/4}\frac{1-\cos4x}{2}dx=\left[\frac x2-\frac{\sin4x}{8}\right]_0^{\pi/4}=\frac{\pi}{8}$ ، إذن $a=\frac18$",
  truth=ig(sin(2*x)**2, (x, 0, pi/4))/pi),
# 2026 #29: dy/dx = e^(kx) - e^(-x), curve through (0, c); options = sign of the e^(-x) term x sign of the constant
IndexQ('u5e5q4', L[1], 'medium',
  F(r"يُمثّل الاقتران: $\dfrac{dy}{dx}=«0»$ ميل المماس لمنحنى الاقتران $y$. إذا كان منحنى $y$ يمرّ بالنقطة $(0,\,1)$ ، فإنّ قاعدة الاقتران $y$ هي:", (r'e^{x}+4e^{-2x}', exp(x)+4*exp(-2*x))),
  [O(r'y=e^{x}-2e^{-2x}+2', exp(x)-2*exp(-2*x)+2, 'eq'), O(r'y=e^{x}-2e^{-2x}-2', exp(x)-2*exp(-2*x)-2, 'eq'),
   O(r'y=e^{x}+2e^{-2x}-2', exp(x)+2*exp(-2*x)-2, 'eq'), O(r'y=e^{x}+2e^{-2x}+2', exp(x)+2*exp(-2*x)+2, 'eq')],
  r"$y=\displaystyle\int(e^x+4e^{-2x})dx=e^x-2e^{-2x}+C$ ، و $y(0)=1 \Rightarrow 1-2+C=1 \Rightarrow C=2$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, exp(x)+4*exp(-2*x), 0, 1))),
# 2026 #30: v = k sin(t), total distance over several arches; options = distance, displacement, arch-count and chain slips
Q('u5e5q5', L[1], 'hard',
  F(r"إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: $v(t)=«0»$ ، حيث $v$ سرعته بالمتر لكل ثانية، و $t$ الزمن بالثواني، فإنّ المسافة الكلية بالأمتار التي قطعها الجُسيم في الفترة $[0,\,\pi]$ هي:", (r'6\sin 3t', 6*sin(3*t))),
  [O('12', 12), O('4', 4), O('8', 8), O('36', 36)],
  r"$v=0$ عند $t=\frac{\pi}{3},\ \frac{2\pi}{3}$ ، وعلى كل فترة من الفترات الثلاث $\left|\displaystyle\int6\sin3t\,dt\right|=\left|\big[-2\cos3t\big]\right|=4$" "\n"
  r"المسافة $=4+4+4=12\ \text{m}$",
  truth=sum(Abs(ig(6*sin(3*t), (t, j*pi/3, (j+1)*pi/3))) for j in range(3))),
# 2026 #31: x^n (1 + c/x)^n simplifies to (x + c)^n; options = (x+c)^(n+1)/(n+1), (x+c)^n/n, term-by-term slips
Q('u5e5q6', L[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'x^{4}\left(1-\frac{2}{x}\right)^{4}', x**4*(1-2/x)**4)),
  [A(r'\frac{1}{5}(x-2)^{5}+C', (x-2)**5/5), A(r'\frac{1}{4}(x-2)^{4}+C', (x-2)**4/4),
   A(r'\frac{1}{5}x^{5}-\frac{1}{2}x^{4}+C', x**5/5-x**4/2), A(r'\frac{1}{5}x^{5}+\frac{1}{2}x^{4}+C', x**5/5+x**4/2)],
  r"$x^4\left(1-\frac2x\right)^4=\left(x\left(1-\frac2x\right)\right)^4=(x-2)^4$ ، إذن التكامل $=\frac15(x-2)^5+C$",
  truth=x**4*(1-2/x)**4),
# 2026 #32: sin^2(kx)/cos^4(kx) = tan^2 sec^2; options = sign x cot vs csc (the cot/csc version)
Q('u5e5q7', L[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\cos^{2}2x}{\sin^{4}2x}', cos(2*x)**2/sin(2*x)**4)),
  [A(r'-\frac{1}{6}\cot^{3}2x+C', -cot(2*x)**3/6), A(r'\frac{1}{6}\cot^{3}2x+C', cot(2*x)**3/6),
   A(r'-\frac{1}{6}\csc^{3}2x+C', -csc(2*x)**3/6), A(r'\frac{1}{6}\csc^{3}2x+C', csc(2*x)**3/6)],
  r"$\dfrac{\cos^22x}{\sin^42x}=\cot^22x\csc^22x$ ، وبالتعويض $u=\cot2x \Rightarrow du=-2\csc^22x\,dx$:" "\n"
  r"$\displaystyle-\frac12\int u^2du=-\frac{u^3}{6}+C=-\frac16\cot^32x+C$",
  truth=cos(2*x)**2/sin(2*x)**4),
# 2026 #33: (x^2 + a)/(x^3 + bx) = A/x + Bx/(x^2 + b); options = sign of A x the 1/2 from the ln(x^2 + b) term
Q('u5e5q8', L[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{2}-4}{x^{3}+2x}', (x**2-4)/(x**3+2*x))),
  [A(r'-2\ln|x|+\frac{3}{2}\ln(x^{2}+2)+C', -2*log(x)+R(3, 2)*log(x**2+2)), A(r'2\ln|x|-\frac{3}{2}\ln(x^{2}+2)+C', 2*log(x)-R(3, 2)*log(x**2+2)),
   A(r'-2\ln|x|+3\ln(x^{2}+2)+C', -2*log(x)+3*log(x**2+2)), A(r'2\ln|x|-3\ln(x^{2}+2)+C', 2*log(x)-3*log(x**2+2))],
  r"$\dfrac{x^2-4}{x(x^2+2)}=\dfrac{A}{x}+\dfrac{Bx}{x^2+2}$ ، عند $x=0$: $-4=2A \Rightarrow A=-2$ ، ومعامل $x^2$: $1=A+B \Rightarrow B=3$" "\n"
  r"$\displaystyle\int\left(-\frac2x+\frac{3x}{x^2+2}\right)dx=-2\ln|x|+\frac32\ln(x^2+2)+C$",
  truth=(x**2-4)/(x**3+2*x)),
# 2026 #34: sec^2(sqrt x) by substitution then parts; options = signs of the two terms (csc^2 version)
Q('u5e5q9', L[4], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\csc^{2}\sqrt{x}', csc(sqrt(x))**2)),
  [A(r'-2\sqrt{x}\cot\sqrt{x}+2\ln|\sin\sqrt{x}|+C', -2*sqrt(x)*cot(sqrt(x))+2*log(sin(sqrt(x)))),
   A(r'2\sqrt{x}\cot\sqrt{x}+2\ln|\sin\sqrt{x}|+C', 2*sqrt(x)*cot(sqrt(x))+2*log(sin(sqrt(x)))),
   A(r'-2\sqrt{x}\cot\sqrt{x}-2\ln|\sin\sqrt{x}|+C', -2*sqrt(x)*cot(sqrt(x))-2*log(sin(sqrt(x)))),
   A(r'2\sqrt{x}\cot\sqrt{x}-2\ln|\sin\sqrt{x}|+C', 2*sqrt(x)*cot(sqrt(x))-2*log(sin(sqrt(x))))],
  r"$u=\sqrt x \Rightarrow x=u^2$ ، $dx=2u\,du$: $\displaystyle\int2u\csc^2u\,du$ ، وبالأجزاء: $2\left(-u\cot u+\int\cot u\,du\right)$" "\n"
  r"$=-2\sqrt x\cot\sqrt x+2\ln|\sin\sqrt x|+C$",
  truth=csc(sqrt(x))**2),
# 2024s #8 / 2026 #35: shaded area under k/(x + c) equals a logarithm -> k; options = ratio of logs vs of numbers x inverted
Q('u5e5q10', L[5], 'easy',
  F(r"يُبيّن الشكل الآتي منحنى الاقتران: $f(x)=«0»$ ، حيث $k>0$. إذا كانت مساحة المنطقة المُظلَّلة تساوي $\ln 27$ وحدة مربعة، فإنّ قيمة الثابت $k$ هي:", (r'\frac{k}{x+1}', k/(x+1))),
  [O(r'\frac{3}{2}', R(3, 2)), O(r'\frac{2}{3}', R(2, 3)), O('3', 3), O(r'\frac{1}{3}', R(1, 3))],
  r"$\displaystyle\int_0^8\frac{k}{x+1}dx=k\big[\ln(x+1)\big]_0^8=k\ln9$ ، و $k\ln9=\ln27 \Rightarrow k=\dfrac{3\ln3}{2\ln3}=\dfrac32$",
  truth=lambda: solve(ig(k/(x+1), (x, 0, 8)) - log(27), k)[0],
  figure=figure('u5e5q10', shaded(R(3, 2)/(x+1), 0, 8, (-0.8, 10), (-0.3, 2.0), {0: '$0$', 8: '$8$'}, (1.6, 1.0, r'$f(x)=\frac{k}{x+1}$')), 3.8, 2.8)),
# 2026 #36: volume of the region under a root of (x times exponential); options = sign of 1 x the parts sign slip
Q('u5e5q11', L[5], 'hard',
  F(r"اعتمادًا على التمثيل البياني الآتي الذي يُبيّن منحنى الاقتران: $f(x)=«0»$ ، والمستقيم $x=2$ ، فإنّ حجم المُجسَّم الناتج من دوران المنطقة المُظلَّلة حول المحور $x$ بالوحدات المكعبة هو:", (r'\sqrt{x}\,e^{x}', sqrt(x)*exp(x))),
  [O(r'\frac{\pi(3e^{4}+1)}{4}', pi*(3*E**4+1)/4), O(r'\frac{\pi(3e^{4}-1)}{4}', pi*(3*E**4-1)/4),
   O(r'\frac{\pi(5e^{4}-1)}{4}', pi*(5*E**4-1)/4), O(r'\frac{\pi(5e^{4}+1)}{4}', pi*(5*E**4+1)/4)],
  r"$V=\pi\displaystyle\int_0^2xe^{2x}dx$ ، وبالأجزاء: $\displaystyle\int xe^{2x}dx=\left(\frac x2-\frac14\right)e^{2x}$" "\n"
  r"$V=\pi\left[\left(\frac34\right)e^4-\left(-\frac14\right)\right]=\dfrac{\pi(3e^4+1)}{4}$",
  truth=pi*ig(x*exp(2*x), (x, 0, 2)),
  figure=figure('u5e5q11', region(sqrt(x)*exp(x), 0*x, 0, 2, (-0.4, 2.7), (-1.2, 12), [(1.05, 9.5, r'$f(x)$', '#1f5fbf')]), 3.4, 2.9)),
# 2026 #37: dy/dx = 1/(trig^2 x . trig^2 y); options = 1/2 vs 1/4 sin 2y x its sign
IndexQ('u5e5q12', L[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ هو:", (r'\frac{1}{\cos^{2}x\sin^{2}y}', 1/(cos(x)**2*sin(y)**2))),
  [O(r'\frac{1}{2}y-\frac{1}{4}\sin 2y=\tan x+C', y/2-sin(2*y)/4-tan(x)-Cc, 'rel'), O(r'\frac{1}{2}y+\frac{1}{4}\sin 2y=\tan x+C', y/2+sin(2*y)/4-tan(x)-Cc, 'rel'),
   O(r'\frac{1}{2}y-\frac{1}{2}\sin 2y=\tan x+C', y/2-sin(2*y)/2-tan(x)-Cc, 'rel'), O(r'\frac{1}{2}y+\frac{1}{2}\sin 2y=\tan x+C', y/2+sin(2*y)/2-tan(x)-Cc, 'rel')],
  r"$\sin^2y\,dy=\sec^2x\,dx$ ، و $\sin^2y=\dfrac{1-\cos2y}{2}$ ، إذن $\dfrac12y-\dfrac14\sin2y=\tan x+C$",
  truth=lambda vals: only(vals, lambda F_: ode_gen_ok(F_, 1/(cos(x)**2*sin(y)**2)))),
]

# ============================================================== Exam 6
E6 = [
# 2026r #2: Pythagorean quotient whose denominator is 1; options = sign of the trig term x sign of x
Q('u5e6q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\csc^{2}x+\cot^{2}x}{\csc^{2}x-\cot^{2}x}', (csc(x)**2+cot(x)**2)/(csc(x)**2-cot(x)**2))),
  [A(r'-2\cot x-x+C', -2*cot(x)-x), A(r'2\cot x-x+C', 2*cot(x)-x), A(r'-2\cot x+x+C', -2*cot(x)+x), A(r'2\cot x+x+C', 2*cot(x)+x)],
  r"$\csc^2x-\cot^2x=1$ ، و $\cot^2x=\csc^2x-1$ ، إذن المقدار $=2\csc^2x-1$ ، وتكامله $-2\cot x-x+C$",
  truth=(csc(x)**2+cot(x)**2)/(csc(x)**2-cot(x)**2)),
# 2026r #1: k e^(mx) + a^(nx); options = coefficient of e (divided vs multiplied) x chain factor in a^(nx)
Q('u5e6q2', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'6e^{3x}+5^{2x}', 6*exp(3*x)+5**(2*x))),
  [A(r'2e^{3x}+\frac{5^{2x}}{2\ln 5}+C', 2*exp(3*x)+5**(2*x)/(2*log(5))), A(r'2e^{3x}+\frac{5^{2x}}{\ln 5}+C', 2*exp(3*x)+5**(2*x)/log(5)),
   A(r'18e^{3x}+\frac{5^{2x}}{2\ln 5}+C', 18*exp(3*x)+5**(2*x)/(2*log(5))), A(r'18e^{3x}+\frac{5^{2x}}{\ln 5}+C', 18*exp(3*x)+5**(2*x)/log(5))],
  r"$\displaystyle\int6e^{3x}dx=\frac{6}{3}e^{3x}=2e^{3x}$ ، و $\displaystyle\int5^{2x}dx=\frac{5^{2x}}{2\ln5}$",
  truth=6*exp(3*x)+5**(2*x)),
# 2025 #4: integral from a to 2a of (x + c)/x equals a logarithm -> a; options = coefficient of ln dropped x [x] read as 2a
Q('u5e6q3', L[1], 'medium',
  F(r"إذا كان: $\displaystyle\int_{a}^{2a}«0»\,dx=\ln 24$ ، حيث $a>0$ ، فإنّ قيمة الثابت $a$ هي:", (r'\frac{x+3}{x}', (x+3)/x)),
  [O(r'\ln 3', log(3)), O(r'\ln 12', log(12)), O(r'\frac{1}{2}\ln 3', log(3)/2), O(r'\frac{1}{2}\ln 12', log(12)/2)],
  r"$\displaystyle\int_a^{2a}\left(1+\frac3x\right)dx=\big[x+3\ln x\big]_a^{2a}=a+3\ln2$ ، و $a+3\ln2=\ln24 \Rightarrow a=\ln24-\ln8=\ln3$",
  truth=lambda: solve(expand_log(ig((x+3)/x, (x, ap, 2*ap)), force=True) - log(24), ap)[0]),
# 2024 #5: f'(x) = (p e^x + q)^2 and f(0) -> f; options = 1/2 kept in e^(2x) x the constant integrated to a multiple of x
IndexQ('u5e6q4', L[1], 'medium',
  F(r"إذا كان: $f'(x)=«0»$ ، وكان: $f(0)=2$ ، فإنّ قاعدة الاقتران $f$ هي:", (r'(e^{x}-3)^{2}', (exp(x)-3)**2)),
  [O(r'f(x)=\frac{1}{2}e^{2x}-6e^{x}+9x+\frac{15}{2}', exp(2*x)/2-6*exp(x)+9*x+R(15, 2), 'eq'), O(r'f(x)=e^{2x}-6e^{x}+9x+7', exp(2*x)-6*exp(x)+9*x+7, 'eq'),
   O(r'f(x)=\frac{1}{2}e^{2x}-6e^{x}+\frac{15}{2}', exp(2*x)/2-6*exp(x)+R(15, 2), 'eq'), O(r'f(x)=e^{2x}-6e^{x}+7', exp(2*x)-6*exp(x)+7, 'eq')],
  r"$f'(x)=e^{2x}-6e^x+9$ ، إذن $f(x)=\frac12e^{2x}-6e^x+9x+C$ ، و $f(0)=\frac12-6+C=2 \Rightarrow C=\frac{15}{2}$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, (exp(x)-3)**2, 0, 2))),
# 2026r #5: v = k trig(t/n), total distance on an interval where v changes sign once
Q('u5e6q5', L[1], 'hard',
  F(r"إذا تحرّك جُسيم في مسار مستقيم، وكانت سرعته تُعطى بالاقتران: $v(t)=«0»$ ، حيث $v$ سرعته بالمتر لكل ثانية، و $t$ الزمن بالثواني، فإنّ المسافة الكلية بالأمتار التي قطعها الجُسيم في الفترة $[0,\,3\pi]$ هي:", (r'3\sin\frac{t}{2}', 3*sin(t/2))),
  [O('18', 18), O('6', 6), O('12', 12), O(r'\frac{9}{2}', R(9, 2))],
  r"$v=0$ عند $t=2\pi$ ، و $\displaystyle\int_0^{2\pi}3\sin\frac t2\,dt=\left[-6\cos\frac t2\right]_0^{2\pi}=12$ ، $\displaystyle\int_{2\pi}^{3\pi}3\sin\frac t2\,dt=-6$" "\n"
  r"المسافة $=12+|-6|=18\ \text{m}$",
  truth=ig(3*sin(t/2), (t, 0, 2*pi)) + Abs(ig(3*sin(t/2), (t, 2*pi, 3*pi)))),
# 2026r #9 / 2024s #10: definite integral of x times a root of (x + c); options = sign x (x = u - c vs u + c)
Q('u5e6q6', L[2], 'hard',
  F(r"قيمة: $\displaystyle\int_{-2}^{-1}«0»\,dx$ هي:", (r'x\sqrt{x+2}', x*sqrt(x+2))),
  [O(r'-\frac{14}{15}', -R(14, 15)), O(r'\frac{14}{15}', R(14, 15)), O(r'\frac{26}{15}', R(26, 15)), O(r'-\frac{26}{15}', -R(26, 15))],
  r"$u=x+2$ ، $x=u-2$ ، والحدود: $x=-2\to u=0$ ، $x=-1\to u=1$" "\n"
  r"$\displaystyle\int_0^1(u-2)\sqrt u\,du=\left[\frac25u^{\frac52}-\frac43u^{\frac32}\right]_0^1=\frac25-\frac43=-\frac{14}{15}$",
  truth=ig(x*sqrt(x+2), (x, -2, -1))),
# 2026r #10 / 2024 #7: odd power of sin times a power of cos; options = signs of the two terms
Q('u5e6q7', L[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\sin^{3}x\cos^{4}x', sin(x)**3*cos(x)**4)),
  [A(r'\frac{1}{7}\cos^{7}x-\frac{1}{5}\cos^{5}x+C', cos(x)**7/7-cos(x)**5/5), A(r'\frac{1}{5}\cos^{5}x-\frac{1}{7}\cos^{7}x+C', cos(x)**5/5-cos(x)**7/7),
   A(r'\frac{1}{7}\cos^{7}x+\frac{1}{5}\cos^{5}x+C', cos(x)**7/7+cos(x)**5/5), A(r'-\frac{1}{7}\cos^{7}x-\frac{1}{5}\cos^{5}x+C', -cos(x)**7/7-cos(x)**5/5)],
  r"$\sin^3x=(1-\cos^2x)\sin x$ ، و $u=\cos x \Rightarrow du=-\sin x\,dx$:" "\n"
  r"$\displaystyle-\int(1-u^2)u^4du=-\frac{u^5}{5}+\frac{u^7}{7}+C=\frac17\cos^7x-\frac15\cos^5x+C$",
  truth=sin(x)**3*cos(x)**4),
# 2026r #7 / 2025s #10: (px + q)/(x^2 - cx); options = constants swapped x sign of the second
Q('u5e6q8', L[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{3x-4}{x^{2}-2x}', (3*x-4)/(x**2-2*x))),
  [A(r'2\ln|x|+\ln|x-2|+C', 2*log(x)+log(x-2)), A(r'\ln|x|+2\ln|x-2|+C', log(x)+2*log(x-2)),
   A(r'2\ln|x|-\ln|x-2|+C', 2*log(x)-log(x-2)), A(r'\ln|x|-2\ln|x-2|+C', log(x)-2*log(x-2))],
  r"$\dfrac{3x-4}{x(x-2)}=\dfrac{A}{x}+\dfrac{B}{x-2}$ ، عند $x=0$: $-4=-2A \Rightarrow A=2$ ، عند $x=2$: $2=2B \Rightarrow B=1$",
  truth=(3*x-4)/(x**2-2*x)),
# 2024 #10: ln of a root of x by parts; options = sign of the x term x the 1/n factor on it
Q('u5e6q9', L[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\ln\sqrt[3]{x}', log(cbrt(x)))),
  [A(r'\frac{1}{3}x\ln x-\frac{1}{3}x+C', x*log(x)/3-x/3), A(r'\frac{1}{3}x\ln x+\frac{1}{3}x+C', x*log(x)/3+x/3),
   A(r'\frac{1}{3}x\ln x-x+C', x*log(x)/3-x), A(r'\frac{1}{3}x\ln x+x+C', x*log(x)/3+x)],
  r"$\ln\sqrt[3]{x}=\frac13\ln x$ ، وبالأجزاء: $\displaystyle\int\ln x\,dx=x\ln x-x$ ، إذن الناتج $\frac13x\ln x-\frac13x+C$",
  truth=log(cbrt(x))),
# 2025 #3: area under c - a^x in the first quadrant (figure); options = divide vs multiply by ln a x lower limit kept
Q('u5e6q10', L[5], 'medium',
  F(r"إذا كان الاقتران المُبيّن مُنحناه في الشكل الآتي هو: $f(x)=«0»$ ، فإنّ مساحة المنطقة المُظلَّلة بالوحدات المربعة هي:", (r'4-2^{x}', 4-2**x)),
  [O(r'8-\frac{3}{\ln 2}', 8-3/log(2)), O(r'8-\frac{4}{\ln 2}', 8-4/log(2)), O(r'8-3\ln 2', 8-3*log(2)), O(r'8-4\ln 2', 8-4*log(2))],
  r"المنحنى يقطع المحور $x$ عند $2^x=4 \Rightarrow x=2$ ، فالمساحة $\displaystyle\int_0^2(4-2^x)dx=\left[4x-\frac{2^x}{\ln2}\right]_0^2$" "\n"
  r"$=\left(8-\frac{4}{\ln2}\right)-\left(0-\frac{1}{\ln2}\right)=8-\frac{3}{\ln2}$",
  truth=ig(4-2**x, (x, 0, 2)),
  figure=figure('u5e6q10', region(4-2**x, 0*x, 0, 2, (-0.6, 2.7), (-1.6, 4.4), [(1.55, 2.2, r'$f(x)$', '#1f5fbf')]), 3.4, 2.9)),
# 2026 #36: volume about the x-axis of an exponential on [0, ln c]; options = square kept, 1/2 kept, lower limit kept
Q('u5e6q11', L[5], 'medium',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنى الاقتران: $f(x)=«0»$ والمحور $x$ والمستقيمين: $x=0,\ x=\ln 3$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'e^{x}', exp(x))),
  [O(r'4\pi', 4*pi), O(r'8\pi', 8*pi), O(r'2\pi', 2*pi), O(r'\frac{9\pi}{2}', 9*pi/2)],
  r"$V=\pi\displaystyle\int_0^{\ln3}e^{2x}dx=\pi\left[\frac{e^{2x}}{2}\right]_0^{\ln3}=\pi\left(\frac92-\frac12\right)=4\pi$",
  truth=pi*ig(exp(2*x), (x, 0, log(3)))),
# 2026r #12: dy/dx = y times a polynomial, through a point; options = 1/2 kept x sign of the constant
IndexQ('u5e6q12', L[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ الذي تُحقّقه النقطة $(2,\,1)$ هو:", (r'xy+3y', x*y+3*y)),
  [O(r'\ln|y|=\frac{1}{2}x^{2}+3x-8', log(y)-x**2/2-3*x+8, 'rel'), O(r'\ln|y|=\frac{1}{2}x^{2}+3x+8', log(y)-x**2/2-3*x-8, 'rel'),
   O(r'\ln|y|=x^{2}+3x-10', log(y)-x**2-3*x+10, 'rel'), O(r'\ln|y|=x^{2}+3x+10', log(y)-x**2-3*x-10, 'rel')],
  r"$\dfrac{dy}{y}=(x+3)dx \Rightarrow \ln|y|=\frac12x^2+3x+C$ ، وعند $(2,1)$: $0=2+6+C \Rightarrow C=-8$",
  truth=lambda vals: only(vals, lambda F_: ode_ok_rel(F_, x*y+3*y, 2, 1))),
]

# ============================================================== Exam 7
E7 = [
# 2024s #2: 1/(sin^2 cos^2) through the double angle; options = sign x tan vs cot
Q('u5e7q1', L[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{1}{\sin^{2}\frac{x}{2}\cos^{2}\frac{x}{2}}', 1/(sin(x/2)**2*cos(x/2)**2))),
  [A(r'-4\cot x+C', -4*cot(x)), A(r'4\cot x+C', 4*cot(x)), A(r'-4\tan x+C', -4*tan(x)), A(r'4\tan x+C', 4*tan(x))],
  r"$\sin\frac x2\cos\frac x2=\frac12\sin x$ ، فالمقام $=\frac14\sin^2x$ ، والمقدار $=4\csc^2x$ ، وتكامله $-4\cot x+C$",
  truth=1/(sin(x/2)**2*cos(x/2)**2)),
# 2025s #1: k root(x) - a^(-x); options = power-rule coefficient (divide vs multiply) x sign of the a^(-x) term
Q('u5e7q2', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'4\sqrt[3]{x}+3^{-x}', 4*cbrt(x)+3**(-x))),
  [A(r'3\sqrt[3]{x^{4}}-\frac{3^{-x}}{\ln 3}+C', 3*cbrt(x**4)-3**(-x)/log(3)), A(r'3\sqrt[3]{x^{4}}+\frac{3^{-x}}{\ln 3}+C', 3*cbrt(x**4)+3**(-x)/log(3)),
   A(r'\frac{16}{3}\sqrt[3]{x^{4}}-\frac{3^{-x}}{\ln 3}+C', R(16, 3)*cbrt(x**4)-3**(-x)/log(3)), A(r'\frac{16}{3}\sqrt[3]{x^{4}}+\frac{3^{-x}}{\ln 3}+C', R(16, 3)*cbrt(x**4)+3**(-x)/log(3))],
  r"$\displaystyle\int4x^{\frac13}dx=4\cdot\frac{x^{\frac43}}{\frac43}=3x^{\frac43}$ ، و $\displaystyle\int3^{-x}dx=-\frac{3^{-x}}{\ln3}$",
  truth=4*cbrt(x)+3**(-x)),
# 2024s #5 / 2023 #4: definite integral of |linear| across its zero; options = no absolute value, one triangle, missing 1/2
Q('u5e7q3', L[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{-1}^{3}«0»\,dx$ هي:", (r'\left|2x-2\right|', Abs(2*x-2))),
  [O('8', 8), O('0', 0), O('4', 4), O('16', 16)],
  r"$2x-2=0$ عند $x=1$: $\displaystyle\int_{-1}^{1}(2-2x)dx+\int_1^3(2x-2)dx=4+4=8$",
  truth=num(Integral(Abs(2*x-2), (x, -1, 3)))),
# 2024 #6: displacement for v = k trig(t/n); options = sign x chain factor (multiplied instead of divided)
Q('u5e7q4', L[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=«0»$ ، حيث $v$ السرعة بالمتر لكل ثانية، و $t$ الزمن بالثواني. إنّ إزاحة الجُسيم بالأمتار في الفترة $\left[0,\,\frac{4\pi}{3}\right]$ هي:", (r'4\sin\frac{t}{2}', 4*sin(t/2))),
  [O('12', 12), O('-12', -12), O('3', 3), O('-3', -3)],
  r"الإزاحة $=\displaystyle\int_0^{4\pi/3}4\sin\frac t2\,dt=\left[-8\cos\frac t2\right]_0^{4\pi/3}=-8\left(-\frac12\right)+8=12$",
  truth=ig(4*sin(t/2), (t, 0, 4*pi/3))),
# 2025 #8: price rate p'(x) = k x / root(x^2 + c) and one price -> P(x); options = coefficient (1/2 slip) x sign of the constant
IndexQ('u5e7q5', L[2], 'medium',
  F(r"يُمثّل الاقتران $P(x)$ سعر القطعة الواحدة (بالدينار) من مُنتَج معيّن، حيث $x$ عدد القطع المبيعة بالمئات. إذا كان: $P'(x)=«0»$ هو معدّل التغيّر في سعر هذه القطعة، وكان سعر القطعة الواحدة $15$ JD عندما يكون عدد القطع المبيعة منها $200$ قطعة، فإنّ قاعدة الاقتران $P(x)$ هي:", (r'\frac{-4x}{\sqrt{x^{2}+5}}', -4*x/sqrt(x**2+5))),
  [O(r'P(x)=-4\sqrt{x^{2}+5}+27', -4*sqrt(x**2+5)+27, 'eq'), O(r'P(x)=-4\sqrt{x^{2}+5}-27', -4*sqrt(x**2+5)-27, 'eq'),
   O(r'P(x)=-2\sqrt{x^{2}+5}+21', -2*sqrt(x**2+5)+21, 'eq'), O(r'P(x)=-2\sqrt{x^{2}+5}-21', -2*sqrt(x**2+5)-21, 'eq')],
  r"$u=x^2+5$: $\displaystyle\int\frac{-4x}{\sqrt{x^2+5}}dx=-2\int u^{-\frac12}du=-4\sqrt{x^2+5}+C$ ، و $200$ قطعة تعني $x=2$: $-4(3)+C=15 \Rightarrow C=27$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, -4*x/sqrt(x**2+5), 2, 15))),
# 2025 #6: root(a x^2 - x^4) on a negative interval (|x| = -x); options = sign (|x| = x slip) x the missing 1/2
Q('u5e7q6', L[2], 'hard',
  F(r"قيمة: $\displaystyle\int_{-2}^{0}«0»\,dx$ هي:", (r'\sqrt{4x^{2}-x^{4}}', sqrt(4*x**2-x**4))),
  [O(r'\frac{8}{3}', R(8, 3)), O(r'-\frac{8}{3}', -R(8, 3)), O(r'\frac{16}{3}', R(16, 3)), O(r'-\frac{16}{3}', -R(16, 3))],
  r"$\sqrt{4x^2-x^4}=\sqrt{x^2}\sqrt{4-x^2}=|x|\sqrt{4-x^2}=-x\sqrt{4-x^2}$ في $[-2,0]$" "\n"
  r"$u=4-x^2$: $\displaystyle\int_{-2}^0-x\sqrt{4-x^2}\,dx=\left[\frac13(4-x^2)^{\frac32}\right]_{-2}^0=\frac83$",
  truth=num(Integral(sqrt(4*x**2-x**4), (x, -2, 0)))),
# 2025 #2: improper fraction over a linear factor; options = quotient term halved or not x sign of the ln term
Q('u5e7q7', L[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x^{2}-3x+5}{x-1}', (x**2-3*x+5)/(x-1))),
  [A(r'\frac{x^{2}}{2}-2x+3\ln|x-1|+C', x**2/2-2*x+3*log(x-1)), A(r'\frac{x^{2}}{2}-2x-3\ln|x-1|+C', x**2/2-2*x-3*log(x-1)),
   A(r'x^{2}-2x+3\ln|x-1|+C', x**2-2*x+3*log(x-1)), A(r'x^{2}-2x-3\ln|x-1|+C', x**2-2*x-3*log(x-1))],
  r"بالقسمة: $x^2-3x+5=(x-1)(x-2)+3$ ، إذن $\dfrac{x^2-3x+5}{x-1}=x-2+\dfrac{3}{x-1}$" "\n"
  r"$\displaystyle\int\left(x-2+\frac{3}{x-1}\right)dx=\frac{x^2}{2}-2x+3\ln|x-1|+C$",
  truth=(x**2-3*x+5)/(x-1)),
# 2023 #9: k x^n ln x by parts; options = power of x in the first term x sign of the second
Q('u5e7q8', L[4], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'8x^{3}\ln x', 8*x**3*log(x))),
  [A(r'2x^{4}\ln x-\frac{1}{2}x^{4}+C', 2*x**4*log(x)-x**4/2), A(r'2x^{3}\ln x-\frac{1}{2}x^{4}+C', 2*x**3*log(x)-x**4/2),
   A(r'2x^{4}\ln x+\frac{1}{2}x^{4}+C', 2*x**4*log(x)+x**4/2), A(r'2x^{3}\ln x+\frac{1}{2}x^{4}+C', 2*x**3*log(x)+x**4/2)],
  r"بالأجزاء: $u=\ln x$ ، $dv=8x^3dx \Rightarrow v=2x^4$: $\displaystyle2x^4\ln x-\int2x^4\cdot\frac1x\,dx=2x^4\ln x-\frac12x^4+C$",
  truth=8*x**3*log(x)),
# 2023 #10: k x trig(kx) by parts; options = sign of the first term x sign of the second
Q('u5e7q9', L[4], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'4x\sin 2x', 4*x*sin(2*x))),
  [A(r'-2x\cos 2x+\sin 2x+C', -2*x*cos(2*x)+sin(2*x)), A(r'2x\cos 2x+\sin 2x+C', 2*x*cos(2*x)+sin(2*x)),
   A(r'-2x\cos 2x-\sin 2x+C', -2*x*cos(2*x)-sin(2*x)), A(r'2x\cos 2x-\sin 2x+C', 2*x*cos(2*x)-sin(2*x))],
  r"بالأجزاء: $u=4x$ ، $dv=\sin2x\,dx \Rightarrow v=-\frac12\cos2x$: $\displaystyle-2x\cos2x+\int2\cos2x\,dx=-2x\cos2x+\sin2x+C$",
  truth=4*x*sin(2*x)),
# 2025s #3: area under x(x - c)^2 between its zeros (figure); options = expansion slips
Q('u5e7q10', L[5], 'medium',
  F(r"إذا كان الاقتران المُبيّن مُنحناه في الشكل الآتي هو: $f(x)=«0»$ ، فإنّ مساحة المنطقة المُظلَّلة (بالوحدات المربعة) هي:", (r'x(x-3)^{2}', x*(x-3)**2)),
  [O(r'\frac{27}{4}', R(27, 4)), O(r'\frac{81}{4}', R(81, 4)), O(r'\frac{135}{4}', R(135, 4)), O(r'\frac{189}{4}', R(189, 4))],
  r"المنحنى يمسّ المحور $x$ عند $x=3$ ، و $x(x-3)^2=x^3-6x^2+9x$" "\n"
  r"$\displaystyle\int_0^3(x^3-6x^2+9x)dx=\left[\frac{x^4}{4}-2x^3+\frac{9x^2}{2}\right]_0^3=\frac{81}{4}-54+\frac{81}{2}=\frac{27}{4}$",
  truth=ig(x*(x-3)**2, (x, 0, 3)),
  figure=figure('u5e7q10', region(x*(x-3)**2, 0*x, 0, 3, (-0.8, 4.4), (-1.6, 5.4), [(1.9, 3.6, r'$f(x)$', '#1f5fbf')]), 3.6, 2.9)),
# 2026 #36 family (washers, figure): volume between a line and a parabola; options = squared difference, pi x area, x^2 not squared
Q('u5e7q11', L[5], 'hard',
  F(r"اعتمادًا على الشكل الآتي الذي يُبيّن منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ ، فإنّ حجم المُجسَّم الناتج من دوران المنطقة المُظلَّلة حول المحور $x$ (بالوحدات المكعبة) هو:", (r'2x', 2*x), (r'x^{2}', x**2)),
  [O(r'\frac{64\pi}{15}', 64*pi/15), O(r'\frac{16\pi}{15}', 16*pi/15), O(r'\frac{4\pi}{3}', 4*pi/3), O(r'8\pi', 8*pi)],
  r"التقاطع: $x^2=2x \Rightarrow x=0,\ x=2$ ، و $2x\ge x^2$ في $[0,2]$" "\n"
  r"$V=\pi\displaystyle\int_0^2\left(4x^2-x^4\right)dx=\pi\left(\frac{32}{3}-\frac{32}{5}\right)=\frac{64\pi}{15}$",
  truth=pi*ig((2*x)**2-(x**2)**2, (x, 0, 2)),
  figure=figure('u5e7q11', region(2*x, x**2, 0, 2, (-0.6, 2.7), (-0.6, 5.2), [(2.15, 3.6, r'$f(x)$', '#1f5fbf'), (1.25, 0.6, r'$g(x)$', '#d04a1a')]), 3.4, 3.0)),
# 2025 #12: dy/dx = ((linear) trig y)^2 / (linear), through a point; options = tan vs -cot x sign of the constant
IndexQ('u5e7q12', L[6], 'hard',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ الذي تُحقّقه النقطة $\left(0,\,\frac{\pi}{4}\right)$ هو:", (r'\frac{\left((x+2)\cos y\right)^{2}}{x+2}', ((x+2)*cos(y))**2/(x+2))),
  [O(r'\tan y=\frac{x^{2}}{2}+2x+1', tan(y)-x**2/2-2*x-1, 'rel'), O(r'\tan y=\frac{x^{2}}{2}+2x-1', tan(y)-x**2/2-2*x+1, 'rel'),
   O(r'-\cot y=\frac{x^{2}}{2}+2x-1', -cot(y)-x**2/2-2*x+1, 'rel'), O(r'-\cot y=\frac{x^{2}}{2}+2x+1', -cot(y)-x**2/2-2*x-1, 'rel')],
  r"$\dfrac{dy}{dx}=(x+2)\cos^2y \Rightarrow \sec^2y\,dy=(x+2)dx \Rightarrow \tan y=\frac{x^2}{2}+2x+C$" "\n"
  r"عند $\left(0,\frac{\pi}{4}\right)$: $1=C$",
  truth=lambda vals: only(vals, lambda F_: ode_ok_rel(F_, (x+2)*cos(y)**2, 0, pi/4))),
]

# ============================================================== Exam 8
# shaded area of 2/(x - 1) from 2 to a equals 4 -> a = e^2 + 1
a8 = E**2 + 1
E8 = [
# 2025 #1: a quotient that collapses with sum-to-product; options = sign x sin vs cos
Q('u5e8q1', L[1], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\sin 3x+\sin x}{\sin 2x}', (sin(3*x)+sin(x))/sin(2*x))),
  [A(r'2\sin x+C', 2*sin(x)), A(r'-2\sin x+C', -2*sin(x)), A(r'2\cos x+C', 2*cos(x)), A(r'-2\cos x+C', -2*cos(x))],
  r"$\sin3x+\sin x=2\sin2x\cos x$ ، فالمقدار $=2\cos x$ ، وتكامله $2\sin x+C$",
  truth=(sin(3*x)+sin(x))/sin(2*x)),
# 2024 #1: a^(-x) plus a trig function of -x; options = sign of each term
Q('u5e8q2', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'5^{-x}-\cos(-x)', 5**(-x)-cos(-x))),
  [A(r'-\frac{5^{-x}}{\ln 5}-\sin x+C', -5**(-x)/log(5)-sin(x)), A(r'\frac{5^{-x}}{\ln 5}+\sin x+C', 5**(-x)/log(5)+sin(x)),
   A(r'-\frac{5^{-x}}{\ln 5}+\sin x+C', -5**(-x)/log(5)+sin(x)), A(r'\frac{5^{-x}}{\ln 5}-\sin x+C', 5**(-x)/log(5)-sin(x))],
  r"$\displaystyle\int5^{-x}dx=-\frac{5^{-x}}{\ln5}$ ، و $\cos(-x)=\cos x$ ، و $\displaystyle\int\cos x\,dx=\sin x$ ، إذن الناتج $-\frac{5^{-x}}{\ln5}-\sin x+C$",
  truth=5**(-x)-cos(-x)),
# 2025s #2: |linear| / (its negative) on an interval where the sign is fixed; options = sign x answering the integrand value
Q('u5e8q3', L[1], 'easy',
  F(r"قيمة: $\displaystyle\int_{3}^{6}«0»\,dx$ هي:", (r'\frac{|2-x|}{2-x}', Abs(2-x)/(2-x))),
  [O('-3', -3), O('3', 3), O('-1', -1), O('1', 1)],
  r"في $[3,6]$ يكون $2-x<0$ ، فـ $|2-x|=-(2-x)$ والمقدار $=-1$ ، و $\displaystyle\int_3^6(-1)dx=-3$",
  truth=num(Integral(Abs(2-x)/(2-x), (x, 3, 6)))),
# 2024s #6: population changing at k e^(rt), initial count -> P(t); options = decimal slip in k/r x constant adjusted or not
IndexQ('u5e8q4', L[1], 'medium',
  F(r"في دراسة لأعداد الأسماك في بحيرة، تبيّن أنّ عدد الأسماك $N(t)$ يتغيّر بمعدّل $N'(t)=«0»$ ، حيث $t$ الزمن بالأشهر منذ بدء الدراسة. إذا كان عدد الأسماك عند بدء الدراسة $500$ سمكة، فإنّ قاعدة الاقتران $N(t)$ هي:", (r'0.9e^{0.03t}', R(9, 10)*exp(R(3, 100)*t))),
  [O(r'N(t)=30e^{0.03t}+470', 30*exp(R(3, 100)*t)+470, 'eq'), O(r'N(t)=30e^{0.03t}+500', 30*exp(R(3, 100)*t)+500, 'eq'),
   O(r'N(t)=3e^{0.03t}+497', 3*exp(R(3, 100)*t)+497, 'eq'), O(r'N(t)=3e^{0.03t}+500', 3*exp(R(3, 100)*t)+500, 'eq')],
  r"$N(t)=\displaystyle\int0.9e^{0.03t}dt=\frac{0.9}{0.03}e^{0.03t}+C=30e^{0.03t}+C$ ، و $N(0)=30+C=500 \Rightarrow C=470$",
  truth=lambda vals: only(vals, lambda N_: ode_t_ok(N_, R(9, 10)*exp(R(3, 100)*t), 0, 500))),
# 2024s #7: position after a time for v = k sin(t/n), given the start; options = start added or not x chain slip
Q('u5e8q5', L[1], 'medium',
  F(r"يتحرّك جسم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=«0»$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته بالمتر لكل ثانية. إذا بدأ الجسم حركته من الموقع $x=1$ ، فإنّ موقعه بعد $2\pi$ ثانية من بدء الحركة هو:", (r'2\sin\frac{t}{4}', 2*sin(t/4))),
  [O('9', 9, units='m'), O('8', 8, units='m'), O(r'\frac{3}{2}', R(3, 2), units='m'), O(r'\frac{1}{2}', R(1, 2), units='m')],
  r"$s(2\pi)=1+\displaystyle\int_0^{2\pi}2\sin\frac t4\,dt=1+\left[-8\cos\frac t4\right]_0^{2\pi}=1+(0+8)=9\ \text{m}$",
  truth=1+ig(2*sin(t/4), (t, 0, 2*pi))),
# 2025 #7: e^(nx) times a power of (1 - c e^(-x)) becomes e^x (e^x - c)^k; options = which bracket x sign
Q('u5e8q6', L[2], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'e^{5x}\left(1-3e^{-x}\right)^{4}', exp(5*x)*(1-3*exp(-x))**4)),
  [A(r'\frac{1}{5}(e^{x}-3)^{5}+C', (exp(x)-3)**5/5), A(r'-\frac{1}{5}(e^{x}-3)^{5}+C', -(exp(x)-3)**5/5),
   A(r'\frac{1}{5}(1-3e^{-x})^{5}+C', (1-3*exp(-x))**5/5), A(r'-\frac{1}{5}(1-3e^{-x})^{5}+C', -(1-3*exp(-x))**5/5)],
  r"$e^{5x}(1-3e^{-x})^4=e^x\cdot\left(e^x(1-3e^{-x})\right)^4=e^x(e^x-3)^4$ ، و $u=e^x-3 \Rightarrow du=e^xdx$" "\n"
  r"$\displaystyle\int u^4du=\frac{u^5}{5}+C=\frac15(e^x-3)^5+C$",
  truth=exp(5*x)*(1-3*exp(-x))**4),
# 2024s #9: f'/f^n with a trig inner function; options = sign x 1/(n-1) vs (n-1)
Q('u5e8q7', L[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{\cos x}{(2-\sin x)^{4}}', cos(x)/(2-sin(x))**4)),
  [A(r'\frac{1}{3(2-\sin x)^{3}}+C', 1/(3*(2-sin(x))**3)), A(r'-\frac{1}{3(2-\sin x)^{3}}+C', -1/(3*(2-sin(x))**3)),
   A(r'\frac{3}{(2-\sin x)^{3}}+C', 3/(2-sin(x))**3), A(r'-\frac{3}{(2-\sin x)^{3}}+C', -3/(2-sin(x))**3)],
  r"$u=2-\sin x \Rightarrow du=-\cos x\,dx$: $\displaystyle-\int u^{-4}du=-\frac{u^{-3}}{-3}+C=\frac{1}{3(2-\sin x)^3}+C$",
  truth=cos(x)/(2-sin(x))**4),
# 2025 #10: 1/(x^2 (x - c)) with a repeated factor; options = sign of the logs x sign of 1/x
Q('u5e8q8', L[3], 'hard',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{2}{x^{2}(x+2)}', 2/(x**2*(x+2)))),
  [A(r'\frac{1}{2}\ln|x+2|-\frac{1}{2}\ln|x|-\frac{1}{x}+C', log(x+2)/2-log(x)/2-1/x), A(r'\frac{1}{2}\ln|x+2|-\frac{1}{2}\ln|x|+\frac{1}{x}+C', log(x+2)/2-log(x)/2+1/x),
   A(r'\frac{1}{2}\ln|x|-\frac{1}{2}\ln|x+2|-\frac{1}{x}+C', log(x)/2-log(x+2)/2-1/x), A(r'\frac{1}{2}\ln|x|-\frac{1}{2}\ln|x+2|+\frac{1}{x}+C', log(x)/2-log(x+2)/2+1/x)],
  r"$\dfrac{2}{x^2(x+2)}=\dfrac{A}{x}+\dfrac{B}{x^2}+\dfrac{D}{x+2}$: عند $x=0$: $B=1$ ، عند $x=-2$: $D=\frac12$ ، ومعامل $x^2$: $A+D=0 \Rightarrow A=-\frac12$" "\n"
  r"$\displaystyle\int=-\frac12\ln|x|-\frac1x+\frac12\ln|x+2|+C$",
  truth=2/(x**2*(x+2))),
# 2023s #11: integral of x f'(x) from given values by parts; options = subtract vs add the integral x f(b) vs b f(b)
Q('u5e8q9', L[4], 'medium',
  r"إذا كان: $\displaystyle\int_{0}^{2}f(x)\,dx=3$ ، $f(2)=4$ ، $f(0)=1$ ، فإنّ قيمة $\displaystyle\int_{0}^{2}x\,f'(x)\,dx$ تساوي:",
  [O('5', 5), O('11', 11), O('1', 1), O('7', 7)],
  r"بالأجزاء: $u=x$ ، $dv=f'(x)dx \Rightarrow v=f(x)$: $\displaystyle\int_0^2xf'(x)dx=\big[xf(x)\big]_0^2-\int_0^2f(x)dx=(2\times4-0)-3=5$",
  # an explicit f with f(0) = 1, f(2) = 4 and integral 3 on [0, 2]
  truth=ig(x*diff(1-R(3, 2)*x+R(3, 2)*x**2, x), (x, 0, 2))),
# 2026 #35 / 2026r #6: shaded area under c/(x - h) from a fixed line to a equals k -> a (figure); options = coefficient x shift
Q('u5e8q10', L[5], 'medium',
  F(r"يُبيّن الشكل الآتي منحنى الاقتران: $f(x)=«0»$ ، $x>1$. إذا كانت مساحة المنطقة المُظلَّلة $4$ وحدات مربعة، فإنّ قيمة الثابت $a$ هي:", (r'\frac{2}{x-1}', 2/(x-1))),
  [O(r'e^{2}+1', E**2+1), O(r'e^{2}', E**2), O(r'e^{4}+1', E**4+1), O(r'e^{4}', E**4)],
  r"$\displaystyle\int_2^a\frac{2}{x-1}dx=2\big[\ln(x-1)\big]_2^a=2\ln(a-1)-2\ln1=2\ln(a-1)$" "\n"
  r"$2\ln(a-1)=4 \Rightarrow \ln(a-1)=2 \Rightarrow a=e^2+1$",
  truth=lambda: solve(ig(2/(x-1), (x, 2, ap)) - 4, ap)[0],
  figure=figure('u5e8q10', shaded(2/(x-1), 2, a8, (-0.4, 10.2), (-0.5, 3.6), {2: '$2$', a8: '$a$'}, (3.3, 1.5, r'$f(x)=\frac{2}{x-1}$')), 3.8, 2.8)),
# 2026 #36: volume of a squared trig function on a special interval; options = pi kept x tan of the right angle
Q('u5e8q11', L[5], 'easy',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنى الاقتران: $f(x)=«0»$ والمحور $x$ في الفترة $\left[0,\,\frac{\pi}{3}\right]$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'\sec x', sec(x))),
  [O(r'\sqrt{3}\pi', sqrt(3)*pi), O(r'\sqrt{3}', sqrt(3)), O(r'\frac{\sqrt{3}}{3}\pi', sqrt(3)*pi/3), O(r'\frac{\sqrt{3}}{3}', sqrt(3)/3)],
  r"$V=\pi\displaystyle\int_0^{\pi/3}\sec^2x\,dx=\pi\big[\tan x\big]_0^{\pi/3}=\pi\left(\sqrt3-0\right)=\sqrt3\pi$",
  truth=pi*ig(sec(x)**2, (x, 0, pi/3))),
# 2025s #12: x dy/dx = (power of y)(linear), through (1, 1); options = sign of the y side x sign of the constant
IndexQ('u5e8q12', L[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $x\dfrac{dy}{dx}=«0»$ الذي تُحقّقه النقطة $(1,\,1)$ هو:", (r'y^{2}\cdot(2x-1)', y**2*(2*x-1))),
  [O(r'-\frac{1}{y}=2x-\ln|x|-3', -1/y-2*x+log(x)+3, 'rel'), O(r'\frac{1}{y}=2x-\ln|x|-1', 1/y-2*x+log(x)+1, 'rel'),
   O(r'-\frac{1}{y}=2x-\ln|x|+3', -1/y-2*x+log(x)-3, 'rel'), O(r'\frac{1}{y}=2x-\ln|x|+1', 1/y-2*x+log(x)-1, 'rel')],
  r"$\dfrac{dy}{y^2}=\left(2-\dfrac1x\right)dx \Rightarrow -\dfrac1y=2x-\ln|x|+C$ ، وعند $(1,1)$: $-1=2+C \Rightarrow C=-3$",
  truth=lambda vals: only(vals, lambda F_: ode_ok_rel(F_, y**2*(2*x-1)/x, 1, 1))),
]

# ============================================================== Exam 9
vt9 = [(0, 0), (1, 3), (3, 3), (4, 0), (6, -2), (7, -2), (8, 0)]
E9 = [
# 2023 #2: 1/trig^2(kx) plus a constant; options = tan vs -cot x the constant integrated to cx or left as c
Q('u5e9q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int\left(«0»\right)dx$ هو:", (r'\frac{1}{\cos^{2}4x}-e', 1/cos(4*x)**2-E)),
  [A(r'\frac{1}{4}\tan 4x-ex+C', tan(4*x)/4-E*x), A(r'\frac{1}{4}\tan 4x-e+C', tan(4*x)/4-E),
   A(r'-\frac{1}{4}\cot 4x-ex+C', -cot(4*x)/4-E*x), A(r'-\frac{1}{4}\cot 4x-e+C', -cot(4*x)/4-E)],
  r"$\dfrac{1}{\cos^24x}=\sec^24x$ ، وتكامله $\frac14\tan4x$ ، و $e$ عدد ثابت تكامله $ex$ ، إذن الناتج $\frac14\tan4x-ex+C$",
  truth=1/cos(4*x)**2-E),
# 2023 #1: integral of (a^c)^x on [0, 1]; options = lower limit subtracted or not x the factor c in the denominator
Q('u5e9q2', L[1], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'\left(3^{\pi}\right)^{x}', (3**pi)**x)),
  [O(r'\frac{3^{\pi}-1}{\pi\ln 3}', (3**pi-1)/(pi*log(3))), O(r'\frac{3^{\pi}-1}{\ln 3}', (3**pi-1)/log(3)),
   O(r'\frac{3^{\pi}}{\pi\ln 3}', 3**pi/(pi*log(3))), O(r'\frac{3^{\pi}}{\ln 3}', 3**pi/log(3))],
  r"$(3^\pi)^x$ أسّي أساسه $3^\pi$ ، و $\ln(3^\pi)=\pi\ln3$: $\left[\dfrac{(3^\pi)^x}{\pi\ln3}\right]_0^1=\dfrac{3^\pi-1}{\pi\ln3}$",
  truth=ig((3**pi)**x, (x, 0, 1))),
# 2023s #4: definite integral of a piecewise function across its break; options = one piece only, chain slip
Q('u5e9q3', L[1], 'medium',
  r"إذا كان: $f(x)=\begin{cases}(3-2x)^{2}, & x<1\\ 4x^{3}-2x, & x\ge1\end{cases}$ ، فإنّ قيمة $\displaystyle\int_{0}^{2}f(x)\,dx$ تساوي:",
  [O(r'\frac{49}{3}', R(49, 3)), O('12', 12), O(r'\frac{13}{3}', R(13, 3)), O(r'\frac{10}{3}', R(10, 3))],
  r"$\displaystyle\int_0^1(3-2x)^2dx=\left[\frac{(3-2x)^3}{-6}\right]_0^1=\frac{1-27}{-6}=\frac{13}{3}$ ، و $\displaystyle\int_1^2(4x^3-2x)dx=\big[x^4-x^2\big]_1^2=12$" "\n"
  r"المجموع $=\frac{13}{3}+12=\frac{49}{3}$",
  truth=ig((3-2*x)**2, (x, 0, 1))+ig(4*x**3-2*x, (x, 1, 2))),
# 2023 #5: f' a quotient by a power of x, and f(1) -> f; options = power rule (divided or not) x sign of the 1/x term
IndexQ('u5e9q4', L[1], 'medium',
  F(r"إذا كان: $f'(x)=«0»$ ، وكان: $f(1)=3$ ، فإنّ قاعدة الاقتران $f$ هي:", (r'\frac{4x^{4}-2}{x^{2}}', (4*x**4-2)/x**2)),
  [O(r'f(x)=\frac{4}{3}x^{3}+\frac{2}{x}-\frac{1}{3}', R(4, 3)*x**3+2/x-R(1, 3), 'eq'), O(r'f(x)=\frac{4}{3}x^{3}-\frac{2}{x}+\frac{11}{3}', R(4, 3)*x**3-2/x+R(11, 3), 'eq'),
   O(r'f(x)=4x^{3}+\frac{2}{x}-3', 4*x**3+2/x-3, 'eq'), O(r'f(x)=4x^{3}-\frac{2}{x}+1', 4*x**3-2/x+1, 'eq')],
  r"$f'(x)=4x^2-2x^{-2}$ ، إذن $f(x)=\frac43x^3+2x^{-1}+C$ ، و $f(1)=\frac43+2+C=3 \Rightarrow C=-\frac13$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, (4*x**4-2)/x**2, 1, 3))),
# 2025s #7: position from v = c - (linear)^2 and the initial position; options = start added or not x chain slip
Q('u5e9q5', L[1], 'hard',
  F(r"يتحرّك جُسيم في مسار مستقيم، وتُعطى سرعته بالاقتران: $v(t)=«0»$ ، حيث $v$ السرعة بالمتر لكل ثانية و $t$ الزمن بالثواني. إذا كان الموقع الابتدائي للجُسيم $5\ \text{m}$ ، فإنّ موقع الجُسيم بعد ثانيتين هو:", (r'30-(3t-6)^{2}', 30-(3*t-6)**2)),
  [O('41', 41, units='m'), O('36', 36, units='m'), O('-7', -7, units='m'), O('-12', -12, units='m')],
  r"$\displaystyle\int_0^2\big(30-(3t-6)^2\big)dt=\left[30t-\frac{(3t-6)^3}{9}\right]_0^2=60-\left(0+\frac{216}{9}\right)=36$" "\n"
  r"الموقع $=5+36=41\ \text{m}$",
  truth=5+ig(30-(3*t-6)**2, (t, 0, 2))),
# 2023s #7: (linear) times a cube root of a quadratic whose derivative is a multiple of it; options = sign x cube vs fourth root
Q('u5e9q6', L[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'(3-6x)\sqrt[3]{9+3x-3x^{2}}', (3-6*x)*cbrt(9+3*x-3*x**2))),
  [A(r'\frac{3}{4}\sqrt[3]{(9+3x-3x^{2})^{4}}+C', R(3, 4)*cbrt((9+3*x-3*x**2)**4)), A(r'-\frac{3}{4}\sqrt[3]{(9+3x-3x^{2})^{4}}+C', -R(3, 4)*cbrt((9+3*x-3*x**2)**4)),
   A(r'\frac{3}{4}\sqrt[4]{(9+3x-3x^{2})^{3}}+C', R(3, 4)*((9+3*x-3*x**2)**3)**R(1, 4)), A(r'-\frac{3}{4}\sqrt[4]{(9+3x-3x^{2})^{3}}+C', -R(3, 4)*((9+3*x-3*x**2)**3)**R(1, 4))],
  r"$u=4+3x-3x^2 \Rightarrow du=(3-6x)dx$: $\displaystyle\int u^{\frac13}du=\frac34u^{\frac43}+C=\frac34\sqrt[3]{(4+3x-3x^2)^4}+C$",
  truth=(3-6*x)*cbrt(9+3*x-3*x**2)),
# 2023s #8: a power of a trig function times sin 2x; options = sign x the 2 of sin 2x
Q('u5e9q7', L[2], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos^{3}x\sin 2x', cos(x)**3*sin(2*x))),
  [A(r'-\frac{2}{5}\cos^{5}x+C', -2*cos(x)**5/5), A(r'\frac{2}{5}\cos^{5}x+C', 2*cos(x)**5/5),
   A(r'-\frac{1}{5}\cos^{5}x+C', -cos(x)**5/5), A(r'\frac{1}{5}\cos^{5}x+C', cos(x)**5/5)],
  r"$\sin2x=2\sin x\cos x$ ، فالمقدار $=2\cos^4x\sin x$ ، و $u=\cos x \Rightarrow du=-\sin x\,dx$: $\displaystyle-2\int u^4du=-\frac25\cos^5x+C$",
  truth=cos(x)**3*sin(2*x)),
# 2024 #9: c/((x - p)(x + q)); options = difference vs sum of logs, ln of the product
Q('u5e9q8', L[3], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{6}{(x-1)(x+2)}', 6/((x-1)*(x+2)))),
  [A(r'2\ln|x-1|-2\ln|x+2|+C', 2*log(x-1)-2*log(x+2)), A(r'2\ln|x-1|+2\ln|x+2|+C', 2*log(x-1)+2*log(x+2)),
   A(r'6\ln|(x-1)(x+2)|+C', 6*log((x-1)*(x+2))), A(r'3\ln|(x-1)(x+2)|+C', 3*log((x-1)*(x+2)))],
  r"$\dfrac{6}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}$ ، عند $x=1$: $6=3A \Rightarrow A=2$ ، عند $x=-2$: $6=-3B \Rightarrow B=-2$",
  truth=6/((x-1)*(x+2))),
# 2023 #11: definite integral of x a^x by parts; options = sign of the second term x lower limit kept
Q('u5e9q9', L[4], 'hard',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'x\,3^{x}', x*3**x)),
  [O(r'\frac{3\ln 3-2}{(\ln 3)^{2}}', (3*log(3)-2)/log(3)**2), O(r'\frac{3\ln 3+2}{(\ln 3)^{2}}', (3*log(3)+2)/log(3)**2),
   O(r'\frac{3\ln 3-3}{(\ln 3)^{2}}', (3*log(3)-3)/log(3)**2), O(r'\frac{3\ln 3+3}{(\ln 3)^{2}}', (3*log(3)+3)/log(3)**2)],
  r"بالأجزاء: $u=x$ ، $dv=3^xdx \Rightarrow v=\dfrac{3^x}{\ln3}$: $\displaystyle\int x3^xdx=\frac{x3^x}{\ln3}-\frac{3^x}{(\ln3)^2}$" "\n"
  r"$\left[\dfrac{x3^x}{\ln3}-\dfrac{3^x}{(\ln3)^2}\right]_0^1=\dfrac{3}{\ln3}-\dfrac{3}{(\ln3)^2}+\dfrac{1}{(\ln3)^2}=\dfrac{3\ln3-2}{(\ln3)^2}$",
  truth=ig(x*3**x, (x, 0, 1))),
# 2024 #12 / 2023 #12: velocity-time graph, start given -> final position; options = displacement vs distance x start added or not
Q('u5e9q10', L[5], 'medium',
  r"يُبيّن الشكل الآتي منحنى السرعة – الزمن لجسم يتحرّك على المحور $x$ في الفترة $[0,\,8]$. إذا بدأ الجسم الحركة من $x=2$ عندما $t=0$ ، فإنّ الموقع النهائي للجسم هو:",
  [O('6', 6, units='m'), O('16', 16, units='m'), O('4', 4, units='m'), O('14', 14, units='m')],
  r"المساحة فوق محور $t$: $\frac12(1)(3)+2(3)+\frac12(1)(3)=9$ ، وتحته: $\frac12(2)(2)+1(2)+\frac12(1)(2)=5$" "\n"
  r"الإزاحة $=9-5=4$ ، والموقع النهائي $=2+4=6\ \text{m}$",
  truth=2+pw_integral(vt9, 0, 8), figure=figure('u5e9q10', vt_graph(vt9, 8, -2, 3), 4.2, 3.0)),
# 2026 #36: volume of the root of a trig function; options = sign (ln cos) x ln root 2 vs ln 2
Q('u5e9q11', L[5], 'medium',
  F(r"حجم المُجسَّم الناتج من دوران المنطقة المحصورة بين منحنى الاقتران: $f(x)=«0»$ والمحور $x$ في الفترة $\left[0,\,\frac{\pi}{4}\right]$ حول المحور $x$ (بالوحدات المكعبة) هو:", (r'\sqrt{\tan x}', sqrt(tan(x)))),
  [O(r'\frac{\pi}{2}\ln 2', pi*log(2)/2), O(r'-\frac{\pi}{2}\ln 2', -pi*log(2)/2), O(r'\pi\ln 2', pi*log(2)), O(r'-\pi\ln 2', -pi*log(2))],
  r"$V=\pi\displaystyle\int_0^{\pi/4}\tan x\,dx=\pi\big[-\ln|\cos x|\big]_0^{\pi/4}=-\pi\ln\frac{1}{\sqrt2}=\frac{\pi}{2}\ln2$",
  truth=pi*ig(tan(x), (x, 0, pi/4))),
# 2024 #13: dy/dx = e^(px + y) through the origin; options = 1/p kept x sign
IndexQ('u5e9q12', L[6], 'medium',
  F(r"حلّ المعادلة التفاضلية: $\dfrac{dy}{dx}=«0»$ الذي يُحقّق النقطة $(0,\,0)$ هو:", (r'e^{2x+y}', exp(2*x+y))),
  [O(r'2e^{-y}=3-e^{2x}', 2*exp(-y)-3+exp(2*x), 'rel'), O(r'2e^{-y}=e^{2x}-3', 2*exp(-y)-exp(2*x)+3, 'rel'),
   O(r'e^{-y}=2-e^{2x}', exp(-y)-2+exp(2*x), 'rel'), O(r'e^{-y}=e^{2x}-2', exp(-y)-exp(2*x)+2, 'rel')],
  r"$e^{-y}dy=e^{2x}dx \Rightarrow -e^{-y}=\frac12e^{2x}+C$ ، وعند $(0,0)$: $-1=\frac12+C \Rightarrow C=-\frac32$ ، ونضرب في $-2$: $2e^{-y}=3-e^{2x}$",
  truth=lambda vals: only(vals, lambda F_: ode_ok_rel(F_, exp(2*x+y), 0, 0))),
]

# ============================================================== Exam 10
vt10 = [(0, 4), (2, 0), (3, -2), (6, -2)]
E10 = [
# 2023s #2: trig of (c - kx); options = sign x divide vs multiply by k
Q('u5e10q1', L[1], 'easy',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\cos(4-5x)', cos(4-5*x))),
  [A(r'-\frac{1}{5}\sin(4-5x)+C', -sin(4-5*x)/5), A(r'\frac{1}{5}\sin(4-5x)+C', sin(4-5*x)/5),
   A(r'-5\sin(4-5x)+C', -5*sin(4-5*x)), A(r'5\sin(4-5x)+C', 5*sin(4-5*x))],
  r"$\displaystyle\int\cos(4-5x)dx=\frac{\sin(4-5x)}{-5}+C=-\frac15\sin(4-5x)+C$ (نقسم على معامل $x$ وهو $-5$)",
  truth=cos(4-5*x)),
# 2024s #1: integral of (1/a)^(linear); options = sign (ln of 1/a) x chain factor
Q('u5e10q2', L[1], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'\left(\frac{1}{3}\right)^{2x-2}', R(1, 3)**(2*x-2))),
  [O(r'\frac{4}{\ln 3}', 4/log(3)), O(r'-\frac{4}{\ln 3}', -4/log(3)), O(r'\frac{8}{\ln 3}', 8/log(3)), O(r'-\frac{8}{\ln 3}', -8/log(3))],
  r"$\left(\frac13\right)^{2x-2}=3^{2-2x}$ ، و $\left[\dfrac{3^{2-2x}}{-2\ln3}\right]_0^1=\dfrac{1-9}{-2\ln3}=\dfrac{4}{\ln3}$",
  truth=ig(R(1, 3)**(2*x-2), (x, 0, 1))),
# 2024 #3: integral of 1/(a + x/k) from 0 to ma, a > 0; options = factor k kept x limits reversed
Q('u5e10q3', L[1], 'hard',
  F(r"قيمة: $\displaystyle\int_{0}^{2a}«0»\,dx$ ، حيث $a>0$ ، هي:", (r'\frac{1}{a+\frac{x}{4}}', 1/(a+x/4))),
  [O(r'\ln\frac{81}{16}', log(R(81, 16))), O(r'\ln\frac{3}{2}', log(R(3, 2))), O(r'\ln\frac{16}{81}', log(R(16, 81))), O(r'\ln\frac{2}{3}', log(R(2, 3)))],
  r"$\displaystyle\int\frac{1}{a+\frac x4}dx=4\ln\left(a+\frac x4\right)$ ، و $\left[4\ln\left(a+\frac x4\right)\right]_0^{2a}=4\ln\frac{3a}{2}-4\ln a=4\ln\frac32=\ln\frac{81}{16}$",
  truth=simplify(ig(1/(ap+x/4), (x, 0, 2*ap)))),
# 2023s #5: f' = e^x -+ e^(-x) and a point -> f; options = sign of e^(-x) x the constant (e^0 = 1)
IndexQ('u5e10q4', L[1], 'easy',
  F(r"إذا كان: $f'(x)=«0»$ يُمثّل ميل المماس لمنحنى الاقتران $f$ ، وكان منحنى الاقتران يمرّ بالنقطة $(0,\,3)$ ، فإنّ قاعدة الاقتران $f$ هي:", (r'e^{x}-e^{-x}', exp(x)-exp(-x))),
  [O(r'f(x)=e^{x}+e^{-x}+1', exp(x)+exp(-x)+1, 'eq'), O(r'f(x)=e^{x}-e^{-x}+3', exp(x)-exp(-x)+3, 'eq'),
   O(r'f(x)=e^{x}+e^{-x}+3', exp(x)+exp(-x)+3, 'eq'), O(r'f(x)=e^{x}-e^{-x}+1', exp(x)-exp(-x)+1, 'eq')],
  r"$f(x)=\displaystyle\int(e^x-e^{-x})dx=e^x+e^{-x}+C$ ، و $f(0)=1+1+C=3 \Rightarrow C=1$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, exp(x)-exp(-x), 0, 3))),
# 2023 #6: displacement for v = k t/(t^2 + c); options = sign x the 1/2 from du = 2t dt
Q('u5e10q5', L[2], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، وتُعطى سرعته المتجهة بالاقتران: $v(t)=«0»$ ، حيث $t$ الزمن بالثواني، و $v$ سرعته المتجهة بالمتر لكل ثانية. إزاحة الجُسيم بالأمتار في الفترة $[0,\,2]$ تساوي:", (r'\frac{-4t}{t^{2}+1}', -4*t/(t**2+1))),
  [O(r'-2\ln 5', -2*log(5)), O(r'2\ln 5', 2*log(5)), O(r'-4\ln 5', -4*log(5)), O(r'4\ln 5', 4*log(5))],
  r"$u=t^2+1 \Rightarrow du=2t\,dt$: $\displaystyle\int_0^2\frac{-4t}{t^2+1}dt=\big[-2\ln(t^2+1)\big]_0^2=-2\ln5$",
  truth=ig(-4*t/(t**2+1), (t, 0, 2))),
# 2024 #8: definite integral of k x (1 - x)^n by substitution; options = sign (limits) x (x = 1 - u vs 1 + u)
Q('u5e10q6', L[2], 'hard',
  F(r"قيمة: $\displaystyle\int_{0}^{1}«0»\,dx$ هي:", (r'12x(1-x)^{5}', 12*x*(1-x)**5)),
  [O(r'\frac{2}{7}', R(2, 7)), O(r'-\frac{2}{7}', -R(2, 7)), O(r'\frac{26}{7}', R(26, 7)), O(r'-\frac{26}{7}', -R(26, 7))],
  r"$u=1-x$ ، $x=1-u$ ، $dx=-du$ ، والحدود: $x=0\to u=1$ ، $x=1\to u=0$" "\n"
  r"$\displaystyle\int_1^0-12(1-u)u^5du=12\int_0^1(u^5-u^6)du=12\left(\frac16-\frac17\right)=\frac27$",
  truth=ig(12*x*(1-x)**5, (x, 0, 1))),
# 2024s #11: (px + q)/(cx - x^2); options = sign of the second log, ln of the denominator
Q('u5e10q7', L[3], 'medium',
  F(r"ناتج: $\displaystyle\int «0»\,dx$ هو:", (r'\frac{x+3}{2x-x^{2}}', (x+3)/(2*x-x**2))),
  [A(r'\frac{3}{2}\ln|x|-\frac{5}{2}\ln|2-x|+C', R(3, 2)*log(x)-R(5, 2)*log(2-x)), A(r'\frac{3}{2}\ln|x|+\frac{5}{2}\ln|2-x|+C', R(3, 2)*log(x)+R(5, 2)*log(2-x)),
   A(r'\ln|2x-x^{2}|+C', log(2*x-x**2)), A(r'-\ln|2x-x^{2}|+C', -log(2*x-x**2))],
  r"$\dfrac{x+3}{x(2-x)}=\dfrac{A}{x}+\dfrac{B}{2-x}$ ، عند $x=0$: $3=2A \Rightarrow A=\frac32$ ، عند $x=2$: $5=2B \Rightarrow B=\frac52$" "\n"
  r"و $\displaystyle\int\frac{\frac52}{2-x}dx=-\frac52\ln|2-x|$",
  truth=(x+3)/(2*x-x**2)),
# 2025s #5: improper fraction integrated into a given form -> a constant; options = quotient coefficient slips
Q('u5e10q8', L[3], 'medium',
  F(r"إذا كان: $\displaystyle\int «0»\,dx=ax^{2}-x+2\ln|x+1|+C$ ، فإنّ قيمة الثابت $a$ هي:", (r'\frac{3x^{2}+2x+1}{x+1}', (3*x**2+2*x+1)/(x+1))),
  [O(r'\frac{3}{2}', R(3, 2)), O('3', 3), O(r'\frac{2}{3}', R(2, 3)), O(r'\frac{1}{2}', R(1, 2))],
  r"بالقسمة: $3x^2+2x+1=(x+1)(3x-1)+2$ ، إذن التكامل $=\displaystyle\int\left(3x-1+\frac{2}{x+1}\right)dx=\frac32x^2-x+2\ln|x+1|+C$ ، و $a=\frac32$",
  truth=lambda: solve((diff(a*x**2-x+2*log(x+1), x)-(3*x**2+2*x+1)/(x+1)).subs(x, 2), a)[0]),
# 2023s #9 family: definite integral of x trig x by parts; options = sign of the second term, lower limit
Q('u5e10q9', L[4], 'medium',
  F(r"قيمة: $\displaystyle\int_{0}^{\pi/2}«0»\,dx$ هي:", (r'x\cos x', x*cos(x))),
  [O(r'\frac{\pi}{2}-1', pi/2-1), O(r'\frac{\pi}{2}+1', pi/2+1), O(r'\frac{\pi}{2}', pi/2), O(r'1-\frac{\pi}{2}', 1-pi/2)],
  r"بالأجزاء: $\displaystyle\int x\cos x\,dx=x\sin x+\cos x$ ، و $\big[x\sin x+\cos x\big]_0^{\pi/2}=\left(\frac{\pi}{2}+0\right)-(0+1)=\frac{\pi}{2}-1$",
  truth=ig(x*cos(x), (x, 0, pi/2))),
# 2023s #12: velocity-time graph starting above the axis, start given -> final position
Q('u5e10q10', L[5], 'medium',
  r"معتمدًا على الشكل المجاور الذي يُمثّل منحنى السرعة المتجهة – الزمن لجسم يتحرّك على المحور $x$ في الفترة الزمنية $[0,\,6]$. إذا بدأ الجسم الحركة من $x=5$ عندما $t=0$ ، فإنّ موقع الجسم النهائي هو:",
  [O('2', 2, units='m'), O('8', 8, units='m'), O('16', 16, units='m'), O('-3', -3, units='m')],
  r"المساحة فوق محور $t$: $\frac12(2)(4)=4$ ، وتحته: $\frac12(1)(2)+3(2)=7$ ، فالإزاحة $=4-7=-3$" "\n"
  r"الموقع النهائي $=5+(-3)=2\ \text{m}$",
  truth=5+pw_integral(vt10, 0, 6), figure=figure('u5e10q10', vt_graph(vt10, 6, -2, 4), 4.0, 3.0)),
# 2025 #3 family (figure): area between a parabola and a line; options = intersection sign slip x integral of x slip
Q('u5e10q11', L[5], 'medium',
  F(r"اعتمادًا على الشكل الآتي الذي يُبيّن منحنيي الاقترانين: $f(x)=«0»$ و $g(x)=«1»$ ، فإنّ مساحة المنطقة المُظلَّلة (بالوحدات المربعة) هي:", (r'2-x', 2-x), (r'x^{2}-4', x**2-4)),
  [O(r'\frac{125}{6}', R(125, 6)), O(r'\frac{95}{6}', R(95, 6)), O(r'\frac{70}{3}', R(70, 3)), O(r'\frac{40}{3}', R(40, 3))],
  r"التقاطع: $x^2-4=2-x \Rightarrow x^2+x-6=0 \Rightarrow (x+3)(x-2)=0 \Rightarrow x=-3,\ x=2$" "\n"
  r"$\displaystyle A=\int_{-3}^{2}(6-x-x^2)dx=\left[6x-\frac{x^2}{2}-\frac{x^3}{3}\right]_{-3}^{2}=\frac{22}{3}+\frac{27}{2}=\frac{125}{6}$",
  truth=ig((2-x)-(x**2-4), (x, -3, 2)),
  figure=figure('u5e10q11', region(2-x, x**2-4, -3, 2, (-4, 3.2), (-5, 6.5), [(-3.9, 5.2, r'$f(x)$', '#1f5fbf'), (2.3, 1.2, r'$g(x)$', '#d04a1a')]), 3.6, 3.2)),
# 2023s #13: dy/dx = trig + x e^(x^2) with an initial value; options = sign of ln|cos x| x the constant (e^0 = 1)
IndexQ('u5e10q12', L[6], 'easy',
  F(r"إذا كانت: $\dfrac{dy}{dx}=«0»$ ، فإنّ الحلّ الخاص الذي يُحقّق الشرط $y(0)=3$ هو:", (r'\tan x+2xe^{x^{2}}', tan(x)+2*x*exp(x**2))),
  [O(r'y=-\ln|\cos x|+e^{x^{2}}+2', -log(cos(x))+exp(x**2)+2, 'eq'), O(r'y=\ln|\cos x|+e^{x^{2}}+2', log(cos(x))+exp(x**2)+2, 'eq'),
   O(r'y=-\ln|\cos x|+e^{x^{2}}+3', -log(cos(x))+exp(x**2)+3, 'eq'), O(r'y=\ln|\cos x|+e^{x^{2}}+3', log(cos(x))+exp(x**2)+3, 'eq')],
  r"$y=\displaystyle\int\left(\tan x+2xe^{x^2}\right)dx=-\ln|\cos x|+e^{x^2}+C$ ، و $y(0)=0+1+C=3 \Rightarrow C=2$",
  truth=lambda vals: only(vals, lambda Y_: ode_ok(Y_, tan(x)+2*x*exp(x**2), 0, 3))),
]

EXAMS_5_10 = [('الاختبار الخامس', E5), ('الاختبار السادس', E6), ('الاختبار السابع', E7),
              ('الاختبار الثامن', E8), ('الاختبار التاسع', E9), ('الاختبار العاشر', E10)]
