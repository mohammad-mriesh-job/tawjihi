from qb import *
import math

L1, L2, L3 = 'u4-l1', 'u4-l2', 'u4-l3'
meta = dict(id='u4', number=4, semester=1, title='الأعداد المُركَّبة',
    description='الوحدة التخيلية والصورة القياسية، المرافق والمقياس والسعة والصورة المثلثية، العمليات على الأعداد المركبة والجذور التربيعية وحل المعادلات، والمحل الهندسي في المستوى المركب.',
    lessons=[dict(id=L1, title='الأعداد المُركَّبة'), dict(id=L2, title='العمليات على الأعداد المُركَّبة'),
             dict(id=L3, title='المحل الهندسي في المستوى المُركَّب')])
R = Rational
P = pi
X, Y = symbols('X Y', real=True)
NOTE = r"(حيث $i=\sqrt{-1}$ ، و $\text{Arg}$ السعة الرئيسة: $-\pi<\text{Arg}(z)\le\pi$)"
pol = lambda r_, th_: r_*(cos(th_) + I*sin(th_))
def trig(r_tex, th_tex):
    return rf'{r_tex}\left(\cos({th_tex})+i\sin({th_tex})\right)'
def croots(poly):
    return FiniteSet(*[nsimplify(expand(r_)) for r_ in solve(poly, z)])
def circ(c_, r_):
    return T(rf'دائرة مركزها $({latex(re(c_))},\,{latex(im(c_))})$ ونصف قطرها ${latex(r_)}$', Tuple(re(c_), im(c_), r_))
def eqline(expr_x_y):
    """|z-a|=|z-b| as y = f(x): expand both squared moduli"""
    return expr_x_y

def complex_axes(ax, lim):
    axes_style(ax, (-lim, lim), (-lim, lim), xlabel=r'\mathrm{Re}', ylabel=r'\mathrm{Im}', grid=True)
    ax.set_aspect('equal')
    ax.set_xticks(range(-lim + 1, lim)); ax.set_yticks(range(-lim + 1, lim))
    ax.tick_params(labelsize=8)

def fig_quarter(fig, ax):
    import numpy as np
    complex_axes(ax, 5)
    c0 = (1, 1)
    th_ = np.linspace(0, np.pi/2, 80)
    xs = np.concatenate([[c0[0]], c0[0] + 2*np.cos(th_), [c0[0]]]); ys = np.concatenate([[c0[1]], c0[1] + 2*np.sin(th_), [c0[1]]])
    ax.fill(xs, ys, color='#9cc3ef', alpha=0.7)
    ax.plot(c0[0] + 2*np.cos(th_), c0[1] + 2*np.sin(th_), color='#1f5fbf', lw=1.8)
    ax.plot([1, 3], [1, 1], color='#1f5fbf', lw=1.8); ax.plot([1, 1], [1, 3], color='#1f5fbf', lw=1.8)
    ax.plot(*c0, 'o', color='#1f5fbf', ms=4)

def fig_sector(fig, ax):
    import numpy as np
    complex_axes(ax, 5)
    th_ = np.linspace(np.pi/6, np.pi/2, 80)
    xs = np.concatenate([[0], 4*np.cos(th_), [0]]); ys = np.concatenate([[0], 4*np.sin(th_), [0]])
    ax.fill(xs, ys, color='#9cc3ef', alpha=0.7)
    ax.plot(4*np.cos(th_), 4*np.sin(th_), color='#1f5fbf', lw=1.8)
    ax.plot([0, 4*np.cos(np.pi/6)], [0, 4*np.sin(np.pi/6)], color='#1f5fbf', lw=1.8)
    ax.plot([0, 0], [0, 4], color='#1f5fbf', lw=1.8)
    ax.plot(0, 0, 'o', mfc='white', mec='#1f5fbf', ms=5)

def fig_half(fig, ax):
    import numpy as np
    complex_axes(ax, 6)
    # points A(0,2) and B(4,0); bisector: 2y = 4x - ... : |z-2i| = |z-4| -> x^2+(y-2)^2=(x-4)^2+y^2 -> y = 2x - 3
    xs = np.linspace(-6, 6, 10)
    ax.fill_between(xs, 2*xs - 3, 6.5, color='#9cc3ef', alpha=0.7)
    ax.plot(xs, 2*xs - 3, '--', color='#1f5fbf', lw=1.8)
    ax.plot(0, 2, 'x', color='#d04a1a', ms=7); ax.text(-1.6, 2.2, r'$2i$', color='#d04a1a')
    ax.plot(4, 0, 'x', color='#d04a1a', ms=7); ax.text(4.1, -0.9, r'$4$', color='#d04a1a')
    ax.set_ylim(-6, 6)

# ============================================================== Exam 1
z1, w1 = 3 + 2*I, -1 + 4*I
E1 = [
Q('u4e1q1', L1, 'easy',
  r"قيمة المقدار: $i^{18}+i^{21}$ هي: " + r"(حيث $i=\sqrt{-1}$)",
  [O('-1+i', -1+I), O('1-i', 1-I), O('-1-i', -1-I), O('1+i', 1+I)],
  r"$18=4(4)+2 \Rightarrow i^{18}=i^2=-1$ ، و $21=4(5)+1 \Rightarrow i^{21}=i$" "\n" r"إذن المجموع $-1+i$",
  truth=I**18+I**21),
Q('u4e1q2', L1, 'medium',
  r"إذا كان: $z=a-2i$ ، حيث $a<0$ ، وكان $|z|=4$ ، فإنّ الصورة المثلثية للعدد $z$ هي: " + NOTE,
  [O(trig('4', r'-\frac{5\pi}{6}'), pol(4, -5*P/6)), O(trig('4', r'\frac{5\pi}{6}'), pol(4, 5*P/6)),
   O(trig('4', r'-\frac{\pi}{6}'), pol(4, -P/6)), O(trig('4', r'-\frac{2\pi}{3}'), pol(4, -2*P/3))],
  r"$\sqrt{a^2+4}=4 \Rightarrow a^2=12 \Rightarrow a=-2\sqrt3$ (لأن $a<0$)" "\n"
  r"$z=-2\sqrt3-2i$ يقع في الربع الثالث، وزاوية الإسناد $\tan^{-1}\left(\frac{2}{2\sqrt3}\right)=\frac{\pi}{6}$" "\n"
  r"إذن $\text{Arg}(z)=-\pi+\frac{\pi}{6}=-\frac{5\pi}{6}$ ، و $z=4\left(\cos\left(-\frac{5\pi}{6}\right)+i\sin\left(-\frac{5\pi}{6}\right)\right)$",
  truth=lambda: (lambda a0: a0 - 2*I)([r_ for r_ in solve(a**2+4-16, a) if r_ < 0][0])),
Q('u4e1q3', L1, 'easy',
  r"إذا كان: $z=2-3i$ ، فإنّ قيمة $z\bar{z}+\text{Re}(z)$ هي:",
  [O('15', 15), O('11', 11), O('13', 13), O('17', 17)],
  r"$z\bar z=|z|^2=4+9=13$ ، و $\text{Re}(z)=2$ ، إذن المقدار $=15$",
  truth=expand((2-3*I)*(2+3*I))+2),
Q('u4e1q4', L1, 'hard',
  r"إذا كان: $z=\dfrac{b+4i}{1+bi}$ ، فإنّ القيمتين المُمكنتين للثابت الحقيقي $b$ اللّتين تجعلان $z$ عددًا حقيقيًّا هما: " + r"(حيث $i=\sqrt{-1}$)",
  [O(r'\pm 2', FiniteSet(2, -2), 'set'), O(r'\pm 4', FiniteSet(4, -4), 'set'), O(r'\pm 1', FiniteSet(1, -1), 'set'), O(r'\pm\sqrt{2}', FiniteSet(sqrt(2), -sqrt(2)), 'set')],
  r"نضرب في مرافق المقام: $z=\dfrac{(b+4i)(1-bi)}{1+b^2}=\dfrac{b-b^2i+4i+4b}{1+b^2}=\dfrac{5b+(4-b^2)i}{1+b^2}$" "\n"
  r"يكون $z$ حقيقيًّا إذا انعدم الجزء التخيلي: $4-b^2=0 \Rightarrow b=\pm2$",
  truth=lambda: FiniteSet(*solve(im(expand((X+4*I)*(1-X*I))), X))),
Q('u4e1q5', L2, 'easy',
  r"إذا كان: $z=3+2i$ ، $w=-1+4i$ ، فإنّ ناتج $z-iw$ هو:",
  [O('7+3i', 7+3*I), O('-1+3i', -1+3*I), O('7+i', 7+I), O('-1+i', -1+I)],
  r"$iw=i(-1+4i)=-i+4i^2=-4-i$" "\n" r"$z-iw=(3+2i)-(-4-i)=7+3i$",
  truth=expand(z1 - I*w1)),
Q('u4e1q6', L2, 'easy',
  r"إذا كان: $z=3+2i$ ، $w=-1+4i$ ، فإنّ ناتج $zw$ هو:",
  [O('-11+10i', -11+10*I), O('5+10i', 5+10*I), O('-11+14i', -11+14*I), O('5-10i', 5-10*I)],
  r"$zw=(3+2i)(-1+4i)=-3+12i-2i+8i^2=-3+10i-8=-11+10i$",
  truth=expand(z1*w1)),
Q('u4e1q7', L2, 'medium',
  r"المعادلة التربيعية ذات المعاملات الحقيقية التي أحد جذريها العدد المركب $(2+3i)$ هي:",
  [O('x^{2}-4x+13=0', x**2-4*x+13, 'rel'), O('x^{2}+4x+13=0', x**2+4*x+13, 'rel'),
   O('x^{2}-4x+5=0', x**2-4*x+5, 'rel'), O('x^{2}+4x-13=0', x**2+4*x-13, 'rel')],
  r"المعاملات حقيقية، فالجذر الآخر هو المرافق $2-3i$" "\n"
  r"مجموع الجذرين $=4$ ، وحاصل ضربهما $=(2+3i)(2-3i)=4+9=13$" "\n"
  r"المعادلة على الصورة $x^2-Sx+P=0$ ، حيث $S$ مجموع الجذرين و $P$ حاصل ضربهما: $x^2-4x+13=0$",
  truth=expand((x-(2+3*I))*(x-(2-3*I)))),
Q('u4e1q8', L2, 'medium',
  r"إذا كان: $z=6\left(\cos\frac{5\pi}{6}+i\sin\frac{5\pi}{6}\right)$ ، $w=2\left(\cos\left(-\frac{\pi}{6}\right)+i\sin\left(-\frac{\pi}{6}\right)\right)$ ، فإنّ الصورة القياسية لناتج $\dfrac{z}{w}$ هي:",
  [O('-3', -3), O('3', 3), O('3i', 3*I), O('-3i', -3*I)],
  r"عند القسمة نقسم المقاييس ونطرح السعات: $\dfrac{z}{w}=3\left(\cos\left(\frac{5\pi}{6}+\frac{\pi}{6}\right)+i\sin\left(\frac{5\pi}{6}+\frac{\pi}{6}\right)\right)$" "\n"
  r"$=3(\cos\pi+i\sin\pi)=3(-1+0)=-3$",
  truth=pol(6, 5*P/6)/pol(2, -P/6)),
Q('u4e1q9', L3, 'easy',
  r"المحل الهندسي للنقاط التي تُمثّل العدد المركب $z$ الذي يُحقّق المعادلة $|z+2-i|=3$ هو:",
  [circ(-2+I, 3), circ(2-I, 3), circ(-2+I, 9), circ(-2-I, 3)],
  r"نكتب المعادلة على الصورة $|z-z_1|=r$: $|z-(-2+i)|=3$" "\n"
  r"فهي دائرة مركزها النقطة التي تُمثّل العدد $-2+i$ أي $(-2,\,1)$ ، ونصف قطرها $3$",
  truth=Tuple(-2, 1, 3)),
Q('u4e1q10', L3, 'medium',
  r"المعادلة الديكارتية للمحل الهندسي: $|z-3|=|z+i|$ هي:",
  [O('y=-3x+4', -3*x+4, 'eq'), O('y=3x-4', 3*x-4, 'eq'), O('y=-3x-4', -3*x-4, 'eq'), O(r'y=\frac{1}{3}x+4', x/3+4, 'eq')],
  r"بوضع $z=x+iy$: $(x-3)^2+y^2=x^2+(y+1)^2$" "\n"
  r"$-6x+9=2y+1 \Rightarrow y=-3x+4$" "\n" r"(وهو العمود المنصّف للقطعة الواصلة بين $(3,0)$ و $(0,-1)$)",
  truth=lambda: solve(expand((X-3)**2+Y**2-X**2-(Y+1)**2), Y)[0].subs(X, x)),
Q('u4e1q11', L3, 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z-1-i|\le2$ ، $0\le\text{Arg}(z-1-i)\le\frac{\pi}{2}$'), T(r'$|z+1+i|\le2$ ، $0\le\text{Arg}(z+1+i)\le\frac{\pi}{2}$'),
   T(r'$|z-1-i|\le2$ ، $0\le\text{Arg}(z)\le\frac{\pi}{2}$'), T(r'$|z-1-i|\le4$ ، $0\le\text{Arg}(z-1-i)\le\frac{\pi}{2}$')],
  r"المنطقة ربع قرص مركزه النقطة $(1,1)$ أي العدد $1+i$ ، ونصف قطره $2$ ، وحدوده مرسومة بخط متصل فالمتباينات تشمل المساواة" "\n"
  r"النقاط داخل الدائرة: $|z-(1+i)|\le2$ ، والزاوية من الشعاع الأفقي المارّ بالمركز ($0$) إلى الشعاع الرأسي ($\frac{\pi}{2}$): $0\le\text{Arg}(z-1-i)\le\frac{\pi}{2}$",
  manual='region drawn: quarter disc centre 1+i radius 2 between arg 0 and pi/2 (solid boundary)', figure=figure('u4e1q11', fig_quarter, 3.6, 3.6)),
Q('u4e1q12', L3, 'medium',
  r"الأعداد المركبة $z$ التي تُحقّق المعادلتين: $|z-4|=|z-4i|$ و $|z|=2\sqrt{2}$ معًا هي:",
  [O(r'2+2i,\ -2-2i', FiniteSet(2+2*I, -2-2*I), 'set'), O(r'2+2i', FiniteSet(2+2*I), 'set'),
   O(r'2-2i,\ -2+2i', FiniteSet(2-2*I, -2+2*I), 'set'), O(r'4+4i,\ -4-4i', FiniteSet(4+4*I, -4-4*I), 'set')],
  r"$|z-4|=|z-4i|$ هو العمود المنصّف للقطعة بين $(4,0)$ و $(0,4)$: المستقيم $y=x$" "\n"
  r"$|z|=2\sqrt2$ دائرة مركزها الأصل ونصف قطرها $2\sqrt2$ ، وبالتعويض $y=x$: $2x^2=8 \Rightarrow x=\pm2$" "\n"
  r"العددان: $2+2i$ و $-2-2i$",
  truth=lambda: FiniteSet(*[sx + I*sy for sx, sy in solve([Eq(Abs(X+I*Y-4)**2, Abs(X+I*Y-4*I)**2), X**2+Y**2-8], [X, Y])])),
]

# ============================================================== Exam 2
E2 = [
Q('u4e2q1', L1, 'easy',
  r"مرافق العدد المركب $z=\dfrac{2+i}{i}$ هو: " + r"(حيث $i=\sqrt{-1}$)",
  [O('1+2i', 1+2*I), O('1-2i', 1-2*I), O('-1+2i', -1+2*I), O('2-i', 2-I)],
  r"$z=\dfrac{(2+i)(-i)}{i(-i)}=\dfrac{-2i-i^2}{1}=1-2i$ ، فالمرافق $\bar z=1+2i$",
  truth=conjugate(expand((2+I)*(-I)))),
Q('u4e2q2', L1, 'medium',
  r"السعة الرئيسة للعدد المركب $z=-\sqrt{3}-i$ هي:",
  [O(r'-\frac{5\pi}{6}', -5*P/6), O(r'\frac{7\pi}{6}', 7*P/6), O(r'\frac{\pi}{6}', P/6), O(r'-\frac{\pi}{6}', -P/6)],
  r"العدد في الربع الثالث، وزاوية الإسناد $\tan^{-1}\left(\frac{1}{\sqrt3}\right)=\frac{\pi}{6}$" "\n"
  r"$\text{Arg}(z)=-\pi+\frac{\pi}{6}=-\frac{5\pi}{6}$ ، أما $\frac{7\pi}{6}$ فهي سعة للعدد لكنها ليست الرئيسة.",
  truth=arg(-sqrt(3)-I)),
Q('u4e2q3', L1, 'medium',
  r"قيمة المقدار: $\dfrac{|(3-4i)(1+i)|}{|2i|}$ هي:",
  [O(r'\frac{5\sqrt{2}}{2}', 5*sqrt(2)/2), O(r'5\sqrt{2}', 5*sqrt(2)), O(r'\frac{5}{2}', R(5, 2)), O(r'\frac{7}{2}', R(7, 2))],
  r"من خصائص المقياس: $\dfrac{|3-4i|\,|1+i|}{|2i|}=\dfrac{5\cdot\sqrt2}{2}=\dfrac{5\sqrt2}{2}$",
  truth=Abs(expand((3-4*I)*(1+I)))/2),
Q('u4e2q4', L1, 'hard',
  r"إذا كان: $z+2\bar{z}=9-2i$ ، فإنّ العدد المركب $z$ هو:",
  [O('3+2i', 3+2*I), O('3-2i', 3-2*I), O('9-2i', 9-2*I), O(r'3+\frac{2}{3}i', 3+R(2, 3)*I)],
  r"نفرض $z=x+iy$: $(x+iy)+2(x-iy)=3x-iy=9-2i$" "\n" r"بمساواة الجزأين: $3x=9 \Rightarrow x=3$ ، $-y=-2 \Rightarrow y=2$ ، إذن $z=3+2i$",
  truth=lambda: (lambda s_: s_[X]+I*s_[Y])(solve([re(expand(X+I*Y+2*(X-I*Y)-(9-2*I))), im(expand(X+I*Y+2*(X-I*Y)-(9-2*I)))], [X, Y]))),
Q('u4e2q5', L2, 'easy',
  r"ناتج $(2-i)^{3}$ هو:",
  [O('2-11i', 2-11*I), O('2+11i', 2+11*I), O('8-i', 8-I), O('-2-11i', -2-11*I)],
  r"$(2-i)^2=4-4i+i^2=3-4i$" "\n" r"$(2-i)^3=(3-4i)(2-i)=6-3i-8i+4i^2=2-11i$",
  truth=expand((2-I)**3)),
Q('u4e2q6', L2, 'medium',
  r"الجذران التربيعيان للعدد المركب $5-12i$ هما:",
  [O(r'\pm(3-2i)', FiniteSet(3-2*I, -3+2*I), 'set'), O(r'\pm(2-3i)', FiniteSet(2-3*I, -2+3*I), 'set'),
   O(r'\pm(3+2i)', FiniteSet(3+2*I, -3-2*I), 'set'), O(r'\pm(2+3i)', FiniteSet(2+3*I, -2-3*I), 'set')],
  r"نفرض $(a+bi)^2=5-12i \Rightarrow a^2-b^2=5$ ، $2ab=-12$" "\n"
  r"$a^2-\dfrac{36}{a^2}=5 \Rightarrow a^4-5a^2-36=0 \Rightarrow (a^2-9)(a^2+4)=0 \Rightarrow a=\pm3$ ، $b=\mp2$" "\n"
  r"تحقق: $(3-2i)^2=9-12i-4=5-12i$ ✔",
  truth=lambda: croots(z**2-(5-12*I))),
Q('u4e2q7', L2, 'medium',
  r"إذا كان: $z_1=1+\sqrt{3}\,i$ ، $z_2=-2-2i$ ، فإنّ قياس الزاوية الصغرى المحصورة بين $z_1$ و $z_2$ هو:",
  [O(r'\frac{11\pi}{12}', 11*P/12), O(r'\frac{13\pi}{12}', 13*P/12), O(r'\frac{5\pi}{12}', 5*P/12), O(r'\frac{7\pi}{12}', 7*P/12)],
  r"$\text{Arg}(z_1)=\frac{\pi}{3}$ ، $\text{Arg}(z_2)=-\frac{3\pi}{4}$" "\n"
  r"الفرق بين السعتين $\frac{\pi}{3}+\frac{3\pi}{4}=\frac{13\pi}{12}>\pi$ ، فالزاوية الصغرى $2\pi-\frac{13\pi}{12}=\frac{11\pi}{12}$",
  truth=acos(re(expand((1+sqrt(3)*I)*conjugate(-2-2*I)))/(Abs(1+sqrt(3)*I)*Abs(-2-2*I)))),
Q('u4e2q8', L2, 'hard',
  r"إذا كان العدد $1-2i$ أحد جذور المعادلة: $z^{3}-3z^{2}+az-5=0$ ، حيث $a$ عدد حقيقي، فإنّ قيمة $a$ هي:",
  [O('7', 7), O('-7', -7), O('5', 5), O('3', 3)],
  r"المعاملات حقيقية، إذن $1+2i$ جذر أيضًا، و $(z-1+2i)(z-1-2i)=z^2-2z+5$" "\n"
  r"الحد الثابت $-5$ يعني أن الجذر الثالث $r$ يحقق $5\cdot(-r)=-5 \Rightarrow r=1$" "\n"
  r"$(z^2-2z+5)(z-1)=z^3-3z^2+7z-5$ ، إذن $a=7$",
  truth=lambda: solve([re(expand((1-2*I)**3-3*(1-2*I)**2+X*(1-2*I)-5)), im(expand((1-2*I)**3-3*(1-2*I)**2+X*(1-2*I)-5))], X)[X]),
Q('u4e2q9', L3, 'easy',
  r"المحل الهندسي للنقاط التي تُمثّل العدد المركب $z$ الذي يُحقّق المعادلة $|z-4i|=2$ هو:",
  [circ(4*I, 2), circ(-4*I, 2), circ(4, 2), circ(4*I, 4)],
  r"$|z-4i|=2$ دائرة مركزها النقطة التي تُمثّل العدد $4i$ أي $(0,\,4)$ ، ونصف قطرها $2$",
  truth=Tuple(0, 4, 2)),
Q('u4e2q10', L3, 'medium',
  r"المحل الهندسي للنقاط التي تُمثّل العدد المركب $z$ الذي يُحقّق المعادلة $\text{Arg}(z+1-2i)=\dfrac{\pi}{3}$ هو:",
  [T(r'شعاع يبدأ بالنقطة $(-1,\,2)$ (ولا يشملها)، ويصنع زاوية قياسها $\frac{\pi}{3}$ مع الاتجاه الموجب لمستقيم يوازي المحور الحقيقي'),
   T(r'شعاع يبدأ بالنقطة $(1,\,-2)$ (ولا يشملها)، ويصنع زاوية قياسها $\frac{\pi}{3}$ مع الاتجاه الموجب لمستقيم يوازي المحور الحقيقي'),
   T(r'شعاع يبدأ بنقطة الأصل، ويصنع زاوية قياسها $\frac{\pi}{3}$ مع الاتجاه الموجب للمحور الحقيقي'),
   T(r'مستقيم كامل يمرّ بالنقطة $(-1,\,2)$ ويصنع زاوية قياسها $\frac{\pi}{3}$ مع المحور الحقيقي')],
  r"نكتب المعادلة على الصورة $\text{Arg}(z-(a+ib))=\theta$: $\text{Arg}(z-(-1+2i))=\frac{\pi}{3}$" "\n"
  r"فهي شعاع يبدأ بالنقطة $(-1,\,2)$ ، ولا يشمل بدايته لأن $\text{Arg}(0)$ غير مُعرَّفة (تُرسم دائرة مُفرَّغة)، ويصنع زاوية $\frac{\pi}{3}$ مع مستقيم يوازي المحور الحقيقي.",
  manual='Arg(z - z1) = theta: ray from z1=(-1,2), excluded, angle pi/3'),
Q('u4e2q11', L3, 'hard',
  r"نظام المتباينات (بدلالة $z$) الذي يُمثّل المحل الهندسي المُمثَّل بالمنطقة المُظلَّلة في الشكل الآتي هو:",
  [T(r'$|z|\le4$ ، $\frac{\pi}{6}\le\text{Arg}(z)\le\frac{\pi}{2}$'), T(r'$|z|\le4$ ، $\frac{\pi}{3}\le\text{Arg}(z)\le\frac{\pi}{2}$'),
   T(r'$|z|\ge4$ ، $\frac{\pi}{6}\le\text{Arg}(z)\le\frac{\pi}{2}$'), T(r'$|z-4|\le4$ ، $\frac{\pi}{6}\le\text{Arg}(z)\le\frac{\pi}{2}$')],
  r"المنطقة قطاع دائري مركزه الأصل ونصف قطره $4$ ، فالنقاط تحقق $|z|\le4$" "\n"
  r"الحدّ السفلي شعاع من الأصل يصنع زاوية $\frac{\pi}{6}$ ($30^\circ$) مع المحور الحقيقي، والحدّ العلوي الجزء الموجب من المحور التخيلي ($\frac{\pi}{2}$) ، والخطوط متصلة فتشمل المساواة.",
  manual='region drawn: sector |z|<=4 between arg pi/6 and pi/2', figure=figure('u4e2q11', fig_sector, 3.6, 3.6)),
IndexQ('u4e2q12', L3, 'medium',
  r"أيّ الأعداد المركبة الآتية يقع على المحل الهندسي: $|z+1-2i|=\sqrt{5}$ ؟",
  [O('-3+3i', -3+3*I), O('1+2i', 1+2*I), O('-2+i', -2+I), O('2-2i', 2-2*I)],
  r"المحل دائرة مركزها $(-1,\,2)$ ونصف قطرها $\sqrt5$ ، نختبر كل عدد:" "\n"
  r"$|-3+3i+1-2i|=|-2+i|=\sqrt5$ ✔ ، $|1+2i+1-2i|=2$ ، $|-2+i+1-2i|=|-1-i|=\sqrt2$ ، $|2-2i+1-2i|=|3-4i|=5$",
  truth=lambda vals: only(vals, lambda w_: same(Abs(w_+1-2*I), sqrt(5)))),
]

# ============================================================== Exam 3
E3 = [
Q('u4e3q1', L1, 'easy',
  r"إذا كان: $z=\dfrac{2-3i}{i}$ ، فإنّ: " + r"(حيث $i=\sqrt{-1}$)",
  [O(r'\text{Re}(z)=-3,\ \text{Im}(z)=-2', Tuple(-3, -2), 'pairs'), O(r'\text{Re}(z)=3,\ \text{Im}(z)=2', Tuple(3, 2), 'pairs'),
   O(r'\text{Re}(z)=-3,\ \text{Im}(z)=2', Tuple(-3, 2), 'pairs'), O(r'\text{Re}(z)=-2,\ \text{Im}(z)=-3', Tuple(-2, -3), 'pairs')],
  r"$z=\dfrac{(2-3i)(-i)}{i(-i)}=-2i+3i^2=-3-2i$ ، فالجزء الحقيقي $-3$ والجزء التخيلي $-2$",
  truth=lambda: Tuple(re(expand((2-3*I)*(-I))), im(expand((2-3*I)*(-I))))),
Q('u4e3q2', L1, 'medium',
  r"العدد المركب الذي مقياسه $6$ وسعته $-\dfrac{2\pi}{3}$ هو:",
  [O(r'-3-3\sqrt{3}i', -3-3*sqrt(3)*I), O(r'-3+3\sqrt{3}i', -3+3*sqrt(3)*I), O(r'3-3\sqrt{3}i', 3-3*sqrt(3)*I), O(r'-3\sqrt{3}-3i', -3*sqrt(3)-3*I)],
  r"$z=6\left(\cos\left(-\frac{2\pi}{3}\right)+i\sin\left(-\frac{2\pi}{3}\right)\right)=6\left(-\frac12-\frac{\sqrt3}{2}i\right)=-3-3\sqrt3\,i$",
  truth=expand(pol(6, -2*P/3))),
Q('u4e3q3', L1, 'easy',
  r"إذا كان: $z=4+bi$ ، حيث $b$ عدد حقيقي، وكان $\bar{z}+2z=12-3i$ ، فإنّ قيمة $b$ هي:",
  [O('-3', -3), O('3', 3), O('-1', -1), O('1', 1)],
  r"$\bar z+2z=(4-bi)+2(4+bi)=12+bi$" "\n" r"$12+bi=12-3i \Rightarrow b=-3$",
  truth=lambda: solve(im(expand((4-X*I)+2*(4+X*I)))+3, X)[0]),
Q('u4e3q4', L1, 'hard',
  r"إذا كان: $z=a+2i$ ، حيث $a>0$ ، وكانت سعة $z$ تساوي $\dfrac{\pi}{6}$ ، فإنّ قيمة $a$ هي:",
  [O(r'2\sqrt{3}', 2*sqrt(3)), O(r'\frac{2\sqrt{3}}{3}', 2*sqrt(3)/3), O(r'\sqrt{3}', sqrt(3)), O('4', 4)],
  r"العدد في الربع الأول: $\tan\frac{\pi}{6}=\dfrac{2}{a} \Rightarrow \dfrac{1}{\sqrt3}=\dfrac{2}{a} \Rightarrow a=2\sqrt3$",
  truth=lambda: solve(tan(pi/6) - 2/X, X)[0]),
Q('u4e3q5', L2, 'easy',
  r"ناتج $(1+i)^{8}$ هو:",
  [O('16', 16), O('-16', -16), O('16i', 16*I), O('8i', 8*I)],
  r"$(1+i)^2=1+2i+i^2=2i$ ، إذن $(1+i)^8=(2i)^4=16i^4=16$",
  truth=expand((1+I)**8)),
Q('u4e3q6', L2, 'medium',
  r"إذا كان: $z=2\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right)$ ، $w=3\left(\cos\frac{5\pi}{6}+i\sin\frac{5\pi}{6}\right)$ ، فإنّ الصورة القياسية لناتج $zw$ هي:",
  [O('-6i', -6*I), O('6i', 6*I), O('-6', -6), O('6', 6)],
  r"نضرب المقاييس ونجمع السعات: $zw=6\left(\cos\frac{3\pi}{2}+i\sin\frac{3\pi}{2}\right)=6(0-i)=-6i$",
  truth=expand(pol(2, 2*P/3)*pol(3, 5*P/6))),
Q('u4e3q7', L2, 'medium',
  r"إذا كان: $z=3+4i$ ، فإنّ $z^{-1}$ يساوي:",
  [O(r'\frac{3-4i}{25}', (3-4*I)/25), O(r'\frac{3-4i}{5}', (3-4*I)/5), O(r'\frac{-3+4i}{25}', (-3+4*I)/25), O(r'\frac{3+4i}{25}', (3+4*I)/25)],
  r"$z^{-1}=\dfrac{1}{3+4i}\cdot\dfrac{3-4i}{3-4i}=\dfrac{3-4i}{9+16}=\dfrac{3-4i}{25}$",
  truth=1/(3+4*I)),
Q('u4e3q8', L2, 'hard',
  r"مجموعة حلّ المعادلة: $z^{2}+2iz+3=0$ هي:",
  [O(r'\{i,\ -3i\}', FiniteSet(I, -3*I), 'set'), O(r'\{-i,\ 3i\}', FiniteSet(-I, 3*I), 'set'),
   O(r'\{1+i,\ 1-i\}', FiniteSet(1+I, 1-I), 'set'), O(r'\{2i,\ -2i\}', FiniteSet(2*I, -2*I), 'set')],
  r"بالقانون العام: $z=\dfrac{-2i\pm\sqrt{(2i)^2-4(1)(3)}}{2}=\dfrac{-2i\pm\sqrt{-16}}{2}=\dfrac{-2i\pm4i}{2}$" "\n"
  r"$z=i$ أو $z=-3i$ (لاحظ أن الجذرين ليسا مترافقين لأن أحد المعاملات $2i$ غير حقيقي)",
  truth=lambda: croots(z**2+2*I*z+3)),
IndexQ('u4e3q9', L3, 'easy',
  r"أيّ الأعداد المركبة الآتية يقع على المحل الهندسي: $|z-1|=|z-5|$ ؟",
  [O('3+7i', 3+7*I), O('2+3i', 2+3*I), O('1+5i', 1+5*I), O('5+i', 5+I)],
  r"المحل هو العمود المنصّف للقطعة الواصلة بين $(1,0)$ و $(5,0)$ ، أي المستقيم $x=3$" "\n"
  r"العدد الوحيد الذي جزؤه الحقيقي $3$ هو $3+7i$",
  truth=lambda vals: only(vals, lambda w_: same(Abs(w_-1), Abs(w_-5)))),
Q('u4e3q10', L3, 'medium',
  r"المعادلة التي تُمثّل دائرة طرفا أحد أقطارها النقطتان اللتان تُمثّلان العددين $1+i$ و $5+3i$ هي:",
  [T(r'$|z-3-2i|=\sqrt{5}$', Tuple(3+2*I, sqrt(5))), T(r'$|z+3+2i|=\sqrt{5}$', Tuple(-3-2*I, sqrt(5))),
   T(r'$|z-3-2i|=5$', Tuple(3+2*I, 5)), T(r'$|z-3-2i|=2\sqrt{5}$', Tuple(3+2*I, 2*sqrt(5)))],
  r"المركز منتصف القطر: $\dfrac{(1+i)+(5+3i)}{2}=3+2i$" "\n"
  r"نصف القطر $=|(3+2i)-(1+i)|=|2+i|=\sqrt5$ ، إذن المعادلة $|z-(3+2i)|=\sqrt5$",
  truth=Tuple((1+I+5+3*I)/2, Abs((5+3*I-(1+I))/2))),
Q('u4e3q11', L3, 'hard',
  r"المتباينة (بدلالة $z$) التي تُمثّل المنطقة المُظلَّلة في الشكل الآتي (الخط المتقطّع هو العمود المنصّف للقطعة الواصلة بين النقطتين اللتين تُمثّلان العددين $2i$ و $4$) هي:",
  [T(r'$|z-2i|<|z-4|$'), T(r'$|z-2i|>|z-4|$'), T(r'$|z-2i|\le|z-4|$'), T(r'$|z+2i|<|z+4|$')],
  r"النقاط المُظلَّلة تقع في جهة العدد $2i$ من العمود المنصّف، أي أنها أقرب إلى $2i$ منها إلى $4$: $|z-2i|<|z-4|$" "\n"
  r"والخط متقطّع، فنقاطه لا تنتمي إلى المنطقة، لذا نستعمل $<$ وليس $\le$" "\n"
  r"(تحقق بنقطة: $z=0$ في المنطقة؟ $|0-2i|=2<|0-4|=4$ ✔ ، والأصل يقع فعلًا في المنطقة المُظلَّلة)",
  manual='shaded side contains 2i and origin; dashed boundary: strict inequality', figure=figure('u4e3q11', fig_half, 3.6, 3.6)),
Q('u4e3q12', L3, 'medium',
  r"عدد الأعداد المركبة $z$ التي تُحقّق المعادلتين: $|z-3|=2$ و $\text{Arg}(z)=0$ معًا هو:",
  [O('2', 2), O('1', 1), O('0', 0), T('عدد لا نهائي', oo)],
  r"$|z-3|=2$ دائرة مركزها $(3,0)$ ونصف قطرها $2$ ، و $\text{Arg}(z)=0$ الشعاع الموجب من المحور الحقيقي ($y=0,\ x>0$)" "\n"
  r"الدائرة تقطع المحور الحقيقي عند $x=1$ و $x=5$ ، وكلاهما موجب، إذن يوجد عددان: $1$ و $5$",
  truth=lambda: len([r_ for r_ in solve((X-3)**2-4, X) if r_ > 0])),
]

exams = [dict(id='u4-e1', title='الاختبار الأول', questions=E1),
         dict(id='u4-e2', title='الاختبار الثاني', questions=E2),
         dict(id='u4-e3', title='الاختبار الثالث', questions=E3)]
build(meta, exams, 'u4')
