"""Semester-1 mock papers 6-10 (m6q1..m10q30), same layout as papers 1-5:
U1 items 1-4, U2 items 5-10, U3 items 11-22, U4 items 23-30.
Every item is modelled on a named official ministry item (the comment above each Q gives it: 2026 = paper of
2 July 2026, gen 2008; 2025/2024 = summer paper 1; 2025s/2024s = supplementary; 2026r = 2026 repeaters; 2023 =
summer paper 1), or "E" for an expected item (a 2008-book skill not asked yet, ministry template, no harder than
the ministry items of its lesson): same skill, same stem structure, same kind of function and numbers, same option
grid -- new function and numbers. Region items are checked by sampling: each option is a predicate, the shaded figure is drawn
from the correct predicate, and the distractors must differ from it inside the plane or on its boundary."""
import cmath
import math
from s1_helpers import *
from s1_helpers import _sketch


# ================================================================== PAPER 6
# Each item names the official item it is modelled on (2026 = 2 July 2026 paper, gen 2008; 2025/2024 = summer
# paper 1; 2025s/2024s = supplementary; 2026r = 2026 repeaters; E = a 2008-book skill the ministry has not asked yet,
# written with a ministry template). Same skill, same stem structure, same kind of function and numbers, same option
# grid -- new function and numbers.
F6, G6 = [(0, 5), (4, 1), (6, 3)], [(0, 0), (2, 4), (6, 2)]
_q6 = complex(1 - (math.sqrt(2) + math.sqrt(34))/2/math.sqrt(2), -1 + (math.sqrt(2) + math.sqrt(34))/2/math.sqrt(2))
R6 = both(disk(-1j, 3), sector(1 - 1j, 0, 3*math.pi/4, hi_open=True))
PR6 = [('arc', -1j, 3, False, (0.0, cmath.phase(_q6 + 1j))), ('seg', 1 - 1j, 3 - 1j, False), ('seg', 1 - 1j, _q6, True), ('open', 1 - 1j)]
P6 = [
# ---------------- unit 1
# E (expected: factor theorem, (x + 2) is a factor -> the constant), template 2026 #3:
# options = sign x magnitude (10 = the value of -2k, not divided by -2)
Q('m6q1', U1[1], 'easy',
  F(r"إذا كان $(x+2)$ أحد عوامل الاقتران: $f(x)=«0»$ ، فإنّ قيمة الثابت $k$ هي:", (r'x^{3}-x^{2}+kx+2', x**3-x**2+k*x+2)),
  [O('-5', -5), O('5', 5), O('-10', -10), O('10', 10)],
  r"$(x+2)$ عامل $\Rightarrow f(-2)=0$: $-8-4-2k+2=0$" "\n" r"$-10-2k=0 \Rightarrow -2k=10 \Rightarrow k=-5$",
  truth=lambda: solve(rem(x**3-x**2+k*x+2, -2), k)[0], tag='نظرية العوامل وإيجاد ثابت'),
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
# E (expected: decomposition with distinct linear factors), template 2026 #2: which is the decomposition;
# options = numerators swapped x signs of the factors
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
# 2026 #5: simplest form with a sum identity (cos(x + pi/3) + k sin x, the sin terms cancel); options = coefficient x cos/sin
Q('m6q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x+\frac{\pi}{3})+\frac{\sqrt{3}}{2}\sin x', cos(x+pi/3)+sqrt(3)/2*sin(x))),
  [O(r'\frac{1}{2}\cos x', cos(x)/2), O(r'\frac{\sqrt{3}}{2}\cos x', sqrt(3)/2*cos(x)), O(r'\frac{1}{2}\sin x', sin(x)/2), O(r'\frac{\sqrt{3}}{2}\sin x', sqrt(3)/2*sin(x))],
  r"$\cos\left(x+\frac{\pi}{3}\right)=\frac12\cos x-\frac{\sqrt3}{2}\sin x$ ، وبإضافة $\frac{\sqrt3}{2}\sin x$ يبقى $\frac12\cos x$",
  truth=cos(x+pi/3)+sqrt(3)/2*sin(x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# E (expected: simplest form with related angles pi + x, pi/2 - x and the even function cos), template 2026 #5 grid:
# options = sign of sin(pi + x) x cofunction cos(pi/2 - x) = sin x right or wrong (cos vs sin survives)
Q('m6q7', U2[1], 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\dfrac{\sin(\pi+x)\cos(-x)}{\cos(\frac{\pi}{2}-x)}', sin(pi+x)*cos(-x)/cos(pi/2-x))),
  [O(r'-\cos x', -cos(x)), O(r'\cos x', cos(x)), O(r'-\sin x', -sin(x)), O(r'\sin x', sin(x))],
  r"$\sin(\pi+x)=-\sin x$ ، $\cos(-x)=\cos x$ ، $\cos\left(\frac{\pi}{2}-x\right)=\sin x$" "\n" r"$\dfrac{(-\sin x)\cos x}{\sin x}=-\cos x$",
  truth=sin(pi+x)*cos(-x)/cos(pi/2-x), tag='المتطابقات: الزوايا المنتسبة والزوجية والفردية'),
# E (expected: double-angle exact value from 1 - 2sin^2 a = cos 2a), template 2026 #9 grid (double angle):
# options = sign (quadrant of 2a) x cos 2a vs sin 2a
Q('m6q8', U2[2], 'easy',
  F(r"قيمة المقدار: $«0»$ هي:", (r'1-2\sin^{2}\frac{7\pi}{12}', 1-2*sin(7*pi/12)**2)),
  [O(r'-\frac{\sqrt{3}}{2}', -sqrt(3)/2), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2))],
  r"$1-2\sin^2a=\cos2a$ ، فالمقدار $\cos\frac{7\pi}{6}$" "\n" r"$\frac{7\pi}{6}$ في الربع الثالث: $\cos\frac{7\pi}{6}=-\cos\frac{\pi}{6}=-\frac{\sqrt3}{2}$",
  truth=1-2*sin(7*pi/12)**2, tag='قيم دقيقة بمتطابقات ضعف الزاوية'),
# 2026 #7: quadratic in sin x factoring as (sin x - 2)(sin x + 1), one root rejected, single quadrantal answer;
# options = the four quadrantal angles (sign slip in the factors / sin-cos confusion)
Q('m6q9', U2[3], 'easy',
  F(r"حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هو:", (r'\sin^{2}x-\sin x-2', sin(x)**2-sin(x)-2)),
  [O(st(r'\frac{3\pi}{2}'), S_(3*P/2), 'set'), O(st(r'\frac{\pi}{2}'), S_(P/2), 'set'), O(st(r'\pi'), S_(P), 'set'), O(st('0'), S_(0), 'set')],
  r"$(\sin x-2)(\sin x+1)=0$ ، و $\sin x=2$ مرفوض لأنّ $-1\le\sin x\le1$" "\n" r"$\sin x=-1 \Rightarrow x=\frac{3\pi}{2}$",
  truth=lambda: sols(sin(x)**2-sin(x)-2, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
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
# 2025s #5 (also 2025 #5): slope of the normal to a^(linear) at a point; options = tangent vs normal slope x sign (2025s #5 grid)
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
# 2026 #12 (temperature after sunset -> a patient's temperature after a fever reducer): c + k/(t + 1)^2, rate at t = 1,
# units in stem and options; options = sign x the factor 2 of the power dropped (2026 #12 grid)
Q('m6q15', U3[3], 'medium',
  F(r"إذا أمكن التعبير عن درجة حرارة جسم مريض بالحُمّى بعد تناوله دواءً خافضًا للحرارة بالاقتران: $T(t)=«0»$ ، حيث $t$ الزمن بالساعات، و $T$ درجة الحرارة بالسيلسيوس، فإنّ معدّل تغيّر درجة حرارة جسم المريض عندما $t=1$ هو:", (r'37+\frac{3}{(t+1)^{2}}', 37+3/(t+1)**2)),
  [O(r'-\frac{3}{4}', -R(3, 4), units='°C/h'), O(r'\frac{3}{4}', R(3, 4), units='°C/h'), O(r'-\frac{3}{8}', -R(3, 8), units='°C/h'), O(r'\frac{3}{8}', R(3, 8), units='°C/h')],
  r"$T(t)=37+3(t+1)^{-2} \Rightarrow T'(t)=-6(t+1)^{-3}$" "\n" r"$T'(1)=-\dfrac{6}{8}=-\dfrac34\ ^\circ\text{C/h}$",
  truth=diff(37+3/(t+1)**2, t).subs(t, 1), tag='معدل التغير في سياق حياتي'),
# 2024s #5: h = f g read from two graphs (product rule), graphs and options in the 2026 #14 format
# (two piecewise-linear graphs on a grid; options = sign x magnitude)
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
# 2025 #9: h = root of (c + f^m) from the values f(a), f'(a); options = sign x missing 1/2 (model: sign x missing inner factor)
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
# 2024s #12 (ripples -> an oil spill): dA/dt given -> dC/dt at a radius; options = factor 2 x pi slip (3/pi = dr/dt, as the model)
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
# 2026 #20: first item of a shared stem (z + iw + k -> 2z - iw); options = i^2 = +1 slip x sign slip in the imaginary part
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
# 2025 #19: z - k conj(z) = a + bi -> z; options = sign of the imaginary part (z vs conj z) x real and imaginary parts swapped
Q('m6q26', U4[1], 'medium',
  r"إذا كان $z$ عددًا مركّبًا، وكان: $z-3\bar{z}=-4+12i$ ، فإنّ $z$ هو:",
  [O('2+3i', 2+3*I), O('2-3i', 2-3*I), O('3+2i', 3+2*I), O('3-2i', 3-2*I)],
  r"نفرض $z=a+bi$: $a+bi-3(a-bi)=-2a+4bi=-4+12i$" "\n" r"$-2a=-4 \Rightarrow a=2$ ، $4b=12 \Rightarrow b=3$ ، إذن $z=2+3i$",
  truth=lambda: (lambda s_: s_[X]+s_[Y]*I)(solve([re(expand(X+Y*I-3*(X-Y*I)+4-12*I)), im(expand(X+Y*I-3*(X-Y*I)+4-12*I))], [X, Y])),
  tag='معادلة فيها العدد ومرافقه'),
# 2026 #22: two values of a constant making a quotient real; options = +-k list
Q('m6q27', U4[2], 'medium',
  r"إذا كان: $z=\dfrac{a+8i}{2+ai}$ ، فإنّ القيمتين المُمكنتين للثابت $a$ اللتين تجعلان $z$ عددًا حقيقيًّا هما:",
  [O(r'\pm 4', S_(4, -4), 'set'), O(r'\pm 2', S_(2, -2), 'set'), O(r'\pm 8', S_(8, -8), 'set'), O(r'\pm 1', S_(1, -1), 'set')],
  r"نضرب في مرافق المقام: $(a+8i)(2-ai)=2a-a^2i+16i+8a=10a+(16-a^2)i$" "\n" r"حقيقي: $16-a^2=0 \Rightarrow a=\pm4$",
  truth=lambda: FiniteSet(*solve(im(expand((X+8*I)*(2-X*I))), X)), tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
# 2026 #23: quadratic with a given complex root; options = sign of the sum x sum/product swapped
Q('m6q28', U4[2], 'easy',
  r"المعادلة التربيعية التي أحد جذريها العدد المركّب $(3-2i)$ هي:",
  [O(r'x^{2}-6x+13=0', x**2-6*x+13, 'rel'), O(r'x^{2}+6x+13=0', x**2+6*x+13, 'rel'),
   O(r'x^{2}-13x+6=0', x**2-13*x+6, 'rel'), O(r'x^{2}+13x+6=0', x**2+13*x+6, 'rel')],
  r"الجذر الآخر هو المرافق $3+2i$ ، المجموع $6$ والضرب $(3-2i)(3+2i)=9+4=13$" "\n" r"$x^2-Sx+P=0 \Rightarrow x^2-6x+13=0$",
  truth=expand((x-(3-2*I))*(x-(3+2*I))), tag='معادلة تربيعية بمعلومية جذر مركب'),
# 2026 #24: smaller angle between two numbers in the lower half-plane (difference of the arguments < pi);
# options = the difference / the sizes added / one argument alone / reference angles subtracted
Q('m6q29', U4[1], 'medium',
  r"إذا كان: $z_1=3-i\sqrt{3}$ ، $z_2=-2-2i\sqrt{3}$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{\pi}{2}', P/2), O(r'\frac{5\pi}{6}', 5*P/6), O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{\pi}{6}', P/6)],
  r"$\text{Arg}(z_1)=-\frac{\pi}{6}$ (الربع الرابع) ، $\text{Arg}(z_2)=-\pi+\frac{\pi}{3}=-\frac{2\pi}{3}$ (الربع الثالث)" "\n"
  r"الزاوية الصغرى $\left|-\frac{\pi}{6}+\frac{2\pi}{3}\right|=\frac{\pi}{2}$ (وهي أقل من $\pi$)",
  truth=smaller_angle(3-sqrt(3)*I, -2-2*sqrt(3)*I), tag='الزاوية بين عددين مركبين'),
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
N7_ = Symbol('N')


def fig_drone7():
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
# E (expected: decomposition with an irreducible quadratic factor), template 2026 #2: which is the decomposition; options = A halved or not x sign of the linear numerator
Q('m7q2', U1[2], 'medium',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{3x^{2}+1}{(x-1)(x^{2}+1)}', (3*x**2+1)/((x-1)*(x**2+1)))),
  [O(r'\frac{2}{x-1}+\frac{x+1}{x^{2}+1}', 2/(x-1)+(x+1)/(x**2+1)), O(r'\frac{4}{x-1}+\frac{x+1}{x^{2}+1}', 4/(x-1)+(x+1)/(x**2+1)),
   O(r'\frac{2}{x-1}+\frac{x-1}{x^{2}+1}', 2/(x-1)+(x-1)/(x**2+1)), O(r'\frac{4}{x-1}+\frac{x-1}{x^{2}+1}', 4/(x-1)+(x-1)/(x**2+1))],
  r"$3x^2+1=A(x^2+1)+(Bx+C)(x-1)$" "\n" r"عند $x=1$: $4=2A \Rightarrow A=2$ ، معامل $x^2$: $3=A+B \Rightarrow B=1$ ، الحدّ الثابت: $1=A-C \Rightarrow C=1$",
  truth=(3*x**2+1)/((x-1)*(x**2+1)), tag='تجزئة: عامل تربيعي غير قابل للتحليل'),
# E (expected: factor theorem then remainder theorem), template 2026 #3: the factor (x - 2) gives a at once, then the remainder on (x + 1) is f(-1); options = sign slip in a x zero of (x + 1) taken as 1
Q('m7q3', U1[1], 'medium',
  F(r"إذا كان $(x-2)$ أحد عوامل الاقتران: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x+1)$ يساوي $b$ ، فإنّ قيمتي الثابتين $a$ و $b$ هما:", (r'x^{3}+ax^{2}-4x+4', x**3+a*x**2-4*x+4)),
  [O(r'a=-1,\ b=6', Tuple(-1, 6), 'pairs'), O(r'a=-1,\ b=0', Tuple(-1, 0), 'pairs'), O(r'a=1,\ b=8', Tuple(1, 8), 'pairs'), O(r'a=1,\ b=2', Tuple(1, 2), 'pairs')],
  r"$f(2)=8+4a-8+4=0 \Rightarrow 4a=-4 \Rightarrow a=-1$" "\n" r"$b=f(-1)=-1+a+4+4=7+a=6$",
  truth=lambda: (lambda a_: Tuple(a_, rem((x**3+a*x**2-4*x+4).subs(a, a_), -1)))(solve(rem(x**3+a*x**2-4*x+4, 2), a)[0]),
  tag='نظرية الباقي والعوامل معًا'),
# E (expected: remainder theorem with high powers of -1), template 2026 #3: remainder on (x + 1) = f(-1); options = the parity slips
Q('m7q4', U1[1], 'easy',
  F(r"باقي قسمة الاقتران: $f(x)=«0»$ على $(x+1)$ هو:", (r'x^{20}-3x^{9}+2', x**20-3*x**9+2)),
  [O('6', 6), O('4', 4), O('0', 0), O('-2', -2)],
  r"الباقي $f(-1)=(-1)^{20}-3(-1)^9+2=1+3+2=6$",
  truth=rem(x**20-3*x**9+2, -1), tag='نظرية الباقي: قوى عالية'),
# ---------------- unit 2
# E (expected: product to sum, exact value), template 2026 #5 (special values): cos A cos B with A - B = pi/6, A + B = pi/4; options = + vs - between the cosines x factor 1/2 kept/lost
Q('m7q5', U2[2], 'easy',
  F(r"قيمة المقدار: $«0»$ هي:", (r'\cos\frac{5\pi}{24}\cos\frac{\pi}{24}', cos(5*pi/24)*cos(pi/24))),
  [O(r'\frac{\sqrt{3}+\sqrt{2}}{4}', (sqrt(3)+sqrt(2))/4), O(r'\frac{\sqrt{3}-\sqrt{2}}{4}', (sqrt(3)-sqrt(2))/4),
   O(r'\frac{\sqrt{3}+\sqrt{2}}{2}', (sqrt(3)+sqrt(2))/2), O(r'\frac{\sqrt{3}-\sqrt{2}}{2}', (sqrt(3)-sqrt(2))/2)],
  r"$\cos A\cos B=\frac12\left[\cos(A-B)+\cos(A+B)\right]$" "\n"
  r"$\frac12\left[\cos\frac{\pi}{6}+\cos\frac{\pi}{4}\right]=\frac12\left[\frac{\sqrt3}{2}+\frac{\sqrt2}{2}\right]=\frac{\sqrt3+\sqrt2}{4}$",
  truth=cos(5*pi/24)*cos(pi/24), tag='تحويل الضرب إلى مجموع'),
# 2026 #5 with a difference identity; options = coefficient x sin/cos
Q('m7q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x-\frac{\pi}{4})-\frac{\sqrt{2}}{2}\sin x', cos(x-pi/4)-sqrt(2)/2*sin(x))),
  [O(r'\frac{\sqrt{2}}{2}\cos x', sqrt(2)/2*cos(x)), O(r'\frac{\sqrt{2}}{2}\sin x', sqrt(2)/2*sin(x)), O(r'\sqrt{2}\cos x', sqrt(2)*cos(x)), O(r'\sqrt{2}\sin x', sqrt(2)*sin(x))],
  r"$\cos\left(x-\frac{\pi}{4}\right)=\cos x\cdot\frac{\sqrt2}{2}+\sin x\cdot\frac{\sqrt2}{2}$ ، وبطرح $\frac{\sqrt2}{2}\sin x$ يبقى $\frac{\sqrt2}{2}\cos x$",
  truth=cos(x-pi/4)-sqrt(2)/2*sin(x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# E (expected: tan(pi/4 + x) = k -> tan x), template 2026 #4 grid: tangent-sum identity, then a linear equation; options = sign of tan x in the identity x numerator/denominator order (reciprocal)
Q('m7q7', U2[1], 'medium',
  F(r"إذا كان: $«0»=5$ ، فإنّ قيمة $\tan x$ هي:", (r'\tan\left(\frac{\pi}{4}+x\right)', tan(pi/4+x))),
  [O(r'\frac{2}{3}', R(2, 3)), O(r'-\frac{2}{3}', -R(2, 3)), O(r'\frac{3}{2}', R(3, 2)), O(r'-\frac{3}{2}', -R(3, 2))],
  r"$\tan\left(\frac{\pi}{4}+x\right)=\dfrac{1+\tan x}{1-\tan x}=5$" "\n" r"$1+\tan x=5-5\tan x \Rightarrow 6\tan x=4 \Rightarrow \tan x=\dfrac23$",
  truth=tan(atan(5)-pi/4), tag='ظل المجموع والفرق: tan(π/4 ± x)'),
# E (expected: exact value by a difference identity), template 2026 #5: sin(pi/3 - pi/4) with exact values; options = order of the surds x sum vs difference
Q('m7q8', U2[1], 'easy',
  r"قيمة $\sin\frac{\pi}{12}$ هي:",
  [O(r'\frac{\sqrt{6}-\sqrt{2}}{4}', (sqrt(6)-sqrt(2))/4), O(r'\frac{\sqrt{2}-\sqrt{6}}{4}', (sqrt(2)-sqrt(6))/4),
   O(r'\frac{\sqrt{6}+\sqrt{2}}{4}', (sqrt(6)+sqrt(2))/4), O(r'-\frac{\sqrt{6}+\sqrt{2}}{4}', -(sqrt(6)+sqrt(2))/4)],
  r"$\frac{\pi}{12}=\frac{\pi}{3}-\frac{\pi}{4}$" "\n" r"$\sin\frac{\pi}{3}\cos\frac{\pi}{4}-\cos\frac{\pi}{3}\sin\frac{\pi}{4}=\frac{\sqrt3}{2}\cdot\frac{\sqrt2}{2}-\frac12\cdot\frac{\sqrt2}{2}=\frac{\sqrt6-\sqrt2}{4}$",
  truth=sin(pi/12), tag='قيم دقيقة بمتطابقات المجموع والفرق'),
# E (expected: Pythagorean substitution -> quadratic in cos x), template 2026 #7: factorable quadratic in cos x, three solutions; options = include 0 x sign of cos
Q('m7q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\sin^{2}x+3\cos x-3', 2*sin(x)**2+3*cos(x)-3)),
  [O(st('0', r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(0, P/3, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'),
   O(st('0', r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(0, 2*P/3, 4*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set')],
  r"$2(1-\cos^2x)+3\cos x-3=0 \Rightarrow 2\cos^2x-3\cos x+1=0 \Rightarrow (2\cos x-1)(\cos x-1)=0$" "\n"
  r"$\cos x=1 \Rightarrow x=0$ ، $\cos x=\frac12 \Rightarrow x=\frac{\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*sin(x)**2+3*cos(x)-3, 0, 2*pi), tag='معادلة تربيعية بعد استعمال متطابقة فيثاغورس'),
# 2026 #8: reciprocal ratio -> sin 2x = -1/2 on the half-period interval (pi, 2pi), doubled for 2x; options = halved or not x interval doubled or not
Q('m7q10', U2[3], 'hard',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $(\pi,\,2\pi)$ هي:", (r'4\cos x+\csc x', 4*cos(x)+csc(x))),
  [O(st(r'\frac{19\pi}{12}', r'\frac{23\pi}{12}'), S_(19*P/12, 23*P/12), 'set'), O(st(r'\frac{7\pi}{12}', r'\frac{11\pi}{12}'), S_(7*P/12, 11*P/12), 'set'),
   O(st(r'\frac{19\pi}{6}', r'\frac{23\pi}{6}'), S_(19*P/6, 23*P/6), 'set'), O(st(r'\frac{7\pi}{6}', r'\frac{11\pi}{6}'), S_(7*P/6, 11*P/6), 'set')],
  r"نضرب في $\sin x\ne0$: $4\sin x\cos x=-1 \Rightarrow 2\sin2x=-1 \Rightarrow \sin2x=-\frac12$" "\n"
  r"$2\pi<2x<4\pi$: $2x=\frac{19\pi}{6},\ \frac{23\pi}{6} \Rightarrow x=\frac{19\pi}{12},\ \frac{23\pi}{12}$",
  truth=lambda: sols(4*cos(x)+csc(x), pi, 2*pi, closed_lo=False), tag='معادلة فيها مقلوب نسبة وزاوية مضاعفة'),
# ---------------- unit 3
# 2025 #2 / 2026r #5: value of the derivative of a trig combination; options = sec^2 vs sec x sign of the cos term
Q('m7q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{3}\right)$ هي:", (r'2\tan x-4\cos x', 2*tan(x)-4*cos(x))),
  [O(r'8+2\sqrt{3}', 8+2*sqrt(3)), O(r'8-2\sqrt{3}', 8-2*sqrt(3)), O(r'4+2\sqrt{3}', 4+2*sqrt(3)), O(r'4-2\sqrt{3}', 4-2*sqrt(3))],
  r"$f'(x)=2\sec^2x+4\sin x$" "\n" r"$f'\left(\frac{\pi}{3}\right)=2(2)^2+4\cdot\frac{\sqrt3}{2}=8+2\sqrt3$",
  truth=Dx(2*tan(x)-4*cos(x)).subs(x, pi/3), tag='مشتقات الاقترانات المثلثية'),
# 2024 #6: x-coordinate where the tangent is parallel to a given line (exponential minus linear); options = chain factor 2 lost / slope sign / ln 4 not halved
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
  truth=lambda: solve(diff(N7_*exp(t/2), t).subs(t, 4)-300*E**2, N7_)[0], tag='معدل التغير في سياق حياتي'),
# 2024s #7: third derivative of a polynomial plus a reciprocal; options = sign x keeping a constant
Q('m7q14', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، $x\ne0$ ، فإنّ $f'''(x)$ هي:", (r'3x^{2}-\frac{2}{x}', 3*x**2-2/x)),
  [O(r'\frac{12}{x^{4}}', 12/x**4), O(r'-\frac{12}{x^{4}}', -12/x**4), O(r'6+\frac{12}{x^{4}}', 6+12/x**4), O(r'6-\frac{12}{x^{4}}', 6-12/x**4)],
  r"$f'(x)=6x+2x^{-2}$ ، $f''(x)=6-4x^{-3}$ ، $f'''(x)=12x^{-4}=\dfrac{12}{x^4}$",
  truth=diff(3*x**2-2/x, x, 3), tag='المشتقات العليا'),
# 2026r #3 (h = f/(g + 1)) / 2024s #5 (both rule terms): two piecewise-linear graphs, h = f/g at a grid point; options = numerator order x slope sign
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
# 2026r #9: dy/dx of log (base 10, not written) of a polynomial, domain given; options = ln 10 below / above / missing, or the fraction inverted
Q('m7q17', U3[3], 'medium',
  r"إذا كان: $y=\log(x^{3}+3x)$ ، $x>0$ ، فإنّ $\dfrac{dy}{dx}$ هي:",
  [O(r'\frac{3x^{2}+3}{(x^{3}+3x)\ln 10}', (3*x**2+3)/((x**3+3*x)*log(10))), O(r'\frac{(3x^{2}+3)\ln 10}{x^{3}+3x}', (3*x**2+3)*log(10)/(x**3+3*x)),
   O(r'\frac{3x^{2}+3}{x^{3}+3x}', (3*x**2+3)/(x**3+3*x)), O(r'\frac{x^{3}+3x}{3x^{2}+3}', (x**3+3*x)/(3*x**2+3))],
  r"$\dfrac{d}{dx}\log u=\dfrac{u'}{u\ln10}$ ، و $u=x^3+3x$ ، $u'=3x^2+3$" "\n" r"$\dfrac{dy}{dx}=\dfrac{3x^2+3}{(x^3+3x)\ln10}$",
  truth=Dx(log(x**3+3*x, 10)), tag='مشتقة اللوغاريتم لأساس غير e'),
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
# E (expected: normal line to an implicit curve), template 2026 #17: a line at a lattice point of an implicit curve, one intercept asked; options = normal vs tangent x x- vs y-intercept
Q('m7q20', U3[4], 'medium',
  F(r"إذا مثّل المستقيم $l$ العمودي على المماس لمنحنى العلاقة: $«0»=20$ عند النقطة $(4,\,2)$ ، فإنّ المقطع $x$ للمستقيم $l$ هو:", (r'xy+2x+y^{2}', x*y+2*x+y**2)),
  [O('3', 3), O('-6', -6), O('8', 8), O('4', 4)],
  r"$y+xy'+2+2yy'=0 \Rightarrow y'=-\dfrac{y+2}{x+2y}=-\dfrac48=-\dfrac12$ عند $(4,2)$" "\n" r"ميل العمودي $2$: $y-2=2(x-4)$ ، وعند $y=0$: $x=3$",
  truth=lambda: (lambda m_: 4 - 2/(-1/m_))(imp(x*y+2*x+y**2-20, (4, 2))), tag='العمودي على المماس لمنحنى علاقة ضمنية'),
# 2024 #10: dy/dx (slope at any point) of x^(ln x) by logarithmic differentiation, answer in x and y; options = factor y kept/forgotten x factor 2 of (ln x)^2
Q('m7q21', U3[4], 'medium',
  F(r"إذا كانت: $y=«0»$ ، $x>0$ ، فإنّ ميل المماس لمنحنى العلاقة عند أيّ نقطة تقع عليها هو:", (r'x^{\ln x}', x**log(x))),
  [O(r'\frac{2y\ln x}{x}', 2*x**log(x)*log(x)/x, sym={'y': x**log(x)}), O(r'\frac{2\ln x}{x}', 2*log(x)/x),
   O(r'\frac{y\ln x}{x}', x**log(x)*log(x)/x, sym={'y': x**log(x)}), O(r'\frac{\ln x}{x}', log(x)/x)],
  r"$\ln y=\ln x\cdot\ln x=(\ln x)^2$" "\n" r"$\dfrac1y\dfrac{dy}{dx}=\dfrac{2\ln x}{x} \Rightarrow \dfrac{dy}{dx}=\dfrac{2y\ln x}{x}$",
  truth=Dx(x**log(x)), tag='الاشتقاق اللوغاريتمي'),
# 2024 #11: angle of elevation of an object rising vertically, watched from a point a fixed distance away (figure); dtheta/dt at a given height; options = sign x sec^2 kept/forgotten
Q('m7q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي طائرة مُسيّرة ترتفع رأسيًّا بسرعة $15\ \text{m/min}$ ، ويرصدها شخص عند النقطة $A$ التي تبعد $40\ \text{m}$ عن نقطة إقلاعها. معدّل تغيّر زاوية الارتفاع $\theta$ عندما يكون ارتفاع الطائرة $30\ \text{m}$ هو:",
  [O(r'\frac{6}{25}', R(6, 25), units='rad/min'), O(r'\frac{3}{8}', R(3, 8), units='rad/min'), O(r'-\frac{6}{25}', -R(6, 25), units='rad/min'), O(r'-\frac{3}{8}', -R(3, 8), units='rad/min')],
  r"$\tan\theta=\dfrac{h}{40} \Rightarrow \sec^2\theta\dfrac{d\theta}{dt}=\dfrac{1}{40}\dfrac{dh}{dt}$" "\n"
  r"عندما $h=30$: الوتر $50$ ، $\cos\theta=\frac45$ ، $\dfrac{d\theta}{dt}=\dfrac{15}{40}\cdot\dfrac{16}{25}=\dfrac{6}{25}\ \text{rad/min}$",
  truth=(diff(atan(s/40), s)*15).subs(s, 30), figure=figure('m7q22', fig_drone7(), 3.4, 2.8), tag='معدلات مرتبطة: معدل تغير زاوية'),
# ---------------- unit 4
# 2025 #18: trigonometric form of a number shown as a point (here in the third quadrant); options = sign of the argument (quadrant III vs II) x reference angle pi/6 vs pi/3
Q('m7q23', U4[1], 'easy',
  r"الصورة المثلثية للعدد المركّب $w$ المُمثَّل في المستوى المركّب الآتي هي:",
  [O(trig('2', r'-\frac{5\pi}{6}'), pol(2, -5*P/6)), O(trig('2', r'\frac{5\pi}{6}'), pol(2, 5*P/6)),
   O(trig('2', r'-\frac{2\pi}{3}'), pol(2, -2*P/3)), O(trig('2', r'\frac{2\pi}{3}'), pol(2, 2*P/3))],
  r"$w=-\sqrt3-i$ ، $|w|=\sqrt{3+1}=2$ ، وهو في الربع الثالث" "\n" r"زاوية الإسناد $\tan\theta=\dfrac{1}{\sqrt3} \Rightarrow \theta=\frac{\pi}{6}$ ، و $\text{Arg}(w)=-\left(\pi-\frac{\pi}{6}\right)=-\frac{5\pi}{6}$",
  truth=-sqrt(3)-I, figure=figure('m7q23', fig_point(-math.sqrt(3), -1, r'$-\sqrt{3}$', r'$-1$', 'w', 3), 3.0, 3.0),
  tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2025 #21: first item of a shared stem, Arg(z - w) on a diagonal (reference angle pi/4); options = the four angles with reference pi/4
Q('m7q24', U4[1], 'easy',
  r"قيمة $\text{Arg}(z-w)$ هي:",
  [O(r'-\frac{\pi}{4}', -P/4), O(r'\frac{\pi}{4}', P/4), O(r'-\frac{3\pi}{4}', -3*P/4), O(r'\frac{3\pi}{4}', 3*P/4)],
  r"$z-w=(4-1)+(-1-2)i=3-3i$ في الربع الرابع، وزاوية الإسناد $\frac{\pi}{4}$ ، إذن $\text{Arg}(z-w)=-\frac{\pi}{4}$",
  truth=arg(3-3*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=4-i$ ، $w=1+2i$", 24, 25)),
# 2026r #21: the quotient z/w of the shared numbers (there it is the first item of the stem); options = i^2 slip x conjugate slip
Q('m7q25', U4[2], 'medium',
  r"ناتج $\dfrac{z}{w}$ هو:",
  [O(r'\frac{2}{5}-\frac{9}{5}i', R(2, 5)-R(9, 5)*I), O(r'\frac{6}{5}-\frac{9}{5}i', R(6, 5)-R(9, 5)*I),
   O(r'\frac{2}{5}+\frac{9}{5}i', R(2, 5)+R(9, 5)*I), O(r'\frac{6}{5}+\frac{7}{5}i', R(6, 5)+R(7, 5)*I)],
  r"$\dfrac{4-i}{1+2i}\cdot\dfrac{1-2i}{1-2i}=\dfrac{4-8i-i+2i^2}{1+4}=\dfrac{2-9i}{5}$",
  truth=(4-I)/(1+2*I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2025s #25: |z1 z2| given -> the two values of p in z1 = a + pi (|z2| = 5 from 3 + 4i); options = +-k pairs (+-10 = |z1| itself)
Q('m7q26', U4[1], 'medium',
  r"إذا كان: $z_1=8+pi$ ، $z_2=3+4i$ ، وكان: $|z_1z_2|=50$ ، فإنّ القيمتين المُمكنتين للثابت $p$ هما:",
  [O(r'\pm 6', S_(6, -6), 'set'), O(r'\pm 2', S_(2, -2), 'set'), O(r'\pm 8', S_(8, -8), 'set'), O(r'\pm 10', S_(10, -10), 'set')],
  r"$|z_1z_2|=|z_1||z_2|=5|z_1|=50 \Rightarrow |z_1|=10$" "\n" r"$64+p^2=100 \Rightarrow p^2=36 \Rightarrow p=\pm6$",
  truth=lambda: FiniteSet(*solve(5*sqrt(64+X**2)-50, X)), tag='إيجاد ثابت بمعلومية المقياس'),
# 2026r #24 / 2025s #24: complex root with one unknown part of a real quadratic -> a + b; options = sign of b x a vs a^2
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
# 2023 #24: greatest Arg of the points on a circle |z - c| = r with |c| = 2r; options = multiples of pi/6 (pi/6 = Arg of the centre, 0 = least value)
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


L8 = [('seg', complex(-1.5, -5), complex(3.5, 5), False)]   # y = 2x - 2


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
# E (expected: factor theorem in an application), template 2026 #1: volume of a cylindrical can and its height (x + 3)
# given -> divide, the quotient is r^2 = (x + 2)^2; options = sign x radius vs diameter
Q('m8q1', U1[1], 'medium',
  F(r"يُمثّل الاقتران: $V(x)=«0»$ حجم علبة على شكل أسطوانة دائرية قائمة بالسنتيمتر المكعب. إذا كان ارتفاع العلبة $(x+3)\ \text{cm}$ ، فإنّ طول قُطر قاعدتها هو:", (r'\pi(x^{3}+7x^{2}+16x+12)', pi*(x**3+7*x**2+16*x+12))),
  [O('2x+4', 2*x+4, units='cm'), O('x+2', x+2, units='cm'), O('2x-4', 2*x-4, units='cm'), O('x-2', x-2, units='cm')],
  r"$V=\pi r^2h$ ، وبالقسمة التركيبية على $(x+3)$: $1,\ 7,\ 16,\ 12 \to 1,\ 4,\ 4,\ 0$" "\n"
  r"$r^2=x^2+4x+4=(x+2)^2 \Rightarrow r=x+2$ ، فطول القُطر $2r=2x+4\ \text{cm}$",
  truth=lambda: (lambda p_: (2*sqrt(factor(cancel(pi*(x**3+7*x**2+16*x+12)/(pi*(x+3)))).subs(x, p_))).subs(p_, x))(Symbol('p8', positive=True)),
  tag='تطبيق حياتي على نظرية العوامل'),
# E (expected: improper fraction, divide first), template 2026 #2: quotient kept or dropped x constants swapped
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
# E (expected: remainder on a quadratic divisor, the remainder on x gives b at once), template 2026 #3: r(x) = ax + b
# with f(0) = b, f(-3) = -3a + b; options = sign of a (the zero of x + 3 taken as 3) x remainder written bx + a
Q('m8q4', U1[1], 'medium',
  r"إذا كان باقي قسمة كثير الحدود $f(x)$ على $x$ يساوي $5$ ، وباقي قسمته على $(x+3)$ يساوي $-4$ ، فإنّ باقي قسمة $f(x)$ على $x(x+3)$ هو:",
  [O('3x+5', 3*x+5), O('-3x+5', -3*x+5), O('5x+3', 5*x+3), O('5x-3', 5*x-3)],
  r"الباقي من الدرجة الأولى على الأكثر: $r(x)=ax+b$ ، و $f(x)=x(x+3)q(x)+ax+b$" "\n"
  r"$f(0)=b=5$ ، و $f(-3)=-3a+b=-4 \Rightarrow -3a=-9 \Rightarrow a=3$ ، فالباقي $3x+5$",
  truth=lambda: (lambda s_: s_[a]*x+s_[b])(solve([b-5, -3*a+b+4], [a, b])), tag='باقي القسمة على مقدار تربيعي'),
# ---------------- unit 2
# 2026 #4: sin(theta/2) from sec theta and a quadrant; options = sign x sin/cos half-angle formula
Q('m8q5', U2[2], 'medium',
  r"إذا كان: $\sec\theta=-3$ ، $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\sin\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{\sqrt{6}}{3}', sqrt(6)/3), O(r'-\frac{\sqrt{6}}{3}', -sqrt(6)/3), O(r'\frac{\sqrt{3}}{3}', sqrt(3)/3), O(r'-\frac{\sqrt{3}}{3}', -sqrt(3)/3)],
  r"$\cos\theta=-\frac13$ ، و $\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$ فالجيب موجب" "\n" r"$\sin\frac{\theta}{2}=\sqrt{\dfrac{1-\cos\theta}{2}}=\sqrt{\dfrac{4/3}{2}}=\sqrt{\dfrac23}=\dfrac{\sqrt6}{3}$",
  truth=sin(acos(-R(1, 3))/2), tag='نصف الزاوية مع تحديد الربع'),
# E (expected: related angles and the odd identity), template 2026 #5 ("أبسط صورة", two terms combine into one):
# cos(pi/2 + x) = -sin x, sin(-x) = -sin x; options = sign of the first reduction x sign of the odd identity (k sin x)
Q('m8q6', U2[1], 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos\left(\frac{\pi}{2}+x\right)-2\sin(-x)', cos(pi/2+x)-2*sin(-x))),
  [O(r'\sin x', sin(x)), O(r'3\sin x', 3*sin(x)), O(r'-3\sin x', -3*sin(x)), O(r'-\sin x', -sin(x))],
  r"$\cos\left(\frac{\pi}{2}+x\right)=-\sin x$ ، و $\sin(-x)=-\sin x$ (اقتران فردي) ، إذن $-2\sin(-x)=2\sin x$" "\n"
  r"المقدار $-\sin x+2\sin x=\sin x$",
  truth=cos(pi/2+x)-2*sin(-x), tag='المتطابقات: الزوايا المنتسبة والزوجية والفردية'),
# 2026 #6: equivalent expression (common denominator, Pythagorean and reciprocal identities); options = factor 2 kept
# or lost x sec vs csc
Q('m8q7', U2[1], 'easy',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\dfrac{1}{1-\sin x}+\dfrac{1}{1+\sin x}', 1/(1-sin(x))+1/(1+sin(x)))),
  [O(r'2\sec^{2}x', 2*sec(x)**2), O(r'2\csc^{2}x', 2*csc(x)**2), O(r'\sec^{2}x', sec(x)**2), O(r'\csc^{2}x', csc(x)**2)],
  r"$\dfrac{(1+\sin x)+(1-\sin x)}{(1-\sin x)(1+\sin x)}=\dfrac{2}{1-\sin^2x}=\dfrac{2}{\cos^2x}=2\sec^2x$",
  truth=1/(1-sin(x))+1/(1+sin(x)), tag='المتطابقات الأساسية'),
# E (expected: double angle by squaring), template 2026 #4 (one given value -> another ratio): sin x - cos x = 2/3;
# options = sign x 1 -/+ (2/3)^2
Q('m8q8', U2[2], 'medium',
  F(r"إذا كان: $«0»=\frac{2}{3}$ ، فإنّ قيمة $\sin 2x$ هي:", (r'\sin x-\cos x', sin(x)-cos(x))),
  [O(r'\frac{5}{9}', R(5, 9)), O(r'-\frac{5}{9}', -R(5, 9)), O(r'\frac{13}{9}', R(13, 9)), O(r'-\frac{13}{9}', -R(13, 9))],
  r"بتربيع الطرفين: $\sin^2x-2\sin x\cos x+\cos^2x=\frac49$" "\n" r"$1-\sin2x=\frac49 \Rightarrow \sin2x=\frac59$",
  truth=(lambda xs: sin(2*xs))(nsolve(sin(x)-cos(x)-R(2, 3), x, 1)), tag='ضعف الزاوية بالتربيع'),
# 2026 #7: quadratic in cos with one solution rejected (here by the OPEN interval); options = single angles
Q('m8q9', U2[3], 'easy',
  F(r"حلّ المعادلة: $«0»=0$ في الفترة $(0,\,\pi)$ هو:", (r'2\cos^{2}x+\cos x-1', 2*cos(x)**2+cos(x)-1)),
  [O(st(r'\frac{\pi}{3}'), S_(P/3), 'set'), O(st(r'\pi'), S_(P), 'set'), O(st(r'\frac{2\pi}{3}'), S_(2*P/3), 'set'), O(st(r'\frac{\pi}{6}'), S_(P/6), 'set')],
  r"$(2\cos x-1)(\cos x+1)=0$" "\n" r"$\cos x=-1 \Rightarrow x=\pi$ خارج الفترة المفتوحة، و $\cos x=\frac12 \Rightarrow x=\frac{\pi}{3}$",
  truth=lambda: sols(2*cos(x)**2+cos(x)-1, 0, pi, closed_lo=False), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
# E (expected: equation with a double-angle identity), template 2026 #8 (solutions in an interval): factor, do not
# divide by cos x; options = cos x = 0 kept or lost x sin/cos angles
Q('m8q10', U2[3], 'medium',
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
# 2026r #2: slope of the normal for a ln x + b/x; options = sign x slope/normal slope
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
# 2023 #5: f' given (a rational expression to split first), f''' asked; options = sign x one derivative too many
Q('m8q14', U3[2], 'easy',
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
# 2025s #3: one graph, h = an exponential times f (product rule), h'(1); options = sign x f(1) -/+ f'(1)
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
# 2025s #9: composite from a list of values (one decoy value); options = sign x g' evaluated at the wrong point
Q('m8q18', U3[3], 'easy',
  r"إذا كان: $h(x)=g(f(x))$ ، وكان: $f(3)=2$ ، $f'(3)=-4$ ، $g'(2)=\frac{1}{2}$ ، $g'(3)=7$ ، فإنّ $h'(3)$ هي:",
  [O('-2', -2), O('2', 2), O('-28', -28), O('28', 28)],
  r"$h'(x)=g'(f(x))\cdot f'(x)$" "\n" r"$h'(3)=g'(f(3))\cdot f'(3)=g'(2)\cdot(-4)=\frac12(-4)=-2$",
  truth=R(1, 2)*(-4), tag='قاعدة السلسلة من قيم معطاة'),
# 2026r #6: h = (c - k f(x))^n with f(a), f'(a) given (here (5 - 2f)^3 at x = 2); options = the inner factor -2 kept or
# lost x sign
Q('m8q19', U3[3], 'medium',
  r"إذا كان: $h(x)=\big(5-2f(x)\big)^{3}$ ، وكان: $f(2)=1$ ، $f'(2)=-1$ ، فإنّ $h'(2)$ هي:",
  [O('54', 54), O('-54', -54), O('27', 27), O('-27', -27)],
  r"$h'(x)=3\big(5-2f(x)\big)^2\cdot\big(-2f'(x)\big)$" "\n" r"$h'(2)=3(5-2)^2\cdot(-2)(-1)=3(9)(2)=54$",
  truth=lambda: (lambda f_: diff((5-2*f_(x))**3, x).subs(Derivative(f_(x), x), -1).subs(f_(x), 1))(Function('f')),
  tag='قاعدة السلسلة من قيم معطاة'),
# 2023 #9: implicit relation with a trig term (pi coefficient) at a lattice point; options = sign of cos(pi) x a term
# moved with the wrong sign
Q('m8q20', U3[4], 'hard',
  F(r"إذا كان: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(1,\,1)$ هي:", (r'x^{2}y+\sin(\pi y)', x**2*y+sin(pi*y)), (r'4x-3', 4*x-3)),
  [O(r'\frac{2}{1-\pi}', 2/(1-pi)), O(r'\frac{2}{1+\pi}', 2/(1+pi)), O(r'\frac{6}{1-\pi}', 6/(1-pi)), O(r'\frac{6}{1+\pi}', 6/(1+pi))],
  r"$2xy+x^2\dfrac{dy}{dx}+\pi\cos(\pi y)\dfrac{dy}{dx}=4$" "\n" r"عند $(1,1)$: $2+\dfrac{dy}{dx}-\pi\dfrac{dy}{dx}=4 \Rightarrow (1-\pi)\dfrac{dy}{dx}=2 \Rightarrow \dfrac{dy}{dx}=\dfrac{2}{1-\pi}$",
  truth=imp(x**2*y+sin(pi*y)-4*x+3, (1, 1)), tag='الاشتقاق الضمني عند نقطة'),
# 2026 #17: tangent to an implicit curve at a lattice point, here its x-intercept; options = slope slips
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
# 2026r #18: trigonometric form of k i (a + bi); options = quadrant x reference angle
Q('m8q23', U4[1], 'medium',
  r"الصورة المثلثية للعدد المركّب $w=-2i(\sqrt{3}+i)$ هي:",
  [O(trig('4', r'-\frac{\pi}{3}'), pol(4, -P/3)), O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3)),
   O(trig('4', r'-\frac{\pi}{6}'), pol(4, -P/6)), O(trig('4', r'\frac{2\pi}{3}'), pol(4, 2*P/3))],
  r"$w=-2\sqrt3\,i-2i^2=2-2\sqrt3\,i$ ، $|w|=\sqrt{4+12}=4$ (الربع الرابع)" "\n" r"زاوية الإسناد $\frac{\pi}{3}$ ، و $\text{Arg}(w)=-\frac{\pi}{3}$",
  truth=expand(-2*I*(sqrt(3)+I)), tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2025s #22 (and 2026r #22, a linear combination): shared stem, conj(z) + 2w; options = which number is conjugated
Q('m8q24', U4[2], 'easy',
  r"ناتج $\bar{z}+2w$ هو:",
  [O('9-7i', 9-7*I), O('9-5i', 9-5*I), O('9+5i', 9+5*I), O('9+7i', 9+7*I)],
  r"$\bar z=5-i$ ، $2w=4-6i$" "\n" r"$\bar z+2w=9-7i$",
  truth=conjugate(5+I)+2*(2-3*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=5+i$ ، $w=2-3i$", 24, 25)),
# 2026r #25: |z1 z2| for two given numbers (here the second item of the shared stem); options = moduli added vs
# multiplied, |z|^2
Q('m8q25', U4[1], 'easy',
  r"قيمة $|zw|$ هي:",
  [O(r'13\sqrt{2}', 13*sqrt(2)), O(r'\sqrt{39}', sqrt(39)), O(r'\sqrt{26}+\sqrt{13}', sqrt(26)+sqrt(13)), O('26', 26)],
  r"$|z|=\sqrt{26}$ ، $|w|=\sqrt{13}$ ، و $|zw|=|z||w|=\sqrt{338}=13\sqrt2$",
  truth=Abs(expand((5+I)*(2-3*I))), tag='المقياس والعمليات (نص مشترك)'),
# 2024 #22: equality with a quotient -> the real constant a; options = sign x answering b instead of a
Q('m8q26', U4[2], 'medium',
  r"إذا كان: $\dfrac{a+5i}{2+i}=b+3i$ ، حيث $a$ و $b$ ثابتان حقيقيان، فإنّ قيمة الثابت $a$ هي:",
  [O('-5', -5), O('5', 5), O('-1', -1), O('1', 1)],
  r"$a+5i=(b+3i)(2+i)=2b+bi+6i+3i^2=(2b-3)+(b+6)i$" "\n" r"$b+6=5 \Rightarrow b=-1$ ، و $a=2b-3=-5$",
  truth=lambda: solve([re(expand(X+5*I-(Y+3*I)*(2+I))), im(expand(X+5*I-(Y+3*I)*(2+I)))], [X, Y])[X], tag='معادلة فيها العدد ومرافقه'),
# 2023 #23: one square root of a complex number has a given form (real part given) -> b; options = sign x b vs b^2
Q('m8q27', U4[2], 'medium',
  r"إذا كان: $3+bi$ أحد الجذرين التربيعيين للعدد المركّب $5-12i$ ، فإنّ قيمة الثابت الحقيقي $b$ هي:",
  [O('-2', -2), O('2', 2), O('-4', -4), O('4', 4)],
  r"$(3+bi)^2=9-b^2+6bi=5-12i$" "\n" r"$6b=-12 \Rightarrow b=-2$ (وتحقّق $9-b^2=5$)",
  truth=lambda: [r_ for r_ in solve(im(expand((3+X*I)**2))+12, X) if (9-r_**2) == 5][0], tag='الجذور التربيعية للعدد المركب'),
# 2024 #20: Arg of a related number in terms of alpha (here -3 + 2i = i(2 + 3i), a rotation by pi/2); options =
# pi/2 vs pi x order/sign
Q('m8q28', U4[1], 'medium',
  r"إذا كان: $\text{Arg}(2+3i)=\alpha$ ، فإنّ $\text{Arg}(-3+2i)$ هي:",
  [O(r'\alpha+\frac{\pi}{2}', atan(R(3, 2))+pi/2, sym={'alpha': atan(R(3, 2))}), O(r'\frac{\pi}{2}-\alpha', pi/2-atan(R(3, 2)), sym={'alpha': atan(R(3, 2))}),
   O(r'\pi-\alpha', pi-atan(R(3, 2)), sym={'alpha': atan(R(3, 2))}), O(r'\alpha-\frac{\pi}{2}', atan(R(3, 2))-pi/2, sym={'alpha': atan(R(3, 2))})],
  r"$-3+2i=i(2+3i)$ ، والضرب في $i$ يدوّر العدد بزاوية $\frac{\pi}{2}$ عكس عقارب الساعة" "\n" r"$\text{Arg}(-3+2i)=\alpha+\frac{\pi}{2}$ (وهي أقل من $\pi$ لأنّ $\alpha<\frac{\pi}{2}$)",
  truth=arg(-3+2*I), tag='السعة الرئيسة'),
# 2023 #25: perpendicular bisector drawn with its two points (the line does not pass through O); options = sign of
# each point's term
IndexQ('m8q29', U4[3], 'easy',
  r"معتمدًا الشكل الآتي، ما معادلة المستقيم $l$ المُمثَّل بيانيًّا (بدلالة $z$)؟",
  [T(r'$|z-3i|=|z-4-i|$', bisector(A8, B8)), T(r'$|z+3i|=|z+4+i|$', bisector(-A8, -B8)),
   T(r'$|z-3i|=|z+4+i|$', bisector(A8, -B8)), T(r'$|z+3i|=|z-4-i|$', bisector(-A8, B8))],
  r"$l$ عمود منصّف للقطعة $AB$ ، حيث $A(0,3)$ أي $3i$ ، و $B(4,1)$ أي $4+i$" "\n" r"$|z-3i|=|z-(4+i)|=|z-4-i|$",
  truth=region_truth(bisector(A8, B8), L8, 5), figure=figure('m8q29', fig_bisector(), 3.2, 3.2), tag='كتابة معادلة محل هندسي'),
# 2025s #23: a wedge from a point (open vertex), one ray dashed; options = vertex sign x strictness
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
F9_4 = 4*x**3 - 8*x**2 + x + 3


def ratzeros9(f_):
    """possible rational zeros +-p/q of a polynomial: p | constant term, q | leading coefficient."""
    P_ = Poly(f_, x)
    return {sg*R(pp, qq) for pp in divisors(abs(P_.TC())) for qq in divisors(abs(P_.LC())) for sg in (1, -1)}


def htan9(rel):
    """a of the only point (a, b) with b > 0 where rel(x, y) = 0 has a horizontal tangent (F_x = 0, F_y != 0)."""
    pts = [s_ for s_ in solve([rel, diff(rel, x)], [x, y], dict=True) if diff(rel, y).subs(s_) != 0 and s_[y] > 0]
    assert len(pts) == 1, pts
    return pts[0][x]


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
# E (expected: division algorithm f(x) = (x - a)q(x) + r), template 2026 #3: remainder on division by (x - 1) given -> the constant; options = +-2, +-6 (zero sign, term moved, k taken as that remainder)
Q('m9q1', U1[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x-1)$ يساوي $2$ ، فإنّ قيمة الثابت $k$ هي:", (r'(x-3)(x^{2}+2x-1)+k', (x-3)*(x**2+2*x-1)+k)),
  [O('6', 6), O('-6', -6), O('-2', -2), O('2', 2)],
  r"الصورة المعطاة خوارزمية القسمة على $(x-3)$ ، فـ $k$ باقي القسمة على $(x-3)$ لا على $(x-1)$" "\n"
  r"نظرية الباقي: $f(1)=(1-3)(1+2-1)+k=-4+k=2 \Rightarrow k=6$",
  truth=lambda: solve(rem((x-3)*(x**2+2*x-1)+k, 1)-2, k)[0], tag='الباقي من صورة خوارزمية القسمة'),
# 2026 #2: repeated linear factor, "which is the decomposition"; options as the model = A, B swapped and two wrong forms (linear numerator over the square, + and -)
Q('m9q2', U1[2], 'easy',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{2x-5}{(x-3)^{2}}', (2*x-5)/(x-3)**2)),
  [O(r'\frac{2}{x-3}+\frac{1}{(x-3)^{2}}', 2/(x-3)+1/(x-3)**2), O(r'\frac{1}{x-3}+\frac{2}{(x-3)^{2}}', 1/(x-3)+2/(x-3)**2),
   O(r'\frac{1}{x-3}+\frac{x+2}{(x-3)^{2}}', 1/(x-3)+(x+2)/(x-3)**2), O(r'\frac{1}{x-3}-\frac{x+2}{(x-3)^{2}}', 1/(x-3)-(x+2)/(x-3)**2)],
  r"$\dfrac{2x-5}{(x-3)^2}=\dfrac{A}{x-3}+\dfrac{B}{(x-3)^2} \Rightarrow 2x-5=A(x-3)+B$" "\n" r"معامل $x$: $A=2$ ، وعند $x=3$: $B=6-5=1$",
  truth=(2*x-5)/(x-3)**2, tag='تجزئة: عامل خطي مكرر'),
# 2026 #3 (remainder theorem -> constant) with one remainder and a divisor (ax + b); options = the right zero -1/2, the zeros +1/2 and -2, a sign slip
Q('m9q3', U1[1], 'medium',
  F(r"إذا كان باقي قسمة الاقتران: $f(x)=«0»$ على $(2x+1)$ يساوي $3$ ، فإنّ قيمة الثابت $k$ هي:", (r'4x^{3}+kx^{2}-2x+1', 4*x**3+k*x**2-2*x+1)),
  [O('6', 6), O('10', 10), O(r'\frac{15}{2}', R(15, 2)), O('-6', -6)],
  r"صفر المقسوم عليه $x=-\frac12$" "\n" r"$f\left(-\frac12\right)=-\frac12+\frac k4+1+1=\frac32+\frac k4=3 \Rightarrow k=6$",
  truth=lambda: solve(rem(4*x**3+k*x**2-2*x+1, -R(1, 2))-3, k)[0], tag='نظرية الباقي: القسمة على (ax−b)'),
# E (expected: rational zeros theorem, a value that is not a possible zero), template «أيُّ الآتية …؟» (2026 #2, #6); options = fractions p/q, the answer is the swapped fraction 4/3
IndexQ('m9q4', U1[1], 'easy',
  F(r"أيُّ الآتية ليس من الأصفار النسبية المُحتملة للاقتران: $f(x)=«0»$ ؟", (r'4x^{3}-8x^{2}+x+3', F9_4)),
  [O(r'\frac{4}{3}', R(4, 3)), O(r'\frac{3}{4}', R(3, 4)), O(r'-\frac{3}{2}', -R(3, 2)), O(r'\frac{1}{4}', R(1, 4))],
  r"الأصفار النسبية المحتملة $\pm\frac{p}{q}$: $p$ من عوامل الحدّ الثابت $3$ ، و $q$ من عوامل المعامل الرئيس $4$" "\n"
  r"فهي: $\pm1,\ \pm3,\ \pm\frac12,\ \pm\frac32,\ \pm\frac14,\ \pm\frac34$ ، و $\frac43$ ليس منها ($4$ لا يقسم $3$)",
  truth=lambda vals: only(vals, lambda v_: v_ not in ratzeros9(F9_4)), tag='الأصفار النسبية المحتملة'),
# ---------------- unit 2
# E (expected: double angle by squaring), template 2026 #4 (a given relation -> a value): sin x + cos x = 1/3 -> sin 2x; options = sign (1 moved the wrong way) x halved (sin x cos x)
Q('m9q5', U2[2], 'medium',
  F(r"إذا كان: $«0»=\frac{1}{3}$ ، فإنّ قيمة $\sin 2x$ تساوي:", (r'\sin x+\cos x', sin(x)+cos(x))),
  [O(r'-\frac{8}{9}', -R(8, 9)), O(r'\frac{8}{9}', R(8, 9)), O(r'-\frac{4}{9}', -R(4, 9)), O(r'\frac{4}{9}', R(4, 9))],
  r"نربّع الطرفين: $\sin^2x+2\sin x\cos x+\cos^2x=\frac19$" "\n" r"$1+\sin2x=\frac19 \Rightarrow \sin2x=\frac19-1=-\frac89$",
  truth=lambda: nsimplify(N(sin(2*(asin(sqrt(2)/6)-pi/4)), 60)), tag='ضعف الزاوية بالتربيع'),
# 2026 #5: simplest form, ONE difference formula sin(x - pi/6) plus k cos x, the cos terms cancel; options = coefficient x sin/cos
Q('m9q6', U2[1], 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(x-\frac{\pi}{6})+\frac{1}{2}\cos x', sin(x-pi/6)+cos(x)/2)),
  [O(r'\frac{\sqrt{3}}{2}\sin x', sqrt(3)/2*sin(x)), O(r'\frac{1}{2}\sin x', sin(x)/2), O(r'\frac{\sqrt{3}}{2}\cos x', sqrt(3)/2*cos(x)), O(r'\frac{1}{2}\cos x', cos(x)/2)],
  r"$\sin\left(x-\frac{\pi}{6}\right)=\sin x\cos\frac{\pi}{6}-\cos x\sin\frac{\pi}{6}=\frac{\sqrt3}{2}\sin x-\frac12\cos x$" "\n" r"بإضافة $\frac12\cos x$ يُحذف حدّا $\cos x$ ، فيبقى $\frac{\sqrt3}{2}\sin x$",
  truth=sin(x-pi/6)+cos(x)/2, tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# E (expected: cos(A - B) from one ratio of each angle in given quadrants), template 2026 #4 (ratio + quadrant -> value); options = difference vs sum formula x sign of cos B (+-77/85, +-13/85)
Q('m9q7', U2[1], 'medium',
  r"إذا كان: $\cos A=-\frac{4}{5}$ ، $\frac{\pi}{2}<A<\pi$ ، و $\sin B=-\frac{15}{17}$ ، $\frac{3\pi}{2}<B<2\pi$ ، فإنّ قيمة $\cos(A-B)$ تساوي:",
  [O(r'-\frac{77}{85}', -R(77, 85)), O(r'\frac{77}{85}', R(77, 85)), O(r'\frac{13}{85}', R(13, 85)), O(r'-\frac{13}{85}', -R(13, 85))],
  r"$\sin A=\frac35$ (الربع الثاني: الجيب موجب) ، و $\cos B=\frac{8}{17}$ (الربع الرابع: جيب التمام موجب)" "\n"
  r"$\cos(A-B)=\cos A\cos B+\sin A\sin B=-\frac{32}{85}-\frac{45}{85}=-\frac{77}{85}$",
  truth=lambda: nsimplify(N(cos(acos(-R(4, 5)) - (2*pi - asin(R(15, 17)))), 60)), tag='المجموع والفرق بمعلومية نسب في أرباع مختلفة'),
# E (expected: sum to product, exact value), template 2026 #5: cos A - cos B at multiples of pi/12; options = sign of -2 sin sin x sin(pi/6) vs cos(pi/6)
Q('m9q8', U2[2], 'easy',
  F(r"قيمة المقدار: $«0»$ هي:", (r'\cos\frac{5\pi}{12}-\cos\frac{\pi}{12}', cos(5*pi/12)-cos(pi/12))),
  [O(r'-\frac{\sqrt{2}}{2}', -sqrt(2)/2), O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2), O(r'-\frac{\sqrt{6}}{2}', -sqrt(6)/2), O(r'\frac{\sqrt{6}}{2}', sqrt(6)/2)],
  r"$\cos A-\cos B=-2\sin\dfrac{A+B}{2}\sin\dfrac{A-B}{2}$" "\n" r"$-2\sin\frac{\pi}{4}\sin\frac{\pi}{6}=-2\cdot\frac{\sqrt2}{2}\cdot\frac12=-\frac{\sqrt2}{2}$",
  truth=cos(5*pi/12)-cos(pi/12), tag='تحويل المجموع إلى ضرب'),
# E (expected: equation with a double-angle identity), template 2026 #8 (solutions in an interval): cos 2x = cos x on [0, pi]; options = signs of the factors x the quadrantal root kept or dropped
Q('m9q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=«1»$ في الفترة $[0,\,\pi]$ هي:", (r'\cos 2x', cos(2*x)), (r'\cos x', cos(x))),
  [O(st('0', r'\frac{2\pi}{3}'), S_(0, 2*P/3), 'set'), O(st(r'\frac{2\pi}{3}'), S_(2*P/3), 'set'),
   O(st(r'\frac{\pi}{3}', r'\pi'), S_(P/3, P), 'set'), O(st(r'\frac{\pi}{3}'), S_(P/3), 'set')],
  r"$\cos2x=2\cos^2x-1$: $2\cos^2x-\cos x-1=0 \Rightarrow (2\cos x+1)(\cos x-1)=0$" "\n"
  r"$\cos x=1 \Rightarrow x=0$ ، و $\cos x=-\frac12 \Rightarrow x=\frac{2\pi}{3}$ (الحلّ الوحيد في $[0,\pi]$)",
  truth=lambda: sols(cos(2*x)-cos(x), 0, pi, closed_hi=True), tag='معادلة باستعمال متطابقة ضعف الزاوية'),
# 2026 #8 without the reciprocal ratio: cos 2x = -1/2 on (pi, 2pi), interval doubled for 2x; options = interval doubled or not x halved or not
Q('m9q10', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $(\pi,\,2\pi)$ هي:", (r'2\cos 2x+1', 2*cos(2*x)+1)),
  [O(st(r'\frac{4\pi}{3}', r'\frac{5\pi}{3}'), S_(4*P/3, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set'),
   O(st(r'\frac{8\pi}{3}', r'\frac{10\pi}{3}'), S_(8*P/3, 10*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set')],
  r"$\cos2x=-\frac12$ ، و $2\pi<2x<4\pi$" "\n" r"$2x=2\pi+\frac{2\pi}{3}=\frac{8\pi}{3}$ أو $2x=2\pi+\frac{4\pi}{3}=\frac{10\pi}{3}$ ، إذن $x=\frac{4\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*cos(2*x)+1, pi, 2*pi, closed_lo=False), tag='معادلة بزاوية مضاعفة في فترة'),
# ---------------- unit 3
# 2025s #1: ln of a power of x over a power of e, log laws first; options = constant kept x chain factor of sqrt x (1/(2x) vs 1/sqrt x)
Q('m9q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، $x>0$ ، فإنّ $f'(x)$ هي:", (r'\ln(\frac{\sqrt{x}}{e^{3}})', log(sqrt(x)/E**3))),
  [O(r'\frac{1}{2x}', 1/(2*x)), O(r'\frac{1}{2x}-3', 1/(2*x)-3), O(r'\frac{1}{\sqrt{x}}', 1/sqrt(x)), O(r'\frac{1}{\sqrt{x}}-3', 1/sqrt(x)-3)],
  r"$f(x)=\ln\sqrt x-\ln e^3=\frac12\ln x-3$" "\n"
  r"$f'(x)=\dfrac{1}{2x}$",
  truth=Dx(log(sqrt(x)/E**3)), tag='مشتقة الاقتران اللوغاريتمي'),
# 2025s #6 (cot pi x at 1/4) / 2024s #6: tan of a multiple of x at a point; options = chain factor pi kept or dropped x sec squared or not
Q('m9q12', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{1}{3}\right)$ هي:", (r'2\tan(\pi x)', 2*tan(pi*x))),
  [O(r'8\pi', 8*pi), O('8', 8), O(r'4\pi', 4*pi), O('4', 4)],
  r"$f'(x)=2\pi\sec^2(\pi x)$ ، و $\sec\frac{\pi}{3}=2$" "\n" r"$f'\left(\frac13\right)=2\pi(4)=8\pi$",
  truth=Dx(2*tan(pi*x)).subs(x, R(1, 3)), tag='مشتقات الاقترانات المثلثية'),
# 2025s #10: s = c - k sin t, position at the first instant of momentary rest (the first zero of v); options = the start s(0), the second rest, the amplitude
Q('m9q13', U3[1], 'medium',
  F(r"إذا كان الاقتران: $s(t)=«0»$ ، $t\ge0$ يُمثّل موقع جُسيم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار و $t$ الزمن بالثواني، فإنّ موقع الجُسيم عندما كان في حالة سكون لحظي أوّل مرة بعد انطلاقه هو:", (r'8-3\sin t', 8-3*sin(t))),
  [O('5', 5, units='m'), O('8', 8, units='m'), O('11', 11, units='m'), O('3', 3, units='m')],
  r"$v(t)=-3\cos t=0 \Rightarrow t=\frac{\pi}{2},\ \frac{3\pi}{2},\ \dots$ ، وأوّل سكون بعد الانطلاق عند $t=\frac{\pi}{2}$" "\n" r"$s\left(\frac{\pi}{2}\right)=8-3\sin\frac{\pi}{2}=5\ \text{m}$",
  truth=(8-3*sin(t)).subs(t, min(r_ for r_ in solve(diff(8-3*sin(t), t), t) if r_ > 0)), tag='الحركة: اتجاه الحركة والسكون'),
# 2026 #11: f'' + 2f' for sin 2x + cos 2x (2026: e^(2x) + e^(-2x)), one function cancels; options = sign x surviving function
Q('m9q14', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''(x)+2f'(x)$ هي:", (r'\sin 2x+\cos 2x', sin(2*x)+cos(2*x))),
  [O(r'-8\sin 2x', -8*sin(2*x)), O(r'8\sin 2x', 8*sin(2*x)), O(r'-8\cos 2x', -8*cos(2*x)), O(r'8\cos 2x', 8*cos(2*x))],
  r"$f'(x)=2\cos2x-2\sin2x$ ، $f''(x)=-4\sin2x-4\cos2x$" "\n" r"$f''+2f'=-4\sin2x-4\cos2x+4\cos2x-4\sin2x=-8\sin2x$",
  truth=diff(sin(2*x)+cos(2*x), x, 2)+2*Dx(sin(2*x)+cos(2*x)), tag='المشتقات العليا وتراكيبها'),
# 2026r #11: growth model c a^(1/(t+m)) in a new context (fish; base 1/8, exponent 1/(t+2)), rate at t = 1, unit in the stem only; options = sign x missing square (40 vs 120)
Q('m9q15', U3[3], 'hard',
  F(r"إذا كان الاقتران: $N(t)=«0»$ ، $t\ge0$ يُمثّل عدد الأسماك في بحيرة بعد $t$ شهر من تزويدها بالأسماك، فإنّ معدّل نموّ عدد الأسماك بعد شهر واحد (بالسمكة لكلّ شهر) هو:", (r'720(\frac{1}{8})^{\frac{1}{t+2}}', 720*R(1, 8)**(1/(t+2)))),
  [O(r'40\ln 8', 40*log(8)), O(r'-40\ln 8', -40*log(8)), O(r'120\ln 8', 120*log(8)), O(r'-120\ln 8', -120*log(8))],
  r"$N'(t)=720\left(\frac18\right)^{\frac{1}{t+2}}\ln\frac18\cdot\left(-\dfrac{1}{(t+2)^2}\right)$" "\n" r"$N'(1)=720\cdot\frac12\cdot(-\ln8)\cdot\left(-\frac19\right)=40\ln8$",
  truth=diff(720*R(1, 8)**(1/(t+2)), t).subs(t, 1), tag='معدل التغير في سياق حياتي'),
# 2026 #14 with a composite: h = f(g(x)) read from two graphs; options = sign x evaluating f' at x instead of g(x)
Q('m9q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=f(g(x))$ ، فإنّ $h'(1)$ هي:",
  [O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{2}', -R(1, 2)), O('-2', -2), O('2', 2)],
  r"من الشكل: $g(1)=4$ ، $g'(1)=-1$ ، و $f'(4)=-\frac12$ (ميل قطعة $f$ من $(2,5)$ إلى $(6,3)$)" "\n" r"$h'(1)=f'(g(1))\cdot g'(1)=f'(4)\cdot(-1)=\frac12$",
  truth=lambda: (lambda fv, fs, gv, gs: fs(gv(1))*gs(1))(*pw(F9), *pw(G9)),
  figure=figure('m9q16', draw_two(F9, G9, 6, 5, (2.6, 5.2), (4.6, 1.3))), tag='المشتقة من التمثيل البياني'),
# 2025 #11: log10 of a product (a - x)(a + x) on an interval; options = ln 10 up or down x sign (denominator written x^2 - 4)
Q('m9q17', U3[3], 'medium',
  r"إذا كان: $f(x)=\log\big((2-x)(2+x)\big)$ ، $-2<x<2$ ، فإنّ $f'(x)$ هي:",
  [O(r'\frac{2x}{(x^{2}-4)\ln 10}', 2*x/((x**2-4)*log(10))), O(r'\frac{-2x}{(x^{2}-4)\ln 10}', -2*x/((x**2-4)*log(10))),
   O(r'\frac{2x\cdot\ln 10}{x^{2}-4}', 2*x*log(10)/(x**2-4)), O(r'\frac{-2x\cdot\ln 10}{x^{2}-4}', -2*x*log(10)/(x**2-4))],
  r"$f(x)=\log(4-x^2)$ ، $f'(x)=\dfrac{-2x}{(4-x^2)\ln10}=\dfrac{2x}{(x^2-4)\ln10}$",
  truth=Dx(log((2-x)*(2+x), 10)), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2024s #8: ln of a squared trig ratio (csc^2 here, sec^2 in 2024s) at a special angle; options = sign x cot vs tan
Q('m9q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، $0<x<\frac{\pi}{2}$ ، فإنّ $f'\left(\frac{\pi}{6}\right)$ هي:", (r'\ln(\csc^{2}x)', log(csc(x)**2))),
  [O(r'-2\sqrt{3}', -2*sqrt(3)), O(r'2\sqrt{3}', 2*sqrt(3)), O(r'-\frac{2\sqrt{3}}{3}', -2*sqrt(3)/3), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3)],
  r"$f(x)=2\ln(\csc x)$ ، $f'(x)=2\cdot\dfrac{-\csc x\cot x}{\csc x}=-2\cot x$" "\n" r"$f'\left(\frac{\pi}{6}\right)=-2\sqrt3$",
  truth=Dx(log(csc(x)**2)).subs(x, pi/6), tag='قاعدة السلسلة مع اللوغاريتم'),
# 2026 #15 (x = a sec t, y = tan t) asked as a function of t, as 2023 #8 asks the derivative itself; options = reciprocal x sign
Q('m9q19', U3[3], 'easy',
  F(r"إذا كان: $x=«0»$ ، $y=«1»$ ، $0<t<\frac{\pi}{2}$ ، فإنّ $\dfrac{dy}{dx}$ هي:", (r'\sec t', sec(t)), (r'\tan t', tan(t))),
  [O(r'\csc t', csc(t)), O(r'\sin t', sin(t)), O(r'-\csc t', -csc(t)), O(r'-\sin t', -sin(t))],
  r"$\dfrac{dy}{dx}=\dfrac{\sec^2t}{\sec t\tan t}=\dfrac{\sec t}{\tan t}=\dfrac{1/\cos t}{\sin t/\cos t}=\dfrac{1}{\sin t}=\csc t$",
  truth=diff(tan(t), t)/diff(sec(t), t), tag='مشتقة المعادلات الوسيطية'),
# 2026 #16: a^(xy) relation, the point from x = 0 (2026 finds x from y = 1); options = sign of ln 3 x sign of 1 (y' moved across)
Q('m9q20', U3[4], 'hard',
  F(r"إذا كان: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $x=0$ هو:", (r'3^{xy}', 3**(x*y)), (r'x+y', x+y)),
  [O(r'\ln 3-1', log(3)-1), O(r'1-\ln 3', 1-log(3)), O(r'\ln 3+1', log(3)+1), O(r'-\ln 3-1', -log(3)-1)],
  r"عندما $x=0$: $3^0=0+y \Rightarrow y=1$" "\n" r"$3^{xy}\ln3\left(y+x\dfrac{dy}{dx}\right)=1+\dfrac{dy}{dx}$ ، وعند $(0,1)$: $\ln3=1+\dfrac{dy}{dx} \Rightarrow \dfrac{dy}{dx}=\ln3-1$",
  truth=imp(3**(x*y)-x-y, (0, 1)), tag='الاشتقاق الضمني عند نقطة'),
# E (expected: horizontal tangent of an implicit curve), template 2026 #17 (tangent to a relation): x^2 + xy + y^2 = 12 at (a, b), b > 0 -> a; options = numerator vs denominator of dy/dx = 0 (2 vs 4) x the sign of b
Q('m9q21', U3[4], 'medium',
  F(r"إذا كان لمنحنى العلاقة: $«0»=12$ مماس أفقي عند النقطة $(a,\,b)$ ، حيث $b>0$ ، فإنّ قيمة $a$ هي:", (r'x^{2}+xy+y^{2}', x**2+x*y+y**2)),
  [O('-2', -2), O('2', 2), O('-4', -4), O('4', 4)],
  r"$2x+y+x\dfrac{dy}{dx}+2y\dfrac{dy}{dx}=0 \Rightarrow \dfrac{dy}{dx}=-\dfrac{2x+y}{x+2y}$" "\n"
  r"المماس أفقي عندما $2x+y=0$ أي $y=-2x$: $x^2-2x^2+4x^2=12 \Rightarrow x=\pm2$" "\n"
  r"النقطتان $(2,-4)$ و $(-2,4)$ ، والشرط $b>0$ يعطي $(-2,4)$ ، إذن $a=-2$",
  truth=lambda: htan9(x**2+x*y+y**2-12), tag='مماس أفقي لمنحنى ضمني'),
# 2023 #11: two perpendicular roads, fixed station, the car moving away; options = sign x divided by the fixed side 8 instead of the hypotenuse 10
Q('m9q22', U3[5], 'medium',
  r"$l$ و $m$ طريقان مستقيمان متعامدان في النقطة $C$. تقع محطة شرطة على الطريق $m$ وتبعد $8\ \text{km}$ عن $C$. إذا تحرّكت سيارة على الطريق $l$ مبتعدةً عن $C$ بسرعة $60\ \text{km/h}$ ، فما معدّل تغيّر المسافة بين السيارة والمحطة عندما تكون السيارة على بُعد $6\ \text{km}$ من $C$ ؟",
  [O('36', 36, units='km/h'), O('-36', -36, units='km/h'), O('45', 45, units='km/h'), O('-45', -45, units='km/h')],
  r"$d^2=x^2+8^2 \Rightarrow 2d\dfrac{dd}{dt}=2x\dfrac{dx}{dt}$" "\n" r"عند $x=6$: $d=10$ ، $\dfrac{dd}{dt}=\dfrac{6}{10}(60)=36\ \text{km/h}$",
  truth=(diff(sqrt(s**2+64), s)*60).subs(s, 6), tag='معدلات مرتبطة: نظرية فيثاغورس'),
# ---------------- unit 4
# 2024 #23: a power of z given in a "minus" form r cos(theta) - i r sin(theta); options = modulus power (16 vs 8) x sign of the angle
Q('m9q23', U4[2], 'medium',
  r"إذا كان: $z=2\cos\frac{\pi}{8}-2i\sin\frac{\pi}{8}$ ، فإنّ الصورة المثلثية للعدد $z^{4}$ هي:",
  [O(trig('16', r'-\frac{\pi}{2}'), pol(16, -P/2)), O(trig('16', r'\frac{\pi}{2}'), pol(16, P/2)),
   O(trig('8', r'-\frac{\pi}{2}'), pol(8, -P/2)), O(trig('8', r'\frac{\pi}{2}'), pol(8, P/2))],
  r"$z=2\left(\cos\left(-\frac{\pi}{8}\right)+i\sin\left(-\frac{\pi}{8}\right)\right)$" "\n" r"$z^4=2^4\left(\cos\left(-\frac{\pi}{2}\right)+i\sin\left(-\frac{\pi}{2}\right)\right)$ ، و $2^4=16$",
  truth=expand(pol(2, -pi/8)**4), tag='قوى العدد المركب', lead=NOTE_I(23, 30)),
# 2024 #21: z^2 - w^2 as the FIRST item of a shared stem (the device of 2026 #20-21 / 2025 #21-22); options = i^2 slip x
# order of subtraction
Q('m9q24', U4[2], 'medium',
  r"قيمة المقدار $z^{2}-w^{2}$ هي:",
  [O('-6-8i', -6-8*I), O('2-8i', 2-8*I), O('6+8i', 6+8*I), O('-2+8i', -2+8*I)],
  r"$z^2=1-4i+4i^2=-3-4i$ ، $w^2=4+4i+i^2=3+4i$" "\n" r"$z^2-w^2=-6-8i$",
  truth=expand((1-2*I)**2-(2+I)**2), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=1-2i$ ، $w=2+i$", 24, 25)),
# 2025 #22: second item of the shared stem, 1/z + w/|z|^2; options = conjugate forgotten in 1/z x w vs conj(w)
Q('m9q25', U4[2], 'easy',
  r"ناتج $\dfrac{1}{z}+\dfrac{w}{5}$ هو:",
  [O(r'\frac{3}{5}+\frac{3}{5}i', R(3, 5)+R(3, 5)*I), O(r'\frac{3}{5}-\frac{1}{5}i', R(3, 5)-R(1, 5)*I), O(r'\frac{3}{5}+\frac{1}{5}i', R(3, 5)+R(1, 5)*I), O(r'\frac{3}{5}-\frac{3}{5}i', R(3, 5)-R(3, 5)*I)],
  r"$\dfrac1z=\dfrac{1}{1-2i}\cdot\dfrac{1+2i}{1+2i}=\dfrac{1+2i}{5}$" "\n" r"$\dfrac{1+2i}{5}+\dfrac{2+i}{5}=\dfrac{3+3i}{5}$",
  truth=1/(1-2*I)+(2+I)/5, tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2024s #21: z = a + ik with |z| and an Arg interval -> k; options = sign (quadrant) x magnitude (k vs the modulus 4)
Q('m9q26', U4[1], 'medium',
  r"إذا كان: $z=2\sqrt{3}+ik$ ، حيث: $|z|=4$ ، و $-\frac{\pi}{2}<\text{Arg}(z)<0$ ، فإنّ قيمة الثابت $k$ هي:",
  [O('-2', -2), O('2', 2), O('-4', -4), O('4', 4)],
  r"$12+k^2=16 \Rightarrow k=\pm2$" "\n" r"السعة بين $-\frac{\pi}{2}$ و $0$ تعني الربع الرابع، فالجزء التخيلي سالب: $k=-2$",
  truth=lambda: [r_ for r_ in solve(12+X**2-16, X) if r_ < 0][0], tag='إيجاد ثابت بمعلومية المقياس'),
# 2024s #20: x + y + (x^2 - c)i = a + bi with x > 0 -> y; options = sign slip x the rejected root x = -3
Q('m9q27', U4[1], 'medium',
  r"قيمة $y$ الحقيقية التي تحقّق المعادلة: $2x+y+(x^{2}-4)i=5+5i$ ، حيث $x>0$ هي:",
  [O('-1', -1), O('1', 1), O('11', 11), O('-11', -11)],
  r"$x^2-4=5 \Rightarrow x=3$ (لأنّ $x>0$)" "\n" r"$2(3)+y=5 \Rightarrow y=-1$",
  truth=lambda: [5-2*r_ for r_ in solve(X**2-4-5, X) if r_ > 0][0], tag='تساوي عددين مركبين'),
# 2023 #18: i^n x sqrt(-k^2) with n = 1 (mod 4) and a perfect square; options = sign (i^2025 = +-i) x real vs imaginary (sqrt(-25) = 5i vs 5)
Q('m9q28', U4[1], 'easy',
  F(r"قيمة المقدار: $«0»$ هي:", (r'i^{2025}\times\sqrt{-25}', I**2025*sqrt(-25))),
  [O('-5', -5), O('5', 5), O('5i', 5*I), O('-5i', -5*I)],
  r"$2025=4\times506+1$ ، فـ $i^{2025}=i$ ، و $\sqrt{-25}=5i$" "\n" r"$i\times5i=5i^2=-5$",
  truth=I**2025*sqrt(-25), tag='قوى i'),
# 2025 #23: square in the complex plane from two adjacent vertices (z3 on the real axis), here z4 only; options = rotation direction, the vertex z1, the side vector
Q('m9q29', U4[2], 'medium',
  r"يظهر في المستوى المركّب الآتي مربّع رؤوسه الأعداد المركّبة $z_1,\ z_2,\ z_3,\ z_4$. إذا علمت أنّ: $z_2=-2+3i$ ، $z_3=1$ ، فإنّ $z_4$ هو:",
  [O('4+3i', 4+3*I), O('-2-3i', -2-3*I), O('1+6i', 1+6*I), O('3+3i', 3+3*I)],
  r"$\overrightarrow{z_3z_2}=z_2-z_3=-3+3i$ ، والضلع $\overrightarrow{z_3z_4}$ ناتج عن تدويره بزاوية $\frac{\pi}{2}$ مع عقارب الساعة (الضرب في $-i$)" "\n"
  r"$(-3+3i)(-i)=3i-3i^2=3+3i$ ، إذن $z_4=z_3+(3+3i)=4+3i$",
  truth=1+(-2+3*I-1)*(-I), figure=figure('m9q29', fig_square(), 3.0, 2.6), tag='تمثيل العمليات في المستوى المركب'),
# 2026 #25 family: a dashed disc cut by a solid perpendicular-bisector half-plane (2026: a wedge); options = centre sign x which boundary is strict
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
# E (expected: synthetic division by (ax - b): quotient and remainder), template 2026 #1 (synthetic division, "... هما:"):
# divide by the zero -1/2 of (2x + 1), then halve the quotient; options = quotient halved or not x remainder halved or not
Q('m10q3', U1[1], 'medium',
  F(r"عند قسمة $f(x)=«0»$ على $(2x+1)$ ، فإنّ ناتج القسمة $q(x)$ والباقي $r$ هما:", (r'4x^{3}+4x^{2}-3x+1', 4*x**3+4*x**2-3*x+1)),
  [O(r'q(x)=2x^{2}+x-2,\ r=3', Tuple(2*x**2+x-2, 3), 'pairs'), O(r'q(x)=4x^{2}+2x-4,\ r=3', Tuple(4*x**2+2*x-4, 3), 'pairs'),
   O(r'q(x)=2x^{2}+x-2,\ r=\frac{3}{2}', Tuple(2*x**2+x-2, R(3, 2)), 'pairs'), O(r'q(x)=4x^{2}+2x-4,\ r=\frac{3}{2}', Tuple(4*x**2+2*x-4, R(3, 2)), 'pairs')],
  r"صفر $(2x+1)$ هو $x=-\frac12$ ، وبالقسمة التركيبية: $4,\ 4,\ -3,\ 1 \to 4,\ 2,\ -4,\ 3$" "\n"
  r"$f(x)=\left(x+\frac12\right)(4x^2+2x-4)+3=(2x+1)(2x^2+x-2)+3$ ، إذن $q(x)=2x^2+x-2$ و $r=3$",
  truth=lambda: Tuple(*div(4*x**3+4*x**2-3*x+1, 2*x+1, x)), tag='القسمة التركيبية على (ax−b)'),
# E (expected: factor theorem -> constant), template 2026 #3: (2x - 1) is a factor, so f(1/2) = 0; options = the zero
# used (2 or -1/2 instead of 1/2), a sign slip
Q('m10q4', U1[1], 'medium',
  F(r"إذا كان $(2x-1)$ أحد عوامل الاقتران: $f(x)=«0»$ ، فإنّ قيمة الثابت $k$ هي:", (r'2x^{3}+kx^{2}-5x+2', 2*x**3+k*x**2-5*x+2)),
  [O('1', 1), O('-2', -2), O('-17', -17), O('-1', -1)],
  r"$(2x-1)$ عامل $\Leftrightarrow f\left(\frac12\right)=0$" "\n" r"$\frac14+\frac k4-\frac52+2=0 \Rightarrow \frac k4=\frac14 \Rightarrow k=1$",
  truth=lambda: solve(rem(2*x**3+k*x**2-5*x+2, R(1, 2)), k)[0], tag='نظرية العوامل وإيجاد ثابت'),
# ---------------- unit 2
# 2026 #4: cos(theta/2) from cos theta and a quadrant (2nd); options = sign x cos/sin half-angle formula
Q('m10q5', U2[2], 'medium',
  r"إذا كان: $\cos\theta=-\frac{1}{9}$ ، $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\cos\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{2}{3}', R(2, 3)), O(r'-\frac{2}{3}', -R(2, 3)), O(r'\frac{\sqrt{5}}{3}', sqrt(5)/3), O(r'-\frac{\sqrt{5}}{3}', -sqrt(5)/3)],
  r"$\frac{\pi}{4}<\frac{\theta}{2}<\frac{\pi}{2}$ (الربع الأول)، فجيب التمام موجب" "\n" r"$\cos\frac{\theta}{2}=\sqrt{\dfrac{1+\cos\theta}{2}}=\sqrt{\dfrac{1-\frac19}{2}}=\sqrt{\dfrac49}=\dfrac23$",
  truth=cos(acos(-R(1, 9))/2), tag='نصف الزاوية مع تحديد الربع'),
# E (expected: compressed difference formula sin A cos B - cos A sin B -> exact value), template 2026 #5 (difference
# identity with special angles, "... هي:"); options = special values (sum formula used, angles in reverse order, cos for sin)
Q('m10q6', U2[1], 'easy',
  F(r"قيمة المقدار: $«0»$ هي:", (r'\sin\frac{5\pi}{12}\cos\frac{\pi}{12}-\cos\frac{5\pi}{12}\sin\frac{\pi}{12}', sin(5*pi/12)*cos(pi/12)-cos(5*pi/12)*sin(pi/12))),
  [O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O('1', 1), O(r'-\frac{\sqrt{3}}{2}', -sqrt(3)/2), O(r'\frac{1}{2}', R(1, 2))],
  r"$\sin A\cos B-\cos A\sin B=\sin(A-B)$" "\n" r"$\sin\left(\frac{5\pi}{12}-\frac{\pi}{12}\right)=\sin\frac{4\pi}{12}=\sin\frac{\pi}{3}=\frac{\sqrt3}{2}$",
  truth=sin(5*pi/12)*cos(pi/12)-cos(5*pi/12)*sin(pi/12), tag='قيم دقيقة بمتطابقات المجموع والفرق'),
# 2026 #6: cos x + sin x tan x = sec x -> sin x + cos x cot x = csc x (quotient identity, common denominator,
# Pythagorean, reciprocal); options = reciprocal vs double x sin vs cos (2 sin x = cot x taken as sin x / cos x)
Q('m10q7', U2[1], 'easy',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\sin x+\cos x\cot x', sin(x)+cos(x)*cot(x))),
  [O(r'\csc x', csc(x)), O(r'\sec x', sec(x)), O(r'2\sin x', 2*sin(x)), O(r'2\cos x', 2*cos(x))],
  r"$\sin x+\cos x\cdot\dfrac{\cos x}{\sin x}=\dfrac{\sin^2x+\cos^2x}{\sin x}=\dfrac{1}{\sin x}=\csc x$",
  truth=sin(x)+cos(x)*cot(x), tag='المتطابقات الأساسية'),
# E (expected: exact value by power reduction), template 2026 #4 (a value from a half-angle identity, "... تساوي:"):
# cos^2(pi/8) = (1 + cos(pi/4))/2; options = sign (cos^2 vs sin^2 formula) x coefficient 1/2 kept or dropped
Q('m10q8', U2[2], 'medium',
  F(r"قيمة المقدار: $«0»$ تساوي:", (r'\cos^{2}\frac{\pi}{8}', cos(pi/8)**2)),
  [O(r'\frac{2+\sqrt{2}}{4}', (2+sqrt(2))/4), O(r'\frac{2-\sqrt{2}}{4}', (2-sqrt(2))/4), O(r'\frac{2+\sqrt{2}}{2}', (2+sqrt(2))/2), O(r'\frac{2-\sqrt{2}}{2}', (2-sqrt(2))/2)],
  r"$\cos^2\theta=\dfrac{1+\cos2\theta}{2}$ ، ومع $\theta=\frac{\pi}{8}$: $\cos^2\frac{\pi}{8}=\dfrac{1+\cos\frac{\pi}{4}}{2}$" "\n"
  r"$\dfrac{1+\frac{\sqrt2}{2}}{2}=\dfrac{2+\sqrt2}{4}$",
  truth=cos(pi/8)**2, tag='تقليص القوة ونصف الزاوية'),
# 2026 #7: quadratic in cos with one root rejected (|cos x| <= 1); options = sign x reference angle
Q('m10q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\cos^{2}x+3\cos x-2', 2*cos(x)**2+3*cos(x)-2)),
  [O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'), O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set'),
   O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set'), O(st(r'\frac{5\pi}{6}', r'\frac{7\pi}{6}'), S_(5*P/6, 7*P/6), 'set')],
  r"$(2\cos x-1)(\cos x+2)=0$ ، و $\cos x=-2$ مرفوض" "\n" r"$\cos x=\frac12$: الربعان الأول والرابع: $x=\frac{\pi}{3},\ \frac{5\pi}{3}$",
  truth=lambda: sols(2*cos(x)**2+3*cos(x)-2, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
# E (expected: multiple angle in an interval), template 2026 #8: sin 2x = cos 2x -> tan 2x = 1 in [0, pi), so 2x in
# [0, 2pi); options = halved or not x second solution kept or lost
Q('m10q10', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,\pi)$ هي:", (r'\sin 2x-\cos 2x', sin(2*x)-cos(2*x))),
  [O(st(r'\frac{\pi}{8}', r'\frac{5\pi}{8}'), S_(P/8, 5*P/8), 'set'), O(st(r'\frac{\pi}{4}', r'\frac{5\pi}{4}'), S_(P/4, 5*P/4), 'set'),
   O(st(r'\frac{\pi}{8}'), S_(P/8), 'set'), O(st(r'\frac{\pi}{4}'), S_(P/4), 'set')],
  r"$\tan2x=1$ ، و $0\le2x<2\pi$: $2x=\frac{\pi}{4},\ \frac{5\pi}{4}$" "\n" r"$x=\frac{\pi}{8},\ \frac{5\pi}{8}$",
  truth=lambda: sols(sin(2*x)-cos(2*x), 0, pi), tag='معادلة بزاوية مضاعفة في فترة'),
# ---------------- unit 3
# 2024 #2: f'(pi/2) of a trig function of a shifted angle plus a polynomial over pi (2 sin(x + pi) - x^2/pi ->
# 3 cos(x - pi) + x^2/(2pi)); options = sign x magnitude
Q('m10q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{2}\right)$ هي:", (r'3\cos(x-\pi)+\frac{x^{2}}{2\pi}', 3*cos(x-pi)+x**2/(2*pi))),
  [O(r'\frac{7}{2}', R(7, 2)), O(r'-\frac{5}{2}', -R(5, 2)), O(r'\frac{5}{2}', R(5, 2)), O(r'-\frac{7}{2}', -R(7, 2))],
  r"$f'(x)=-3\sin(x-\pi)+\dfrac{x}{\pi}$" "\n" r"$f'\left(\frac{\pi}{2}\right)=-3\sin\left(-\frac{\pi}{2}\right)+\frac12=3+\frac12=\frac72$",
  truth=Dx(3*cos(x-pi)+x**2/(2*pi)).subs(x, pi/2), tag='مشتقات الاقترانات المثلثية'),
# 2024s #10: b^(linear) with the value f'(a) given -> the point a (2^(-3x) -> 3^(2x - 1)); options = small integers
Q('m10q12', U3[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(a)=6\ln 3$ ، فإنّ قيمة الثابت $a$ هي:", (r'3^{2x-1}', 3**(2*x-1))),
  [O('1', 1), O('0', 0), O('2', 2), O('-1', -1)],
  r"$f'(x)=3^{2x-1}\ln3\cdot2$" "\n" r"$2\ln3\cdot3^{2a-1}=6\ln3 \Rightarrow 3^{2a-1}=3 \Rightarrow 2a-1=1 \Rightarrow a=1$",
  truth=lambda: [r_ for r_ in solve(Dx(3**(2*x-1)).subs(x, X)-6*log(3), X) if r_.is_real][0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2024 #3: velocity when the particle returns to its starting position (solve s(t) = s(0), t > 0); options = v(0), v(2),
# sign
Q('m10q13', U3[1], 'medium',
  F(r"يُمثّل الاقتران: $s(t)=«0»$ ، $t\ge0$ موقع جسم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار، و $t$ الزمن بالثواني، فإنّ سرعة الجسم المتجهة في اللحظة التي يعود فيها إلى موقعه الابتدائي هي:", (r't^{3}-6t^{2}+5', t**3-6*t**2+5)),
  [O('36', 36, units='m/s'), O('0', 0, units='m/s'), O('-12', -12, units='m/s'), O('-36', -36, units='m/s')],
  r"$s(0)=5$ ، و $t^3-6t^2+5=5 \Rightarrow t^2(t-6)=0 \Rightarrow t=6$ (بعد الانطلاق)" "\n" r"$v(t)=3t^2-12t \Rightarrow v(6)=108-72=36\ \text{m/s}$",
  truth=diff(t**3-6*t**2+5, t).subs(t, [r_ for r_ in solve(t**3-6*t**2, t) if r_ > 0][0]), tag='الحركة: السرعة والتسارع'),
# 2024 #5: f'' at a special angle of a reciprocal trig function plus a constant (csc x + e^2 at pi/4 -> sec x - pi^2 at
# pi/3); options = one product-rule term only (6, 8), the constant differentiated
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
# 2026r #8: x of the horizontal tangent of a^(quadratic) (6^(1 - x^2) -> 4^(2x - x^2)); options = list (the zeros 0 and 2
# of the exponent, the base 4 = f(1))
Q('m10q19', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ قيمة $x$ التي يكون عندها لمنحنى الاقتران $f(x)$ مماس أفقيّ هي:", (r'4^{2x-x^{2}}', 4**(2*x-x**2))),
  [O('1', 1), O('0', 0), O('2', 2), O('4', 4)],
  r"$f'(x)=4^{2x-x^2}\ln4\cdot(2-2x)$ ، و $4^{2x-x^2}\ln4\ne0$" "\n" r"$f'(x)=0 \Rightarrow 2-2x=0 \Rightarrow x=1$",
  truth=lambda: solve(Dx(4**(2*x-x**2)), x)[0], tag='نقاط المماس الأفقي'),
# 2026 #16: a^x ln y = x/y - 1 at y = 1 -> x e^y + y = 2x - 1 at y = 0 (the point found first); options = unit fractions
# and slips
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
# 2025s #19: division by a pure imaginary number (a single item there), here the first item of a shared stem as in
# 2026 #20-21; options = sign of the real part x sign of the imaginary part
Q('m10q24', U4[2], 'easy',
  r"ناتج $\dfrac{z}{w}$ بالصورة القياسية هو:",
  [O('-3+i', -3+I), O('3-i', 3-I), O('-3-i', -3-I), O('3+i', 3+I)],
  r"$\dfrac{2+6i}{-2i}\cdot\dfrac{i}{i}=\dfrac{2i+6i^2}{-2i^2}=\dfrac{-6+2i}{2}=-3+i$",
  truth=(2+6*I)/(-2*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=2+6i$ ، $w=-2i$", 24, 25)),
# 2025s #18: |z^2| for z = a + bi (a single item there), here the second item of the shared stem; options = |z|, a part
# of z^2, |z|^4
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
