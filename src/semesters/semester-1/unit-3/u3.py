from qb import *

L = {i: f'u3-l{i}' for i in range(1, 6)}
meta = dict(id='u3', number=3, semester=1, title='التفاضل وتطبيقاته',
    description='مشتقات الاقترانات الأسية واللوغاريتمية والمثلثية وتطبيقاتها (المماس والعمودي والحركة)، مشتقتا الضرب والقسمة والمشتقات العليا، قاعدة السلسلة والمعادلات الوسيطية، الاشتقاق الضمني، والمعدلات المرتبطة.',
    lessons=[dict(id=L[1], title='مشتقة اقترانات خاصة'), dict(id=L[2], title='مشتقتا الضرب والقسمة والمشتقات العليا'),
             dict(id=L[3], title='قاعدة السلسلة'), dict(id=L[4], title='الاشتقاق الضمني'),
             dict(id=L[5], title='المُعدَّلات المرتبطة')])
R = Rational
P = pi
Dx = lambda f_: diff(f_, x)
def imp(eq, pt, order=1):
    return idiff(eq, y, x, order).subs({x: pt[0], y: pt[1]})
def tangent(f_, x0):
    return f_.subs(x, x0) + Dx(f_).subs(x, x0)*(x - x0)
def pw(points):
    """piecewise-linear function through points (as python callable + slope finder)"""
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

def draw_two(fpts, gpts, xmax, ymax, flabel=(None, None), glabel=(None, None)):
    def draw(fig, ax):
        axes_style(ax, (-0.6, xmax + 0.6), (-0.6, ymax + 0.8), grid=True)
        ax.set_xticks(range(0, xmax + 1)); ax.set_yticks(range(0, ymax + 1))
        fx, fy = zip(*fpts); gx, gy = zip(*gpts)
        ax.plot(fx, fy, color='#1f5fbf', lw=2)
        ax.plot(gx, gy, color='#d04a1a', lw=2)
        ax.text(*flabel, r'$f(x)$', color='#1f5fbf', fontsize=12)
        ax.text(*glabel, r'$g(x)$', color='#d04a1a', fontsize=12)
    return draw

# ============================================================== Exam 1
f_e1_8, fs_e1_8 = pw([(0, 5), (3, 2), (6, 5)])
g_e1_8, gs_e1_8 = pw([(0, 0), (2, 4), (6, 2)])
fig_e1_8 = figure('u3e1q8', draw_two([(0, 5), (3, 2), (6, 5)], [(0, 0), (2, 4), (6, 2)], 6, 5, (5.2, 4.3), (4.9, 2.6)))
E1 = [
Q('u3e1q1', L[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'3e^{x}-2\ln x+5^{x}', 3*exp(x)-2*log(x)+5**x)),
  [O(r'3e-2+5\ln 5', 3*E-2+5*log(5)), O(r'3e+2+5\ln 5', 3*E+2+5*log(5)), O(r'3e-2+5', 3*E-2+5), O(r'3e-2+\ln 5', 3*E-2+log(5))],
  r"$f'(x)=3e^x-\dfrac{2}{x}+5^x\ln5$ ، إذن $f'(1)=3e-2+5\ln5$",
  truth=Dx(3*exp(x)-2*log(x)+5**x).subs(x, 1)),
Q('u3e1q2', L[1], 'medium',
  F(r"معادلة العمودي على المماس لمنحنى الاقتران: $y=«0»$ عند $x=0$ هي:", (r'2\sin x+\cos x', 2*sin(x)+cos(x))),
  [O(r'y=-\frac{1}{2}x+1', -x/2+1, 'eq'), O(r'y=2x+1', 2*x+1, 'eq'), O(r'y=-2x+1', -2*x+1, 'eq'), O(r'y=\frac{1}{2}x+1', x/2+1, 'eq')],
  r"نقطة التماس: $y(0)=0+1=1$ ، أي $(0,\,1)$" "\n"
  r"$y'=2\cos x-\sin x \Rightarrow$ ميل المماس عند $x=0$ يساوي $2$ ، فميل العمودي $-\frac12$" "\n"
  r"$y-1=-\frac12(x-0) \Rightarrow y=-\frac12x+1$",
  truth=1 - x/Dx(2*sin(x)+cos(x)).subs(x, 0)),
Q('u3e1q3', L[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t>0$ الزمن بالثواني، و $s$ الموقع بالأمتار. الزمن الذي يكون عنده الجُسيم في حالة سكون لحظي هو:", (r't^{2}-6\ln t', t**2-6*log(t))),
  [O(r'\sqrt{3}', sqrt(3), units='s'), O('3', 3, units='s'), O(r'\sqrt{6}', sqrt(6), units='s'), O('6', 6, units='s')],
  r"$v(t)=s'(t)=2t-\dfrac{6}{t}$" "\n" r"$v(t)=0 \Rightarrow 2t^2=6 \Rightarrow t^2=3 \Rightarrow t=\sqrt3$ (لأن $t>0$)",
  truth=lambda: [r_ for r_ in solve(diff(t**2-6*log(t), t), t) if r_.is_positive][0]),
Q('u3e1q4', L[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'x^{2}e^{x}', x**2*exp(x))),
  [O('3e', 3*E), O('2e', 2*E), O('e', E), O(r'e^{2}', E**2)],
  r"بقاعدة مشتقة الضرب: $f'(x)=2xe^x+x^2e^x=e^x(x^2+2x)$ ، إذن $f'(1)=3e$",
  truth=Dx(x**2*exp(x)).subs(x, 1)),
Q('u3e1q5', L[2], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f''(x)-2f'(x)+f(x)$ يساوي:", (r'xe^{x}', x*exp(x))),
  [O('0', 0), O(r'e^{x}', exp(x)), O(r'xe^{x}', x*exp(x)), O(r'2e^{x}', 2*exp(x))],
  r"$f'(x)=e^x+xe^x=e^x(x+1)$ ، $f''(x)=e^x(x+1)+e^x=e^x(x+2)$" "\n"
  r"$f''-2f'+f=e^x\left[(x+2)-2(x+1)+x\right]=e^x(0)=0$",
  truth=diff(x*exp(x), x, 2)-2*Dx(x*exp(x))+x*exp(x)),
Q('u3e1q6', L[3], 'easy',
  F(r"إذا كان: $y=«0»$ ، حيث $0<x<\frac{\pi}{2}$ ، فإنّ $\dfrac{dy}{dx}$ تساوي:", (r'\ln(\cos x)', log(cos(x)))),
  [O(r'-\tan x', -tan(x)), O(r'\tan x', tan(x)), O(r'-\cot x', -cot(x)), O(r'\frac{1}{\cos x}', 1/cos(x))],
  r"بقاعدة السلسلة: $\dfrac{dy}{dx}=\dfrac{1}{\cos x}\cdot(-\sin x)=-\tan x$",
  truth=Dx(log(cos(x)))),
Q('u3e1q7', L[3], 'medium',
  F(r"إذا كان: $x=«0»$ ، $y=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\frac{\pi}{3}$ هي:", (r'3\sin t', 3*sin(t)), (r'2\cos t', 2*cos(t))),
  [O(r'-\frac{2\sqrt{3}}{3}', -2*sqrt(3)/3), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3), O(r'-\frac{\sqrt{3}}{2}', -sqrt(3)/2), O(r'-\frac{3\sqrt{3}}{2}', -3*sqrt(3)/2)],
  r"$\dfrac{dy}{dx}=\dfrac{dy/dt}{dx/dt}=\dfrac{-2\sin t}{3\cos t}=-\frac23\tan t$" "\n"
  r"عند $t=\frac{\pi}{3}$: $-\frac23\sqrt3=-\dfrac{2\sqrt3}{3}$",
  truth=(diff(2*cos(t), t)/diff(3*sin(t), t)).subs(t, pi/3)),
Q('u3e1q8', L[3], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $h(x)=f\big(g(x)\big)$ ، فإنّ $h'(1)$ تساوي:",
  [O('-2', -2), O('2', 2), O('-1', -1), O('4', 4)],
  r"بقاعدة السلسلة: $h'(1)=f'\big(g(1)\big)\cdot g'(1)$" "\n"
  r"من الشكل: $g(1)=2$ و $g'(1)=$ ميل القطعة من $(0,0)$ إلى $(2,4)$ $=2$" "\n"
  r"$f'(2)=$ ميل القطعة من $(0,5)$ إلى $(3,2)$ $=-1$ ، إذن $h'(1)=(-1)(2)=-2$",
  truth=lambda: fs_e1_8(g_e1_8(1))*gs_e1_8(1), figure=fig_e1_8),
Q('u3e1q9', L[4], 'easy',
  F(r"ميل المماس لمنحنى العلاقة: $«0»=11$ عند النقطة $(1,\,2)$ هو:", (r'x^{2}+3xy+y^{2}', x**2+3*x*y+y**2)),
  [O(r'-\frac{8}{7}', -R(8, 7)), O(r'\frac{8}{7}', R(8, 7)), O(r'-\frac{7}{8}', -R(7, 8)), O('-2', -2)],
  r"باشتقاق الطرفين ضمنيًّا: $2x+3y+3x\dfrac{dy}{dx}+2y\dfrac{dy}{dx}=0 \Rightarrow \dfrac{dy}{dx}=-\dfrac{2x+3y}{3x+2y}$" "\n"
  r"عند $(1,2)$: $\dfrac{dy}{dx}=-\dfrac{2+6}{3+4}=-\dfrac87$",
  truth=imp(x**2+3*x*y+y**2-11, (1, 2))),
Q('u3e1q10', L[4], 'hard',
  F(r"إذا مثّل المستقيم $l$ مماسًّا لمنحنى العلاقة: $«0»=10$ عند النقطة $(3,\,1)$ ، فإنّ المقطع $x$ للمستقيم $l$ هو:", (r'x^{2}y+y^{3}', x**2*y+y**3)),
  [O('5', 5), O(r'\frac{5}{2}', R(5, 2)), O('3', 3), O('1', 1)],
  r"باشتقاق الطرفين: $2xy+x^2y'+3y^2y'=0 \Rightarrow y'=\dfrac{-2xy}{x^2+3y^2}$ ، عند $(3,1)$: $y'=\dfrac{-6}{12}=-\dfrac12$" "\n"
  r"معادلة المماس: $y-1=-\frac12(x-3)$ ، وعند $y=0$: $-1=-\frac12(x-3) \Rightarrow x=5$",
  truth=lambda: solve(1 + imp(x**2*y+y**3-10, (3, 1))*(x-3), x)[0]),
Q('u3e1q11', L[5], 'medium',
  r"خزّان على شكل أسطوانة دائرية قائمة، طول قُطر قاعدتها $2\ \text{m}$. يُضَخّ إليه الماء بمعدّل $300\ \text{L/min}$ ، فإنّ معدّل ارتفاع الماء في الخزّان عند أيّ لحظة هو:",
  [O(r'\frac{3}{10\pi}', 3/(10*pi), units='m/min'), O(r'\frac{300}{\pi}', 300/pi, units='m/min'),
   O(r'\frac{3}{40\pi}', 3/(40*pi), units='m/min'), O(r'\frac{10}{3\pi}', 10/(3*pi), units='m/min')],
  r"نحوّل الوحدة: $300\ \text{L}=0.3\ \text{m}^3$ (لأن $1\ \text{m}^3=1000\ \text{L}$)" "\n"
  r"نصف القطر $r=1\ \text{m}$ ، $V=\pi r^2h=\pi h \Rightarrow \dfrac{dV}{dt}=\pi\dfrac{dh}{dt}$" "\n"
  r"$0.3=\pi\dfrac{dh}{dt} \Rightarrow \dfrac{dh}{dt}=\dfrac{0.3}{\pi}=\dfrac{3}{10\pi}\ \text{m/min}$",
  truth=R(3, 10)/(pi*1**2)),
Q('u3e1q12', L[5], 'medium',
  r"مربّع تزداد مساحته بمعدّل $24\ \text{cm}^2/\text{s}$. معدّل تغيّر محيطه في اللحظة التي يكون فيها طول ضلعه $6\ \text{cm}$ هو:",
  [O('8', 8, units='cm/s'), O('2', 2, units='cm/s'), O('4', 4, units='cm/s'), O('12', 12, units='cm/s')],
  r"$A=s^2 \Rightarrow \dfrac{dA}{dt}=2s\dfrac{ds}{dt} \Rightarrow 24=12\dfrac{ds}{dt} \Rightarrow \dfrac{ds}{dt}=2\ \text{cm/s}$" "\n"
  r"المحيط $P=4s \Rightarrow \dfrac{dP}{dt}=4\dfrac{ds}{dt}=8\ \text{cm/s}$",
  truth=4*R(24, 2*6)),
]

# ============================================================== Exam 2
E2 = [
Q('u3e2q1', L[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'\left(\frac{\pi}{4}\right)$ تساوي:", (r'4\tan x-3\sec x', 4*tan(x)-3*sec(x))),
  [O(r'8-3\sqrt{2}', 8-3*sqrt(2)), O(r'8+3\sqrt{2}', 8+3*sqrt(2)), O(r'4-3\sqrt{2}', 4-3*sqrt(2)), O(r'2-3\sqrt{2}', 2-3*sqrt(2))],
  r"$f'(x)=4\sec^2x-3\sec x\tan x$" "\n"
  r"$\sec\frac{\pi}{4}=\sqrt2$ ، $\tan\frac{\pi}{4}=1$ ، إذن $f'\left(\frac{\pi}{4}\right)=4(2)-3\sqrt2=8-3\sqrt2$",
  truth=Dx(4*tan(x)-3*sec(x)).subs(x, pi/4)),
Q('u3e2q2', L[1], 'hard',
  r"معادلة المماس لمنحنى الاقتران $y=e^{x}$ ، والمارّ بنقطة الأصل، هي:",
  [O(r'y=ex', E*x, 'eq'), O(r'y=x+1', x+1, 'eq'), O(r'y=ex-e', E*x-E, 'eq'), O(r'y=2x', 2*x, 'eq')],
  r"نفرض نقطة التماس $(a,\,e^a)$ ، فميل المماس $e^a$ ومعادلته: $y-e^a=e^a(x-a)$" "\n"
  r"يمر بالأصل: $0-e^a=e^a(0-a) \Rightarrow a=1$" "\n"
  r"إذن المماس: $y-e=e(x-1) \Rightarrow y=ex$",
  truth=lambda: (lambda a0: exp(a0) + exp(a0)*(x-a0))(solve(-exp(a) - exp(a)*(0-a), a)[0])),
Q('u3e2q3', L[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $0\le t\le2\pi$. الأزمنة التي تنعدم عندها سرعة الجُسيم هي:", (r'2\sin t+t', 2*sin(t)+t)),
  [O(r't=\frac{2\pi}{3},\ t=\frac{4\pi}{3}', FiniteSet(2*P/3, 4*P/3), 'set'), O(r't=\frac{\pi}{3},\ t=\frac{5\pi}{3}', FiniteSet(P/3, 5*P/3), 'set'),
   O(r't=\frac{5\pi}{6},\ t=\frac{7\pi}{6}', FiniteSet(5*P/6, 7*P/6), 'set'), O(r't=\frac{\pi}{2},\ t=\frac{3\pi}{2}', FiniteSet(P/2, 3*P/2), 'set')],
  r"$v(t)=2\cos t+1=0 \Rightarrow \cos t=-\frac12$" "\n" r"$t=\frac{2\pi}{3}$ أو $t=\frac{4\pi}{3}$",
  truth=lambda: numsols(2*cos(t)+1, 0, 2*pi, closed_hi=True)),
Q('u3e2q4', L[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ تساوي:", (r'\frac{x-1}{x+1}', (x-1)/(x+1))),
  [O(r'\frac{2}{(x+1)^{2}}', 2/(x+1)**2), O(r'-\frac{2}{(x+1)^{2}}', -2/(x+1)**2), O(r'\frac{1}{(x+1)^{2}}', 1/(x+1)**2), O(r'\frac{2x}{(x+1)^{2}}', 2*x/(x+1)**2)],
  r"بقاعدة مشتقة القسمة: $f'(x)=\dfrac{(1)(x+1)-(x-1)(1)}{(x+1)^2}=\dfrac{2}{(x+1)^2}$",
  truth=Dx((x-1)/(x+1))),
Q('u3e2q5', L[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ المشتقة الرابعة $f^{(4)}(x)$ تساوي:", (r'\ln x', log(x))),
  [O(r'-\frac{6}{x^{4}}', -6/x**4), O(r'\frac{6}{x^{4}}', 6/x**4), O(r'-\frac{24}{x^{5}}', -24/x**5), O(r'\frac{2}{x^{3}}', 2/x**3)],
  r"$f'(x)=\dfrac1x$ ، $f''(x)=-\dfrac{1}{x^2}$ ، $f'''(x)=\dfrac{2}{x^3}$ ، $f^{(4)}(x)=-\dfrac{6}{x^4}$",
  truth=diff(log(x), x, 4)),
Q('u3e2q6', L[3], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'(3x^{2}-1)^{4}', (3*x**2-1)**4)),
  [O('192', 192), O('32', 32), O('96', 96), O('384', 384)],
  r"$f'(x)=4(3x^2-1)^3\cdot6x$ ، إذن $f'(1)=4(2)^3(6)=192$",
  truth=Dx((3*x**2-1)**4).subs(x, 1)),
Q('u3e2q7', L[3], 'medium',
  F(r"يُمثّل الاقتران: $P(t)=«0»$ عدد أفراد مجتمع من الطيور بعد $t$ سنة. معدّل تغيّر عدد الطيور (طائر/سنة) عندما $t=0$ هو:", (r'\frac{500}{1+e^{-t}}', 500/(1+exp(-t)))),
  [O('125', 125), O('250', 250), O('-125', -125), O('500', 500)],
  r"$P(t)=500(1+e^{-t})^{-1} \Rightarrow P'(t)=-500(1+e^{-t})^{-2}\cdot(-e^{-t})=\dfrac{500e^{-t}}{(1+e^{-t})^2}$" "\n"
  r"$P'(0)=\dfrac{500(1)}{(2)^2}=125$ طائرًا في السنة",
  truth=diff(500/(1+exp(-t)), t).subs(t, 0)),
Q('u3e2q8', L[3], 'hard',
  F(r"إذا أُعطي منحنى بالمعادلتين الوسيطيتين: $x=«0»$ ، $y=«1»$ ، فإنّ النقاط على المنحنى التي يكون عندها المماس أفقيًّا هي:", (r't^{2}-1', t**2-1), (r't^{3}-3t', t**3-3*t)),
  [O(r'(0,-2),\ (0,2)', FiniteSet(Tuple(0, -2), Tuple(0, 2)), 'tset'), O(r'(0,2)', FiniteSet(Tuple(0, 2)), 'tset'),
   O(r'(-1,0),\ (3,2)', FiniteSet(Tuple(-1, 0), Tuple(3, 2)), 'tset'), O(r'(1,-2),\ (1,2)', FiniteSet(Tuple(1, -2), Tuple(1, 2)), 'tset')],
  r"المماس أفقي عندما $\dfrac{dy}{dt}=0$ و $\dfrac{dx}{dt}\ne0$: $3t^2-3=0 \Rightarrow t=\pm1$ ، و $\dfrac{dx}{dt}=2t\ne0$ عندهما" "\n"
  r"$t=1$: $(0,\,-2)$ ، $t=-1$: $(0,\,2)$",
  truth=lambda: FiniteSet(*[Tuple((t**2-1).subs(t, r_), (t**3-3*t).subs(t, r_)) for r_ in solve(diff(t**3-3*t, t), t) if diff(t**2-1, t).subs(t, r_) != 0])),
Q('u3e2q9', L[4], 'medium',
  F(r"إذا كان: $«0»=1$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(0,\,1)$ تساوي:", (r'x\sin y+y', x*sin(y)+y)),
  [O(r'-\sin 1', -sin(1)), O(r'\sin 1', sin(1)), O(r'-\cos 1', -cos(1)), O('-1', -1)],
  r"باشتقاق الطرفين: $\sin y+x\cos y\,\dfrac{dy}{dx}+\dfrac{dy}{dx}=0 \Rightarrow \dfrac{dy}{dx}=\dfrac{-\sin y}{x\cos y+1}$" "\n"
  r"عند $(0,1)$: $\dfrac{dy}{dx}=\dfrac{-\sin1}{0+1}=-\sin1$",
  truth=imp(x*sin(y)+y-1, (0, 1))),
Q('u3e2q10', L[4], 'hard',
  F(r"إذا كان: $«0»=8$ ، فإنّ $\dfrac{d^{2}y}{dx^{2}}$ عند النقطة $(2,\,1)$ تساوي:", (r'x^{2}+4y^{2}', x**2+4*y**2)),
  [O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2)), O(r'-\frac{1}{4}', -R(1, 4)), O('-2', -2)],
  r"$2x+8yy'=0 \Rightarrow y'=-\dfrac{x}{4y}$ ، وعند $(2,1)$: $y'=-\frac12$" "\n"
  r"$y''=-\dfrac{4y-x\cdot4y'}{16y^2}=-\dfrac{y-xy'}{4y^2}$ ، وعند $(2,1)$: $y''=-\dfrac{1-2\left(-\frac12\right)}{4}=-\dfrac{2}{4}=-\dfrac12$",
  truth=imp(x**2+4*y**2-8, (2, 1), 2)),
Q('u3e2q11', L[5], 'easy',
  r"تزداد مساحة دائرة بمعدّل $10\pi\ \text{cm}^2/\text{s}$. معدّل تزايد نصف قطرها عندما يكون نصف قطرها $5\ \text{cm}$ هو:",
  [O('1', 1, units='cm/s'), O('2', 2, units='cm/s'), O('5', 5, units='cm/s'), O('10', 10, units='cm/s')],
  r"$A=\pi r^2 \Rightarrow \dfrac{dA}{dt}=2\pi r\dfrac{dr}{dt} \Rightarrow 10\pi=2\pi(5)\dfrac{dr}{dt} \Rightarrow \dfrac{dr}{dt}=1\ \text{cm/s}$",
  truth=10*pi/(2*pi*5)),
Q('u3e2q12', L[5], 'hard',
  r"سُلّم طوله $5\ \text{m}$ يستند طرفه العلوي إلى جدار رأسي وطرفه السفلي على أرض أفقية. إذا انزلق طرفه العلوي إلى الأسفل بمعدّل $0.6\ \text{m/s}$ ، فإنّ معدّل ابتعاد طرفه السفلي عن الجدار عندما يكون طرفه العلوي على ارتفاع $4\ \text{m}$ هو:",
  [D('0.8', 'm/s'), D('0.45', 'm/s'), D('0.6', 'm/s'), D('1.2', 'm/s')],
  r"$x^2+y^2=25$ ، وعند $y=4$: $x=3$" "\n"
  r"$2x\dfrac{dx}{dt}+2y\dfrac{dy}{dt}=0 \Rightarrow 3\dfrac{dx}{dt}+4(-0.6)=0 \Rightarrow \dfrac{dx}{dt}=0.8\ \text{m/s}$",
  truth=-4*R(-6, 10)/3),
]

# ============================================================== Exam 3
E3 = [
Q('u3e3q1', L[1], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(0)$ تساوي:", (r'x^{3}+2^{x}', x**3+2**x)),
  [O(r'\ln 2', log(2)), O('1', 1), O('0', 0), O('2', 2)],
  r"$f'(x)=3x^2+2^x\ln2$ ، إذن $f'(0)=0+1\cdot\ln2=\ln2$",
  truth=Dx(x**3+2**x).subs(x, 0)),
Q('u3e3q2', L[1], 'medium',
  F(r"إذا كان المماس لمنحنى الاقتران: $y=«0»$ عند $x=2$ يوازي المستقيم $y=3x$ ، فإنّ قيمة الثابت $a$ هي:", (r'a\ln x', a*log(x))),
  [O('6', 6), O(r'\frac{3}{2}', R(3, 2)), O('3', 3), O('2', 2)],
  r"$y'=\dfrac{a}{x}$ ، والمماس يوازي المستقيم إذا تساوى الميلان: $\dfrac{a}{2}=3 \Rightarrow a=6$",
  truth=lambda: solve(Dx(a*log(x)).subs(x, 2)-3, a)[0]),
Q('u3e3q3', L[1], 'hard',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t\ge0$ بالثواني و $s$ بالأمتار. تسارع الجُسيم عندما تنعدم سرعته هو:", (r'e^{t}-6t', exp(t)-6*t)),
  [O('6', 6, units='m/s^2'), O('0', 0, units='m/s^2'), O(r'\ln 6', log(6), units='m/s^2'), O(r'e^{6}', exp(6), units='m/s^2')],
  r"$v(t)=e^t-6=0 \Rightarrow t=\ln6$" "\n" r"$a(t)=e^t \Rightarrow a(\ln6)=e^{\ln6}=6\ \text{m/s}^2$",
  truth=lambda: (exp(t)).subs(t, solve(exp(t)-6, t)[0])),
Q('u3e3q4', L[2], 'medium',
  r"إذا كان: $f(2)=3,\ f'(2)=-1,\ g(2)=4,\ g'(2)=2$ ، فإنّ $\left(\dfrac{f}{g}\right)'(2)$ تساوي:",
  [O(r'-\frac{5}{8}', -R(5, 8)), O(r'\frac{5}{8}', R(5, 8)), O(r'-\frac{1}{8}', -R(1, 8)), O(r'-\frac{1}{2}', -R(1, 2))],
  r"$\left(\dfrac{f}{g}\right)'(2)=\dfrac{f'(2)g(2)-f(2)g'(2)}{\big(g(2)\big)^2}=\dfrac{(-1)(4)-(3)(2)}{16}=\dfrac{-10}{16}=-\dfrac58$",
  truth=R(-1*4 - 3*2, 16)),
Q('u3e3q5', L[2], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، وكان $f'(0)=3$ ، فإنّ قيمة الثابت $b$ هي:", (r'(x+b)e^{x}', (x+b)*exp(x))),
  [O('2', 2), O('3', 3), O('1', 1), O('-2', -2)],
  r"$f'(x)=e^x+(x+b)e^x$ ، إذن $f'(0)=1+b=3 \Rightarrow b=2$",
  truth=lambda: solve(Dx((x+b)*exp(x)).subs(x, 0)-3, b)[0]),
Q('u3e3q6', L[3], 'easy',
  F(r"إذا كان: $y=«0»$ ، فإنّ $\dfrac{dy}{dx}$ تساوي:", (r'\sec 3x', sec(3*x))),
  [O(r'3\sec 3x\tan 3x', 3*sec(3*x)*tan(3*x)), O(r'\sec 3x\tan 3x', sec(3*x)*tan(3*x)), O(r'3\sec^{2}3x', 3*sec(3*x)**2), O(r'3\tan^{2}3x', 3*tan(3*x)**2)],
  r"بقاعدة السلسلة: $\dfrac{dy}{dx}=\sec3x\tan3x\cdot3=3\sec3x\tan3x$",
  truth=Dx(sec(3*x))),
Q('u3e3q7', L[3], 'medium',
  r"إذا كان $h(x)=\sqrt{f(x)}$ ، وكان $f(1)=4$ و $f'(1)=6$ ، فإنّ $h'(1)$ تساوي:",
  [O(r'\frac{3}{2}', R(3, 2)), O('3', 3), O(r'\frac{1}{2}', R(1, 2)), O('6', 6)],
  r"$h'(x)=\dfrac{f'(x)}{2\sqrt{f(x)}} \Rightarrow h'(1)=\dfrac{6}{2\sqrt4}=\dfrac64=\dfrac32$",
  truth=R(6, 2*2)),
Q('u3e3q8', L[3], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(2)$ تساوي:", (r'\log_{2}(x^{2}+4)', log(x**2+4, 2))),
  [O(r'\frac{1}{\ln 4}', 1/log(4)), O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{1}{\ln 2}', 1/log(2)), O(r'\frac{2}{\ln 2}', 2/log(2))],
  r"$f'(x)=\dfrac{2x}{(x^2+4)\ln2}$ ، إذن $f'(2)=\dfrac{4}{8\ln2}=\dfrac{1}{2\ln2}=\dfrac{1}{\ln4}$",
  truth=Dx(log(x**2+4, 2)).subs(x, 2)),
Q('u3e3q9', L[4], 'easy',
  F(r"إذا كان: $«0»=3$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(2,\,1)$ تساوي:", (r'y^{3}+xy', y**3+x*y)),
  [O(r'-\frac{1}{5}', -R(1, 5)), O(r'\frac{1}{5}', R(1, 5)), O(r'-\frac{1}{3}', -R(1, 3)), O('-1', -1)],
  r"باشتقاق الطرفين: $3y^2y'+y+xy'=0 \Rightarrow y'=\dfrac{-y}{3y^2+x}$" "\n" r"عند $(2,1)$: $y'=\dfrac{-1}{3+2}=-\dfrac15$",
  truth=imp(y**3+x*y-3, (2, 1))),
Q('u3e3q10', L[4], 'hard',
  F(r"إذا كان: $x=«0»$ ، $y=«1»$ ، فإنّ $\dfrac{d^{2}y}{dx^{2}}$ عندما $t=0$ تساوي:", (r'e^{t}', exp(t)), (r't^{2}', t**2)),
  [O('2', 2), O('0', 0), O('-2', -2), O('1', 1)],
  r"$\dfrac{dy}{dx}=\dfrac{2t}{e^t}=2te^{-t}$" "\n"
  r"$\dfrac{d^2y}{dx^2}=\dfrac{\frac{d}{dt}\left(2te^{-t}\right)}{dx/dt}=\dfrac{2e^{-t}-2te^{-t}}{e^t}$ ، وعند $t=0$: $\dfrac{2-0}{1}=2$",
  truth=(diff(diff(t**2, t)/diff(exp(t), t), t)/diff(exp(t), t)).subs(t, 0)),
Q('u3e3q11', L[5], 'medium',
  r"يتمدّد مكعّب بحيث يزداد حجمه بمعدّل $36\ \text{cm}^3/\text{s}$. معدّل تزايد مساحة سطحه الكلية عندما يكون طول حرفه $2\ \text{cm}$ هو:",
  [O('72', 72, units='cm^2/s'), O('36', 36, units='cm^2/s'), O('24', 24, units='cm^2/s'), O('144', 144, units='cm^2/s')],
  r"$V=s^3 \Rightarrow 36=3(2)^2\dfrac{ds}{dt} \Rightarrow \dfrac{ds}{dt}=3\ \text{cm/s}$" "\n"
  r"$A=6s^2 \Rightarrow \dfrac{dA}{dt}=12s\dfrac{ds}{dt}=12(2)(3)=72\ \text{cm}^2/\text{s}$",
  truth=12*2*R(36, 3*4)),
Q('u3e3q12', L[5], 'hard',
  r"رجل طوله $1.8\ \text{m}$ يسير مبتعدًا عن عمود إنارة ارتفاعه $6\ \text{m}$ بسرعة $1.4\ \text{m/s}$. معدّل تغيّر طول ظلّه هو:",
  [D('0.6', 'm/s'), D('1.4', 'm/s'), D('2', 'm/s'), D('0.42', 'm/s')],
  r"نفرض $x$ بُعد الرجل عن العمود، و $s$ طول ظله. من تشابه المثلثين: $\dfrac{s}{1.8}=\dfrac{x+s}{6}$" "\n"
  r"$6s=1.8x+1.8s \Rightarrow 4.2s=1.8x \Rightarrow s=\dfrac37x$" "\n"
  r"$\dfrac{ds}{dt}=\dfrac37\cdot\dfrac{dx}{dt}=\dfrac37(1.4)=0.6\ \text{m/s}$",
  truth=lambda: (lambda s0: s0.coeff(x))(solve(Eq(s/R(18, 10), (x+s)/6), s)[0])*R(14, 10)),
]

# ============================================================== Exam 4
f_e4_5, fs_e4_5 = pw([(0, 6), (4, 2), (8, 4)])
g_e4_5, gs_e4_5 = pw([(0, 1), (6, 4), (8, 0)])
fig_e4_5 = figure('u3e4q5', draw_two([(0, 6), (4, 2), (8, 4)], [(0, 1), (6, 4), (8, 0)], 8, 6, (0.3, 6.2), (6.3, 4.2)))
E4 = [
Q('u3e4q1', L[1], 'easy',
  r"إذا كان: $f(x)=7\log x$ ، حيث $\log$ هو اللوغاريتم للأساس $10$ ، فإنّ $f'(x)$ تساوي:",
  [O(r'\frac{7}{x\ln 10}', 7/(x*log(10))), O(r'\frac{7}{x}', 7/x), O(r'\frac{7\ln 10}{x}', 7*log(10)/x), O(r'\frac{7}{10x}', 7/(10*x))],
  r"$\dfrac{d}{dx}\log_ax=\dfrac{1}{x\ln a}$ ، إذن $f'(x)=\dfrac{7}{x\ln10}$",
  truth=Dx(7*log(x, 10))),
Q('u3e4q2', L[1], 'medium',
  F(r"يتحرّك جُسيم في مسار مستقيم، ويُعطى موقعه بالاقتران: $s(t)=«0»$ ، حيث $t$ بالثواني و $s$ بالأمتار. تسارع الجُسيم عندما $t=\frac{\pi}{2}$ هو:", (r'3\cos t+4\sin t', 3*cos(t)+4*sin(t))),
  [O('-4', -4, units='m/s^2'), O('4', 4, units='m/s^2'), O('-3', -3, units='m/s^2'), O('3', 3, units='m/s^2')],
  r"$v(t)=-3\sin t+4\cos t$ ، $a(t)=-3\cos t-4\sin t$" "\n" r"$a\left(\frac{\pi}{2}\right)=0-4=-4\ \text{m/s}^2$",
  truth=diff(3*cos(t)+4*sin(t), t, 2).subs(t, pi/2)),
Q('u3e4q3', L[1], 'medium',
  F(r"النقطة على منحنى الاقتران: $y=«0»$ التي يكون عندها المماس أفقيًّا هي:", (r'e^{x}-2x', exp(x)-2*x)),
  [O(r'(\ln 2,\ 2-2\ln 2)', Tuple(log(2), 2-2*log(2)), 'tuple'), O(r'(\ln 2,\ 2+2\ln 2)', Tuple(log(2), 2+2*log(2)), 'tuple'),
   O(r'(2,\ e^{2}-4)', Tuple(2, exp(2)-4), 'tuple'), O(r'(0,\ 1)', Tuple(0, 1), 'tuple')],
  r"$y'=e^x-2=0 \Rightarrow x=\ln2$" "\n" r"$y(\ln2)=e^{\ln2}-2\ln2=2-2\ln2$",
  truth=lambda: (lambda r_: Tuple(r_, exp(r_)-2*r_))(solve(exp(x)-2, x)[0])),
Q('u3e4q4', L[2], 'easy',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ تساوي:", (r'x\ln x-x', x*log(x)-x)),
  [O(r'\ln x', log(x)), O(r'\ln x-1', log(x)-1), O(r'\frac{1}{x}', 1/x), O(r'x\ln x', x*log(x))],
  r"$f'(x)=\left(1\cdot\ln x+x\cdot\dfrac1x\right)-1=\ln x+1-1=\ln x$",
  truth=Dx(x*log(x)-x)),
Q('u3e4q5', L[2], 'medium',
  r"يُبيّن الشكل الآتي منحنيي الاقترانين $f(x)$ و $g(x)$. إذا كان: $q(x)=\dfrac{f(x)}{g(x)}$ ، فإنّ $q'(2)$ تساوي:",
  [O('-1', -1), O('1', 1), O(r'-\frac{1}{2}', -R(1, 2)), O('0', 0)],
  r"من الشكل: $f(2)=4$ ، $f'(2)=$ ميل القطعة من $(0,6)$ إلى $(4,2)$ $=-1$" "\n"
  r"$g(2)=2$ ، $g'(2)=$ ميل القطعة من $(0,1)$ إلى $(6,4)$ $=\frac12$" "\n"
  r"$q'(2)=\dfrac{f'(2)g(2)-f(2)g'(2)}{\big(g(2)\big)^2}=\dfrac{(-1)(2)-(4)\left(\frac12\right)}{4}=\dfrac{-4}{4}=-1$",
  truth=lambda: (fs_e4_5(2)*g_e4_5(2) - f_e4_5(2)*gs_e4_5(2))/g_e4_5(2)**2, figure=fig_e4_5),
Q('u3e4q6', L[3], 'medium',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(x)$ تساوي:", (r'\sin^{2}(3x)', sin(3*x)**2)),
  [O(r'3\sin 6x', 3*sin(6*x)), O(r'6\sin 3x', 6*sin(3*x)), O(r'2\sin 3x', 2*sin(3*x)), O(r'6\sin 6x', 6*sin(6*x))],
  r"$f'(x)=2\sin3x\cdot\cos3x\cdot3=3(2\sin3x\cos3x)=3\sin6x$",
  truth=Dx(sin(3*x)**2)),
Q('u3e4q7', L[3], 'hard',
  F(r"إذا كان: $f(x)=«0»$ ، فإنّ $f'(1)$ تساوي:", (r'e^{x^{2}}\ln x', exp(x**2)*log(x))),
  [O('e', E), O('2e', 2*E), O('0', 0), O('1', 1)],
  r"$f'(x)=2xe^{x^2}\ln x+e^{x^2}\cdot\dfrac1x$" "\n" r"$f'(1)=2e(0)+e(1)=e$",
  truth=Dx(exp(x**2)*log(x)).subs(x, 1)),
Q('u3e4q8', L[3], 'medium',
  F(r"إذا كان: $x=«0»$ ، $y=«1»$ ، فإنّ $\dfrac{dy}{dx}$ عندما $t=\frac{\pi}{8}$ تساوي:", (r'1+\cos 2t', 1+cos(2*t)), (r'\sin 2t', sin(2*t))),
  [O('-1', -1), O('1', 1), O(r'-\sqrt{2}', -sqrt(2)), O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2)],
  r"$\dfrac{dy}{dx}=\dfrac{2\cos2t}{-2\sin2t}=-\cot2t$" "\n" r"عند $t=\frac{\pi}{8}$: $-\cot\frac{\pi}{4}=-1$",
  truth=(diff(sin(2*t), t)/diff(1+cos(2*t), t)).subs(t, pi/8)),
Q('u3e4q9', L[4], 'medium',
  F(r"إذا كان: $«0»=2$ ، فإنّ $\dfrac{dy}{dx}$ عند النقطة $(1,\,1)$ تساوي:", (r'2^{x}y+\ln y', 2**x*y+log(y))),
  [O(r'-\frac{2\ln 2}{3}', -2*log(2)/3), O(r'\frac{2\ln 2}{3}', 2*log(2)/3), O(r'-\frac{\ln 2}{3}', -log(2)/3), O(r'-\frac{2}{3}', -R(2, 3))],
  r"باشتقاق الطرفين: $2^x\ln2\cdot y+2^xy'+\dfrac{y'}{y}=0$" "\n"
  r"عند $(1,1)$: $2\ln2+2y'+y'=0 \Rightarrow y'=-\dfrac{2\ln2}{3}$",
  truth=imp(2**x*y+log(y)-2, (1, 1))),
Q('u3e4q10', L[4], 'hard',
  F(r"المماس لمنحنى العلاقة: $«0»=25$ عند النقطة $(3,\,4)$ يقطع محور $x$ عند النقطة التي إحداثيها $x$ يساوي:", (r'x^{2}+y^{2}', x**2+y**2)),
  [O(r'\frac{25}{3}', R(25, 3)), O('3', 3), O(r'\frac{16}{3}', R(16, 3)), O(r'\frac{25}{4}', R(25, 4))],
  r"$2x+2yy'=0 \Rightarrow y'=-\dfrac{x}{y}=-\dfrac34$ عند $(3,4)$" "\n"
  r"المماس: $y-4=-\frac34(x-3)$ ، وعند $y=0$: $x-3=\frac{16}{3} \Rightarrow x=\frac{25}{3}$",
  truth=lambda: solve(4 + imp(x**2+y**2-25, (3, 4))*(x-3), x)[0]),
Q('u3e4q11', L[5], 'medium',
  r"خزّان على شكل مخروط دائري قائم رأسه إلى الأسفل، ارتفاعه $10\ \text{m}$ ونصف قطر قاعدته $5\ \text{m}$. يتسرّب منه الماء فينخفض مستوى الماء بمعدّل $0.2\ \text{m/min}$. معدّل تناقص حجم الماء عندما يكون عمقه $4\ \text{m}$ هو:",
  [O(r'0.8\pi', R(8, 10)*pi, units='m^3/min'), O(r'3.2\pi', R(32, 10)*pi, units='m^3/min'), O(r'0.2\pi', R(2, 10)*pi, units='m^3/min'), O(r'1.6\pi', R(16, 10)*pi, units='m^3/min')],
  r"من تشابه المثلثات: $\dfrac{r}{h}=\dfrac{5}{10} \Rightarrow r=\dfrac{h}{2}$ ، و $V=\frac13\pi r^2h=\dfrac{\pi h^3}{12}$" "\n"
  r"$\dfrac{dV}{dt}=\dfrac{\pi h^2}{4}\cdot\dfrac{dh}{dt}=\dfrac{16\pi}{4}(-0.2)=-0.8\pi$ ، أي يتناقص الحجم بمعدّل $0.8\pi\ \text{m}^3/\text{min}$",
  truth=-(pi*16/4)*R(-2, 10)),
Q('u3e4q12', L[5], 'hard',
  r"انطلقت سيارتان في اللحظة نفسها من النقطة نفسها، الأولى نحو الشرق بسرعة $60\ \text{km/h}$ ، والثانية نحو الشمال بسرعة $80\ \text{km/h}$. معدّل تزايد المسافة بينهما بعد ساعتين من انطلاقهما هو:",
  [O('100', 100, units='km/h'), O('140', 140, units='km/h'), O('20', 20, units='km/h'), O('70', 70, units='km/h')],
  r"بعد ساعتين: $x=120$ ، $y=160$ ، والمسافة $D=\sqrt{120^2+160^2}=200$" "\n"
  r"$D^2=x^2+y^2 \Rightarrow D\dfrac{dD}{dt}=x\dfrac{dx}{dt}+y\dfrac{dy}{dt}$" "\n"
  r"$200\dfrac{dD}{dt}=120(60)+160(80)=20000 \Rightarrow \dfrac{dD}{dt}=100\ \text{km/h}$",
  truth=(120*60+160*80)/sqrt(120**2+160**2)),
]

exams = [dict(id=f'u3-e{i+1}', title=tt, questions=qq) for i, (tt, qq) in enumerate(
    [('الاختبار الأول', E1), ('الاختبار الثاني', E2), ('الاختبار الثالث', E3), ('الاختبار الرابع', E4)])]
build(meta, exams, 'u3')
