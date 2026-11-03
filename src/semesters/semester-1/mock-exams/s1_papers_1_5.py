"""Semester-1 mock papers 1-5 (m1q1..m5q30). Per paper: U1 items 1-4, U2 items 5-10, U3 items 11-22, U4 items 23-30.
Every item names the official ministry item it is modelled on in the comment above it (2026 = paper of 2 July 2026,
gen 2008; 2026r = 2026 repeaters; 2025/2024/2023 = summer paper 1; 2025s/2024s = supplementary), or "E" for an
expected item: a 2008-book skill the ministry has not asked yet, written with a ministry template and no harder than
the ministry items of its lesson. Region items are checked by sampling (see s1_papers_6_10.py)."""
import cmath
import math
from s1_helpers import *
from s1_helpers import _sketch

# ================================================================== PAPER 1
# Each item names the official item it is modelled on (2026 = 2 July 2026 paper, gen 2008; 2025/2024/2023 = summer
# paper 1; 2025s/2024s = supplementary; 2026r = 2026 repeaters; E = expected skill of the 2008 book, written with a
# ministry template). Same skill, same stem structure, same kind of function and numbers, same option grid.
f1_17, fs1_17 = pw([(0, 1), (2, 5), (6, 3)])
g1_17, gs1_17 = pw([(0, 6), (4, 2), (6, 6)])
C1_30, V1_30 = 1j, -1 + 1j
R1_30 = both(disk(C1_30, 3), sector(V1_30, -math.pi/2, math.pi/4, hi_open=True))
PR1_30 = [('arc', C1_30, 3, False, (0.0, 2*math.pi)), ('seg', V1_30, -1 - 2.6j, False), ('seg', V1_30, 2.3 + 4.3j, True), ('open', V1_30)]
P1 = [
# ---------------- unit 1
# 2026 #1: one root given, equation not set to zero (x^3 + ax^2 = bx + c), the quotient factors over the integers;
# options = sign of each of the other two roots
Q('m1q1', U1[1], 'easy',
  F(r"إذا كان $x=-3$ حلًّا للمعادلة: $«0»=«1»$ ، فإنّ لها حلَّين آخرين هما:", (r'x^{3}+5x^{2}', x**3+5*x**2), (r'2x+24', 2*x+24)),
  [O(st('2', '-4'), S_(2, -4), 'set'), O(st('-2', '4'), S_(-2, 4), 'set'), O(st('2', '4'), S_(2, 4), 'set'), O(st('-2', '-4'), S_(-2, -4), 'set')],
  r"نكتب المعادلة: $x^3+5x^2-2x-24=0$ ، وبالقسمة التركيبية على $(x+3)$: $1,\ 5,\ -2,\ -24 \to 1,\ 2,\ -8,\ 0$" "\n"
  r"$x^2+2x-8=(x+4)(x-2)=0 \Rightarrow x=2,\ x=-4$",
  truth=lambda: other_roots(x**3+5*x**2-2*x-24, -3), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# E (expected: remainder on a quadratic divisor from two remainders), template 2026 #3: the divisor x gives b at once,
# then f(2) gives a; options = zero of (x - 2) right or wrong (sign of a) x remainder written ax + b or bx + a
Q('m1q2', U1[1], 'medium',
  r"إذا كان باقي قسمة كثير الحدود $f(x)$ على $x$ هو $3$ ، وباقي قسمته على $(x-2)$ هو $7$ ، فإنّ باقي قسمة $f(x)$ على $x(x-2)$ هو:",
  [O('2x+3', 2*x+3), O('-2x+3', -2*x+3), O('3x+2', 3*x+2), O('3x-2', 3*x-2)],
  r"الباقي على الصورة $ax+b$: $f(0)=b=3$" "\n" r"$f(2)=2a+b=7 \Rightarrow 2a=4 \Rightarrow a=2$ ، والباقي $2x+3$",
  truth=lambda: (lambda s_: s_[a]*x+s_[b])(solve([b-3, 2*a+b-7], [a, b])), tag='باقي القسمة على مقدار تربيعي'),
# 2026 #2: which is the decomposition, repeated linear factor; options = constants swapped, sign of B, the constant
# term taken as A
Q('m1q3', U1[2], 'easy',
  F(r"أيّ الآتية يُمثّل تجزئة المقدار النسبي: $«0»$ إلى كسور جزئية؟", (r'\frac{4x+11}{(x+2)^{2}}', (4*x+11)/(x+2)**2)),
  [O(r'\frac{4}{x+2}+\frac{3}{(x+2)^{2}}', 4/(x+2)+3/(x+2)**2), O(r'\frac{3}{x+2}+\frac{4}{(x+2)^{2}}', 3/(x+2)+4/(x+2)**2),
   O(r'\frac{4}{x+2}-\frac{3}{(x+2)^{2}}', 4/(x+2)-3/(x+2)**2), O(r'\frac{11}{x+2}+\frac{4}{(x+2)^{2}}', 11/(x+2)+4/(x+2)**2)],
  r"$4x+11=A(x+2)+B$ ، عند $x=-2$: $B=3$ ، ومعامل $x$: $A=4$",
  truth=(4*x+11)/(x+2)**2, tag='تجزئة: عامل خطي مكرر'),
# E (expected: constants of a given decomposition), template 2026 #2 / #10: x = 4 gives a at once, then x = -2 gives A;
# options = small integers (a alone, A alone, a slip)
Q('m1q4', U1[2], 'medium',
  F(r"إذا كان: $«0»=\dfrac{A}{x+2}+\dfrac{3}{x-4}$ ، حيث $a,\ A$ ثابتان، فإنّ قيمة $a+A$ هي:", (r'\frac{ax-2}{(x+2)(x-4)}', (a*x-2)/((x+2)*(x-4)))),
  [O('7', 7), O('5', 5), O('2', 2), O('8', 8)],
  r"$ax-2=A(x-4)+3(x+2)$" "\n" r"عند $x=4$: $4a-2=18 \Rightarrow a=5$" "\n" r"عند $x=-2$: $-2a-2=-6A \Rightarrow -12=-6A \Rightarrow A=2$ ، إذن $a+A=7$",
  truth=lambda: (lambda s_: s_[a]+s_[b])(solve(Poly(expand(a*x-2-b*(x-4)-3*(x+2)), x).all_coeffs(), [a, b])), tag='إيجاد ثوابت في التجزئة'),
# ---------------- unit 2
# 2026 #4: sin(theta/2) from cos theta and a quadrant (3rd); options = sign x sin/cos half-angle formula
Q('m1q5', U2[2], 'medium',
  r"إذا كان $\cos\theta=-\frac{7}{9}$ ، حيث $\pi<\theta<\frac{3\pi}{2}$ ، فإنّ قيمة $\sin\frac{\theta}{2}$ تساوي:",
  [O(r'\frac{2\sqrt{2}}{3}', 2*sqrt(2)/3), O(r'-\frac{2\sqrt{2}}{3}', -2*sqrt(2)/3), O(r'\frac{1}{3}', R(1, 3)), O(r'-\frac{1}{3}', -R(1, 3))],
  r"$\frac{\pi}{2}<\frac{\theta}{2}<\frac{3\pi}{4}$ ، أي في الربع الثاني فالجيب موجب" "\n"
  r"$\sin\frac{\theta}{2}=\sqrt{\dfrac{1-\cos\theta}{2}}=\sqrt{\dfrac{1+\frac79}{2}}=\sqrt{\dfrac89}=\dfrac{2\sqrt2}{3}$",
  truth=sin((pi+acos(R(7, 9)))/2), tag='نصف الزاوية مع تحديد الربع'),
# 2026 #5: simplest form with a sum identity, one term cancels; options = coefficient (cos vs sin of pi/3) x surviving
# function, and the coefficient dropped
Q('m1q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\sin(x+\frac{\pi}{3})-\frac{\sqrt{3}}{2}\cos x', sin(x+pi/3)-sqrt(3)/2*cos(x))),
  [O(r'\frac{1}{2}\sin x', sin(x)/2), O(r'\frac{\sqrt{3}}{2}\sin x', sqrt(3)/2*sin(x)), O(r'\frac{1}{2}\cos x', cos(x)/2), O(r'\sin x', sin(x))],
  r"$\sin\left(x+\frac{\pi}{3}\right)=\sin x\cos\frac{\pi}{3}+\cos x\sin\frac{\pi}{3}=\frac12\sin x+\frac{\sqrt3}{2}\cos x$" "\n" r"بطرح $\frac{\sqrt3}{2}\cos x$ يبقى $\frac12\sin x$",
  truth=sin(x+pi/3)-sqrt(3)/2*cos(x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# E (expected: double angle from a ratio and a quadrant), template 2026 #4: cos 2theta from tan theta in the 2nd
# quadrant; options = sign x cos 2theta / sin 2theta value
Q('m1q7', U2[2], 'medium',
  r"إذا كان $\tan\theta=-\frac{3}{4}$ ، حيث $\frac{\pi}{2}<\theta<\pi$ ، فإنّ قيمة $\cos2\theta$ تساوي:",
  [O(r'\frac{7}{25}', R(7, 25)), O(r'-\frac{7}{25}', -R(7, 25)), O(r'\frac{24}{25}', R(24, 25)), O(r'-\frac{24}{25}', -R(24, 25))],
  r"$\cos2\theta=\dfrac{1-\tan^2\theta}{1+\tan^2\theta}=\dfrac{1-\frac{9}{16}}{1+\frac{9}{16}}=\dfrac{7}{25}$" "\n" r"(أو: $\cos\theta=-\frac45$ ، $\cos2\theta=2\cos^2\theta-1=\frac{32}{25}-1=\frac{7}{25}$)",
  truth=cos(2*(pi-atan(R(3, 4)))), tag='ضعف الزاوية بمعلومية نسبة'),
# E (expected: sum to product, exact value), template 2026 #5: cos 75 + cos 15; options = special values (sin 30 used
# for cos 30, cos 30 alone, 1)
Q('m1q8', U2[2], 'easy',
  r"قيمة المقدار: $\cos75^\circ+\cos15^\circ$ هي:",
  [O(r'\frac{\sqrt{6}}{2}', sqrt(6)/2), O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O('1', 1)],
  r"$\cos A+\cos B=2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}=2\cos45^\circ\cos30^\circ=2\cdot\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}=\frac{\sqrt6}{2}$",
  truth=cos(deg(75))+cos(deg(15)), tag='تحويل المجموع إلى ضرب'),
# 2026 #7: quadratic in sin x, one root rejected (sin x = -3); options = solution pairs (sign of sin x, reference angle,
# quadrant)
Q('m1q9', U2[3], 'easy',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\sin^{2}x+5\sin x-3', 2*sin(x)**2+5*sin(x)-3)),
  [O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'), O(st(r'\frac{7\pi}{6}', r'\frac{11\pi}{6}'), S_(7*P/6, 11*P/6), 'set'),
   O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set')],
  r"بالتحليل: $(2\sin x-1)(\sin x+3)=0$" "\n" r"$\sin x=-3$ مرفوض، و $\sin x=\frac12 \Rightarrow x=\frac{\pi}{6},\ \frac{5\pi}{6}$",
  truth=lambda: sols(2*sin(x)**2+5*sin(x)-3, 0, 2*pi), tag='معادلة تربيعية في نسبة مثلثية مع رفض حل'),
# E (expected: half-angle equation in an interval), template 2026 #8: tan(x/2) + 1 = 0 in [0, 2pi), so x/2 in [0, pi);
# options = doubled or not x interval of x/2 halved or not (an extra solution shifted out of the interval)
Q('m1q10', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'\tan\frac{x}{2}+1', tan(x/2)+1)),
  [O(st(r'\frac{3\pi}{2}'), S_(3*P/2), 'set'), O(st(r'\frac{3\pi}{2}', r'\frac{7\pi}{2}'), S_(3*P/2, 7*P/2), 'set'),
   O(st(r'\frac{3\pi}{4}'), S_(3*P/4), 'set'), O(st(r'\frac{3\pi}{4}', r'\frac{7\pi}{4}'), S_(3*P/4, 7*P/4), 'set')],
  r"$0\le x<2\pi \Rightarrow 0\le\frac{x}{2}<\pi$ ، و $\tan\frac{x}{2}=-1$" "\n"
  r"في $[0,\pi)$ يكون الظل سالبًا في الربع الثاني فقط: $\frac{x}{2}=\frac{3\pi}{4} \Rightarrow x=\frac{3\pi}{2}$",
  truth=lambda: sols(tan(x/2)+1, 0, 2*pi), tag='معادلة بنصف الزاوية'),
# ---------------- unit 3
# 2026 #9: f'(x) and f(x) combine into one ratio (f = sec x + tan x, f'/f = sec x); options = sec x, tan x, sec x tan x,
# csc x
Q('m1q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $\dfrac{f'(x)}{f(x)}$ يساوي:", (r'\sec x+\tan x', sec(x)+tan(x))),
  [O(r'\sec x', sec(x)), O(r'\tan x', tan(x)), O(r'\sec x\tan x', sec(x)*tan(x)), O(r'\csc x', csc(x))],
  r"$f'(x)=\sec x\tan x+\sec^2x=\sec x(\tan x+\sec x)=\sec x\cdot f(x)$ ، إذن $\dfrac{f'(x)}{f(x)}=\sec x$",
  truth=Dx(sec(x)+tan(x))/(sec(x)+tan(x)), tag='مشتقات الاقترانات المثلثية'),
# 2025 #6: dy/dx of (a + sin 2x)/(b + cos 2x), numerator simplified with sin^2 + cos^2, denominator rewritten as
# (b - 1 + 2cos^2 x)^2; options = numerator constant 2 vs 1 x denominator form (right, wrong identity, not rewritten)
Q('m1q12', U3[2], 'medium',
  F(r"إذا كان: $y=«0»$ ، فإنّ $\dfrac{dy}{dx}$ هي:", (r'\frac{2+\sin 2x}{4+\cos 2x}', (2+sin(2*x))/(4+cos(2*x)))),
  [O(r'\frac{4\sin 2x+8\cos 2x+2}{(3+2\cos^{2}x)^{2}}', (4*sin(2*x)+8*cos(2*x)+2)/(3+2*cos(x)**2)**2),
   O(r'\frac{4\sin 2x+8\cos 2x+1}{(3+2\cos^{2}x)^{2}}', (4*sin(2*x)+8*cos(2*x)+1)/(3+2*cos(x)**2)**2),
   O(r'\frac{4\sin 2x+8\cos 2x+2}{(5+2\cos^{2}x)^{2}}', (4*sin(2*x)+8*cos(2*x)+2)/(5+2*cos(x)**2)**2),
   O(r'\frac{4\sin 2x+8\cos 2x+1}{(4+\cos 2x)^{2}}', (4*sin(2*x)+8*cos(2*x)+1)/(4+cos(2*x))**2)],
  r"$\dfrac{dy}{dx}=\dfrac{2\cos2x\,(4+\cos2x)-(2+\sin2x)(-2\sin2x)}{(4+\cos2x)^2}=\dfrac{8\cos2x+4\sin2x+2(\cos^22x+\sin^22x)}{(4+\cos2x)^2}$" "\n"
  r"البسط $4\sin2x+8\cos2x+2$ ، و $4+\cos2x=4+2\cos^2x-1=3+2\cos^2x$",
  truth=diff((2+sin(2*x))/(4+cos(2*x)), x), tag='مشتقة القسمة'),
# 2025s #7: point on y = k/(x + c) with a domain restriction where f'(x) has a given value, the domain rejects one root;
# options = which root of (x - 1)^2 = 4 x sign of the y-coordinate
Q('m1q13', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»,\ x<1$ ، فإنّ إحداثيَّي النقطة التي يكون عندها $f'(x)=-2$ هما:", (r'\frac{8}{x-1}', 8/(x-1))),
  [O(r'(-1,\ -4)', Tuple(-1, -4), 'tuple'), O(r'(-1,\ 4)', Tuple(-1, 4), 'tuple'), O(r'(3,\ 4)', Tuple(3, 4), 'tuple'), O(r'(3,\ -4)', Tuple(3, -4), 'tuple')],
  r"$f'(x)=-\dfrac{8}{(x-1)^2}=-2 \Rightarrow (x-1)^2=4 \Rightarrow x=3$ أو $x=-1$" "\n"
  r"الشرط $x<1$ يرفض $x=3$ ، إذن $x=-1$ و $f(-1)=\dfrac{8}{-2}=-4$ ، والنقطة $(-1,\,-4)$",
  truth=lambda: (lambda r_: Tuple(r_, 8/(r_-1)))([r_ for r_ in solve(Dx(8/(x-1))+2, x) if r_ < 1][0]), tag='نقطة بمعلومية قيمة المشتقة'),
# 2024s #11: log base a of a quadratic at a point; options = ln a missing / inverted, chain factor slip
Q('m1q14', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(2)$ تساوي:", (r'\log_{5}(x^{2}+1)', log(x**2+1, 5))),
  [O(r'\frac{4}{5\ln 5}', 4/(5*log(5))), O(r'\frac{4}{5}', R(4, 5)), O(r'\frac{4\ln 5}{5}', 4*log(5)/5), O(r'\frac{2}{5\ln 5}', 2/(5*log(5)))],
  r"$f'(x)=\dfrac{2x}{(x^2+1)\ln5} \Rightarrow f'(2)=\dfrac{4}{5\ln5}$",
  truth=Dx(log(x**2+1, 5)).subs(x, 2), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2026r #5: f'(special angle) of a reciprocal-trig function minus (c + another one): tan x - (2 + csc x) at pi/4 ->
# sec x - (4 + cot x) at pi/6; options = list of values (the sum, sign slip on the bracket term, each term alone)
Q('m1q15', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{6}\right)$ هي:", (r'\sec x-(4+\cot x)', sec(x)-(4+cot(x)))),
  [O(r'\frac{14}{3}', R(14, 3)), O(r'-\frac{10}{3}', -R(10, 3)), O(r'\frac{2}{3}', R(2, 3)), O('4', 4)],
  r"$f'(x)=\sec x\tan x-(0-\csc^2x)=\sec x\tan x+\csc^2x$" "\n"
  r"$f'\left(\frac{\pi}{6}\right)=\frac{2}{\sqrt3}\cdot\frac{1}{\sqrt3}+(2)^2=\frac23+4=\frac{14}{3}$",
  truth=Dx(sec(x)-(4+cot(x))).subs(x, pi/6), tag='مشتقات الاقترانات المثلثية'),
# 2023 #15: interval of motion in the negative direction for a cubic s(t); options = intervals built from the zeros of v
IndexQ('m1q16', U3[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t\ge0$ الزمن بالثواني، و $s$ الموقع بالأمتار. الفترة الزمنية التي يتحرّك فيها الجُسيم في الاتجاه السالب هي:", (r't^{3}-9t^{2}+24t', t**3-9*t**2+24*t)),
  [T(r'$(2,\ 4)$', Interval.open(2, 4)), T(r'$(0,\ 2)$', Interval.open(0, 2)), T(r'$(4,\ \infty)$', Interval.open(4, oo)), T(r'$(0,\ 4)$', Interval.open(0, 4))],
  r"$v(t)=3t^2-18t+24=3(t-2)(t-4)$" "\n" r"تكون $v(t)<0$ عندما $2<t<4$ ، فيتحرّك الجُسيم في الاتجاه السالب في الفترة $(2,\,4)$",
  truth=lambda vals: only(vals, lambda iv: iv == solve_univariate_inequality(diff(t**3-9*t**2+24*t, t) < 0, t, relational=False)), tag='الحركة: اتجاه الحركة والسكون'),
# 2024s #5: two piecewise-linear graphs, product rule h = f g at a point; options = integers from the readings (sign of
# g', f(1) alone)
Q('m1q17', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=f(x)\cdot g(x)$ ، فإنّ $h'(1)$ تساوي:",
  [O('7', 7), O('13', 13), O('-7', -7), O('3', 3)],
  r"من الشكل: $f(1)=3$ ، $f'(1)=2$ (ميل القطعة من $(0,1)$ إلى $(2,5)$) ، $g(1)=5$ ، $g'(1)=-1$ (ميل القطعة من $(0,6)$ إلى $(4,2)$)" "\n"
  r"$h'(1)=f'(1)g(1)+f(1)g'(1)=2(5)+3(-1)=7$",
  truth=lambda: fs1_17(1)*g1_17(1)+f1_17(1)*gs1_17(1), figure=figure('m1q17', draw_two([(0, 1), (2, 5), (6, 3)], [(0, 6), (4, 2), (6, 6)], 6, 6, (0.3, 6.3), (5.0, 5.6))),
  tag='المشتقة من التمثيل البياني'),
# 2025s #4 (plant height t^2/(4 + t^2): quotient rule at t = 1, units in the options): drug concentration 20t/(t^2 + 4);
# options = numerator order (sign), the value C(1), a slip
Q('m1q18', U3[2], 'medium',
  F(r"يُمثّل الاقتران: $C(t)=«0»$ تركيز دواء في الدم بالمليغرام لكل لتر بعد $t$ ساعة من تناوله. معدّل تغيّر التركيز عندما $t=1$ هو:", (r'\frac{20t}{t^{2}+4}', 20*t/(t**2+4))),
  [O(r'\frac{12}{5}', R(12, 5), units='mg/L/h'), O(r'-\frac{12}{5}', -R(12, 5), units='mg/L/h'), O('4', 4, units='mg/L/h'), O(r'\frac{4}{5}', R(4, 5), units='mg/L/h')],
  r"$C'(t)=\dfrac{20(t^2+4)-20t(2t)}{(t^2+4)^2}=\dfrac{80-20t^2}{(t^2+4)^2}$ ، إذن $C'(1)=\dfrac{60}{25}=\dfrac{12}{5}$",
  truth=diff(20*t/(t**2+4), t).subs(t, 1), tag='معدل التغير في سياق حياتي'),
# 2026 #15: parametric with csc/cot at a special t; options = reciprocal (dx/dy), sign, sin used for cos
Q('m1q19', U3[3], 'medium',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، حيث $0<t<\pi$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\frac{\pi}{3}$ هي:", (r'3\csc t', 3*csc(t)), (r'\cot t-2', cot(t)-2)),
  [O(r'\frac{2}{3}', R(2, 3)), O(r'\frac{3}{2}', R(3, 2)), O(r'-\frac{2}{3}', -R(2, 3)), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3)],
  r"$\dfrac{dy}{dx}=\dfrac{-\csc^2t}{-3\csc t\cot t}=\dfrac{\csc t}{3\cot t}=\dfrac{1}{3\cos t}$" "\n" r"عند $t=\frac{\pi}{3}$: $\dfrac{1}{3\cdot\frac12}=\dfrac23$",
  truth=(diff(cot(t)-2, t)/diff(3*csc(t), t)).subs(t, pi/3), tag='مشتقة المعادلات الوسيطية'),
# 2024 #9: implicit dy/dx of y^2 = ln(xy) at (e, 1) -> y^3 = ln(xy) at (e, 1); options = y'/y kept or dropped in
# d/dx ln y x sign of that term when it is collected
Q('m1q20', U3[4], 'medium',
  F(r"إذا كانت: $«0»=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(e,\,1)$ هي:", (r'y^{3}', y**3), (r'\ln(xy)', log(x*y))),
  [O(r'\frac{1}{2e}', 1/(2*E)), O(r'\frac{1}{4e}', 1/(4*E)), O(r'\frac{1+e}{3e}', (1+E)/(3*E)), O(r'\frac{1-e}{3e}', (1-E)/(3*E))],
  r"$\ln(xy)=\ln x+\ln y$ ، فباشتقاق الطرفين: $3y^2\dfrac{dy}{dx}=\dfrac1x+\dfrac1y\dfrac{dy}{dx}$" "\n"
  r"عند $(e,1)$: $3y'=\dfrac1e+y' \Rightarrow 2y'=\dfrac1e \Rightarrow y'=\dfrac{1}{2e}$",
  truth=imp(y**3-log(x*y), (E, 1)), tag='الاشتقاق الضمني عند نقطة'),
# 2026 #17: tangent to an implicit curve at a lattice point, y-intercept; options = sign slip in the line, the slope,
# sign of the intercept
Q('m1q21', U3[4], 'hard',
  F(r"إذا مثّل المستقيم $l$ مماسًّا لمنحنى العلاقة: $«0»=7$ عند النقطة $(-1,\,2)$ ، فإنّ المقطع $y$ للمستقيم $l$ هو:", (r'x^{2}-xy+y^{2}', x**2-x*y+y**2)),
  [O(r'\frac{14}{5}', R(14, 5)), O(r'\frac{6}{5}', R(6, 5)), O(r'\frac{4}{5}', R(4, 5)), O(r'-\frac{14}{5}', -R(14, 5))],
  r"$2x-y-xy'+2yy'=0 \Rightarrow y'=\dfrac{y-2x}{2y-x}$ ، وعند $(-1,2)$: $y'=\dfrac{2+2}{4+1}=\dfrac45$" "\n"
  r"المماس: $y-2=\frac45(x+1)$ ، وعند $x=0$: $y=2+\frac45=\frac{14}{5}$",
  truth=lambda: 2 + imp(x**2-x*y+y**2-7, (-1, 2))*(0+1), tag='مماس منحنى علاقة ضمنية'),
# 2026 #18: cylindrical tank (figure: height and base diameter in m) filled in L/min, constant dh/dt in m/min;
# options = L -> m^3 conversion done or not x base area pi r^2 vs the height used instead of r^2
Q('m1q22', U3[5], 'medium',
  r"يُبيّن الشكل الآتي خزّانًا على شكل أسطوانة دائرية قائمة ارتفاعه $5\ \text{m}$ ، وطول قُطر قاعدته $3\ \text{m}$ ، يُضَخّ إليه الماء بمعدّل $450\ \text{L/min}$ ، فإنّ معدّل تغيّر ارتفاع الماء في الخزّان عند أيّ لحظة هو:",
  [O(r'\frac{1}{5\pi}', 1/(5*pi), units='m/min'), O(r'\frac{9}{100\pi}', R(9, 100)/pi, units='m/min'), O(r'\frac{200}{\pi}', 200/pi, units='m/min'), O(r'\frac{90}{\pi}', 90/pi, units='m/min')],
  r"$450\ \text{L}=0.45\ \text{m}^3$ ، ونصف القطر $r=1.5\ \text{m}$" "\n"
  r"$V=\pi r^2h=2.25\pi h \Rightarrow 0.45=2.25\pi\dfrac{dh}{dt} \Rightarrow \dfrac{dh}{dt}=\dfrac{0.45}{2.25\pi}=\dfrac{1}{5\pi}\ \text{m/min}$",
  truth=R(45, 100)/(pi*R(3, 2)**2), figure=figure('m1q22', fig_tank(r'$3\ \mathrm{m}$', r'$5\ \mathrm{m}$'), 2.8, 3.2), tag='معدلات مرتبطة مع تحويل الوحدات'),
# ---------------- unit 4
# 2026 #19: z = a + bi with a sign condition and |z| given -> trig form; options = quadrant and reference-angle slips
Q('m1q23', U4[1], 'medium',
  r"إذا كان: $z=a+2\sqrt{3}\,i$ ، حيث $a<0$ ، وكان: $|z|=4$ ، فإنّ الصورة المثلثية للعدد المُركَّب $z$ هي:",
  [O(trig('4', r'\frac{2\pi}{3}'), pol(4, 2*P/3)), O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3)), O(trig('4', r'-\frac{2\pi}{3}'), pol(4, -2*P/3)), O(trig('4', r'\frac{5\pi}{6}'), pol(4, 5*P/6))],
  r"$a^2+12=16 \Rightarrow a=-2$ (لأن $a<0$) ، فيكون $z=-2+2\sqrt3\,i$ في الربع الثاني" "\n"
  r"زاوية الإسناد $\tan^{-1}\left(\frac{2\sqrt3}{2}\right)=\frac{\pi}{3}$ ، و $\text{Arg}(z)=\pi-\frac{\pi}{3}=\frac{2\pi}{3}$",
  truth=lambda: [r_ for r_ in solve(a**2+12-16, a) if r_ < 0][0] + 2*sqrt(3)*I, tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2026 #20 (z + iw + k) / 2026r #22 (2z - 3w): shared stem, 2z - iw; options = real part x imaginary part slips
Q('m1q24', U4[2], 'easy',
  r"ناتج $2z-iw$ هو:",
  [O('3-7i', 3-7*I), O('1-7i', 1-7*I), O('3-i', 3-I), O('1+7i', 1+7*I)],
  r"$2z=2-4i$ ، $iw=i(3+i)=3i+i^2=-1+3i$" "\n" r"$2z-iw=(2-4i)-(-1+3i)=3-7i$",
  truth=expand(2*(1-2*I)-I*(3+I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=1-2i$ ، $w=3+i$", 24, 25)),
# 2026r #21: second item of the shared stem, the quotient z/w; options = sign of the imaginary part, parts divided
# separately, i^2 slip
Q('m1q25', U4[2], 'medium',
  r"ناتج $\dfrac{z}{w}$ في الصورة القياسية هو:",
  [O(r'\frac{1-7i}{10}', (1-7*I)/10), O(r'\frac{1+7i}{10}', (1+7*I)/10), O(r'\frac{1-i}{2}', (1-I)/2), O(r'\frac{-1-7i}{10}', (-1-7*I)/10)],
  r"$\dfrac{1-2i}{3+i}\cdot\dfrac{3-i}{3-i}=\dfrac{3-i-6i+2i^2}{10}=\dfrac{1-7i}{10}$",
  truth=(1-2*I)/(3+I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2024 #19: z = c + ai with |z| given -> the positive value of a; options = 2x2 value grid (5 or 3 under the root x root
# taken or not)
Q('m1q26', U4[1], 'easy',
  r"إذا كان: $z=2+ai$ ، حيث $|z|=3$ ، فإنّ القيمة الموجبة للثابت $a$ هي:",
  [O(r'\sqrt{5}', sqrt(5)), O('5', 5), O(r'\sqrt{3}', sqrt(3)), O('3', 3)],
  r"$|z|=\sqrt{2^2+a^2}=3 \Rightarrow 4+a^2=9 \Rightarrow a^2=5 \Rightarrow a=\sqrt5$ (القيمة الموجبة)",
  truth=lambda: [r_ for r_ in solve(4+a**2-9, a) if r_ > 0][0], tag='إيجاد ثابت بمعلومية المقياس'),
# 2024s #18: sqrt(-p/q) x k i^n in simplest form (answer real and negative); options = sign x real vs imaginary
Q('m1q27', U4[1], 'easy',
  F(r"قيمة: $«0»$ في أبسط صورة هي:", (r'\sqrt{\dfrac{-25}{8}}\times4\,i^{9}', sqrt(R(-25, 8))*4*I**9)),
  [O(r'-5\sqrt{2}', -5*sqrt(2)), O(r'5\sqrt{2}', 5*sqrt(2)), O(r'5\sqrt{2}\,i', 5*sqrt(2)*I), O(r'-5\sqrt{2}\,i', -5*sqrt(2)*I)],
  r"$\sqrt{\dfrac{-25}{8}}=\dfrac{5}{2\sqrt2}\,i$ ، و $i^9=i^8\cdot i=i$" "\n"
  r"$4\cdot\dfrac{5}{2\sqrt2}\,i\cdot i=\dfrac{10}{\sqrt2}\,i^2=-5\sqrt2$",
  truth=expand(sqrt(R(-25, 8))*4*I**9), tag='قوى i'),
# 2026 #24: smaller angle between two numbers in different quadrants (difference of the arguments below pi); options =
# the larger angle, Arg z2 taken positive, Arg z1 alone
Q('m1q28', U4[2], 'medium',
  r"إذا كان: $z_1=-1+\sqrt{3}\,i$ ، $z_2=\sqrt{3}-i$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{5\pi}{6}', 5*P/6), O(r'\frac{7\pi}{6}', 7*P/6), O(r'\frac{\pi}{2}', P/2), O(r'\frac{2\pi}{3}', 2*P/3)],
  r"$\text{Arg}(z_1)=\frac{2\pi}{3}$ ، $\text{Arg}(z_2)=-\frac{\pi}{6}$ ، والفرق $\frac{2\pi}{3}+\frac{\pi}{6}=\frac{5\pi}{6}<\pi$ فهو الزاوية الصغرى",
  truth=acos(re(expand((-1+sqrt(3)*I)*conjugate(sqrt(3)-I)))/(Abs(-1+sqrt(3)*I)*Abs(sqrt(3)-I))), tag='الزاوية بين عددين مركبين'),
# E (expected: Cartesian equation of a locus |z - z1| = |z - z2|), template 2023 #25 (perpendicular bisector): square
# both moduli and simplify; options = sign slips, the slope of the segment itself
Q('m1q29', U4[3], 'medium',
  r"المعادلة الديكارتية للمحل الهندسي: $|z+2i|=|z-4|$ هي:",
  [O('y=-2x+3', -2*x+3, 'eq'), O('y=2x-3', 2*x-3, 'eq'), O('y=-2x-3', -2*x-3, 'eq'), O(r'y=\frac{1}{2}x+3', x/2+3, 'eq')],
  r"$x^2+(y+2)^2=(x-4)^2+y^2 \Rightarrow 4y+4=-8x+16 \Rightarrow y=-2x+3$",
  truth=lambda: solve(expand(X**2+(Y+2)**2-(X-4)**2-Y**2), Y)[0].subs(X, x), tag='المعادلة الديكارتية لمحل هندسي'),
# 2026 #25: disc (solid) cut by a wedge whose vertex is not the centre, one ray dashed; options = vertex sign x which
# boundary is strict
IndexQ('m1q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثِّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z-i|\le3$ ، $-\frac{\pi}{2}\le\text{Arg}(z+1-i)<\frac{\pi}{4}$', R1_30),
   T(r'$|z-i|\le3$ ، $-\frac{\pi}{2}<\text{Arg}(z+1-i)\le\frac{\pi}{4}$', both(disk(C1_30, 3), sector(V1_30, -math.pi/2, math.pi/4, lo_open=True))),
   T(r'$|z-i|\le3$ ، $-\frac{\pi}{2}\le\text{Arg}(z-1+i)<\frac{\pi}{4}$', both(disk(C1_30, 3), sector(-V1_30, -math.pi/2, math.pi/4, hi_open=True))),
   T(r'$|z-i|\le3$ ، $-\frac{\pi}{2}<\text{Arg}(z-1+i)\le\frac{\pi}{4}$', both(disk(C1_30, 3), sector(-V1_30, -math.pi/2, math.pi/4, lo_open=True)))],
  r"الدائرة متصلة، مركزها $(0,1)$ أي العدد $i$ ، ونصف قطرها $3$: $|z-i|\le3$" "\n"
  r"الشعاعان يبدآن من $(-1,1)$ أي العدد $-1+i$: $\text{Arg}(z+1-i)$ ؛ الرأسي إلى الأسفل متصل ($-\frac{\pi}{2}\le$) والمائل بزاوية $\frac{\pi}{4}$ متقطّع ($<\frac{\pi}{4}$)",
  truth=region_truth(R1_30, PR1_30, 5), figure=figure('m1q30', fig_region2(R1_30, PR1_30, 5), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]


# ================================================================== PAPER 2
F2_16 = [(0, 1), (2, 5), (6, 1)]                     # graph of f (m2q16): f(1) = 3, f'(1) = 2
G2_20 = x**2 + 4*y**2 - 4*x - 8*y                   # implicit curve G2_20 = 8 (m2q20)
C2_30 = 1 - 1j                                      # m2q30: solid disc |z - 1 + i| <= 3 cut by the dashed bisector y = 1
R2_30 = both(disk(C2_30, 3), closer(0, 2j))
A2_30 = math.asin(2/3)
PR2_30 = [('arc', C2_30, 3, False, (math.pi - A2_30, 2*math.pi + A2_30)),
          ('seg', complex(1 - math.sqrt(5), 1), complex(1 + math.sqrt(5), 1), True)]


def fig_rocket2():
    """rocket rising vertically from B, watched from A 3 km away (m2q22)."""
    import matplotlib.patches as mpatches

    def draw(fig, ax):
        _sketch(fig, ax)
        ax.plot([-0.5, 9.6], [0, 0], color='#333333', lw=1.4)
        ax.plot([0, 8], [0, 6.0], color='#555555', lw=1.2, ls='--')
        ax.plot([8, 8], [0, 5.9], color='#1f5fbf', lw=1.2)
        ax.plot([7.6, 7.6, 8], [0, 0.4, 0.4], color='#333333', lw=1)
        ax.add_patch(mpatches.Polygon([[7.82, 6.0], [8.18, 6.0], [8.18, 7.0], [8.0, 7.45], [7.82, 7.0]], closed=True, color='#d04a1a'))
        ax.add_patch(mpatches.Polygon([[7.82, 6.0], [7.6, 5.8], [7.82, 6.4]], closed=True, color='#d04a1a'))
        ax.add_patch(mpatches.Polygon([[8.18, 6.0], [8.4, 5.8], [8.18, 6.4]], closed=True, color='#d04a1a'))
        ax.annotate('', (8.8, 7.6), (8.8, 6.3), arrowprops=dict(arrowstyle='->', color='#333333', lw=1))
        ax.add_patch(mpatches.Arc((0, 0), 2.6, 2.6, theta1=0, theta2=36.87, color='#d04a1a', lw=1.2))
        ax.text(1.45, 0.3, r'$\theta$', fontsize=12, color='#d04a1a')
        ax.text(3.5, -0.8, r'$3\ \mathrm{km}$', fontsize=10); ax.text(8.3, 2.8, r'$h$', fontsize=12, color='#1f5fbf')
        ax.plot(0, 0, 'o', color='#333333', ms=5); ax.text(-0.5, -0.8, r'$A$', fontsize=11)
        ax.plot(8, 0, 'o', color='#333333', ms=4); ax.text(8.15, -0.8, r'$B$', fontsize=11)
        ax.set_xlim(-0.8, 9.8); ax.set_ylim(-1.2, 7.9)
    return draw


P2 = [
# ---------------- unit 1
# E (expected: rational zeros, the set of zeros of a cubic), template 2026 #1: one zero, one synthetic division, factor the quotient; options = sets of three zeros (signs)
Q('m2q1', U1[1], 'medium',
  F(r"مجموعة أصفار الاقتران: $f(x)=«0»$ هي:", (r'2x^{3}+3x^{2}-11x-6', 2*x**3+3*x**2-11*x-6)),
  [O(r'\{2,\ -3,\ -\frac{1}{2}\}', S_(2, -3, -R(1, 2)), 'set'), O(r'\{-2,\ 3,\ \frac{1}{2}\}', S_(-2, 3, R(1, 2)), 'set'),
   O(r'\{2,\ -3,\ \frac{1}{2}\}', S_(2, -3, R(1, 2)), 'set'), O(r'\{1,\ -3,\ -2\}', S_(1, -3, -2), 'set')],
  r"$f(2)=16+12-22-6=0$ ، وبالقسمة التركيبية على $(x-2)$: $2,\ 3,\ -11,\ -6 \to 2,\ 7,\ 3,\ 0$" "\n"
  r"$2x^2+7x+3=(2x+1)(x+3)=0 \Rightarrow x=-\frac12,\ x=-3$",
  truth=lambda: roots(2*x**3+3*x**2-11*x-6), tag='الأصفار النسبية وحل المعادلة'),
# 2026 #3: remainders on division by (x - 3) and (x + 1) related (here one is twice the other) -> the constant k; options = small integers
Q('m2q2', U1[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x-3)$ يساوي مثلي باقي قسمته على $(x+1)$ ، فإنّ قيمة الثابت $k$ هي:", (r'x^{3}-2x^{2}+kx+5', x**3-2*x**2+k*x+5)),
  [O('-2', -2), O('2', 2), O('-3', -3), O('6', 6)],
  r"$f(3)=27-18+3k+5=14+3k$ ، $f(-1)=-1-2-k+5=2-k$" "\n" r"$14+3k=2(2-k) \Rightarrow 5k=-10 \Rightarrow k=-2$",
  truth=lambda: solve(rem(x**3-2*x**2+k*x+5, 3)-2*rem(x**3-2*x**2+k*x+5, -1), k)[0], tag='نظرية الباقي وإيجاد ثابت'),
# E (expected: partial fractions with an irreducible quadratic factor), template 2026 #2: which is the decomposition; options = sign of A x sign of C
Q('m2q3', U1[2], 'medium',
  F(r"أيّ الآتية يُمثّل تجزئة المقدار النسبي: $«0»$ إلى كسور جزئية؟", (r'\frac{x^{2}+5x+2}{(x+1)(x^{2}+1)}', (x**2+5*x+2)/((x+1)*(x**2+1)))),
  [O(r'-\frac{1}{x+1}+\frac{2x+3}{x^{2}+1}', -1/(x+1)+(2*x+3)/(x**2+1)), O(r'\frac{1}{x+1}+\frac{2x+3}{x^{2}+1}', 1/(x+1)+(2*x+3)/(x**2+1)),
   O(r'-\frac{1}{x+1}+\frac{2x-3}{x^{2}+1}', -1/(x+1)+(2*x-3)/(x**2+1)), O(r'-\frac{2}{x+1}+\frac{3x+1}{x^{2}+1}', -2/(x+1)+(3*x+1)/(x**2+1))],
  r"$x^2+5x+2=A(x^2+1)+(Bx+C)(x+1)$ ، عند $x=-1$: $-2=2A \Rightarrow A=-1$" "\n" r"معامل $x^2$: $1=A+B \Rightarrow B=2$ ، الحد الثابت: $2=A+C \Rightarrow C=3$",
  truth=(x**2+5*x+2)/((x+1)*(x**2+1)), tag='تجزئة: عامل تربيعي غير قابل للتحليل'),
# E (expected: remainder on division by the quadratic x(x - 1), high power), template 2026 #3: remainder theorem at the zeros 0 and 1 of the divisor; options = ax + b vs its pieces
Q('m2q4', U1[1], 'medium',
  r"باقي قسمة $x^{21}+3$ على $x^{2}-x$ هو:",
  [O('x+3', x+3), O('3', 3), O('4', 4), O('3x+1', 3*x+1)],
  r"$x^2-x=x(x-1)$ ، والباقي على الصورة $ax+b$: $x^{21}+3=x(x-1)q(x)+ax+b$" "\n" r"عند $x=0$: $b=3$ ، وعند $x=1$: $4=a+b \Rightarrow a=1$ ، والباقي $x+3$",
  truth=lambda: div(x**21+3, x**2-x, x)[1], tag='باقي القسمة على مقدار تربيعي'),
# ---------------- unit 2
# E (expected: exact value by a sum identity), template 2026 #5: cos(pi/3 + pi/4) with exact values; options = sign x sqrt2 - sqrt6 vs sqrt2 + sqrt6
Q('m2q5', U2[1], 'easy',
  r"القيمة الدقيقة لـ $\cos\dfrac{7\pi}{12}$ هي:",
  [O(r'\frac{\sqrt{2}-\sqrt{6}}{4}', (sqrt(2)-sqrt(6))/4), O(r'\frac{\sqrt{6}-\sqrt{2}}{4}', (sqrt(6)-sqrt(2))/4), O(r'\frac{\sqrt{2}+\sqrt{6}}{4}', (sqrt(2)+sqrt(6))/4), O(r'-\frac{\sqrt{2}+\sqrt{6}}{4}', -(sqrt(2)+sqrt(6))/4)],
  r"$\cos\frac{7\pi}{12}=\cos\left(\frac{\pi}{3}+\frac{\pi}{4}\right)=\frac12\cdot\frac{\sqrt2}{2}-\frac{\sqrt3}{2}\cdot\frac{\sqrt2}{2}=\dfrac{\sqrt2-\sqrt6}{4}$",
  truth=cos(7*pi/12), tag='قيم دقيقة بمتطابقات المجموع والفرق'),
# 2026 #6: equivalent expression for tan x + cot x (quotient identities -> common denominator -> Pythagorean -> reciprocal); options = single trig expressions
Q('m2q6', U2[1], 'easy',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\tan x+\cot x', tan(x)+cot(x))),
  [O(r'\sec x\csc x', sec(x)*csc(x)), O('1', 1), O(r'\sin x\cos x', sin(x)*cos(x)), O(r'\sec^{2}x', sec(x)**2)],
  r"$\tan x+\cot x=\dfrac{\sin x}{\cos x}+\dfrac{\cos x}{\sin x}=\dfrac{\sin^2x+\cos^2x}{\sin x\cos x}=\dfrac{1}{\sin x\cos x}=\sec x\csc x$",
  truth=tan(x)+cot(x), tag='المتطابقات الأساسية'),
# E (expected: sin(A + B) from ratios in given quadrants), template 2026 #4: the missing ratio with its quadrant sign; options = sign x 87 vs 297 (one sign slip)
Q('m2q7', U2[1], 'medium',
  r"إذا كان $\sin A=-\frac{8}{17}$ حيث $\pi<A<\frac{3\pi}{2}$ ، و $\cos B=\frac{24}{25}$ حيث $\frac{3\pi}{2}<B<2\pi$ ، فإنّ قيمة $\sin(A+B)$ هي:",
  [O(r'-\frac{87}{425}', -R(87, 425)), O(r'\frac{87}{425}', R(87, 425)), O(r'-\frac{297}{425}', -R(297, 425)), O(r'\frac{297}{425}', R(297, 425))],
  r"$\cos A=-\frac{15}{17}$ (الربع الثالث) ، $\sin B=-\frac{7}{25}$ (الربع الرابع)" "\n"
  r"$\sin(A+B)=\sin A\cos B+\cos A\sin B=\left(-\frac{8}{17}\right)\frac{24}{25}+\left(-\frac{15}{17}\right)\left(-\frac{7}{25}\right)=\frac{-192+105}{425}=-\frac{87}{425}$",
  truth=sin((pi+asin(R(8, 17))) + (2*pi-acos(R(24, 25)))), tag='المجموع والفرق بمعلومية نسب في أرباع مختلفة'),
# E (expected: double angle by squaring sin x - cos x = k), template 2026 #4: a double-angle value from a given relation; options = 1 - k^2 vs the slips k^2, sign, 1 + k^2
Q('m2q8', U2[2], 'medium',
  r"إذا كان: $\sin x-\cos x=\frac{1}{2}$ ، فإنّ قيمة $\sin2x$ هي:",
  [O(r'\frac{3}{4}', R(3, 4)), O(r'\frac{1}{4}', R(1, 4)), O(r'-\frac{3}{4}', -R(3, 4)), O(r'\frac{5}{4}', R(5, 4))],
  r"بالتربيع: $\sin^2x-2\sin x\cos x+\cos^2x=\frac14 \Rightarrow 1-\sin2x=\frac14 \Rightarrow \sin2x=\frac34$",
  truth=1-R(1, 4), tag='ضعف الزاوية بالتربيع'),
# E (expected: general solution -- which value is not a solution), template 2026 #7: one trig equation; options = four angles, three of them from x = 2pi/3 + n pi
IndexQ('m2q9', U2[3], 'easy',
  F(r"أحد الآتية **لا** يُعَدّ حلًّا للمعادلة: $«0»=-\sqrt{3}$", (r'\tan x', tan(x))),
  [O(r'\frac{7\pi}{3}', 7*P/3), O(r'\frac{5\pi}{3}', 5*P/3), O(r'-\frac{\pi}{3}', -P/3), O(r'\frac{8\pi}{3}', 8*P/3)],
  r"الحل العام: $x=\frac{2\pi}{3}+n\pi$" "\n" r"$\frac{5\pi}{3}=\frac{2\pi}{3}+\pi$ ✔ ، $-\frac{\pi}{3}=\frac{2\pi}{3}-\pi$ ✔ ، $\frac{8\pi}{3}=\frac{2\pi}{3}+2\pi$ ✔" "\n" r"أما $\frac{7\pi}{3}=\frac{\pi}{3}+2\pi$ فظلّها $\sqrt3$ ، إذن ليست حلًّا",
  truth=lambda vals: only(vals, lambda v_: not same(tan(v_)+sqrt(3), 0)), tag='الحل العام: أيّ القيم ليست حلًّا'),
# E (expected: equation with a double-angle identity), template 2026 #7: cos 2x = 1 - 2 sin^2 x gives a factorable quadratic in sin x; options = complete set vs a lost factor x sign
Q('m2q10', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'\cos 2x+3\sin x-2', cos(2*x)+3*sin(x)-2)),
  [O(st(r'\frac{\pi}{6}', r'\frac{\pi}{2}', r'\frac{5\pi}{6}'), S_(P/6, P/2, 5*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'),
   O(st(r'\frac{7\pi}{6}', r'\frac{3\pi}{2}', r'\frac{11\pi}{6}'), S_(7*P/6, 3*P/2, 11*P/6), 'set'), O(st(r'\frac{\pi}{2}'), S_(P/2), 'set')],
  r"$1-2\sin^2x+3\sin x-2=0 \Rightarrow 2\sin^2x-3\sin x+1=0 \Rightarrow (2\sin x-1)(\sin x-1)=0$" "\n" r"$\sin x=\frac12 \Rightarrow x=\frac{\pi}{6},\frac{5\pi}{6}$ ، $\sin x=1 \Rightarrow x=\frac{\pi}{2}$",
  truth=lambda: sols(cos(2*x)+3*sin(x)-2, 0, 2*pi), tag='معادلة باستعمال متطابقة ضعف الزاوية'),
# ---------------- unit 3
# E (expected: derivatives of a^x and log_a x), template 2025 #2: value of the derivative of a two-term combination at a point; options = ln 4 below / missing / multiplied x sign
Q('m2q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'4^{x}-\log_{4}x', 4**x-log(x, 4))),
  [O(r'4\ln 4-\frac{1}{\ln 4}', 4*log(4)-1/log(4)), O(r'4-\frac{1}{4}', 4-R(1, 4)), O(r'4\ln 4-\ln 4', 3*log(4)), O(r'4\ln 4+\frac{1}{\ln 4}', 4*log(4)+1/log(4))],
  r"$f'(x)=4^x\ln4-\dfrac{1}{x\ln4} \Rightarrow f'(1)=4\ln4-\dfrac{1}{\ln4}$",
  truth=Dx(4**x-log(x, 4)).subs(x, 1), tag='مشتقة الاقتران الأسي واللوغاريتمي'),
# 2024s #4 with the roles swapped (v = 0 as in 2025 #4 / 2025s #10): acceleration at the instant of rest; options = values with units (a(0), v(1))
Q('m2q12', U3[3], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t\ge0$ بالثواني و $s$ بالأمتار. تسارع الجُسيم في اللحظة التي يكون فيها في حالة سكون لحظي هو:", (r'2t-4\ln(t+1)', 2*t-4*log(t+1))),
  [O('1', 1, units='m/s^2'), O('4', 4, units='m/s^2'), O('2', 2, units='m/s^2'), O('0', 0, units='m/s^2')],
  r"$v(t)=2-\dfrac{4}{t+1}=0 \Rightarrow t=1$" "\n" r"$a(t)=\dfrac{4}{(t+1)^2} \Rightarrow a(1)=\dfrac44=1\ \text{m/s}^2$",
  truth=lambda: diff(2*t-4*log(t+1), t, 2).subs(t, solve(diff(2*t-4*log(t+1), t), t)[0]), tag='الحركة: السرعة والتسارع'),
# 2024 #6: x-coordinate where the tangent is parallel to a line ax + by + c = 0 (linear minus k ln x here); options = slope -a/b vs +a/b vs the x-coefficient, and the y-coordinate
Q('m2q13', U3[1], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، $x>0$ ، فإنّ الإحداثي $x$ للنقطة التي يكون عندها المماس موازيًا للمستقيم الذي معادلته: $2x+2y-3=0$ هو:", (r'3x-4\ln x', 3*x-4*log(x))),
  [O('1', 1), O('2', 2), O('4', 4), O('3', 3)],
  r"ميل المستقيم $-\frac22=-1$ ، و $f'(x)=3-\dfrac4x$" "\n" r"$3-\dfrac4x=-1 \Rightarrow \dfrac4x=4 \Rightarrow x=1$",
  truth=lambda: [r_ for r_ in solve(Dx(3*x-4*log(x))+1, x) if r_ > 0][0], tag='مماس يوازي مستقيمًا معلومًا'),
# 2024s #7 (higher derivative), exponential as in 2026 #11: f^(5) of e^(-2x); options = sign of (-2)^5 x 32 vs 10 / 16
Q('m2q14', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ المشتقة الخامسة $f^{(5)}(x)$ تساوي:", (r'e^{-2x}', exp(-2*x))),
  [O(r'-32e^{-2x}', -32*exp(-2*x)), O(r'32e^{-2x}', 32*exp(-2*x)), O(r'-10e^{-2x}', -10*exp(-2*x)), O(r'-16e^{-2x}', -16*exp(-2*x))],
  r"كل اشتقاق يضرب في $-2$: $f^{(5)}(x)=(-2)^5e^{-2x}=-32e^{-2x}$",
  truth=diff(exp(-2*x), x, 5), tag='المشتقات العليا'),
# 2026 #10: constant from a given derivative value (a quotient here instead of the product with a cube root); options = small integers (-4 = numerator order of the quotient rule reversed, 3 = the -1 term lost)
Q('m2q15', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(2)=-3$ ، فإنّ قيمة الثابت $a$ هي:", (r'\frac{x+a}{x-1}', (x+a)/(x-1))),
  [O('2', 2), O('-2', -2), O('-4', -4), O('3', 3)],
  r"$f'(x)=\dfrac{(x-1)-(x+a)}{(x-1)^2}=\dfrac{-1-a}{(x-1)^2}$ ، إذن $f'(2)=-1-a=-3 \Rightarrow a=2$",
  truth=lambda: solve(Dx((x+a)/(x-1)).subs(x, 2)+3, a)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2024 #4: g = -1/f with f(a) and f'(a) read from ONE piecewise-linear graph; options = sign x f(a)^2 vs f(a)
Q('m2q16', U3[2], 'medium',
  r"يُمثّل الشكل الآتي منحنى الاقتران $f(x)$ ، إذا كان: $g(x)=\dfrac{-1}{f(x)}$ ، فإنّ $g'(1)$ هي:",
  [O(r'\frac{2}{9}', R(2, 9)), O(r'-\frac{2}{9}', -R(2, 9)), O(r'\frac{2}{3}', R(2, 3)), O(r'-\frac{2}{3}', -R(2, 3))],
  r"من الشكل: $f(1)=3$ ، و $f'(1)=2$ (ميل القطعة من $(0,1)$ إلى $(2,5)$)" "\n" r"$g'(x)=\dfrac{f'(x)}{(f(x))^2} \Rightarrow g'(1)=\dfrac{2}{3^2}=\dfrac29$",
  truth=lambda: (lambda fv, fs: diff(-1/u, u).subs(u, fv(1))*fs(1))(*pw(F2_16)),
  figure=figure('m2q16', fig_one(F2_16, (0, 6), (0, 5), (4.3, 3.6)), 3.4, 2.8), tag='المشتقة من التمثيل البياني'),
# 2025 #8: f'(0) of c e^(x^n) sqrt(kx + b), product of two composites with the first term vanishing at 0; options = small values (inner factor 2 lost, 1/2 of the root lost, 0)
Q('m2q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(0)$ هو:", (r'4e^{x^{3}}\sqrt{2x+9}', 4*exp(x**3)*sqrt(2*x+9))),
  [O(r'\frac{4}{3}', R(4, 3)), O(r'\frac{2}{3}', R(2, 3)), O(r'\frac{8}{3}', R(8, 3)), O('0', 0)],
  r"$f'(x)=4\left[3x^2e^{x^3}\sqrt{2x+9}+e^{x^3}\cdot\dfrac{2}{2\sqrt{2x+9}}\right]$" "\n" r"$f'(0)=4\left[0+1\cdot\dfrac{1}{3}\right]=\dfrac43$",
  truth=Dx(4*exp(x**3)*sqrt(2*x+9)).subs(x, 0), tag='مشتقة الضرب'),
# 2023 #7: x where a^(x^2 + c) has a horizontal tangent; options = small integers 0-3 (2 = the base, 3 = the constant of the exponent)
Q('m2q18', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ قيمة $x$ التي يكون للاقتران عندها مماس أفقي هي:", (r'2^{(x^{2}+3)}', 2**(x**2+3))),
  [O('0', 0), O('1', 1), O('2', 2), O('3', 3)],
  r"$f'(x)=2^{x^2+3}\cdot\ln2\cdot2x$ ، و $2^{x^2+3}\ln2\ne0$" "\n" r"$2x=0 \Rightarrow x=0$",
  truth=lambda: solve(Dx(2**(x**2+3)), x)[0], tag='نقاط المماس الأفقي'),
# E (expected: second derivative by implicit differentiation), template 2026 #16: implicit derivative at a given point; options = sign x factor slips
Q('m2q19', U3[4], 'medium',
  F(r"إذا كان: $«0»=4x$ ، فإنّ $\dfrac{d^{2}y}{dx^{2}}$ عند النقطة $(1,\,2)$ تساوي:", (r'y^{2}', y**2)),
  [O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{4}', -R(1, 4)), O('-1', -1)],
  r"$2yy'=4 \Rightarrow y'=\dfrac2y=1$ عند $(1,2)$" "\n" r"$y''=-\dfrac{2y'}{y^2}=-\dfrac{2}{4}=-\dfrac12$",
  truth=imp(y**2-4*x, (1, 2), 2), tag='المشتقة الثانية بالاشتقاق الضمني'),
# E (expected: horizontal tangent of an implicit curve), template 2026 #17: tangent to an implicit curve at lattice points; options = numerator vs denominator of dy/dx set to 0 (vertical tangents) x signs of the roots read off the factors
Q('m2q20', U3[4], 'medium',
  F(r"النقطتان اللتان يكون عندهما لمنحنى العلاقة: $«0»=8$ مماس أفقي هما:", (r'x^{2}+4y^{2}-4x-8y', G2_20)),
  [O(r'(2,\ 3),\ (2,\ -1)', FiniteSet(Tuple(2, 3), Tuple(2, -1)), 'tset'), O(r'(2,\ -3),\ (2,\ 1)', FiniteSet(Tuple(2, -3), Tuple(2, 1)), 'tset'),
   O(r'(6,\ 1),\ (-2,\ 1)', FiniteSet(Tuple(6, 1), Tuple(-2, 1)), 'tset'), O(r'(-6,\ 1),\ (2,\ 1)', FiniteSet(Tuple(-6, 1), Tuple(2, 1)), 'tset')],
  r"$2x+8yy'-4-8y'=0 \Rightarrow y'=\dfrac{4-2x}{8y-8}$ ، والمماس أفقي عندما $4-2x=0$ ، أي $x=2$" "\n"
  r"$4+4y^2-8-8y=8 \Rightarrow y^2-2y-3=0 \Rightarrow (y-3)(y+1)=0 \Rightarrow y=3,\ y=-1$",
  truth=lambda: FiniteSet(*[Tuple(sx, sy) for sx, sy in solve([diff(G2_20, x), G2_20-8], [x, y]) if diff(G2_20, y).subs({x: sx, y: sy}) != 0]),
  tag='مماس أفقي لمنحنى ضمني'),
# 2024 #12: cube whose side grows at a constant rate from a given length; dV/dt after t minutes (update the side first); options = side 12 vs 9 (time added instead of rate x time) x rate factor kept/dropped
Q('m2q21', U3[5], 'medium',
  r"مكعب معدني طول ضلعه $6\ \text{cm}$ ، سُخِّن فبدأ يتمدّد بحيث يزداد طول ضلعه بمعدّل $2\ \text{cm/min}$ ، وظلّ محافظًا على شكله، فإنّ معدّل تغيّر حجمه بعد $3\ \text{min}$ من بدء التسخين هو:",
  [O('864', 864, units='cm^3/min'), O('432', 432, units='cm^3/min'), O('486', 486, units='cm^3/min'), O('243', 243, units='cm^3/min')],
  r"بعد $3\ \text{min}$: طول الضلع $6+2(3)=12\ \text{cm}$" "\n" r"$V=x^3 \Rightarrow \dfrac{dV}{dt}=3x^2\dfrac{dx}{dt}=3(144)(2)=864\ \text{cm}^3/\text{min}$",
  truth=lambda: (diff(s**3, s)*2).subs(s, 6 + 2*3), tag='معدلات مرتبطة: مكعب'),
# 2024 #11: angle of elevation of an object rising vertically, watched from a point a fixed distance away (figure); dtheta/dt at a given height; options = decimals with the unit
Q('m2q22', U3[5], 'hard',
  r"يُبيّن الشكل الآتي صاروخًا يرتفع رأسيًّا من النقطة $B$ بسرعة $0.6\ \text{km/s}$ ، ويرصده جهاز عند النقطة $A$ التي تبعد $3\ \text{km}$ عن $B$. معدّل تغيّر زاوية الارتفاع $\theta$ عندما يكون الصاروخ على ارتفاع $4\ \text{km}$ هو:",
  [D('0.072', 'rad/s'), D('0.2', 'rad/s'), D('0.12', 'rad/s'), D('0.048', 'rad/s')],
  r"$\tan\theta=\dfrac{h}{3} \Rightarrow \sec^2\theta\,\dfrac{d\theta}{dt}=\dfrac13\cdot\dfrac{dh}{dt}$" "\n"
  r"عند $h=4$: الوتر $5$ ، $\sec^2\theta=\frac{25}{9}$ ، إذن $\dfrac{d\theta}{dt}=\dfrac{0.6}{3}\cdot\dfrac{9}{25}=0.072\ \text{rad/s}$",
  truth=R(6, 10)/3*R(9, 25), figure=figure('m2q22', fig_rocket2(), 3.4, 2.8), tag='معدلات مرتبطة: معدل تغير زاوية'),
# ---------------- unit 4
# E (expected: negative and large powers of i), template 2023 #18: value of an expression in powers of i; options = sign of the real part x sign of the imaginary part
Q('m2q23', U4[1], 'easy',
  r"قيمة المقدار: $2i^{-1}+i^{2026}$ هي:",
  [O('-1-2i', -1-2*I), O('1-2i', 1-2*I), O('-1+2i', -1+2*I), O('1+2i', 1+2*I)],
  r"$i^{-1}=\dfrac1i=\dfrac{-i}{1}=-i$ ، و $2026=4(506)+2 \Rightarrow i^{2026}=i^2=-1$ ، إذن المقدار $2(-i)+(-1)=-1-2i$",
  truth=2/I+I**2026, tag='قوى i', lead=NOTE_I(23, 30)),
# 2025s #21: first item of a shared stem, Arg(z - w) where z - w is purely imaginary; options = sign x pi/2 vs pi/4 (w - z, z + w)
Q('m2q24', U4[1], 'easy',
  r"قيمة $\text{Arg}(z-w)$ هي:",
  [O(r'\frac{\pi}{2}', P/2), O(r'-\frac{\pi}{2}', -P/2), O(r'\frac{\pi}{4}', P/4), O(r'-\frac{\pi}{4}', -P/4)],
  r"$z-w=(2-2)+(5-(-1))i=6i$ ، وهو على الجزء الموجب من المحور التخيلي، إذن $\text{Arg}(z-w)=\frac{\pi}{2}$",
  truth=arg((2+5*I)-(2-I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=2+5i$ ، و $w=2-i$", 24, 25)),
# 2025s #22: second item of the shared stem, z + 2 conj(w); options = sign of the real part x sign of the imaginary part (6 - 7i = conj(z) + 2w)
Q('m2q25', U4[2], 'easy',
  r"ناتج $z+2\bar{w}$ هو:",
  [O('6+7i', 6+7*I), O('6-7i', 6-7*I), O('-6+7i', -6+7*I), O('-6-7i', -6-7*I)],
  r"$\bar{w}=2+i$ ، إذن $z+2\bar{w}=(2+5i)+(4+2i)=6+7i$",
  truth=(2+5*I)+2*conjugate(2-I), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2026 #23: quadratic (real coefficients) with the complex root 3 - i; options = sign of the sum / product with i^2 = +1 / sum halved
Q('m2q26', U4[2], 'easy',
  r"المعادلة التربيعية ذات المعاملات الحقيقية التي أحد جذريها العدد المُركَّب $(3-i)$ هي:",
  [O('x^{2}-6x+10=0', x**2-6*x+10, 'rel'), O('x^{2}+6x+10=0', x**2+6*x+10, 'rel'), O('x^{2}-6x+8=0', x**2-6*x+8, 'rel'), O('x^{2}-3x+10=0', x**2-3*x+10, 'rel')],
  r"الجذر الآخر هو المرافق $3+i$ ، المجموع $6$ ، وحاصل الضرب $(3-i)(3+i)=10$" "\n" r"المعادلة: $x^2-6x+10=0$",
  truth=expand((x-(3-I))*(x-(3+I))), tag='معادلة تربيعية بمعلومية جذر مركب'),
# 2023 #22: quotient of two numbers given in trig form (unlike denominators, one negative argument), answer in trig form; options = moduli divided vs subtracted x arguments subtracted vs the sign of -pi/4 lost
Q('m2q27', U4[2], 'easy',
  r"إذا كان: $z=8\left(\cos\frac{\pi}{12}+i\sin\frac{\pi}{12}\right)$ ، $w=2\left(\cos\left(-\frac{\pi}{4}\right)+i\sin\left(-\frac{\pi}{4}\right)\right)$ ، فإنّ $\dfrac{z}{w}$ هي:",
  [O(trig('4', r'\frac{\pi}{3}'), pol(4, P/3)), O(trig('4', r'-\frac{\pi}{6}'), pol(4, -P/6)),
   O(trig('6', r'\frac{\pi}{3}'), pol(6, P/3)), O(trig('6', r'-\frac{\pi}{6}'), pol(6, -P/6))],
  r"المقياس: $\frac82=4$ ، والسعة: $\frac{\pi}{12}-\left(-\frac{\pi}{4}\right)=\frac{\pi}{12}+\frac{3\pi}{12}=\frac{\pi}{3}$" "\n" r"$\dfrac{z}{w}=4\left(\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}\right)$",
  truth=expand(pol(8, pi/12)/pol(2, -pi/4)), tag='الضرب والقسمة بالصورة المثلثية'),
# 2025 #19: z - k conj(z) = a + bi -> z; options = sign of the real part / sign of the imaginary part / the given number misread
Q('m2q28', U4[1], 'medium',
  r"إذا كان: $z-2\bar{z}=3+6i$ ، فإنّ العدد المُركَّب $z$ هو:",
  [O('-3+2i', -3+2*I), O('3+2i', 3+2*I), O('-3-2i', -3-2*I), O('3-6i', 3-6*I)],
  r"نفرض $z=x+iy$: $(x+iy)-2(x-iy)=-x+3iy=3+6i$" "\n" r"$-x=3 \Rightarrow x=-3$ ، $3y=6 \Rightarrow y=2$ ، إذن $z=-3+2i$",
  truth=lambda: (lambda s_: s_[X]+I*s_[Y])(solve([re(expand(X+I*Y-2*(X-I*Y)-3-6*I)), im(expand(X+I*Y-2*(X-I*Y)-3-6*I))], [X, Y])), tag='معادلة فيها العدد ومرافقه'),
# E (expected: intersection of two loci), template 2023 #25 (perpendicular bisector |z - z1| = |z - z2|) with the circle |z| = r: the points on both; options = line y = -x vs y = x / radius slip / one point lost
Q('m2q29', U4[3], 'medium',
  r"الأعداد المُركَّبة $z$ التي تُحقّق المعادلتين: $|z-2i|=|z+2|$ و $|z|=2$ معًا هي:",
  [O(r'\sqrt{2}-\sqrt{2}i,\ -\sqrt{2}+\sqrt{2}i', S_(sqrt(2)-sqrt(2)*I, -sqrt(2)+sqrt(2)*I), 'set'), O(r'\sqrt{2}+\sqrt{2}i,\ -\sqrt{2}-\sqrt{2}i', S_(sqrt(2)+sqrt(2)*I, -sqrt(2)-sqrt(2)*I), 'set'),
   O(r'2-2i,\ -2+2i', S_(2-2*I, -2+2*I), 'set'), O(r'\sqrt{2}-\sqrt{2}i', S_(sqrt(2)-sqrt(2)*I), 'set')],
  r"$|z-2i|=|z+2|$: العمود المنصّف للقطعة بين $(0,2)$ و $(-2,0)$: $x^2+(y-2)^2=(x+2)^2+y^2 \Rightarrow y=-x$" "\n"
  r"مع $|z|=2$: $x^2+x^2=4 \Rightarrow x=\pm\sqrt2$ ، فالعددان: $\sqrt2-\sqrt2\,i$ و $-\sqrt2+\sqrt2\,i$",
  truth=lambda: FiniteSet(*[sx+I*sy for sx, sy in solve([Eq(X**2+(Y-2)**2, (X+2)**2+Y**2), X**2+Y**2-4], [X, Y])]), tag='تقاطع محلين هندسيين'),
# 2026 #25 (13f): solid disc cut by a dashed perpendicular-bisector half-plane; options = centre sign x which boundary is strict
IndexQ('m2q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثِّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z-1+i|\le3$ ، $|z|<|z-2i|$', R2_30),
   T(r'$|z-1+i|<3$ ، $|z|\le|z-2i|$', both(disk(C2_30, 3, strict=True), nearer(0, 2j))),
   T(r'$|z+1-i|\le3$ ، $|z|<|z-2i|$', both(disk(-C2_30, 3), closer(0, 2j))),
   T(r'$|z+1-i|<3$ ، $|z|\le|z-2i|$', both(disk(-C2_30, 3, strict=True), nearer(0, 2j)))],
  r"الدائرة متصلة، مركزها $(1,-1)$ ونصف قطرها $3$: $|z-1+i|\le3$" "\n"
  r"المستقيم المتقطّع $y=1$ هو العمود المنصّف للقطعة بين $0$ و $2i$ ، والمنطقة في جهة الأصل: $|z|<|z-2i|$",
  truth=region_truth(R2_30, PR2_30, 5), figure=figure('m2q30', fig_region2(R2_30, PR2_30, 5, marks=((C2_30, ''),)), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]


# ================================================================== PAPER 3
f3_16, fs3_16 = pw([(0, 0), (3, 6), (6, 3)])
g3_16, gs3_16 = pw([(0, 5), (4, 1), (6, 3)])
V3 = x**3 + 6*x**2 + 3*x - 10
F3_12 = sqrt(2*log(x))                       # m3q12: f(x)
Z3_29, TH3_29 = 1 + 2j, -3*math.pi/4        # m3q29: vertex and direction of the ray
C3_30 = 1 - 2j                               # m3q30: centre of the half ring


class OptF3(O):
    """option written with f(x) (m3q12): f(x) stands for the function of the stem."""
    def parsed(self):
        return parse_tex(self.tex.replace('f(x)', r'\Phi '), {'Phi': F3_12})


def ray3(z0, th0):
    """the ray Arg(z - z0) = th0 (vertex excluded)."""
    return sector(z0, th0, th0)


def half_ring3(c_, inner_strict, outer_strict):
    """1 <(=) |z - c| <(=) 3 and 0 <= Arg(z - c) <= pi (m3q30 options)."""
    return both(outside(c_, 1, strict=inner_strict), disk(c_, 3, strict=outer_strict), sector(c_, 0, math.pi))


R3_30 = half_ring3(C3_30, True, False)
P3_30 = [('arc', C3_30, 3, False, (0.0, math.pi)), ('arc', C3_30, 1, True, (0.0, math.pi)),
         ('seg', C3_30 + 1, C3_30 + 3, False), ('seg', C3_30 - 3, C3_30 - 1, False)]
P3_29 = [('seg', Z3_29, Z3_29 + 9*cmath.exp(1j*TH3_29), False), ('open', Z3_29)]


def fig_island3():
    """round island (centre O, radius r) and a boat B at distance h from the shore; theta between BT (tangent) and BO (m3q13)."""
    def draw(fig, ax):
        mp = __import__('matplotlib.patches', fromlist=['Arc'])
        _sketch(fig, ax)
        r_, d_ = 1.0, 2.35
        ts = np.linspace(0, 2*np.pi, 300)
        ax.fill(r_*np.cos(ts), r_*np.sin(ts), color='#d8e9c8', zorder=1)
        ax.plot(r_*np.cos(ts), r_*np.sin(ts), color='#4f7a3a', lw=1.5, zorder=2)
        ph = math.acos(r_/d_)
        tx, ty = r_*math.cos(ph), r_*math.sin(ph)
        ax.plot([0, tx], [0, ty], color='#555555', lw=1.1, ls='--', zorder=3)
        ax.plot([0, r_], [0, 0], color='#555555', lw=1.1, ls='--', zorder=3)
        ax.text(tx/2 - 0.2, ty/2 + 0.02, r'$r$', fontsize=11)
        ax.text(r_/2 - 0.06, 0.07, r'$r$', fontsize=11)
        ax.plot([r_, d_], [0, 0], color='#1f5fbf', lw=1.8, zorder=3)
        ax.annotate('', (r_, -0.28), (d_, -0.28), arrowprops=dict(arrowstyle='<->', color='#1f5fbf', lw=1))
        ax.text((r_ + d_)/2 - 0.06, -0.55, r'$h$', fontsize=12, color='#1f5fbf')
        ax.plot([d_, tx], [0, ty], color='#333333', lw=1.5, zorder=3)
        ux, uy = -tx, -ty                                    # T -> O (unit, r = 1)
        vx, vy = (d_ - tx), (0 - ty)
        vn = math.hypot(vx, vy); vx, vy = vx/vn, vy/vn       # T -> B (unit)
        q_ = 0.11
        ax.plot([tx + q_*ux, tx + q_*(ux + vx), tx + q_*vx], [ty + q_*uy, ty + q_*(uy + vy), ty + q_*vy], color='#333333', lw=0.9)
        ax.plot(0, 0, 'o', color='#333333', ms=4, zorder=5); ax.text(-0.2, -0.25, r'$O$', fontsize=11)
        ax.plot(tx, ty, 'o', color='#333333', ms=3, zorder=5); ax.text(tx - 0.05, ty + 0.1, r'$T$', fontsize=11)
        th_deg = math.degrees(math.asin(r_/d_))
        ax.add_patch(mp.Arc((d_, 0), 0.9, 0.9, theta1=180 - th_deg, theta2=180, color='#d04a1a', lw=1.2))
        ax.text(d_ - 0.68, 0.06, r'$\theta$', fontsize=12, color='#d04a1a')
        hull = [(d_ - 0.16, 0.02), (d_ + 0.16, 0.02), (d_ + 0.1, -0.08), (d_ - 0.1, -0.08)]
        ax.fill([p_[0] for p_ in hull], [p_[1] for p_ in hull], color='#8a5a2b', zorder=6)
        ax.fill([d_, d_, d_ + 0.13], [0.04, 0.3, 0.04], color='#f2f2f2', ec='#555555', lw=0.8, zorder=6)
        ax.text(d_ + 0.16, 0.1, r'$B$', fontsize=11, color='#d04a1a')
        ax.set_xlim(-1.25, 2.75); ax.set_ylim(-1.15, 1.2)
    return draw


def fig_heli3():
    """helicopter hovering 120 m above a straight road, its searchlight on an approaching car; theta at the helicopter (m3q22)."""
    def draw(fig, ax):
        mp = __import__('matplotlib.patches', fromlist=['Arc'])
        _sketch(fig, ax)
        hx, hy, cx = 0.0, 4.0, -3.0
        ax.plot([-4.8, 1.3], [0, 0], color='#333333', lw=1.6)
        ax.plot([hx, hx], [0, hy - 0.2], color='#555555', lw=1.1, ls='--')
        ax.plot([hx - 0.25, hx - 0.25, hx], [0, 0.25, 0.25], color='#333333', lw=0.9)
        ax.text(hx + 0.15, 1.8, r'$120\ \mathrm{m}$', fontsize=10)
        ax.add_patch(mp.Ellipse((hx, hy + 0.1), 0.9, 0.42, color='#4a6fa5', zorder=5))
        ax.plot([hx + 0.4, hx + 1.25], [hy + 0.14, hy + 0.24], color='#4a6fa5', lw=2.2, zorder=5)
        ax.plot([hx + 1.25, hx + 1.25], [hy + 0.08, hy + 0.42], color='#4a6fa5', lw=1.6, zorder=5)
        ax.plot([hx, hx], [hy + 0.3, hy + 0.48], color='#333333', lw=1.4, zorder=5)
        ax.plot([hx - 0.9, hx + 0.9], [hy + 0.48, hy + 0.48], color='#333333', lw=1.6, zorder=5)
        ax.plot([hx - 0.25, hx + 0.25], [hy - 0.17, hy - 0.17], color='#333333', lw=1.2, zorder=5)
        ax.fill([hx, cx - 0.12, cx + 0.12], [hy - 0.05, 0.05, 0.05], color='#ffe680', alpha=0.55, zorder=2)
        ax.plot([hx, cx], [hy - 0.05, 0.12], color='#c9a000', lw=1.2, zorder=3)
        ax.add_patch(mp.FancyBboxPatch((cx - 0.38, 0.12), 0.76, 0.28, boxstyle='round,pad=0.02', color='#d04a1a', zorder=6))
        ax.add_patch(mp.FancyBboxPatch((cx - 0.2, 0.36), 0.38, 0.16, boxstyle='round,pad=0.02', color='#d04a1a', zorder=6))
        for wx in (cx - 0.22, cx + 0.22):
            ax.add_patch(mp.Circle((wx, 0.1), 0.09, color='#222222', zorder=7))
        ax.annotate('', (cx + 1.5, -0.35), (cx + 0.3, -0.35), arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2))
        ang = math.degrees(math.atan2(0.12 - (hy - 0.05), cx - hx))
        ax.add_patch(mp.Arc((hx, hy - 0.05), 1.5, 1.5, theta1=ang % 360, theta2=270, color='#d04a1a', lw=1.2))
        ax.text(hx - 0.55, hy - 1.15, r'$\theta$', fontsize=12, color='#d04a1a')
        ax.set_xlim(-4.9, 1.6); ax.set_ylim(-0.7, 4.8)
    return draw


def fig_ray3():
    """the ray Arg(z - 1 - 2i) = -3pi/4: open vertex, dashed reference line to the right, arrowhead (m3q29)."""
    def draw(fig, ax):
        complex_axes(ax, 4)
        end = Z3_29 + 6.3*cmath.exp(1j*TH3_29)
        ax.plot([Z3_29.real, 3.7], [Z3_29.imag, Z3_29.imag], color='#777777', lw=1.1, ls='--')
        ax.annotate('', (end.real, end.imag), (Z3_29.real, Z3_29.imag),
                    arrowprops=dict(arrowstyle='-|>', color=LINE, lw=1.8, shrinkA=0, shrinkB=0, mutation_scale=12))
        ax.plot(Z3_29.real, Z3_29.imag, 'o', mfc='white', mec=LINE, ms=6, zorder=5)
        ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    return draw


P3 = [
# ---------------- unit 1
# E (expected: synthetic division by (ax - b)), template 2026 #1: divide by the zero 2/3, then the quotient by 3;
# options = quotient divided by 3 or not x remainder kept or tripled (+ a sign slip)
Q('m3q1', U1[1], 'medium',
  F(r"عند قسمة $f(x)=«0»$ على $(3x-2)$ ، فإنّ ناتج القسمة $q(x)$ والباقي $r$ هما:", (r'6x^{3}-x^{2}+4x-3', 6*x**3-x**2+4*x-3)),
  [O(r'q(x)=2x^{2}+x+2,\ r=1', Tuple(2*x**2+x+2, 1), 'pairs'), O(r'q(x)=6x^{2}+3x+6,\ r=1', Tuple(6*x**2+3*x+6, 1), 'pairs'),
   O(r'q(x)=2x^{2}+x+2,\ r=3', Tuple(2*x**2+x+2, 3), 'pairs'), O(r'q(x)=2x^{2}-x+2,\ r=1', Tuple(2*x**2-x+2, 1), 'pairs')],
  r"نقسم قسمةً تركيبية على $x=\frac23$: $6,\ -1,\ 4,\ -3 \to 6,\ 3,\ 6$ والباقي $1$" "\n"
  r"ناتج القسمة على $\left(x-\frac23\right)$ هو $6x^2+3x+6$ ، وبما أن $3x-2=3\left(x-\frac23\right)$ نقسمه على $3$: $q(x)=2x^2+x+2$ ، والباقي $1$",
  truth=lambda: Tuple(*div(6*x**3-x**2+4*x-3, 3*x-2, x)), tag='القسمة التركيبية على (ax−b)'),
# E (expected: factor theorem in an application, box volume), template 2026 #1: divide V(x) by the given height,
# then factor the quotient; options = signs of the two factors / other factor pairs of 10
Q('m3q2', U1[1], 'easy',
  F(r"يُمثّل الاقتران: $V(x)=«0»$ حجم صندوق على شكل متوازي مستطيلات. إذا كان ارتفاع الصندوق $(x-1)$ ، فإنّ البعدين الآخرين له هما:", (r'x^{3}+6x^{2}+3x-10', V3)),
  [T(r'$(x+2)$ و $(x+5)$', (x+2)*(x+5)), T(r'$(x-2)$ و $(x-5)$', (x-2)*(x-5)), T(r'$(x+1)$ و $(x+10)$', (x+1)*(x+10)), T(r'$(x+2)$ و $(x+3)$', (x+2)*(x+3))],
  r"بالقسمة التركيبية على $(x-1)$: $1,\ 6,\ 3,\ -10 \to 1,\ 7,\ 10,\ 0$" "\n" r"$x^2+7x+10=(x+2)(x+5)$",
  truth=lambda: cancel(V3/(x-1)), tag='تطبيق حياتي على نظرية العوامل'),
# E (expected: improper fraction, divide first), template 2026 #2: one division step (quotient x), then two linear
# factors; options = quotient kept or dropped x sign of the second constant
Q('m3q3', U1[2], 'medium',
  F(r"أيُّ الآتية يُمثِّل تجزئة المقدار النسبي $«0»$ إلى كسور جزئية؟", (r'\frac{x^{3}+2x^{2}+x+6}{x^{2}+2x}', (x**3+2*x**2+x+6)/(x**2+2*x))),
  [O(r'x+\frac{3}{x}-\frac{2}{x+2}', x+3/x-2/(x+2)), O(r'x+\frac{3}{x}+\frac{2}{x+2}', x+3/x+2/(x+2)),
   O(r'\frac{3}{x}-\frac{2}{x+2}', 3/x-2/(x+2)), O(r'\frac{3}{x}+\frac{2}{x+2}', 3/x+2/(x+2))],
  r"درجة البسط أكبر من درجة المقام: $x^3+2x^2+x+6=x(x^2+2x)+(x+6)$" "\n"
  r"$\dfrac{x+6}{x(x+2)}=\dfrac{A}{x}+\dfrac{B}{x+2}$: عند $x=0$: $A=3$ ، وعند $x=-2$: $B=-2$",
  truth=(x**3+2*x**2+x+6)/(x**2+2*x), tag='تجزئة: كسر غير فعلي'),
# E (expected: constants of a given decomposition), template 2026 #2: three distinct linear factors, one substitution per
# constant (x = 0, 1, -1); options = small integers
Q('m3q4', U1[2], 'medium',
  F(r"إذا كان: $«0»=\dfrac{A}{x}+\dfrac{B}{x-1}+\dfrac{C}{x+1}$ ، فإنّ قيمة $ABC$ هي:", (r'\frac{x^{2}+4x+1}{x^{3}-x}', (x**2+4*x+1)/(x**3-x))),
  [O('3', 3), O('-3', -3), O('1', 1), O('6', 6)],
  r"$x^3-x=x(x-1)(x+1)$ ، و $x^2+4x+1=A(x-1)(x+1)+Bx(x+1)+Cx(x-1)$" "\n"
  r"عند $x=0$: $1=-A \Rightarrow A=-1$ ، عند $x=1$: $6=2B \Rightarrow B=3$ ، عند $x=-1$: $-2=2C \Rightarrow C=-1$" "\n" r"$ABC=(-1)(3)(-1)=3$",
  truth=lambda: (lambda F_: F_.subs(x, 0))(cancel((x**2+4*x+1)/((x-1)*(x+1)))) * cancel((x**2+4*x+1)/(x*(x+1))).subs(x, 1) * cancel((x**2+4*x+1)/(x*(x-1))).subs(x, -1),
  tag='إيجاد ثوابت في التجزئة'),
# ---------------- unit 2
# E (expected: related angles and even-odd identities, which one is NOT an identity), template 2026 #6 ("أيُّ الآتية");
# options = four related-angle statements, tan(pi - x) = tan x is the false one
IndexQ('m3q5', U2[1], 'easy',
  r"إحدى المعادلات الآتية **ليست** متطابقة:",
  [O(r'\tan(\pi-x)=\tan x', tan(pi-x)-tan(x), 'rel'), O(r'\cos(\pi-x)=-\cos x', cos(pi-x)+cos(x), 'rel'),
   O(r'\sin(\pi+x)=-\sin x', sin(pi+x)+sin(x), 'rel'), O(r'\cot(-x)=-\cot x', cot(-x)+cot(x), 'rel')],
  r"$\tan(\pi-x)=\dfrac{\sin(\pi-x)}{\cos(\pi-x)}=\dfrac{\sin x}{-\cos x}=-\tan x$ ، فالمعادلة $\tan(\pi-x)=\tan x$ ليست متطابقة" "\n" r"أما البقية فمتطابقات صحيحة.",
  truth=lambda vals: only(vals, lambda d_: not same(d_, 0)), tag='المتطابقات: الزوايا المنتسبة والزوجية والفردية'),
# E (expected: tan(pi/4 + x) by the sum identity), template 2026 #5 ("أبسط صورة"): one expression, tan(pi/4) = 1;
# options = numerator/denominator swapped (difference formula) x sign of the denominator
Q('m3q6', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\tan\left(\frac{\pi}{4}+x\right)', tan(pi/4+x))),
  [O(r'\frac{1+\tan x}{1-\tan x}', (1+tan(x))/(1-tan(x))), O(r'\frac{1-\tan x}{1+\tan x}', (1-tan(x))/(1+tan(x))),
   O(r'\frac{1+\tan x}{\tan x-1}', (1+tan(x))/(tan(x)-1)), O(r'\frac{\tan x-1}{1+\tan x}', (tan(x)-1)/(1+tan(x)))],
  r"$\tan(A+B)=\dfrac{\tan A+\tan B}{1-\tan A\tan B}$ ، و $\tan\frac{\pi}{4}=1$" "\n"
  r"$\tan\left(\frac{\pi}{4}+x\right)=\dfrac{1+\tan x}{1-\tan x}$",
  truth=tan(pi/4+x), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #4: tan(theta/2) from cos theta and a quadrant; options = sign x reciprocal
Q('m3q7', U2[2], 'medium',
  r"إذا كان $\cos\theta=-\frac{3}{5}$ ، حيث $\pi<\theta<\frac{3\pi}{2}$ ، فإنّ قيمة $\tan\frac{\theta}{2}$ تساوي:",
  [O('-2', -2), O('2', 2), O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2))],
  r"$\frac{\pi}{2}<\frac{\theta}{2}<\frac{3\pi}{4}$ ، فالظل سالب" "\n"
  r"$\tan\frac{\theta}{2}=-\sqrt{\dfrac{1-\cos\theta}{1+\cos\theta}}=-\sqrt{\dfrac{8/5}{2/5}}=-\sqrt4=-2$",
  truth=tan((pi+acos(R(3, 5)))/2), tag='نصف الزاوية مع تحديد الربع'),
# E (expected: product to sum, exact value), template 2026 #5 (one identity, then exact values): sin 105 cos 15;
# options = surd forms (difference instead of sum, sin 90 lost)
Q('m3q8', U2[2], 'easy',
  r"قيمة المقدار: $\sin105^\circ\cos15^\circ$ هي:",
  [O(r'\frac{2+\sqrt{3}}{4}', (2+sqrt(3))/4), O(r'\frac{2-\sqrt{3}}{4}', (2-sqrt(3))/4), O(r'\frac{1+\sqrt{3}}{4}', (1+sqrt(3))/4), O(r'\frac{\sqrt{3}}{4}', sqrt(3)/4)],
  r"$\sin A\cos B=\frac12[\sin(A+B)+\sin(A-B)]=\frac12[\sin120^\circ+\sin90^\circ]=\frac12\left(\frac{\sqrt3}{2}+1\right)=\dfrac{2+\sqrt3}{4}$",
  truth=sin(deg(105))*cos(deg(15)), tag='تحويل الضرب إلى مجموع'),
# E (expected: number of solutions in a closed interval), template 2026 #7: quadratic in cos x on [0, 2pi], the end
# 2pi counted; options = small counts
Q('m3q9', U2[3], 'medium',
  F(r"عدد حلول المعادلة: $«0»=«1»$ في الفترة $[0,\,2\pi]$ هو:", (r'2\cos^{2}x', 2*cos(x)**2), (r'1+\cos x', 1+cos(x))),
  [O('4', 4), O('3', 3), O('2', 2), O('5', 5)],
  r"$2\cos^2x-\cos x-1=0 \Rightarrow (2\cos x+1)(\cos x-1)=0$" "\n"
  r"$\cos x=1 \Rightarrow x=0,\ 2\pi$ (الفترة مغلقة) ، $\cos x=-\frac12 \Rightarrow x=\frac{2\pi}{3},\ \frac{4\pi}{3}$ ، إذن $4$ حلول",
  truth=lambda: len(sols(2*cos(x)**2-1-cos(x), 0, 2*pi, closed_hi=True)), tag='عدد الحلول في فترة مغلقة'),
# E (expected: half-angle equation), template 2026 #8: cos(x/2) = 1/2 on [0, 4pi), the interval halved;
# options = halved or not x the second solution
Q('m3q10', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=\frac{1}{2}$ في الفترة $[0,\,4\pi)$ هي:", (r'\cos\frac{x}{2}', cos(x/2))),
  [O(st(r'\frac{2\pi}{3}', r'\frac{10\pi}{3}'), S_(2*P/3, 10*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'),
   O(st(r'\frac{2\pi}{3}', r'\frac{4\pi}{3}'), S_(2*P/3, 4*P/3), 'set'), O(st(r'\frac{2\pi}{3}'), S_(2*P/3), 'set')],
  r"بما أن $0\le x<4\pi$ فإن $0\le\frac{x}{2}<2\pi$: $\frac{x}{2}=\frac{\pi}{3}$ أو $\frac{x}{2}=\frac{5\pi}{3}$" "\n" r"إذن $x=\frac{2\pi}{3}$ أو $x=\frac{10\pi}{3}$",
  truth=lambda: sols(cos(x/2)-R(1, 2), 0, 4*pi), tag='معادلة بنصف الزاوية'),
# ---------------- unit 3
# 2024s #2: y'(1) of an exponential quotient by x that simplifies (here e^3 x^2 - e^(3x)); options = sign (the factors
# 2 and 3 swapped) x a stray constant 1 (as the model)
Q('m3q11', U3[1], 'easy',
  F(r"إذا كان: $y=«0»$ ، $x\ne0$ ، فإنّ $\dfrac{dy}{dx}$ عندما $x=1$ هي:", (r'\dfrac{(e\,x)^{3}-x\,e^{3x}}{x}', ((E*x)**3-x*exp(3*x))/x)),
  [O(r'-e^{3}', -E**3), O(r'e^{3}', E**3), O(r'1-e^{3}', 1-E**3), O(r'1+e^{3}', 1+E**3)],
  r"نبسّط أولًا: $y=\dfrac{e^3x^3}{x}-\dfrac{xe^{3x}}{x}=e^3x^2-e^{3x}$" "\n"
  r"$\dfrac{dy}{dx}=2e^3x-3e^{3x}$ ، وعند $x=1$: $2e^3-3e^3=-e^3$",
  truth=Dx(((E*x)**3-x*exp(3*x))/x).subs(x, 1), tag='مشتقة الاقتران الأسي'),
# 2023 #6: f'(x) of the root of a logarithm, written through f(x) (here sqrt(2 ln x)); options = arrangements of x, f(x)
# and a constant (derivative of the log inverted, derivative of the root inverted, the 1/2 dropped)
Q('m3q12', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، $x>1$ ، فإنّ $f'(x)$ هي:", (r'\sqrt{2\ln x}', F3_12)),
  [OptF3(r'\frac{1}{x\,f(x)}', 1/(x*F3_12)), OptF3(r'\frac{x}{4f(x)}', x/(4*F3_12)), OptF3(r'\frac{4f(x)}{x}', 4*F3_12/x), OptF3(r'\frac{2}{x\,f(x)}', 2/(x*F3_12))],
  r"$f'(x)=\dfrac{1}{2\sqrt{2\ln x}}\cdot\dfrac{2}{x}=\dfrac{1}{x\sqrt{2\ln x}}=\dfrac{1}{x\,f(x)}$",
  truth=Dx(F3_12), tag='قاعدة السلسلة مع اللوغاريتم'),
# 2025 #7: applied right-triangle figure, h = r csc(theta) - r (here a boat and a round island, r = 300 m), dh/dtheta
# at pi/4; options = sign x sqrt2 vs 1/sqrt2 (csc vs sin of pi/4)
Q('m3q13', U3[1], 'medium',
  r"يُبيّن الشكل الآتي قاربًا عند النقطة $B$ يقترب من جزيرة دائرية الشكل مركزها $O$ ، ويقيس قبطانه الزاوية $\theta$ (بالراديان) بين الخطّ $BT$ المماسّ لشاطئ الجزيرة عند النقطة $T$ والخطّ $BO$. إذا علمت أنّ $h$ يُمثّل المسافة بين القارب وشاطئ الجزيرة بالمتر، و $r$ يُمثّل نصف قطر الجزيرة ويساوي $300\ \text{m}$ ، فإنّ معدّل تغيّر $h$ بالنسبة إلى $\theta$ عندما $\theta=\frac{\pi}{4}$ هو:",
  [O(r'-300\sqrt{2}', -300*sqrt(2)), O(r'300\sqrt{2}', 300*sqrt(2)), O(r'-\frac{300}{\sqrt{2}}', -300/sqrt(2)), O(r'\frac{300}{\sqrt{2}}', 300/sqrt(2))],
  r"المثلث $OTB$ قائم في $T$: $\sin\theta=\dfrac{r}{r+h}$ ، إذن $h=r\csc\theta-r=300\csc\theta-300$" "\n"
  r"$\dfrac{dh}{d\theta}=-300\csc\theta\cot\theta$ ، وعند $\theta=\frac{\pi}{4}$: $-300(\sqrt2)(1)=-300\sqrt2$",
  truth=diff(300/sin(th)-300, th).subs(th, pi/4), figure=figure('m3q13', fig_island3(), 3.7, 2.3),
  tag='تطبيق هندسي على مشتقات الاقترانات المثلثية'),
# 2023 #3: instants of rest of a cubic s(t) with a fractional coefficient (v = 0 has integer roots); options = pairs of
# times (the zero 5/2 of a(t) mixed in, as the model)
Q('m3q14', U3[1], 'easy',
  F(r"يُمثّل الاقتران: $s(t)=«0»$ ، $t\ge0$ موقع جسم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار، و $t$ الزمن بالثواني. ما قيم $t$ بالثواني التي يكون عندها الجسم في حالة سكون لحظي؟", (r't^{3}-\frac{15}{2}t^{2}+18t', t**3-R(15, 2)*t**2+18*t)),
  [O(r'2,\ 3', S_(2, 3), 'set'), O(r'2,\ \frac{5}{2}', S_(2, R(5, 2)), 'set'), O(r'\frac{5}{2},\ 3', S_(R(5, 2), 3), 'set'), O(r'1,\ 6', S_(1, 6), 'set')],
  r"$v(t)=s'(t)=3t^2-15t+18=3(t^2-5t+6)=3(t-2)(t-3)$" "\n" r"$v(t)=0 \Rightarrow t=2$ أو $t=3$",
  truth=lambda: FiniteSet(*solve(diff(t**3-R(15, 2)*t**2+18*t, t), t)), tag='الحركة: اتجاه الحركة والسكون'),
# 2026 #10: constant from a derivative value of a product (product rule, evaluate, solve a linear equation); options =
# small values
Q('m3q15', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(1)=6e$ ، فإنّ قيمة الثابت $a$ هي:", (r'axe^{x}', a*x*exp(x))),
  [O('3', 3), O('6', 6), O('2', 2), O(r'\frac{1}{3}', R(1, 3))],
  r"$f'(x)=a\left(e^x+xe^x\right)=ae^x(1+x)$ ، إذن $f'(1)=2ae=6e \Rightarrow a=3$",
  truth=lambda: solve(diff(a*x*exp(x), x).subs(x, 1)-6*E, a)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2026 #14 (composite version, as m9q16): two piecewise-linear graphs, p = f(g(x)), p'(5); options = sign, g(5) used
# for g'(5), one factor only
Q('m3q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $p(x)=f\big(g(x)\big)$ ، فإنّ $p'(5)$ تساوي:",
  [O('2', 2), O('-2', -2), O('4', 4), O('1', 1)],
  r"$p'(5)=f'\big(g(5)\big)\cdot g'(5)$" "\n" r"من الشكل: $g(5)=2$ ، $g'(5)=1$ (ميل القطعة من $(4,1)$ إلى $(6,3)$) ، $f'(2)=2$ (ميل القطعة من $(0,0)$ إلى $(3,6)$)" "\n" r"$p'(5)=2(1)=2$",
  truth=lambda: fs3_16(g3_16(5))*gs3_16(5), figure=figure('m3q16', draw_two([(0, 0), (3, 6), (6, 3)], [(0, 5), (4, 1), (6, 3)], 6, 6, (1.1, 5.6), (0.2, 5.3))), tag='المشتقة من التمثيل البياني'),
# 2024 #8: log base a of a trig function (here log2(cos x)), its value at pi/4; options = sign x ln 2 divided or
# multiplied (+ tan(pi/4) taken as sqrt2)
Q('m3q17', U3[3], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $0<x<\frac{\pi}{2}$ ، فإنّ $f'\left(\frac{\pi}{4}\right)$ تساوي:", (r'\log_{2}(\cos x)', log(cos(x), 2))),
  [O(r'-\frac{1}{\ln 2}', -1/log(2)), O(r'\frac{1}{\ln 2}', 1/log(2)), O(r'-\ln 2', -log(2)), O(r'-\frac{\sqrt{2}}{\ln 2}', -sqrt(2)/log(2))],
  r"$f'(x)=\dfrac{-\sin x}{\cos x\,\ln2}=-\dfrac{\tan x}{\ln2} \Rightarrow f'\left(\frac{\pi}{4}\right)=-\dfrac{1}{\ln2}$",
  truth=Dx(log(cos(x), 2)).subs(x, pi/4), tag='مشتقة اللوغاريتم لأساس غير e'),
# 2026r #11: exponential model in context, rate of growth at a given time (here the simpler 1000 e^(0.05t));
# options = the rate vs the value P(20) x e^(0.05t) kept or dropped
Q('m3q18', U3[3], 'easy',
  F(r"يُمثّل الاقتران: $P(t)=«0»$ عدد سكان مدينة (بالآلاف) بعد $t$ سنة. معدّل تغيّر عدد السكان (ألف نسمة/سنة) عندما $t=20$ هو:", (r'1000e^{0.05t}', 1000*exp(R(5, 100)*t))),
  [O('50e', 50*E), O('1000e', 1000*E), O('50', 50), O('20e', 20*E)],
  r"$P'(t)=1000(0.05)e^{0.05t}=50e^{0.05t}$ ، إذن $P'(20)=50e^{1}=50e$",
  truth=diff(1000*exp(R(5, 100)*t), t).subs(t, 20), tag='معدل التغير في سياق حياتي'),
# E (expected: tangent line to a parametric curve), template 2026 #15: the point and dy/dx at t = 0, then the line;
# options = intercept slips x slope inverted
Q('m3q19', U3[3], 'medium',
  F(r"معادلة المماس لمنحنى المعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ عندما $t=0$ هي:", (r'e^{t}+1', exp(t)+1), (r'e^{2t}', exp(2*t))),
  [O('y=2x-3', 2*x-3, 'eq'), O('y=2x+1', 2*x+1, 'eq'), O('y=2x-1', 2*x-1, 'eq'), O(r'y=\frac{1}{2}x', x/2, 'eq')],
  r"عند $t=0$: النقطة $(2,\,1)$ ، و $\dfrac{dy}{dx}=\dfrac{2e^{2t}}{e^t}=2e^t=2$" "\n" r"المماس: $y-1=2(x-2) \Rightarrow y=2x-3$",
  truth=1 + (diff(exp(2*t), t)/diff(exp(t)+1, t)).subs(t, 0)*(x-2), tag='مماس منحنى وسيطي'),
# E (expected: normal to an implicit curve, its y-intercept), template 2026 #17: slope at a lattice point, normal slope
# -1/m, then x = 0; options = values from the slips (tangent instead of normal, slope not negated, y0 dropped)
Q('m3q20', U3[4], 'medium',
  F(r"إذا مثّل المستقيم $l$ العمودي على المماس لمنحنى العلاقة: $«0»=16$ عند النقطة $(4,\,1)$ ، فإنّ المقطع $y$ للمستقيم $l$ هو:", (r'x^{2}y', x**2*y)),
  [O('-7', -7), O('3', 3), O('9', 9), O('-8', -8)],
  r"$2xy+x^2\dfrac{dy}{dx}=0 \Rightarrow \dfrac{dy}{dx}=-\dfrac{2y}{x}=-\dfrac12$ عند $(4,1)$ ، فميل العمودي $2$" "\n"
  r"$l$: $y-1=2(x-4) \Rightarrow y=2x-7$ ، فالمقطع $y$ هو $-7$",
  truth=lambda: 1 + (-1/imp(x**2*y-16, (4, 1)))*(0-4), tag='العمودي على المماس لمنحنى علاقة ضمنية'),
# 2026 #16: implicit slope at a point with a ln y term (here x ln y + y^2 = 4, the point handed over); options = sign
# x the factor 2y dropped (+ ln 2 taken as 1)
Q('m3q21', U3[4], 'medium',
  F(r"إذا كان: $«0»=4$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(0,\,2)$ تساوي:", (r'x\ln y+y^{2}', x*log(y)+y**2)),
  [O(r'-\frac{\ln 2}{4}', -log(2)/4), O(r'\frac{\ln 2}{4}', log(2)/4), O(r'-\ln 2', -log(2)), O(r'-\frac{1}{4}', -R(1, 4))],
  r"باشتقاق الطرفين: $\ln y+\dfrac{x}{y}y'+2yy'=0$ ، وعند $(0,2)$: $\ln2+0+4y'=0 \Rightarrow y'=-\dfrac{\ln2}{4}$",
  truth=imp(x*log(y)+y**2-4, (0, 2)), tag='الاشتقاق الضمني عند نقطة'),
# 2025 #12: an elevated observer above a straight road (here a hovering helicopter's searchlight, 120 m) tracking a car
# at 60 km/h, dtheta/dt when the car is right below; options = sign x km/h not converted to m/h. Figure.
Q('m3q22', U3[5], 'medium',
  r"تحلّق طائرة عموديّة ثابتةً على ارتفاع $120\ \text{m}$ فوق طريق مستقيم، ويتتبّع ضوؤها الكاشف سيارة تتحرّك على الطريق نحو النقطة الواقعة أسفل الطائرة بسرعة ثابتة تبلغ $60\ \text{km/h}$ كما في الشكل الآتي، فإنّ معدّل تغيّر الزاوية $\theta$ عندما تكون السيارة أسفل الطائرة تمامًا هو:",
  [O('-500', -500, units='rad/h'), O('500', 500, units='rad/h'), D('-0.5', units='rad/h'), D('0.5', units='rad/h')],
  r"$\tan\theta=\dfrac{x}{120}$ ، حيث $x$ بُعد السيارة الأفقي عن النقطة أسفل الطائرة بالمتر، و $\dfrac{dx}{dt}=-60\ \text{km/h}=-60000\ \text{m/h}$" "\n"
  r"$\sec^2\theta\,\dfrac{d\theta}{dt}=\dfrac{1}{120}\cdot\dfrac{dx}{dt}$ ، وأسفل الطائرة: $\theta=0$ ، $\sec^2\theta=1$: $\dfrac{d\theta}{dt}=\dfrac{-60000}{120}=-500\ \text{rad/h}$",
  truth=diff(atan(s/120), s).subs(s, 0)*(-60000), figure=figure('m3q22', fig_heli3(), 3.6, 3.0),
  tag='معدلات مرتبطة: معدل تغير زاوية'),
# ---------------- unit 4
# 2026 #19: z = a + bi with b < 0 and |z| given -> trigonometric form; options = quadrant x reference angle
Q('m3q23', U4[1], 'medium',
  r"إذا كان: $z=-3+bi$ ، حيث $b<0$ ، وكان: $|z|=6$ ، فإنّ الصورة المثلثية للعدد المُركَّب $z$ هي:",
  [O(trig('6', r'-\frac{2\pi}{3}'), pol(6, -2*P/3)), O(trig('6', r'\frac{2\pi}{3}'), pol(6, 2*P/3)), O(trig('6', r'-\frac{\pi}{3}'), pol(6, -P/3)), O(trig('6', r'-\frac{5\pi}{6}'), pol(6, -5*P/6))],
  r"$9+b^2=36 \Rightarrow b=-3\sqrt3$ (لأن $b<0$) ، فيكون $z=-3-3\sqrt3\,i$ في الربع الثالث" "\n" r"زاوية الإسناد $\tan^{-1}\sqrt3=\frac{\pi}{3}$ ، و $\text{Arg}(z)=-\pi+\frac{\pi}{3}=-\frac{2\pi}{3}$",
  truth=lambda: -3 + I*[r_ for r_ in solve(9+b**2-36, b) if r_ < 0][0], tag='الصورة المثلثية بشروط', lead=NOTE_I(23, 30)),
# 2026 #22: a constant making a quotient real (one value here, the constant in the numerator only); options = sign x
# magnitude (3/2 = the pure-imaginary condition)
Q('m3q24', U4[1], 'medium',
  r"إذا كان: $z=\dfrac{a+3i}{2-i}$ ، فإنّ قيمة الثابت الحقيقي $a$ التي تجعل $z$ عددًا حقيقيًّا هي:",
  [O('-6', -6), O('6', 6), O(r'-\frac{3}{2}', -R(3, 2)), O(r'\frac{3}{2}', R(3, 2))],
  r"$z=\dfrac{(a+3i)(2+i)}{5}=\dfrac{2a+ai+6i-3}{5}=\dfrac{(2a-3)+(a+6)i}{5}$" "\n" r"يكون حقيقيًّا إذا انعدم الجزء التخيلي: $a+6=0 \Rightarrow a=-6$",
  truth=lambda: solve(im(expand((X+3*I)*(2+I))), X)[0], tag='قيمة ثابت تجعل العدد حقيقيًا أو تخيليًا'),
# 2023 #21: (a^2 + b^2)/(a + bi) = p + qi -> a x b (the quotient is the conjugate a - bi); options = product vs sum x
# sign of b (the quotient read as a + bi)
Q('m3q25', U4[2], 'medium',
  F(r"إذا كان: $«0»=«1»$ ، حيث $a$ و $b$ عددان حقيقيان لا يساوي أيٌّ منهما الصفر، فإنّ قيمة $a\times b$ هي:", (r'\dfrac{a^{2}+b^{2}}{a+bi}', (a**2+b**2)/(a+b*I)), (r'4+2i', 4+2*I)),
  [O('-8', -8), O('8', 8), O('2', 2), O('6', 6)],
  r"$a^2+b^2=(a+bi)(a-bi)$ ، إذن $\dfrac{a^2+b^2}{a+bi}=a-bi=4+2i$" "\n" r"$a=4$ ، $-b=2 \Rightarrow b=-2$ ، و $a\times b=-8$",
  truth=lambda: [s_[X]*s_[Y] for s_ in solve([re(expand((4+2*I)*(X+Y*I)))-(X**2+Y**2), im(expand((4+2*I)*(X+Y*I)))], [X, Y], dict=True) if s_[X] != 0][0],
  tag='تساوي عددين مركبين'),
# 2026 #20-21: first item of a shared stem on z, w (here the modulus |z - w|, a modulus as 2026r #25); options = |z + w|,
# the sum of the parts, |z| - |w|
Q('m3q26', U4[1], 'easy',
  r"قيمة $|z-w|$ هي:",
  [O(r'\sqrt{10}', sqrt(10)), O(r'\sqrt{26}', sqrt(26)), O('4', 4), O(r'\sqrt{13}-\sqrt{5}', sqrt(13)-sqrt(5))],
  r"$z-w=(2+3i)-(-1+2i)=3+i$ ، و $|3+i|=\sqrt{9+1}=\sqrt{10}$",
  truth=Abs((2+3*I)-(-1+2*I)), tag='المقياس والعمليات (نص مشترك)', lead=shared(r"إذا كان: $z=2+3i$ ، $w=-1+2i$", 26, 27)),
# 2026 #21: second item of the shared stem, a product (here z times conj w); options = i^2 slip, the imaginary part
Q('m3q27', U4[2], 'easy',
  r"الجزء الحقيقي للعدد $z\bar{w}$ هو:",
  [O('4', 4), O('-8', -8), O('-7', -7), O('8', 8)],
  r"$\bar w=-1-2i$ ، و $z\bar w=(2+3i)(-1-2i)=-2-4i-3i-6i^2=4-7i$ ، فالجزء الحقيقي $4$",
  truth=re(expand((2+3*I)*(-1-2*I))), tag='المقياس والعمليات (نص مشترك)'),
# 2026 #24: smaller angle between two numbers in the lower half-plane (4th and 3rd quadrants), difference of the
# arguments; options = sizes added, |Arg z2| alone, |Arg z1| alone
Q('m3q28', U4[1], 'medium',
  r"إذا كان: $z_1=1-i$ ، $z_2=-1-\sqrt{3}\,i$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{5\pi}{12}', 5*P/12), O(r'\frac{11\pi}{12}', 11*P/12), O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{\pi}{4}', P/4)],
  r"$\text{Arg}(z_1)=-\frac{\pi}{4}$ (الربع الرابع) ، $\text{Arg}(z_2)=-\pi+\frac{\pi}{3}=-\frac{2\pi}{3}$ (الربع الثالث)" "\n"
  r"الزاوية بينهما: $\left|-\frac{\pi}{4}-\left(-\frac{2\pi}{3}\right)\right|=\frac{2\pi}{3}-\frac{\pi}{4}=\frac{5\pi}{12}$",
  truth=smaller_angle(1-I, -1-sqrt(3)*I), tag='الزاوية بين عددين مركبين'),
# 2026r #23: equation of a single ray Arg(z - z0) = theta read from a figure (open vertex, dashed reference line);
# options = vertex sign x the angle vs its reference angle
IndexQ('m3q29', U4[3], 'medium',
  r"معادلة المحل الهندسي (بدلالة $z$) المُمثَّلة في الشكل الآتي هي:",
  [T(r'$\text{Arg}(z-1-2i)=-\frac{3\pi}{4}$', ray3(Z3_29, TH3_29)), T(r'$\text{Arg}(z-1-2i)=-\frac{\pi}{4}$', ray3(Z3_29, -math.pi/4)),
   T(r'$\text{Arg}(z+1+2i)=-\frac{3\pi}{4}$', ray3(-Z3_29, TH3_29)), T(r'$\text{Arg}(z+1+2i)=-\frac{\pi}{4}$', ray3(-Z3_29, -math.pi/4))],
  r"الشعاع يبدأ بالنقطة $(1,2)$ (دائرة مفرغة، لا يشملها) أي $1+2i$ ، فنكتب $\text{Arg}\big(z-(1+2i)\big)=\text{Arg}(z-1-2i)$" "\n"
  r"ويتّجه إلى الأسفل واليسار مارًّا بالنقطتين $(0,1)$ و $(-1,0)$ ، فزاويته مع الاتجاه الموجب (الخط المتقطّع) $-\frac{3\pi}{4}$",
  truth=region_truth(ray3(Z3_29, TH3_29), P3_29, 4), figure=figure('m3q29', fig_ray3(), 3.2, 3.2), tag='المحل الهندسي: الشعاع'),
# 2025 #25: annulus with one dashed circle (here its upper half, cut along a diameter like the 2026 #25 disc and wedge);
# options = centre sign x which circle is strict
IndexQ('m3q30', U4[3], 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثِّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$1<|z-1+2i|\le3$ ، $0\le\text{Arg}(z-1+2i)\le\pi$', R3_30),
   T(r'$1\le|z-1+2i|<3$ ، $0\le\text{Arg}(z-1+2i)\le\pi$', half_ring3(C3_30, False, True)),
   T(r'$1<|z+1-2i|\le3$ ، $0\le\text{Arg}(z+1-2i)\le\pi$', half_ring3(-C3_30, True, False)),
   T(r'$1\le|z+1-2i|<3$ ، $0\le\text{Arg}(z+1-2i)\le\pi$', half_ring3(-C3_30, False, True))],
  r"مركز الدائرتين $(1,-2)$ أي $1-2i$ ، فنكتب $|z-(1-2i)|=|z-1+2i|$" "\n"
  r"الدائرة الداخلية (نصف قطرها $1$) متقطّعة: $1<|z-1+2i|$ ، والخارجية (نصف قطرها $3$) متصلة: $|z-1+2i|\le3$" "\n"
  r"المنطقة فوق القطر الأفقي المرسوم بخط متصل: $0\le\text{Arg}(z-1+2i)\le\pi$",
  truth=region_truth(R3_30, P3_30, 5), figure=figure('m3q30', fig_region2(R3_30, P3_30, 5, marks=((C3_30, ''),)), 3.4, 3.4),
  tag='منطقة في المستوى المركب من الشكل'),
]


# ================================================================== PAPER 4
# Each item names the official item it is modelled on (2026 = 2 July 2026 paper, gen 2008; 2025/2024/2023 = summer
# paper 1; 2025s/2024s = supplementary; 2026r = 2026 repeaters; E = a 2008-book skill the ministry has not asked yet,
# written with a ministry template). Same skill, stem structure, kind of function and numbers, option design.
f4_16, fs4_16 = pw([(0, 3), (2, 1), (6, 5)])
g4_16, gs4_16 = pw([(0, 0), (3, 6), (6, 3)])
A4_29, B4_29 = 3 + 3j, 1 - 1j                                           # m4q29: the bisected segment AB
L4_29 = [('seg', complex(-1.4, 2.7), complex(5.0, -0.5), False)]         # m4q29: the drawn line l (y = -x/2 + 2)
C4_30 = 1 + 1j                                                          # m4q30: centre of the ring
R4_30 = both(outside(C4_30, 1, strict=True), disk(C4_30, 2))
PR4_30 = [('arc', C4_30, 1, True, (0.0, 2*math.pi)), ('arc', C4_30, 2, False, (0.0, 2*math.pi))]


def on_line4(z_):
    """m4q29: the drawn line l from its own equation (through the midpoint (2, 1) of AB, slope -1/2): y = -x/2 + 2."""
    return abs(z_.imag - (-z_.real/2 + 2)) < 1e-6


def fig_bisector4():
    """m4q29: line l = perpendicular bisector of AB, A(3, 3) and B(1, -1) marked on a grid (2023 #25 style)."""
    def draw(fig, ax):
        axes_style(ax, (-1.6, 5.6), (-2.6, 4.6), xlabel=r'\mathrm{Re}', ylabel=r'\mathrm{Im}', grid=True)
        ax.set_aspect('equal'); ax.set_xticks(range(-1, 6)); ax.set_yticks(range(-2, 5)); ax.tick_params(labelsize=8)
        p1, p2 = L4_29[0][1], L4_29[0][2]
        ax.annotate('', (p1.real, p1.imag), (p2.real, p2.imag), arrowprops=dict(arrowstyle='<->', color=LINE, lw=1.8))
        ax.text(-1.25, 3.15, r'$l$', fontsize=13, color=LINE)
        ax.plot([A4_29.real, B4_29.real], [A4_29.imag, B4_29.imag], color='#d04a1a', lw=1.1, ls=':')
        for p_, nm, off in [(A4_29, 'A', (0.18, 0.18)), (B4_29, 'B', (0.2, -0.45))]:
            ax.plot(p_.real, p_.imag, 'x', color='#d04a1a', ms=8, mew=1.6)
            ax.text(p_.real + off[0], p_.imag + off[1], f'${nm}$', fontsize=11, color='#d04a1a')
        m_ = (A4_29 + B4_29)/2
        u_ = (A4_29 - B4_29)/abs(A4_29 - B4_29)           # along AB
        n_ = u_*1j                                        # along l
        for c_ in ((A4_29 + m_)/2, (B4_29 + m_)/2):       # double ticks: the two halves are equal
            for sh in (-0.09, 0.09):
                q0, q1 = c_ + u_*sh - n_*0.16, c_ + u_*sh + n_*0.16
                ax.plot([q0.real, q1.real], [q0.imag, q1.imag], color='#d04a1a', lw=1.1)
        s_ = 0.24                                         # right-angle mark at the midpoint
        sq = [m_ + u_*s_, m_ + u_*s_ + n_*s_, m_ + n_*s_]
        ax.plot([q_.real for q_ in sq], [q_.imag for q_ in sq], color='#333333', lw=0.9)
    return draw


P4 = [
# ---------------- unit 1
# 2026 #1: one root given (here the fraction 1/2, equation already set to zero) -> the other two roots; options = sign of each root
Q('m4q1', U1[1], 'easy',
  F(r"إذا كان $x=\frac{1}{2}$ حلًّا للمعادلة: $«0»=0$ ، فإنّ لها حلّين آخرين هما:", (r'2x^{3}-3x^{2}-3x+2', 2*x**3-3*x**2-3*x+2)),
  [O(r'x=2,\ x=-1', S_(2, -1), 'set'), O(r'x=-2,\ x=1', S_(-2, 1), 'set'), O(r'x=2,\ x=1', S_(2, 1), 'set'), O(r'x=-2,\ x=-1', S_(-2, -1), 'set')],
  r"بالقسمة التركيبية على $\left(x-\frac12\right)$: $2,\ -3,\ -3,\ 2 \to 2,\ -2,\ -4,\ 0$" "\n" r"$2x^2-2x-4=2(x-2)(x+1)=0 \Rightarrow x=2$ أو $x=-1$",
  truth=lambda: other_roots(2*x**3-3*x**2-3*x+2, R(1, 2)), tag='حل معادلة كثير حدود بمعلومية أحد جذورها'),
# E (expected: divisible by a quadratic -> one constant; one zero of the divisor gives it at once), template 2026 #3:
# options = sign x magnitude (14 = the value of 2k, not divided by 2)
Q('m4q2', U1[1], 'medium',
  F(r"إذا كان الاقتران: $f(x)=«0»$ يقبل القسمة على $(«1»)$ ، فإنّ قيمة الثابت $k$ هي:", (r'x^{3}+kx+6', x**3+k*x+6), (r'x^{2}+x-6', x**2+x-6)),
  [O('-7', -7), O('7', 7), O('-14', -14), O('14', 14)],
  r"$x^2+x-6=(x+3)(x-2)$ ، فـ $(x-2)$ عامل من عوامل $f(x)$" "\n"
  r"$f(2)=8+2k+6=0 \Rightarrow 2k=-14 \Rightarrow k=-7$ (تحقّق: $f(-3)=-27+21+6=0$)",
  truth=lambda: solve(Poly(div(x**3+k*x+6, x**2+x-6, x)[1], x).coeffs(), k)[k], tag='قابلية القسمة على مقدار تربيعي'),
# E (expected: decomposition with distinct linear factors), template 2026 #2: which is the decomposition;
# options = numerators swapped / sign of one numerator (a list, as the model)
Q('m4q3', U1[2], 'easy',
  F(r"أيّ الآتية يُمثّل تجزئة المقدار النسبي: $«0»$ إلى كسور جزئية؟", (r'\frac{x+14}{x^{2}-4}', (x+14)/(x**2-4))),
  [O(r'\frac{4}{x-2}-\frac{3}{x+2}', 4/(x-2)-3/(x+2)), O(r'\frac{3}{x-2}-\frac{4}{x+2}', 3/(x-2)-4/(x+2)), O(r'\frac{4}{x-2}+\frac{3}{x+2}', 4/(x-2)+3/(x+2)), O(r'-\frac{4}{x-2}+\frac{3}{x+2}', -4/(x-2)+3/(x+2))],
  r"$x+14=A(x+2)+B(x-2)$ ، عند $x=2$: $16=4A \Rightarrow A=4$ ، عند $x=-2$: $12=-4B \Rightarrow B=-3$",
  truth=(x+14)/(x**2-4), tag='تجزئة: عوامل خطية مختلفة'),
# E (expected: one constant of a given decomposition), template 2026 #2 (repeated linear factor): C from x = 2;
# options = the values of C, A, B and the coefficient 3
Q('m4q4', U1[2], 'medium',
  F(r"إذا كان: $«0»=\dfrac{A}{x+1}+\dfrac{B}{x-2}+\dfrac{C}{(x-2)^{2}}$ ، فإنّ قيمة $C$ هي:", (r'\frac{2x^{2}-3x+5}{(x+1)(x-2)^{2}}', (2*x**2-3*x+5)/((x+1)*(x-2)**2))),
  [O(r'\frac{7}{3}', R(7, 3)), O(r'\frac{10}{9}', R(10, 9)), O(r'\frac{8}{9}', R(8, 9)), O('3', 3)],
  r"$2x^2-3x+5=A(x-2)^2+B(x+1)(x-2)+C(x+1)$" "\n" r"عند $x=2$: $8-6+5=3C \Rightarrow C=\frac73$",
  truth=cancel((2*x**2-3*x+5)/(x+1)).subs(x, 2), tag='تجزئة: عامل خطي مكرر'),
# ---------------- unit 2
# 2026 #5: simplest form with the sum/difference identities (the sin terms cancel); options = coefficient x cos/sin
Q('m4q5', U2[1], 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x-\frac{\pi}{6})+\cos(x+\frac{\pi}{6})', cos(x-pi/6)+cos(x+pi/6))),
  [O(r'\sqrt{3}\cos x', sqrt(3)*cos(x)), O(r'\cos x', cos(x)), O(r'\sqrt{3}\sin x', sqrt(3)*sin(x)), O(r'2\cos x', 2*cos(x))],
  r"بجمع المفكوكين يختفي حدّا الجيب: $2\cos x\cos\frac{\pi}{6}=2\cdot\frac{\sqrt3}{2}\cos x=\sqrt3\cos x$",
  truth=cos(x-pi/6)+cos(x+pi/6), tag='تبسيط باستعمال متطابقات المجموع والفرق'),
# 2026 #6: equivalent expression (common denominator, Pythagorean identity -> one reciprocal function);
# options = 2csc vs 2sec, the constant 2, csc without the factor 2
Q('m4q6', U2[1], 'medium',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\sin x}{1+\cos x}+\frac{1+\cos x}{\sin x}', sin(x)/(1+cos(x))+(1+cos(x))/sin(x))),
  [O(r'2\csc x', 2*csc(x)), O(r'2\sec x', 2*sec(x)), O('2', 2), O(r'\csc x', csc(x))],
  r"$\dfrac{\sin^2x+(1+\cos x)^2}{(1+\cos x)\sin x}=\dfrac{\sin^2x+1+2\cos x+\cos^2x}{(1+\cos x)\sin x}=\dfrac{2(1+\cos x)}{(1+\cos x)\sin x}=\dfrac{2}{\sin x}=2\csc x$",
  truth=sin(x)/(1+cos(x))+(1+cos(x))/sin(x), tag='المتطابقات الأساسية'),
# E (expected: double-angle formula used backwards: cos theta from cos 2theta and the quadrant), template 2026 #4;
# options = cos vs sin of theta, the square root forgotten, a value that fails the check
Q('m4q7', U2[2], 'medium',
  r"إذا كان $\cos2\theta=\frac{1}{8}$ ، حيث $\theta$ زاوية حادّة، فإنّ قيمة $\cos\theta$ هي:",
  [O(r'\frac{3}{4}', R(3, 4)), O(r'\frac{\sqrt{7}}{4}', sqrt(7)/4), O(r'\frac{9}{16}', R(9, 16)), O(r'\frac{1}{4}', R(1, 4))],
  r"$\cos2\theta=2\cos^2\theta-1=\frac18 \Rightarrow \cos^2\theta=\frac{9}{16} \Rightarrow \cos\theta=\frac34$ (لأن $\theta$ حادّة)",
  truth=cos(acos(R(1, 8))/2), tag='ضعف الزاوية بمعلومية نسبة'),
# E (expected: power reduction sin^2 u = (1 - cos 2u)/2), template 2026 #5 grid: sin^2x cos^2x = (1 - cos 4x)/8;
# options = coefficient 1/8 vs 1/4 (the 1/2 squared or not) x 1 - cos 4x vs 1 + cos 4x (sin^2 vs cos^2 formula)
Q('m4q8', U2[2], 'medium',
  F(r"أيُّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\sin^{2}x\cos^{2}x', sin(x)**2*cos(x)**2)),
  [O(r'\frac{1-\cos 4x}{8}', (1-cos(4*x))/8), O(r'\frac{1+\cos 4x}{8}', (1+cos(4*x))/8), O(r'\frac{1-\cos 4x}{4}', (1-cos(4*x))/4), O(r'\frac{1+\cos 4x}{4}', (1+cos(4*x))/4)],
  r"$\sin x\cos x=\frac12\sin2x \Rightarrow \sin^2x\cos^2x=\frac14\sin^22x$" "\n"
  r"$\sin^22x=\dfrac{1-\cos4x}{2} \Rightarrow \sin^2x\cos^2x=\dfrac{1-\cos4x}{8}$",
  truth=sin(x)**2*cos(x)**2, tag='تقليص القوة ونصف الزاوية'),
# E (expected: reciprocal-ratio equation 2 sin x = csc x), template 2026 #8 (solutions in an interval);
# options = the interval respected or not / a quadrant missed / the square root forgotten
Q('m4q9', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=«1»$ في الفترة $(0,\,\pi)$ هي:", (r'2\sin x', 2*sin(x)), (r'\csc x', csc(x))),
  [O(st(r'\frac{\pi}{4}', r'\frac{3\pi}{4}'), S_(P/4, 3*P/4), 'set'), O(st(r'\frac{\pi}{4}', r'\frac{3\pi}{4}', r'\frac{5\pi}{4}', r'\frac{7\pi}{4}'), S_(P/4, 3*P/4, 5*P/4, 7*P/4), 'set'),
   O(st(r'\frac{\pi}{4}'), S_(P/4), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set')],
  r"بالضرب في $\sin x$: $2\sin^2x=1 \Rightarrow \sin x=\pm\frac{\sqrt2}{2}$" "\n" r"في الفترة $(0,\pi)$ الجيب موجب: $x=\frac{\pi}{4},\ \frac{3\pi}{4}$",
  truth=lambda: sols(2*sin(x)**2-1, 0, pi, closed_lo=False), tag='معادلة فيها مقلوب نسبة'),
# E (expected: multiple angle sin 3x = 1 in [0, 2pi)), template 2026 #8 (interval of the multiple angle, then divide);
# options = one turn only / the values of 3x not divided / a value that is not a solution
Q('m4q10', U2[3], 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=1$ في الفترة $[0,\,2\pi)$ هي:", (r'\sin 3x', sin(3*x))),
  [O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}', r'\frac{3\pi}{2}'), S_(P/6, 5*P/6, 3*P/2), 'set'), O(st(r'\frac{\pi}{6}'), S_(P/6), 'set'),
   O(st(r'\frac{\pi}{2}', r'\frac{5\pi}{2}', r'\frac{9\pi}{2}'), S_(P/2, 5*P/2, 9*P/2), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{\pi}{2}', r'\frac{5\pi}{6}'), S_(P/6, P/2, 5*P/6), 'set')],
  r"بما أن $0\le x<2\pi$ فإن $0\le3x<6\pi$: $3x=\frac{\pi}{2},\ \frac{5\pi}{2},\ \frac{9\pi}{2}$" "\n" r"إذن $x=\frac{\pi}{6},\ \frac{5\pi}{6},\ \frac{3\pi}{2}$",
  truth=lambda: sols(sin(3*x)-1, 0, 2*pi), tag='معادلة بزاوية مضاعفة في فترة'),
# ---------------- unit 3
# 2025 #1 / 2025s #1: ln(a x^n) simplified by the log laws (here ln 5x); options = the constant 5 kept x u'/u slips
Q('m4q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>0$ ، فإنّ $f'(x)$ تساوي:", (r'\ln(5x)', log(5*x))),
  [O(r'\frac{1}{x}', 1/x), O(r'\frac{5}{x}', 5/x), O(r'\frac{1}{5x}', 1/(5*x)), O('5', 5)],
  r"$\ln(5x)=\ln5+\ln x$ ، و $\ln5$ ثابت مشتقته صفر، إذن $f'(x)=\dfrac1x$",
  truth=Dx(log(5*x)), tag='مشتقة الاقتران اللوغاريتمي'),
# 2024 #5 / 2024s #7: a higher derivative at a point (product rule once, then the power rule); options = small values
Q('m4q12', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'''(2)$ تساوي:", (r'x^{2}\ln x', x**2*log(x))),
  [O('1', 1), O('2', 2), O(r'\frac{1}{2}', R(1, 2)), O('3', 3)],
  r"$f'(x)=2x\ln x+x$ ، $f''(x)=2\ln x+3$ ، $f'''(x)=\dfrac2x \Rightarrow f'''(2)=1$",
  truth=diff(x**2*log(x), x, 3).subs(x, 2), tag='المشتقات العليا'),
# 2026r #10: an expression that collapses by a Pythagorean identity to one reciprocal function, then f'(x);
# options = csc vs sec x sign
Q('m4q13', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ هي:", (r'\dfrac{\sec^{2}x-\tan^{2}x}{\sin x}', (sec(x)**2-tan(x)**2)/sin(x))),
  [O(r'-\csc x\cot x', -csc(x)*cot(x)), O(r'\csc x\cot x', csc(x)*cot(x)), O(r'\sec x\tan x', sec(x)*tan(x)), O(r'-\sec x\tan x', -sec(x)*tan(x))],
  r"$\sec^2x-\tan^2x=1$ ، فـ $f(x)=\dfrac{1}{\sin x}=\csc x$" "\n" r"$f'(x)=-\csc x\cot x$",
  truth=Dx((sec(x)**2-tan(x)**2)/sin(x)), tag='مشتقات الاقترانات المثلثية'),
# 2026r #4: cubic s(t), position when the acceleration is zero; options = v(2) / s at the instant v = 0 / 0 (in m)
Q('m4q14', U3[2], 'medium',
  F(r"إذا كان الاقتران: $s(t)=«0»$ ، $t\ge0$ يُمثّل موقع جُسيم يتحرّك في مسار مستقيم، حيث $s$ الموقع بالأمتار، و $t$ الزمن بالثواني، فإنّ موقع الجُسيم عندما يكون تسارعه صفرًا هو:", (r'12t^{2}-2t^{3}', 12*t**2-2*t**3)),
  [O('32', 32, units='m'), O('24', 24, units='m'), O('64', 64, units='m'), O('0', 0, units='m')],
  r"$v(t)=24t-6t^2$ ، $a(t)=24-12t=0 \Rightarrow t=2$" "\n" r"$s(2)=48-16=32\ \text{m}$",
  truth=lambda: (12*t**2-2*t**3).subs(t, solve(diff(12*t**2-2*t**3, t, 2), t)[0]), tag='الحركة: السرعة والتسارع'),
# E (expected: n-th derivative of sin/cos by the cycle of 4), template 2026 #9 (f = sin x + cos x);
# options = the four derivatives f''', f', f'', f
Q('m4q15', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f^{(2027)}(x)$ تساوي:", (r'\sin x+\cos x', sin(x)+cos(x))),
  [O(r'\sin x-\cos x', sin(x)-cos(x)), O(r'\cos x-\sin x', cos(x)-sin(x)), O(r'-\sin x-\cos x', -sin(x)-cos(x)), O(r'\sin x+\cos x', sin(x)+cos(x))],
  r"المشتقات تتكرر كل 4: $f'=\cos x-\sin x$ ، $f''=-\sin x-\cos x$ ، $f'''=\sin x-\cos x$ ، $f^{(4)}=f$" "\n" r"$2027=4(506)+3$ ، إذن $f^{(2027)}=f'''=\sin x-\cos x$",
  truth=diff(sin(x)+cos(x), x, 2027), tag='المشتقات العليا: النمط الدوري'),
# 2026 #14: two piecewise-linear graphs, h = f^2 - g, h'(1); options = sign of the g' term / g' dropped / sign
Q('m4q16', U3[3], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=f^{2}(x)-g(x)$ ، فإنّ $h'(1)$ تساوي:",
  [O('-6', -6), O('-2', -2), O('6', 6), O('-4', -4)],
  r"$h'(x)=2f(x)f'(x)-g'(x)$" "\n" r"من الشكل: $f(1)=2$ ، $f'(1)=-1$ (ميل القطعة من $(0,3)$ إلى $(2,1)$) ، $g'(1)=2$ (ميل القطعة من $(0,0)$ إلى $(3,6)$)" "\n" r"$h'(1)=2(2)(-1)-2=-6$",
  truth=lambda: 2*f4_16(1)*fs4_16(1)-gs4_16(1), figure=figure('m4q16', draw_two([(0, 3), (2, 1), (6, 5)], [(0, 0), (3, 6), (6, 3)], 6, 6, (5.0, 4.4), (2.0, 6.2))), tag='المشتقة من التمثيل البياني'),
# E (expected: ln of a quotient, split by the log laws first), template 2025s #1 (log laws, then the derivative);
# options = sign x one term dropped
Q('m4q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، حيث $x>1$ ، فإنّ $f'(2)$ تساوي:", (r'\ln\left(\frac{x+1}{x-1}\right)', log((x+1)/(x-1)))),
  [O(r'-\frac{2}{3}', -R(2, 3)), O(r'\frac{2}{3}', R(2, 3)), O(r'\frac{1}{3}', R(1, 3)), O(r'-\frac{1}{3}', -R(1, 3))],
  r"بخصائص اللوغاريتم: $f(x)=\ln(x+1)-\ln(x-1) \Rightarrow f'(x)=\dfrac{1}{x+1}-\dfrac{1}{x-1}$" "\n" r"$f'(2)=\frac13-1=-\frac23$",
  truth=Dx(log((x+1)/(x-1))).subs(x, 2), tag='قاعدة السلسلة مع اللوغاريتم'),
# 2026r #11: exponential model in context, rate at a given time, units in the options (bacteria -> a cooling cup of tea);
# options = sign / the factor 0.5 dropped / e^(-1) read as e
Q('m4q18', U3[3], 'easy',
  F(r"تُعطى درجة حرارة كوب من الشاي (بالسيليسيوس) بعد $t$ دقيقة بالاقتران: $T(t)=«0»$. معدّل تغيّر درجة حرارة الشاي عندما $t=2$ هو:", (r'25+60e^{-0.5t}', 25+60*exp(-t/2))),
  [O(r'-\frac{30}{e}', -30/E, units='°C/min'), O(r'\frac{30}{e}', 30/E, units='°C/min'), O(r'-\frac{60}{e}', -60/E, units='°C/min'), O('-30e', -30*E, units='°C/min')],
  r"$T'(t)=60(-0.5)e^{-0.5t}=-30e^{-0.5t}$ ، إذن $T'(2)=-30e^{-1}=-\dfrac{30}{e}$ (الإشارة السالبة تعني أن الشاي يبرد)",
  truth=diff(25+60*exp(-t/2), t).subs(t, 2), tag='معدل التغير في سياق حياتي'),
# 2024 #7: a^(quadratic) whose exponent vanishes at x = 3, f'(3) given -> a (a power of e);
# options = chain factor kept/dropped x sign of the exponent
Q('m4q19', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ قيمة الثابت $a$ التي تجعل $f'(3)=6$ هي:", (r'a^{(x^{2}-3x)}', a**(x**2-3*x))),
  [O(r'e^{2}', exp(2)), O(r'e^{-2}', exp(-2)), O(r'e^{6}', exp(6)), O(r'e^{-6}', exp(-6))],
  r"$f'(x)=a^{x^2-3x}\ln a\,(2x-3)$ ، وعند $x=3$ الأس صفر: $f'(3)=1\cdot\ln a\cdot3$" "\n" r"$3\ln a=6 \Rightarrow \ln a=2 \Rightarrow a=e^2$",
  truth=lambda: solve(Dx(a**(x**2-3*x)).subs(x, 3)-6, a)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# E (expected: second derivative of a parametric curve), template 2026 #15 (parametric dy/dx);
# options = the first derivative given instead / slips in the second division
Q('m4q20', U3[4], 'medium',
  F(r"إذا كان: $x=«0»$ ، $y=«1»$ ، حيث $t>0$ ، فإنّ $\dfrac{d^{2}y}{dx^{2}}$ عندما $t=1$ تساوي:", (r'\ln t', log(t)), (r't^{2}', t**2)),
  [O('4', 4), O('2', 2), O('8', 8), O('1', 1)],
  r"$\dfrac{dy}{dx}=\dfrac{2t}{1/t}=2t^2$ ، و $\dfrac{d^2y}{dx^2}=\dfrac{4t}{1/t}=4t^2$ ، وعند $t=1$: $4$",
  truth=(diff(diff(t**2, t)/diff(log(t), t), t)/diff(log(t), t)).subs(t, 1), tag='المشتقة الثانية للمعادلات الوسيطية'),
# 2023 #10: d/dx(ln y) for y = x^(x^3) (variable base and exponent); options = sign x ln x^3 vs (ln x)^3
Q('m4q21', U3[4], 'medium',
  F(r"إذا كان: $y=«0»$ ، $x>0$ ، فإنّ $\dfrac{d}{dx}(\ln y)$ هي:", (r'x^{x^{3}}', x**(x**3))),
  [O(r'x^{2}(1+\ln x^{3})', x**2*(1+log(x**3))), O(r'x^{2}(1-\ln x^{3})', x**2*(1-log(x**3))),
   O(r'x^{2}(1+(\ln x)^{3})', x**2*(1+log(x)**3)), O(r'x^{2}(1-(\ln x)^{3})', x**2*(1-log(x)**3))],
  r"$\ln y=x^3\ln x$ ، وبقاعدة الضرب: $\dfrac{d}{dx}(\ln y)=3x^2\ln x+x^3\cdot\dfrac1x=x^2(1+3\ln x)=x^2(1+\ln x^3)$",
  truth=Dx(x**3*log(x)), tag='الاشتقاق اللوغاريتمي'),
# 2026 #18: cylindrical tank (figure: base diameter) leaking in L/min -> constant rate of the level in cm/min;
# options = L -> cm^3 conversion done or not x r^2 vs r (one filler, 120/pi)
Q('m4q22', U3[5], 'medium',
  r"يُبيّن الشكل الآتي خزّانًا على شكل أسطوانة دائرية قائمة طول قُطر قاعدته $100\ \text{cm}$ ، يتسرّب منه الماء بمعدّل $3\ \text{L/min}$ ، فإنّ معدّل انخفاض مستوى الماء في الخزّان عند أيّ لحظة هو:",
  [O(r'\frac{6}{5\pi}', 6/(5*pi), units='cm/min'), O(r'\frac{3}{2500\pi}', 3/(2500*pi), units='cm/min'), O(r'\frac{120}{\pi}', 120/pi, units='cm/min'), O(r'\frac{3}{50\pi}', 3/(50*pi), units='cm/min')],
  r"$r=\frac{100}{2}=50\ \text{cm}$ ، $3\ \text{L}=3000\ \text{cm}^3$ ، و $V=\pi r^2h=2500\pi h$" "\n" r"$\dfrac{dV}{dt}=2500\pi\dfrac{dh}{dt} \Rightarrow -3000=2500\pi\dfrac{dh}{dt} \Rightarrow \dfrac{dh}{dt}=-\dfrac{6}{5\pi}$ ، أي ينخفض بمعدّل $\dfrac{6}{5\pi}\ \text{cm/min}$",
  truth=R(3000, 2500)/pi, figure=figure('m4q22', fig_tank(r'$100\ \mathrm{cm}$'), 2.8, 3.2), tag='معدلات مرتبطة مع تحويل الوحدات'),
# ---------------- unit 4
# E (expected: principal argument of r(cos + i sin) written with a negative r), template 2024 #23 (a "minus" trig form);
# options = the printed angle kept / not reduced to (-pi, pi] / wrong quadrant
Q('m4q23', U4[1], 'medium',
  r"إذا كان: $z=-2\left(\cos\frac{\pi}{5}+i\sin\frac{\pi}{5}\right)$ ، فإنّ السعة الرئيسة للعدد $z$ هي:",
  [O(r'-\frac{4\pi}{5}', -4*P/5), O(r'\frac{\pi}{5}', P/5), O(r'\frac{6\pi}{5}', 6*P/5), O(r'\frac{4\pi}{5}', 4*P/5)],
  r"المقياس لا يكون سالبًا: $z=2\left(-\cos\frac{\pi}{5}-i\sin\frac{\pi}{5}\right)=2\left(\cos\frac{6\pi}{5}+i\sin\frac{6\pi}{5}\right)$" "\n"
  r"و $\frac{6\pi}{5}>\pi$ ، فالسعة الرئيسة $\frac{6\pi}{5}-2\pi=-\frac{4\pi}{5}$",
  truth=arg(expand(-2*(cos(pi/5)+I*sin(pi/5)))), tag='السعة الرئيسة', lead=NOTE_I(23, 30)),
# 2026 #20: first item of a shared stem (conj(z) - 2w); options = real part x imaginary part slips
Q('m4q24', U4[1], 'easy',
  r"ناتج $\bar{z}-2w$ هو:",
  [O('1-3i', 1-3*I), O('1+5i', 1+5*I), O('5-3i', 5-3*I), O('1+3i', 1+3*I)],
  r"$\bar z=3+i$ ، $2w=2+4i$ ، إذن $\bar z-2w=1-3i$",
  truth=conjugate(3-I)-2*(1+2*I), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=3-i$ ، $w=1+2i$", 24, 25)),
# 2026 #21: second item of the shared stem (product zw); options = i^2 = +1 / sign of the imaginary part / parts multiplied separately
Q('m4q25', U4[2], 'easy',
  r"ناتج $zw$ هو:",
  [O('5+5i', 5+5*I), O('1+5i', 1+5*I), O('5-5i', 5-5*I), O('3-2i', 3-2*I)],
  r"$zw=(3-i)(1+2i)=3+6i-i-2i^2=5+5i$",
  truth=expand((3-I)*(1+2*I)), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2024 #24: a - i sqrt2 (a > 0) is a square root of 1 - 2i sqrt6 -> a; options = same-kind surds
# (sqrt2 dropped from 2a sqrt2 = 2 sqrt6; multiplied instead of divided; a filler, as the model)
Q('m4q26', U4[2], 'medium',
  F(r"إذا كان: $«0»$ ، $a>0$ هو أحد الجذرين التربيعيين للعدد المركّب $«1»$ ، فإنّ قيمة الثابت الحقيقي $a$ هي:", (r'a-i\sqrt{2}', a-I*sqrt(2)), (r'1-2i\sqrt{6}', 1-2*sqrt(6)*I)),
  [O(r'\sqrt{3}', sqrt(3)), O(r'\sqrt{6}', sqrt(6)), O(r'2\sqrt{3}', 2*sqrt(3)), O(r'\sqrt{2}', sqrt(2))],
  r"$(a-i\sqrt2)^2=a^2-2-2a\sqrt2\,i=1-2\sqrt6\,i$" "\n" r"$a^2-2=1 \Rightarrow a^2=3 \Rightarrow a=\sqrt3$ (لأن $a>0$) ، وتحقّق: $2\sqrt3\cdot\sqrt2=2\sqrt6$",
  truth=lambda: [d_[X] for d_ in solve(expand((X-I*sqrt(2))**2-(1-2*sqrt(6)*I)), X, dict=True) if d_[X] > 0][0], tag='الجذور التربيعية للعدد المركب'),
# 2026 #23: quadratic with a given complex root; options = sign of the sum / product slips
Q('m4q27', U4[2], 'easy',
  r"المعادلة التربيعية ذات المعاملات الحقيقية التي أحد جذريها العدد المُركَّب $(-1+2i)$ هي:",
  [O('x^{2}+2x+5=0', x**2+2*x+5, 'rel'), O('x^{2}-2x+5=0', x**2-2*x+5, 'rel'), O('x^{2}+2x+3=0', x**2+2*x+3, 'rel'), O('x^{2}+2x-5=0', x**2+2*x-5, 'rel')],
  r"الجذر الآخر $-1-2i$ ، المجموع $-2$ ، وحاصل الضرب $1+4=5$ ، والمعادلة: $x^2+2x+5=0$",
  truth=expand((x-(-1+2*I))*(x-(-1-2*I))), tag='معادلة تربيعية بمعلومية جذر مركب'),
# 2024s #22: r(cos theta + i sin theta) with a quadrantal angle (3pi/2 here) -> standard form; options = imaginary vs real axis x sign
Q('m4q28', U4[1], 'easy',
  F(r"الصورة القياسية للعدد المركّب: $z=«0»$ هي:", (r'4\left(\cos\frac{3\pi}{2}+i\sin\frac{3\pi}{2}\right)', pol(4, 3*pi/2))),
  [O('-4i', -4*I), O('4i', 4*I), O('-4', -4), O('4', 4)],
  r"$\cos\frac{3\pi}{2}=0$ ، $\sin\frac{3\pi}{2}=-1$ ، إذن $z=4(0-i)=-4i$",
  truth=expand(4*cos(3*pi/2)+4*I*sin(3*pi/2)), tag='من الصورة المثلثية إلى الصورة القياسية'),
# 2023 #25: perpendicular bisector drawn on a grid with its two points (the line does not pass through O);
# options = sign of each point's term
IndexQ('m4q29', U4[3], 'medium',
  r"معتمدًا الشكل الآتي، ما معادلة المستقيم $l$ (بدلالة $z$) المُمثَّل بيانيًّا؟",
  [T(r'$|z-3-3i|=|z-1+i|$', bisector(A4_29, B4_29)), T(r'$|z+3+3i|=|z-1+i|$', bisector(-A4_29, B4_29)),
   T(r'$|z-3-3i|=|z+1-i|$', bisector(A4_29, -B4_29)), T(r'$|z+3+3i|=|z+1-i|$', bisector(-A4_29, -B4_29))],
  r"$l$ عمود منصّف للقطعة $AB$ ، حيث $A(3,3)$ أي $3+3i$ ، و $B(1,-1)$ أي $1-i$" "\n" r"$|z-(3+3i)|=|z-(1-i)| \Rightarrow |z-3-3i|=|z-1+i|$",
  truth=region_truth(on_line4, L4_29, 5), figure=figure('m4q29', fig_bisector4(), 3.4, 3.4), tag='كتابة معادلة محل هندسي'),
# 2025 #25: ring between two circles with the same centre, one circle dashed (here the inner one);
# options = centre sign x which circle is strict
IndexQ('m4q30', U4[3], 'hard',
  r"متباينة المحلّ الهندسي (بدلالة $z$) التي تُمثِّل المنطقة المُظلَّلة في الشكل الآتي هي:",
  [T(r'$1<|z-1-i|\le2$', R4_30),
   T(r'$1<|z+1+i|\le2$', both(outside(-C4_30, 1, strict=True), disk(-C4_30, 2))),
   T(r'$1\le|z-1-i|<2$', both(outside(C4_30, 1), disk(C4_30, 2, strict=True))),
   T(r'$1\le|z+1+i|<2$', both(outside(-C4_30, 1), disk(-C4_30, 2, strict=True)))],
  r"المركز $(1,1)$ أي $1+i$ ، فنكتب $|z-(1+i)|=|z-1-i|$" "\n" r"الدائرة الداخلية (نصف القطر $1$) متقطّعة: $1<$ ، والخارجية (نصف القطر $2$) متصلة: $\le2$",
  truth=region_truth(R4_30, PR4_30, 4), figure=figure('m4q30', fig_region2(R4_30, PR4_30, 4, marks=((C4_30, ''),)), 3.4, 3.4),
  tag='منطقة في المستوى المركب من الشكل'),
]


# ================================================================== PAPER 5
f5_16, fs5_16 = pw([(0, 6), (4, 2), (7, 5)])
g5_16, gs5_16 = pw([(0, 1), (5, 6), (7, 2)])
F5_2 = x**3 + a*x**2 + b*x + 6                     # m5q2
A5, B5, C5 = symbols('A B C')                       # m5q4: unknown constants of a decomposition form
FRAC5_4 = (x**2 + 5)/((x - 2)**2*(x + 1))


def can_form5(form, frac):
    """m5q4: True when constants A, B, C exist that make the form identically equal to the fraction."""
    eqs = Poly(expand(numer(together(form - frac))), x).all_coeffs()
    return linsolve(eqs, [A5, B5, C5]) != EmptySet


def max_arg5(c_, r_, n_=100000):
    """m5q28: greatest principal argument on the circle |z - c| = r, by dense sampling (independent of the tangent rule)."""
    best = max(cmath.phase(c_ + r_*cmath.exp(2j*math.pi*k_/n_)) for k_ in range(n_))
    return nsimplify(best, [pi], tolerance=1e-6)


V5 = -2 - 1j                                         # m5q30: vertex of the wedge
R5_30 = sector(V5, math.pi/4, math.pi/2, hi_open=True)
PR5_30 = [('seg', V5, V5 + 8*cmath.exp(1j*math.pi/4), False), ('seg', V5, V5 + 8j, True), ('open', V5)]
P5 = [
# E (expected: complete factorisation, one zero found by trial), template 2026 #1: one synthetic division + factor the
# quadratic quotient; options = signs of the two other factors (2026 #1 grid)
Q('m5q1', U1[1], 'medium',
  F(r"التحليل الكامل لكثير الحدود: $«0»$ هو:", (r'x^{3}-x^{2}-10x-8', x**3-x**2-10*x-8)),
  [O('(x+1)(x+2)(x-4)', (x+1)*(x+2)*(x-4)), O('(x+1)(x-2)(x+4)', (x+1)*(x-2)*(x+4)),
   O('(x+1)(x+2)(x+4)', (x+1)*(x+2)*(x+4)), O('(x+1)(x-2)(x-4)', (x+1)*(x-2)*(x-4))],
  r"$f(-1)=-1-1+10-8=0$ ، إذن $(x+1)$ عامل" "\n"
  r"بالقسمة التركيبية: $x^3-x^2-10x-8=(x+1)(x^2-2x-8)=(x+1)(x+2)(x-4)$",
  truth=x**3-x**2-10*x-8, tag='التحليل الكامل لكثير حدود'),
# E (expected: factor + remainder -> constants; the equal-remainder condition gives b at once), template 2026 #3:
# equal remainders -> constant; options = sign x 4a not divided by 4 (2026 #3 grid)
Q('m5q2', U1[1], 'medium',
  F(r"إذا كان $(x-2)$ أحد عوامل الاقتران: $f(x)=«0»$ ، وكان باقي قسمة $f(x)$ على $(x-1)$ مساويًا لباقي قسمته على $(x+1)$ ، فإنّ قيمة الثابت $a$ هي:", (r'x^{3}+ax^{2}+bx+6', F5_2)),
  [O('-3', -3), O('3', 3), O('-12', -12), O('12', 12)],
  r"$f(1)=f(-1)$: $a+b+7=a-b+5 \Rightarrow 2b=-2 \Rightarrow b=-1$" "\n" r"$f(2)=0$: $8+4a-2+6=0 \Rightarrow 4a=-12 \Rightarrow a=-3$",
  truth=lambda: solve([rem(F5_2, 1)-rem(F5_2, -1), rem(F5_2, 2)], [a, b])[a], tag='نظرية الباقي والعوامل معًا'),
# E (expected: decomposition with an irreducible quadratic factor), template 2026 #2: which is the decomposition;
# options = numerator sign / A not halved (6) / a constant over the quadratic
Q('m5q3', U1[2], 'medium',
  F(r"أيّ الآتية يُمثّل تجزئة المقدار النسبي: $«0»$ إلى كسور جزئية؟", (r'\frac{2x^{2}+x+6}{x^{3}+2x}', (2*x**2+x+6)/(x**3+2*x))),
  [O(r'\frac{3}{x}+\frac{1-x}{x^{2}+2}', 3/x+(1-x)/(x**2+2)), O(r'\frac{3}{x}+\frac{x-1}{x^{2}+2}', 3/x+(x-1)/(x**2+2)), O(r'\frac{2}{x}+\frac{1}{x^{2}+2}', 2/x+1/(x**2+2)), O(r'\frac{6}{x}+\frac{1-4x}{x^{2}+2}', 6/x+(1-4*x)/(x**2+2))],
  r"$x^3+2x=x(x^2+2)$ ، و $2x^2+x+6=A(x^2+2)+(Bx+C)x$" "\n" r"عند $x=0$: $6=2A \Rightarrow A=3$ ، معامل $x^2$: $2=3+B \Rightarrow B=-1$ ، معامل $x$: $C=1$",
  truth=(2*x**2+x+6)/(x**3+2*x), tag='تجزئة: عامل تربيعي غير قابل للتحليل'),
# E (expected: the correct FORM of a decomposition with a repeated linear factor), template 2026 #2: which is the
# decomposition (repeated linear factor); options = lower power missing / wrong factor repeated / two first-power terms
IndexQ('m5q4', U1[2], 'easy',
  F(r"أيُّ الآتية يُمثّل الصورة الصحيحة لتجزئة المقدار النسبي: $«0»$ إلى كسور جزئية، حيث $A$ و $B$ و $C$ ثوابت؟", (r'\frac{x^{2}+5}{(x-2)^{2}(x+1)}', FRAC5_4)),
  [O(r'\frac{A}{x-2}+\frac{B}{(x-2)^{2}}+\frac{C}{x+1}', A5/(x-2)+B5/(x-2)**2+C5/(x+1)),
   O(r'\frac{A}{(x-2)^{2}}+\frac{B}{x+1}', A5/(x-2)**2+B5/(x+1)),
   O(r'\frac{A}{x-2}+\frac{B}{x+1}+\frac{C}{(x+1)^{2}}', A5/(x-2)+B5/(x+1)+C5/(x+1)**2),
   O(r'\frac{A}{x-2}+\frac{B}{x-2}+\frac{C}{x+1}', A5/(x-2)+B5/(x-2)+C5/(x+1))],
  r"العامل $(x-2)$ مكرّر (مربّع)، فنكتب له كسرين: $\dfrac{A}{x-2}+\dfrac{B}{(x-2)^2}$ ، والعامل الخطي $(x+1)$ كسرًا واحدًا $\dfrac{C}{x+1}$",
  truth=lambda vals: only(vals, lambda v_: can_form5(v_, FRAC5_4)), tag='تجزئة: الصورة الصحيحة للتجزئة'),
# E (expected: cofunction / even-odd identities), template 2026 #6 («أيُّ الآتية …؟»); options = four identities of
# the same shape, the false one has the sign of a cofunction switched
IndexQ('m5q5', U2[1], 'easy',
  r"أيُّ الآتية **ليست** متطابقة؟",
  [O(r'\sin\left(\frac{\pi}{2}-x\right)=-\cos x', sin(P/2-x)+cos(x), 'rel'), O(r'\csc(-x)=-\csc x', csc(-x)+csc(x), 'rel'),
   O(r'\sec\left(\frac{\pi}{2}-x\right)=\csc x', sec(P/2-x)-csc(x), 'rel'), O(r'\tan(-x)=-\tan x', tan(-x)+tan(x), 'rel')],
  r"$\sin\left(\frac{\pi}{2}-x\right)=\cos x$ (اقترانان متتامّان) وليس $-\cos x$" "\n" r"أما $\csc$ و $\tan$ فاقترانان فرديان، و $\sec\left(\frac{\pi}{2}-x\right)=\csc x$",
  truth=lambda vals: only(vals, lambda v_: not same(v_, 0)), tag='المتطابقات: الزوايا المنتسبة والزوجية والفردية'),
# E (expected: tan(A + B) from two ratios in given quadrants), template 2026 #4: a ratio and a quadrant -> exact value;
# options = sign x tan B with the wrong sign (= tan(A - B))
Q('m5q6', U2[1], 'medium',
  r"إذا كان $\tan A=\frac{3}{4}$ حيث $\pi<A<\frac{3\pi}{2}$ ، و $\cos B=-\frac{5}{13}$ حيث $\frac{\pi}{2}<B<\pi$ ، فإنّ قيمة $\tan(A+B)$ هي:",
  [O(r'-\frac{33}{56}', -R(33, 56)), O(r'\frac{33}{56}', R(33, 56)), O(r'-\frac{63}{16}', -R(63, 16)), O(r'\frac{63}{16}', R(63, 16))],
  r"$B$ في الربع الثاني: $\sin B=\frac{12}{13}$ ، $\tan B=-\frac{12}{5}$" "\n"
  r"$\tan(A+B)=\dfrac{\frac34-\frac{12}{5}}{1+\frac34\cdot\frac{12}{5}}=\dfrac{-\frac{33}{20}}{\frac{56}{20}}=-\dfrac{33}{56}$",
  truth=tan((pi+atan(R(3, 4)))+(pi-acos(R(5, 13)))), tag='المجموع والفرق بمعلومية نسب في أرباع مختلفة'),
# E (expected: double-angle exact value), template 2026 #5 (one identity, 2x2 grid); options = sin vs cos of 2a x
# coefficient kept vs doubled
Q('m5q7', U2[2], 'easy',
  F(r"قيمة المقدار: $«0»$ هي:", (r'2\sin\frac{\pi}{12}\cos\frac{\pi}{12}', 2*sin(P/12)*cos(P/12))),
  [O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O('1', 1), O(r'\sqrt{3}', sqrt(3))],
  r"$2\sin\theta\cos\theta=\sin2\theta$ ، إذن $2\sin\frac{\pi}{12}\cos\frac{\pi}{12}=\sin\frac{\pi}{6}=\frac12$",
  truth=2*sin(pi/12)*cos(pi/12), tag='قيم دقيقة بمتطابقات ضعف الزاوية'),
# E (expected: power reduction under a root), template 2026 #5: simplest form; options = angle 2x vs 4x, coefficient
# 2 vs sqrt2, cos vs sin
Q('m5q8', U2[2], 'medium',
  F(r"إذا كانت $0<x<\frac{\pi}{8}$ ، فإنّ أبسط صورة للمقدار $«0»$ هي:", (r'\sqrt{2+2\cos 4x}', sqrt(2+2*cos(4*x)))),
  [O(r'2\cos 2x', 2*cos(2*x)), O(r'2\cos 4x', 2*cos(4*x)), O(r'\sqrt{2}\cos 2x', sqrt(2)*cos(2*x)), O(r'2\sin 2x', 2*sin(2*x))],
  r"$2+2\cos4x=2(1+\cos4x)=2\cdot2\cos^22x=4\cos^22x$ ، فالمقدار $=|2\cos2x|=2\cos2x$ (لأن $0<2x<\frac{\pi}{4}$)",
  truth=2*cos(2*x), tag='تقليص القوة ونصف الزاوية'),
# E (expected: sum of the solutions in an interval), template 2026 #7: quadratic in sin x on [0, 2pi); options = roots
# lost by dividing by sin x / only sin x = 0 / 3pi/2 taken for sin x = 1
Q('m5q9', U2[3], 'medium',
  F(r"مجموع حلول المعادلة: $«0»=«1»$ في الفترة $[0,\,2\pi)$ هو:", (r'\sin^{2}x', sin(x)**2), (r'\sin x', sin(x))),
  [O(r'\frac{3\pi}{2}', 3*P/2), O(r'\frac{\pi}{2}', P/2), O(r'\pi', P), O(r'\frac{5\pi}{2}', 5*P/2)],
  r"$\sin x(\sin x-1)=0$: $\sin x=0 \Rightarrow x=0,\ \pi$ ، $\sin x=1 \Rightarrow x=\frac{\pi}{2}$" "\n" r"المجموع $=0+\pi+\frac{\pi}{2}=\frac{3\pi}{2}$ (لا نقسم على $\sin x$)",
  truth=lambda: sum(sols(sin(x)**2-sin(x), 0, 2*pi)), tag='مجموع الحلول في فترة'),
# E (expected: Pythagorean substitution -> quadratic in sin x, one root rejected), template 2026 #7: quadratic in one
# ratio with a root outside [-1, 1]; options = sign of sin x x reference angle pi/6 vs pi/3
Q('m5q10', U2[3], 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\cos^{2}x+3\sin x', 2*cos(x)**2+3*sin(x))),
  [O(st(r'\frac{7\pi}{6}', r'\frac{11\pi}{6}'), S_(7*P/6, 11*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'),
   O(st(r'\frac{4\pi}{3}', r'\frac{5\pi}{3}'), S_(4*P/3, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set')],
  r"$2(1-\sin^2x)+3\sin x=0 \Rightarrow 2\sin^2x-3\sin x-2=0 \Rightarrow (2\sin x+1)(\sin x-2)=0$" "\n"
  r"$\sin x=2$ مرفوض ، و $\sin x=-\frac12$ في الربعين الثالث والرابع: $x=\frac{7\pi}{6},\ \frac{11\pi}{6}$",
  truth=lambda: sols(2*cos(x)**2+3*sin(x), 0, 2*pi), tag='معادلة تربيعية بعد استعمال متطابقة فيثاغورس'),
# 2024s #9: f'(x) of a root of a power of x, answer as a radical (power rule); options = sign x root in the
# denominator (exponent -1/4) vs numerator (+1/4)
Q('m5q11', U3[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ هي:", (r'\sqrt[4]{x^{3}}', x**R(3, 4))),
  [O(r'\frac{3}{4\sqrt[4]{x}}', R(3, 4)*x**R(-1, 4)), O(r'-\frac{3}{4\sqrt[4]{x}}', -R(3, 4)*x**R(-1, 4)),
   O(r'\frac{3}{4}\sqrt[4]{x}', R(3, 4)*x**R(1, 4)), O(r'-\frac{3}{4}\sqrt[4]{x}', -R(3, 4)*x**R(1, 4))],
  r"$f(x)=x^{\frac34} \Rightarrow f'(x)=\frac34x^{\frac34-1}=\frac34x^{-\frac14}=\dfrac{3}{4\sqrt[4]{x}}$",
  truth=Dx(x**R(3, 4)), tag='قاعدة القوة: اقتران جذري'),
# 2023 #2: product rule, symbolic f'(x); options = sign x which function survives (product rule written as a difference)
Q('m5q12', U3[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ تساوي:", (r'e^{x}(\cos x-\sin x)', exp(x)*(cos(x)-sin(x)))),
  [O(r'-2e^{x}\sin x', -2*exp(x)*sin(x)), O(r'2e^{x}\cos x', 2*exp(x)*cos(x)), O(r'-2e^{x}\cos x', -2*exp(x)*cos(x)), O(r'2e^{x}\sin x', 2*exp(x)*sin(x))],
  r"$f'(x)=e^x(\cos x-\sin x)+e^x(-\sin x-\cos x)=-2e^x\sin x$",
  truth=Dx(exp(x)*(cos(x)-sin(x))), tag='مشتقة الضرب'),
# 2025 #4: s(t) = A sin(kt) in cm, position when the velocity is zero; options = +-A, +-k, 0, +-Ak (new context: a
# fishing float on waves)
Q('m5q13', U3[1], 'easy',
  F(r"إذا تحرّكت عوّامة صيد على سطح الماء إلى الأعلى وإلى الأسفل، وحدّد الاقتران: $s(t)=«0»$ موقعها عند أيّ زمن لاحق، حيث $t$ الزمن بالثواني، و $s$ الموقع بالسنتيمترات، فإنّ موقع العوّامة عندما تكون سرعتها صفرًا هو:", (r'1.5\sin 0.8t', R(3, 2)*sin(R(4, 5)*t))),
  [O(r'\pm 1.5', S_(R(3, 2), -R(3, 2)), 'set', units='cm'), O(r'\pm 0.8', S_(R(4, 5), -R(4, 5)), 'set', units='cm'),
   O('0', S_(0), 'set', units='cm'), O(r'\pm 1.2', S_(R(6, 5), -R(6, 5)), 'set', units='cm')],
  r"$v(t)=s'(t)=1.2\cos0.8t=0 \Rightarrow \cos0.8t=0 \Rightarrow \sin0.8t=\pm1$" "\n" r"$s=1.5(\pm1)=\pm1.5\ \text{cm}$",
  truth=lambda: FiniteSet(*[(R(3, 2)*sin(R(4, 5)*t)).subs(t, t0) for t0 in sols(diff(R(3, 2)*sin(R(4, 5)*t), t), 0, 20)]),
  tag='الحركة: اتجاه الحركة والسكون'),
# E (expected: x-intercept of a tangent line), template 2026 #17: tangent at a point -> intercept; options = values
# from the tangent-line computation (point coordinate, sign slip, 1/2)
Q('m5q14', U3[1], 'medium',
  F(r"المقطع $x$ للمماس لمنحنى الاقتران: $f(x)=«0»$ عند $x=1$ هو:", (r'x-2\ln x', x-2*log(x))),
  [O('2', 2), O('1', 1), O('-2', -2), O(r'\frac{1}{2}', R(1, 2))],
  r"$f(1)=1$ ، $f'(x)=1-\dfrac2x \Rightarrow f'(1)=-1$ ، فالمماس: $y-1=-(x-1) \Rightarrow y=-x+2$" "\n" r"عند $y=0$: $x=2$",
  truth=lambda: solve(1 + Dx(x-2*log(x)).subs(x, 1)*(x-1), x)[0], tag='معادلة المماس ومقاطعه'),
# 2026 #10: cube root times a polynomial with a constant, f'(-1) given -> constant; options = small integers
# (1/3 dropped, sign of the second term, (-1)^2 taken as -1)
Q('m5q15', U3[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان: $f'(-1)=5$ ، فإنّ قيمة الثابت $b$ هي:", (r'\sqrt[3]{x}\,(x^{2}+b)', x**R(1, 3)*(x**2+b))),
  [O('8', 8), O('2', 2), O('20', 20), O('10', 10)],
  r"$f'(x)=\frac13x^{-\frac23}(x^2+b)+\sqrt[3]{x}\cdot2x$" "\n" r"$f'(-1)=\dfrac{1+b}{3}+(-1)(-2)=\dfrac{1+b}{3}+2=5 \Rightarrow 1+b=9 \Rightarrow b=8$",
  truth=lambda: solve(diff(-(-x)**R(1, 3)*(x**2+b), x).subs(x, -1)-5, b)[0], tag='إيجاد ثابت بمعلومية قيمة المشتقة'),
# 2026r #3: quotient of two piecewise-linear graphs at a point; options = sign x magnitude (numerator order reversed,
# slope of f read with the wrong sign, + instead of -)
Q('m5q16', U3[2], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $k(x)=\dfrac{f(x)}{g(x)}$ ، فإنّ $k'(1)$ تساوي:",
  [O(r'-\frac{7}{4}', -R(7, 4)), O(r'\frac{7}{4}', R(7, 4)), O(r'-\frac{3}{4}', -R(3, 4)), O(r'\frac{3}{4}', R(3, 4))],
  r"من الشكل: $f(1)=5$ ، $f'(1)=-1$ ، $g(1)=2$ ، $g'(1)=1$" "\n" r"$k'(1)=\dfrac{f'(1)g(1)-f(1)g'(1)}{g(1)^2}=\dfrac{(-1)(2)-(5)(1)}{4}=-\dfrac74$",
  truth=lambda: (fs5_16(1)*g5_16(1)-f5_16(1)*gs5_16(1))/g5_16(1)**2, figure=figure('m5q16', draw_two([(0, 6), (4, 2), (7, 5)], [(0, 1), (5, 6), (7, 2)], 7, 6, (0.3, 6.3), (5.3, 6.1))), tag='المشتقة من التمثيل البياني'),
# 2024s #11: log base a of an algebraic composite at a point; options = ln 3 missing / (sqrt x)' taken as 1/sqrt x /
# not divided by u(1) = 2
Q('m5q17', U3[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'\log_{3}(x+\sqrt{x})', log(x+sqrt(x), 3))),
  [O(r'\frac{3}{4\ln 3}', 3/(4*log(3))), O(r'\frac{3}{4}', R(3, 4)), O(r'\frac{1}{\ln 3}', 1/log(3)), O(r'\frac{3}{2\ln 3}', 3/(2*log(3)))],
  r"$f'(x)=\dfrac{1+\frac{1}{2\sqrt x}}{(x+\sqrt x)\ln3} \Rightarrow f'(1)=\dfrac{\frac32}{2\ln3}=\dfrac{3}{4\ln3}$",
  truth=Dx(log(x+sqrt(x), 3)).subs(x, 1), tag='مشتقة اللوغاريتم لأساس غير e'),
# E (expected: context model, the time when the rate of change is zero), template 2026 #12 (rate of a context function,
# units in the options); options = list of times (0.5 and 10 are constants of the model)
Q('m5q18', U3[3], 'medium',
  F(r"يُمثّل الاقتران: $N(t)=«0»$ عدد زوّار موقع إلكتروني (بالآلاف) بعد $t$ ساعة من نشر خبر عليه. الزمن الذي يكون عنده معدّل تغيّر عدد الزوّار صفرًا هو:", (r'10te^{-0.5t}', 10*t*exp(-t/2))),
  [O('2', 2, units='h'), O('0.5', R(1, 2), units='h'), O('10', 10, units='h'), O('1', 1, units='h')],
  r"$N'(t)=10e^{-0.5t}+10t(-0.5)e^{-0.5t}=10e^{-0.5t}(1-0.5t)=0 \Rightarrow t=2$",
  truth=lambda: solve(diff(10*t*exp(-t/2), t), t)[0], tag='معدل التغير في سياق حياتي'),
# E (expected: point of a horizontal tangent of a parametric curve), template 2026 #15; options = sign of y /
# t = -2 (rejected) / t = 1 (vertical tangent)
Q('m5q19', U3[3], 'medium',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، حيث $t>0$ ، فإنّ النقطة التي يكون عندها المماس أفقيًّا هي:", (r't^{2}-2t', t**2-2*t), (r't^{3}-12t', t**3-12*t)),
  [O(r'(0,\ -16)', Tuple(0, -16), 'tuple'), O(r'(0,\ 16)', Tuple(0, 16), 'tuple'), O(r'(8,\ 16)', Tuple(8, 16), 'tuple'), O(r'(-1,\ -11)', Tuple(-1, -11), 'tuple')],
  r"المماس أفقي عندما $\dfrac{dy}{dt}=3t^2-12=0 \Rightarrow t=2$ (لأن $t>0$) ، و $\dfrac{dx}{dt}=2t-2=2\ne0$" "\n" r"النقطة: $x=4-4=0$ ، $y=8-24=-16$",
  truth=lambda: (lambda r_: Tuple(r_**2-2*r_, r_**3-12*r_))([q for q in solve(diff(t**3-12*t, t), t) if q > 0][0]), tag='مماس أفقي لمنحنى وسيطي'),
# 2024 #10: dy/dx of a variable base and exponent by logarithmic differentiation, answer in x and y; options = factor y
# kept/forgotten x (sqrt x)' with/without the 2
Q('m5q20', U3[4], 'medium',
  F(r"إذا كانت: $y=«0»$ ، $x>0$ ، فإنّ ميل المماس لمنحنى العلاقة $y$ عند أيّ نقطة تقع عليها، هو:", (r'x^{\sqrt{x}}', x**sqrt(x))),
  [O(r'\frac{y(\ln x+2)}{2\sqrt{x}}', x**sqrt(x)*(log(x)+2)/(2*sqrt(x)), sym={'y': x**sqrt(x)}), O(r'\frac{\ln x+2}{2\sqrt{x}}', (log(x)+2)/(2*sqrt(x))),
   O(r'\frac{y(\ln x+1)}{\sqrt{x}}', x**sqrt(x)*(log(x)+1)/sqrt(x), sym={'y': x**sqrt(x)}), O(r'\frac{\ln x+1}{\sqrt{x}}', (log(x)+1)/sqrt(x))],
  r"$\ln y=\sqrt x\,\ln x$" "\n" r"$\dfrac1y\dfrac{dy}{dx}=\dfrac{\ln x}{2\sqrt x}+\dfrac{\sqrt x}{x}=\dfrac{\ln x+2}{2\sqrt x} \Rightarrow \dfrac{dy}{dx}=\dfrac{y(\ln x+2)}{2\sqrt x}$",
  truth=Dx(x**sqrt(x)), tag='الاشتقاق اللوغاريتمي'),
# 2026 #17: tangent to an implicit curve at a lattice point, y-intercept; options = values from the tangent-line
# computation (sign slip, the slope, the constant of the relation)
Q('m5q21', U3[4], 'medium',
  F(r"إذا مثّل المستقيم $l$ مماسًّا لمنحنى العلاقة: $«0»=9$ عند النقطة $(1,\,2)$ ، فإنّ المقطع $y$ للمستقيم $l$ هو:", (r'x^{3}+y^{3}', x**3+y**3)),
  [O(r'\frac{9}{4}', R(9, 4)), O(r'\frac{7}{4}', R(7, 4)), O(r'-\frac{1}{4}', -R(1, 4)), O('9', 9)],
  r"$3x^2+3y^2y'=0 \Rightarrow y'=-\dfrac{x^2}{y^2}=-\dfrac14$ عند $(1,2)$" "\n" r"المماس: $y-2=-\frac14(x-1)$ ، وعند $x=0$: $y=2+\frac14=\frac94$",
  truth=lambda: 2 + imp(x**3+y**3-9, (1, 2))*(0-1), tag='مماس منحنى علاقة ضمنية'),
# 2026r #13: sphere, related rates between V and r (here dV/dt given -> dr/dt); options = reciprocal / r^2 slips
Q('m5q22', U3[5], 'easy',
  r"كرة ثلج تذوب فيتناقص حجمها بمعدّل $8\pi\ \text{cm}^3/\text{min}$ وتبقى محافظة على شكلها الكروي. معدّل تناقص نصف قطرها عندما يكون نصف قطرها $2\ \text{cm}$ هو:",
  [O(r'\frac{1}{2}', R(1, 2), units='cm/min'), O('2', 2, units='cm/min'), O(r'\frac{1}{8}', R(1, 8), units='cm/min'), O(r'\frac{1}{4}', R(1, 4), units='cm/min')],
  r"$V=\frac43\pi r^3 \Rightarrow \dfrac{dV}{dt}=4\pi r^2\dfrac{dr}{dt} \Rightarrow -8\pi=16\pi\dfrac{dr}{dt} \Rightarrow \dfrac{dr}{dt}=-\dfrac12$" "\n" r"أي يتناقص نصف القطر بمعدّل $\frac12\ \text{cm/min}$",
  truth=8*pi/(4*pi*4), tag='معدلات مرتبطة: كرة'),
# 2025s #25: |z1 z2| given -> the two values of p in z1 = a + pi; options = +-k pairs (|z2|, no squaring, |z1|)
Q('m5q23', U4[1], 'medium',
  r"إذا كان: $z_1=9+pi$ ، و $z_2=2+i\sqrt{5}$ ، وكان: $|z_1z_2|=45$ ، فإنّ القيمتين المُمكنتين للثابت $p$ هما:",
  [O(r'\pm 12', S_(12, -12), 'set'), O(r'\pm 3', S_(3, -3), 'set'), O(r'\pm 6', S_(6, -6), 'set'), O(r'\pm 15', S_(15, -15), 'set')],
  r"$|z_2|=\sqrt{4+5}=3$ ، و $|z_1z_2|=|z_1||z_2| \Rightarrow |z_1|=\frac{45}{3}=15$" "\n" r"$81+p^2=225 \Rightarrow p^2=144 \Rightarrow p=\pm12$",
  truth=lambda: FiniteSet(*solve(Abs(2+sqrt(5)*I)*sqrt(81+X**2)-45, X)), tag='إيجاد ثابت بمعلومية المقياس', lead=NOTE_I(23, 30)),
# 2023 #22: quotient of two numbers given in trig form, answer in trig form; options = moduli divided vs subtracted x
# arguments subtracted vs added
Q('m5q24', U4[2], 'medium',
  F(r"إذا كان: $z_1=«0»$ ، $z_2=«1»$ ، فإنّ $\dfrac{z_1}{z_2}$ هي:",
    (r'6\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right)', 6*pol(1, 2*P/3)), (r'2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right)', 2*pol(1, P/4))),
  [O(trig('3', r'\frac{5\pi}{12}'), 3*pol(1, 5*P/12)), O(trig('3', r'\frac{11\pi}{12}'), 3*pol(1, 11*P/12)),
   O(trig('4', r'\frac{5\pi}{12}'), 4*pol(1, 5*P/12)), O(trig('4', r'\frac{11\pi}{12}'), 4*pol(1, 11*P/12))],
  r"عند القسمة نقسم المقياسين: $\frac62=3$ ، ونطرح السعتين: $\frac{2\pi}{3}-\frac{\pi}{4}=\frac{8\pi-3\pi}{12}=\frac{5\pi}{12}$",
  truth=(6*pol(1, 2*P/3))/(2*pol(1, P/4)), tag='الضرب والقسمة بالصورة المثلثية'),
# 2026r #20: the real a from Arg(a + bi) = special angle; options = list (tan inverted, |z| from sin, its negative)
IndexQ('m5q25', U4[1], 'easy',
  r"إذا كان: $z=a+\sqrt{3}\,i$ ، وكان: $\text{Arg}(z)=\frac{\pi}{3}$ ، فإنّ قيمة الثابت $a$ هي:",
  [O('1', 1), O('3', 3), O('2', 2), O('-2', -2)],
  r"$\tan\frac{\pi}{3}=\dfrac{\sqrt3}{a} \Rightarrow \sqrt3=\dfrac{\sqrt3}{a} \Rightarrow a=1$ (موجب لأن السعة في الربع الأول)",
  truth=lambda vals: only(vals, lambda v_: simplify(arg(v_+sqrt(3)*I)-pi/3) == 0), tag='السعة الرئيسة'),
# 2026r #22: first item of a shared stem, a linear combination a z + b w; options = overall sign (subtraction reversed)
# x imaginary part 17 vs 1 (-2(-4i) taken as -8i)
Q('m5q26', U4[2], 'easy',
  r"ناتج $3z-2w$ هو:",
  [O('-8+17i', -8+17*I), O('8-17i', 8-17*I), O('-8+i', -8+I), O('8-i', 8-I)],
  r"$3z=-6+9i$ ، $2w=2-8i$ ، إذن $3z-2w=(-6-2)+(9+8)i=-8+17i$",
  truth=expand(3*(-2+3*I)-2*(1-4*I)), tag='العمليات على الأعداد المركبة (نص مشترك)', lead=shared(r"إذا كان: $z=-2+3i$ ، $w=1-4i$", 26, 27)),
# 2024 #21 family: second item of the shared stem, w^2 in standard form; options = i^2 = +1 slip x middle term 2ab
# halved
Q('m5q27', U4[2], 'medium',
  r"ناتج $w^{2}$ هو:",
  [O('-15-8i', -15-8*I), O('17-8i', 17-8*I), O('-15-4i', -15-4*I), O('17-4i', 17-4*I)],
  r"$w^2=(1-4i)^2=1-8i+16i^2=1-8i-16=-15-8i$",
  truth=expand((1-4*I)**2), tag='العمليات على الأعداد المركبة (نص مشترك)'),
# 2023 #24: greatest principal Arg of the points on a circle |z - c| = r with |c| = 2r; options = multiples of pi/6
# (Arg of the centre, the half-angle alone, half-angle pi/3 from cos)
Q('m5q28', U4[3], 'hard',
  r"ما القيمة العظمى لسعة الأعداد المركّبة $z$ التي تحقّق المعادلة: $|z-2-2i\sqrt{3}|=2$ ؟",
  [O(r'\frac{\pi}{2}', P/2), O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{6}', P/6), O(r'\frac{2\pi}{3}', 2*P/3)],
  r"دائرة مركزها $(2,\,2\sqrt3)$ ونصف قطرها $2$ ، وبُعد المركز عن الأصل $4$ وسعته $\frac{\pi}{3}$" "\n"
  r"المماس من الأصل يصنع مع الخط الواصل إلى المركز زاوية $\alpha$: $\sin\alpha=\frac24=\frac12 \Rightarrow \alpha=\frac{\pi}{6}$ ، فالعظمى $\frac{\pi}{3}+\frac{\pi}{6}=\frac{\pi}{2}$",
  truth=lambda: max_arg5(2 + 2*math.sqrt(3)*1j, 2), tag='القيمة العظمى للسعة على محل هندسي'),
# E (expected: equation of a circle from its centre and a point on it), template 2023 #25 (equation in z of a locus);
# options = centre sign / radius vs r^2 / conjugate centre
Q('m5q29', U4[3], 'easy',
  r"معادلة الدائرة التي مركزها النقطة التي تُمثّل العدد $2-i$ ، وتمرّ بنقطة الأصل، هي:",
  [O(r'|z-2+i|=\sqrt{5}', Abs(X+I*Y-2+I)-sqrt(5), 'rel', sym={'z': X+I*Y}), O(r'|z+2-i|=\sqrt{5}', Abs(X+I*Y+2-I)-sqrt(5), 'rel', sym={'z': X+I*Y}),
   O(r'|z-2+i|=5', Abs(X+I*Y-2+I)-5, 'rel', sym={'z': X+I*Y}), O(r'|z-2-i|=\sqrt{5}', Abs(X+I*Y-2-I)-sqrt(5), 'rel', sym={'z': X+I*Y})],
  r"نصف القطر = بُعد المركز عن الأصل $=|2-i|=\sqrt5$ ، والمعادلة $|z-(2-i)|=\sqrt5$ أي $|z-2+i|=\sqrt5$",
  truth=Abs(X+I*Y-(2-I))-Abs(2-I), tag='كتابة معادلة محل هندسي'),
# 2025s #23: wedge from a point, one ray dashed, open vertex; options = vertex sign x which ray is strict
IndexQ('m5q30', U4[3], 'hard',
  r"متباينة المحل الهندسي (بدلالة $z$) التي تُمثِّل المنطقة المُظلَّلة في الشكل الآتي هي:",
  [T(r'$\frac{\pi}{4}\le\text{Arg}(z+2+i)<\frac{\pi}{2}$', R5_30),
   T(r'$\frac{\pi}{4}<\text{Arg}(z+2+i)\le\frac{\pi}{2}$', sector(V5, math.pi/4, math.pi/2, lo_open=True)),
   T(r'$\frac{\pi}{4}\le\text{Arg}(z-2-i)<\frac{\pi}{2}$', sector(2 + 1j, math.pi/4, math.pi/2, hi_open=True)),
   T(r'$\frac{\pi}{4}<\text{Arg}(z-2-i)\le\frac{\pi}{2}$', sector(2 + 1j, math.pi/4, math.pi/2, lo_open=True))],
  r"رأس المنطقة $(-2,-1)$ أي العدد $-2-i$ ، فنكتب $\text{Arg}\big(z-(-2-i)\big)=\text{Arg}(z+2+i)$" "\n"
  r"الشعاع المائل ($\frac{\pi}{4}$) متصل فيُشمل: $\frac{\pi}{4}\le$ ، والشعاع الرأسي ($\frac{\pi}{2}$) متقطّع فلا يُشمل: $<\frac{\pi}{2}$",
  truth=region_truth(R5_30, PR5_30, 4), figure=figure('m5q30', fig_region2(R5_30, PR5_30, 4), 3.4, 3.4), tag='منطقة في المستوى المركب من الشكل'),
]
