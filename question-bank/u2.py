from qb import *

L1, L2, L3 = 'u2-l1', 'u2-l2', 'u2-l3'
meta = dict(id='u2', number=2, semester=1, title='المتطابقات والمعادلات المثلثية',
    description='المتطابقات الأساسية ومتطابقات المجموع والفرق، متطابقات ضعف الزاوية ونصفها وتقليص القوة وتحويل الضرب إلى مجموع والمجموع إلى ضرب، وحل المعادلات المثلثية.',
    lessons=[dict(id=L1, title='المتطابقات المثلثية 1'), dict(id=L2, title='المتطابقات المثلثية 2'),
             dict(id=L3, title='حلُّ المعادلات المثلثية')])

R = Rational
P = pi
deg = lambda d_: d_*pi/180
S_ = lambda *v_: FiniteSet(*v_)
def sols(expr, lo, hi, closed_lo=True, closed_hi=False):
    return numsols(expr, lo, hi, closed_lo, closed_hi)
def st(*vals_tex):
    """solution-set option from (tex) strings like r'\frac{\pi}{6}' -> 'x=..., x=...'"""
    return r',\ '.join('x=' + t_ for t_ in vals_tex)

# ============================================================== Exam 1
E1 = [
Q('u2e1q1', L1, 'easy',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\sec x-\cos x}{\tan x}', (sec(x)-cos(x))/tan(x))),
  [O(r'\sin x', sin(x)), O(r'\cos x', cos(x)), O(r'\tan x', tan(x)), O(r'\sec x', sec(x))],
  r"$\sec x-\cos x=\dfrac{1-\cos^2x}{\cos x}=\dfrac{\sin^2x}{\cos x}$" "\n"
  r"بالقسمة على $\tan x=\dfrac{\sin x}{\cos x}$: $\dfrac{\sin^2x}{\cos x}\cdot\dfrac{\cos x}{\sin x}=\sin x$",
  truth=(sec(x)-cos(x))/tan(x)),
Q('u2e1q2', L1, 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x-\frac{\pi}{3})-\frac{1}{2}\cos x', cos(x-pi/3)-cos(x)/2)),
  [O(r'\frac{\sqrt{3}}{2}\sin x', sqrt(3)/2*sin(x)), O(r'\frac{1}{2}\sin x', sin(x)/2),
   O(r'\frac{\sqrt{3}}{2}\cos x', sqrt(3)/2*cos(x)), O(r'\cos x', cos(x))],
  r"$\cos\left(x-\frac{\pi}{3}\right)=\cos x\cos\frac{\pi}{3}+\sin x\sin\frac{\pi}{3}=\frac12\cos x+\frac{\sqrt3}{2}\sin x$" "\n"
  r"بطرح $\frac12\cos x$ يبقى $\frac{\sqrt3}{2}\sin x$",
  truth=cos(x-pi/3)-cos(x)/2),
Q('u2e1q3', L1, 'medium',
  r"إذا كان $\sin A=\frac{5}{13}$ حيث $\frac{\pi}{2}<A<\pi$ ، و $\cos B=-\frac{3}{5}$ حيث $\pi<B<\frac{3\pi}{2}$ ، فإنّ قيمة $\cos(A-B)$ هي:",
  [O(r'\frac{16}{65}', R(16, 65)), O(r'\frac{56}{65}', R(56, 65)), O(r'-\frac{16}{65}', -R(16, 65)), O(r'-\frac{56}{65}', -R(56, 65))],
  r"$A$ في الربع الثاني: $\cos A=-\frac{12}{13}$ ، و $B$ في الربع الثالث: $\sin B=-\frac45$" "\n"
  r"$\cos(A-B)=\cos A\cos B+\sin A\sin B=\left(-\frac{12}{13}\right)\left(-\frac35\right)+\frac{5}{13}\left(-\frac45\right)=\frac{36}{65}-\frac{20}{65}=\frac{16}{65}$",
  truth=cos((pi-asin(R(5, 13))) - (pi+acos(R(3, 5))))),
IndexQ('u2e1q4', L1, 'easy',
  r"إحدى المعادلات الآتية **ليست** متطابقة:",
  [O(r'\sec(-x)=-\sec x', sec(-x)+sec(x), 'rel'), O(r'\sin(-x)=-\sin x', sin(-x)+sin(x), 'rel'),
   O(r'\tan(\frac{\pi}{2}-x)=\cot x', tan(pi/2-x)-cot(x), 'rel'), O(r'\cos(-x)=\cos x', cos(-x)-cos(x), 'rel')],
  r"الاقتران $\sec x$ زوجي مثل $\cos x$ ، أي $\sec(-x)=\dfrac{1}{\cos(-x)}=\dfrac{1}{\cos x}=\sec x$ ، فالمعادلة $\sec(-x)=-\sec x$ ليست متطابقة." "\n"
  r"أما البقية فمتطابقات: $\sin$ فردي، $\cos$ زوجي، و $\tan\left(\frac{\pi}{2}-x\right)=\cot x$",
  truth=lambda vals: only(vals, lambda d_: not same(d_, 0))),
Q('u2e1q5', L2, 'easy',
  r"إذا كان $\tan\theta=2$ ، حيث $\theta$ زاوية حادّة، فإنّ قيمة $\sin2\theta$ هي:",
  [O(r'\frac{4}{5}', R(4, 5)), O(r'\frac{3}{5}', R(3, 5)), O(r'-\frac{3}{5}', -R(3, 5)), O(r'\frac{2}{5}', R(2, 5))],
  r"من مثلث قائم: المقابل $2$ والمجاور $1$ والوتر $\sqrt5$ ، فيكون $\sin\theta=\frac{2}{\sqrt5}$ و $\cos\theta=\frac{1}{\sqrt5}$" "\n"
  r"$\sin2\theta=2\sin\theta\cos\theta=2\cdot\frac{2}{\sqrt5}\cdot\frac{1}{\sqrt5}=\frac45$",
  truth=sin(2*atan(2))),
Q('u2e1q6', L2, 'medium',
  F(r"قيمة المقدار: $«0»$ هي:", (r'8\sin\frac{\pi}{8}\cos\frac{\pi}{8}\cos\frac{\pi}{4}', 8*sin(pi/8)*cos(pi/8)*cos(pi/4))),
  [O('2', 2), O('4', 4), O('1', 1), O(r'\sqrt{2}', sqrt(2))],
  r"$8\sin\frac{\pi}{8}\cos\frac{\pi}{8}=4\sin\frac{\pi}{4}$ ، فيصبح المقدار $4\sin\frac{\pi}{4}\cos\frac{\pi}{4}=2\sin\frac{\pi}{2}=2$",
  truth=8*sin(pi/8)*cos(pi/8)*cos(pi/4)),
Q('u2e1q7', L2, 'medium',
  r"إذا كان $\cos\theta=\frac{1}{4}$ ، حيث $\frac{3\pi}{2}<\theta<2\pi$ ، فإنّ قيمة $\sin\frac{\theta}{2}$ هي:",
  [O(r'\frac{\sqrt{6}}{4}', sqrt(6)/4), O(r'-\frac{\sqrt{6}}{4}', -sqrt(6)/4), O(r'\frac{\sqrt{10}}{4}', sqrt(10)/4), O(r'-\frac{\sqrt{10}}{4}', -sqrt(10)/4)],
  r"$\frac{3\pi}{4}<\frac{\theta}{2}<\pi$ ، أي $\frac{\theta}{2}$ في الربع الثاني فالجيب موجب" "\n"
  r"$\sin\frac{\theta}{2}=\sqrt{\dfrac{1-\cos\theta}{2}}=\sqrt{\dfrac{1-\frac14}{2}}=\sqrt{\dfrac38}=\dfrac{\sqrt6}{4}$",
  truth=sin((2*pi-acos(R(1, 4)))/2)),
Q('u2e1q8', L2, 'hard',
  r"قيمة المقدار: $\sin75^\circ-\sin15^\circ$ هي:",
  [O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2), O(r'\frac{\sqrt{6}}{2}', sqrt(6)/2), O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2)],
  r"$\sin A-\sin B=2\cos\dfrac{A+B}{2}\sin\dfrac{A-B}{2}$" "\n"
  r"$\sin75^\circ-\sin15^\circ=2\cos45^\circ\sin30^\circ=2\cdot\frac{\sqrt2}{2}\cdot\frac12=\frac{\sqrt2}{2}$",
  truth=sin(deg(75))-sin(deg(15))),
Q('u2e1q9', L3, 'easy',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'2\sin^{2}x+\sin x-1', 2*sin(x)**2+sin(x)-1)),
  [O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}', r'\frac{3\pi}{2}'), S_(P/6, 5*P/6, 3*P/2), 'set'),
   O(st(r'\frac{\pi}{2}', r'\frac{7\pi}{6}', r'\frac{11\pi}{6}'), S_(P/2, 7*P/6, 11*P/6), 'set'),
   O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}', r'\frac{\pi}{2}'), S_(P/6, 5*P/6, P/2), 'set'),
   O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set')],
  r"بالتحليل: $(2\sin x-1)(\sin x+1)=0$" "\n"
  r"$\sin x=\frac12 \Rightarrow x=\frac{\pi}{6},\ \frac{5\pi}{6}$ ، أو $\sin x=-1 \Rightarrow x=\frac{3\pi}{2}$",
  truth=lambda: sols(2*sin(x)**2+sin(x)-1, 0, 2*pi)),
Q('u2e1q10', L3, 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=\sqrt{3}$ في الفترة $[0,\,\pi)$ هي:", (r'\tan 2x', tan(2*x))),
  [O(st(r'\frac{\pi}{6}', r'\frac{2\pi}{3}'), S_(P/6, 2*P/3), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{7\pi}{6}'), S_(P/6, 7*P/6), 'set'),
   O(st(r'\frac{\pi}{3}', r'\frac{4\pi}{3}'), S_(P/3, 4*P/3), 'set'), O(st(r'\frac{\pi}{6}'), S_(P/6), 'set')],
  r"بما أن $0\le x<\pi$ فإن $0\le 2x<2\pi$" "\n"
  r"$\tan2x=\sqrt3 \Rightarrow 2x=\frac{\pi}{3}$ أو $2x=\frac{\pi}{3}+\pi=\frac{4\pi}{3}$" "\n"
  r"إذن $x=\frac{\pi}{6}$ أو $x=\frac{2\pi}{3}$",
  truth=lambda: sols(tan(2*x)-sqrt(3), 0, pi)),
Q('u2e1q11', L3, 'hard',
  F(r"حلول المعادلة: $«0»=«1»$ في الفترة $(0,\,2\pi)$ هي:", (r'\cos 2x', cos(2*x)), (r'-\cos x', -cos(x))),
  [O(st(r'\frac{\pi}{3}', r'\pi', r'\frac{5\pi}{3}'), S_(P/3, P, 5*P/3), 'set'), O(st(r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(P/3, 5*P/3), 'set'),
   O(st(r'\frac{2\pi}{3}', r'\pi', r'\frac{4\pi}{3}'), S_(2*P/3, P, 4*P/3), 'set'), O(st('0', r'\frac{\pi}{3}', r'\frac{5\pi}{3}'), S_(0, P/3, 5*P/3), 'set')],
  r"نعوّض $\cos2x=2\cos^2x-1$: $2\cos^2x-1=-\cos x \Rightarrow 2\cos^2x+\cos x-1=0$" "\n"
  r"بالتحليل: $(2\cos x-1)(\cos x+1)=0$" "\n"
  r"$\cos x=\frac12 \Rightarrow x=\frac{\pi}{3},\ \frac{5\pi}{3}$ ، أو $\cos x=-1 \Rightarrow x=\pi$",
  truth=lambda: sols(cos(2*x)+cos(x), 0, 2*pi, closed_lo=False)),
IndexQ('u2e1q12', L3, 'medium',
  F(r"أحد الآتية **لا** يُعَدّ حلًّا للمعادلة: $«0»=0$", (r'2\cos x+\sqrt{3}', 2*cos(x)+sqrt(3))),
  [O(r'\frac{13\pi}{6}', 13*P/6), O(r'\frac{17\pi}{6}', 17*P/6), O(r'\frac{19\pi}{6}', 19*P/6), O(r'-\frac{5\pi}{6}', -5*P/6)],
  r"$\cos x=-\frac{\sqrt3}{2}$ ، فالحل العام: $x=\frac{5\pi}{6}+2n\pi$ أو $x=\frac{7\pi}{6}+2n\pi$" "\n"
  r"$\frac{17\pi}{6}=\frac{5\pi}{6}+2\pi$ ✔ ، $\frac{19\pi}{6}=\frac{7\pi}{6}+2\pi$ ✔ ، $-\frac{5\pi}{6}=\frac{7\pi}{6}-2\pi$ ✔" "\n"
  r"أما $\frac{13\pi}{6}=\frac{\pi}{6}+2\pi$ فجيب تمامها $\frac{\sqrt3}{2}$ ، إذن ليست حلًّا.",
  truth=lambda vals: only(vals, lambda v_: not same(2*cos(v_)+sqrt(3), 0))),
]

# ============================================================== Exam 2
E2 = [
Q('u2e2q1', L1, 'easy',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'(1-\sin^{2}x)(1+\tan^{2}x)', (1-sin(x)**2)*(1+tan(x)**2))),
  [O('1', 1), O(r'\cos^{2}x', cos(x)**2), O(r'\sin^{2}x', sin(x)**2), O(r'\sec^{2}x', sec(x)**2)],
  r"$1-\sin^2x=\cos^2x$ ، و $1+\tan^2x=\sec^2x$ ، إذن المقدار $=\cos^2x\cdot\dfrac{1}{\cos^2x}=1$",
  truth=(1-sin(x)**2)*(1+tan(x)**2)),
Q('u2e2q2', L1, 'easy',
  r"قيمة المقدار: $\cos80^\circ\cos20^\circ+\sin80^\circ\sin20^\circ$ هي:",
  [O(r'\frac{1}{2}', R(1, 2)), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O(r'-\frac{1}{2}', -R(1, 2)), O('1', 1)],
  r"المقدار على صورة $\cos(A-B)$: $\cos(80^\circ-20^\circ)=\cos60^\circ=\frac12$",
  truth=cos(deg(80))*cos(deg(20))+sin(deg(80))*sin(deg(20))),
Q('u2e2q3', L1, 'medium',
  r"إذا كان $\tan x=3$ ، فإنّ قيمة $\tan\left(\frac{\pi}{4}-x\right)$ هي:",
  [O(r'-\frac{1}{2}', -R(1, 2)), O(r'\frac{1}{2}', R(1, 2)), O('-2', -2), O('2', 2)],
  r"$\tan\left(\frac{\pi}{4}-x\right)=\dfrac{\tan\frac{\pi}{4}-\tan x}{1+\tan\frac{\pi}{4}\tan x}=\dfrac{1-3}{1+3}=-\dfrac12$",
  truth=tan(pi/4-atan(3))),
Q('u2e2q4', L1, 'hard',
  r"إذا كان $\tan A=\frac{1}{2}$ و $\tan B=\frac{1}{3}$ ، حيث $A,\ B$ زاويتان حادّتان، فإنّ $A+B$ تساوي:",
  [O(r'\frac{\pi}{4}', P/4), O(r'\frac{\pi}{3}', P/3), O(r'\frac{\pi}{6}', P/6), O(r'\frac{\pi}{2}', P/2)],
  r"$\tan(A+B)=\dfrac{\frac12+\frac13}{1-\frac12\cdot\frac13}=\dfrac{\frac56}{\frac56}=1$" "\n"
  r"وبما أن $0<A+B<\pi$ و $\tan(A+B)>0$ فإن $A+B=\frac{\pi}{4}$",
  truth=atan(R(1, 2))+atan(R(1, 3))),
Q('u2e2q5', L2, 'easy',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{\sin 2x}{1+\cos 2x}', sin(2*x)/(1+cos(2*x)))),
  [O(r'\tan x', tan(x)), O(r'\cot x', cot(x)), O(r'\sin x', sin(x)), O(r'2\tan x', 2*tan(x))],
  r"$\dfrac{2\sin x\cos x}{1+(2\cos^2x-1)}=\dfrac{2\sin x\cos x}{2\cos^2x}=\dfrac{\sin x}{\cos x}=\tan x$",
  truth=sin(2*x)/(1+cos(2*x))),
Q('u2e2q6', L2, 'easy',
  r"إذا كان $\sin\theta=-\frac{2}{3}$ ، فإنّ قيمة $\cos2\theta$ هي:",
  [O(r'\frac{1}{9}', R(1, 9)), O(r'-\frac{1}{9}', -R(1, 9)), O(r'\frac{5}{9}', R(5, 9)), O(r'\frac{7}{9}', R(7, 9))],
  r"$\cos2\theta=1-2\sin^2\theta=1-2\cdot\frac49=\frac19$ (لا نحتاج إلى معرفة الربع)",
  truth=1-2*R(4, 9)),
Q('u2e2q7', L2, 'medium',
  F(r"باستعمال متطابقات تقليص القوة، المقدار $«0»$ يساوي:", (r'\cos^{4}x', cos(x)**4)),
  [O(r'\frac{3+4\cos 2x+\cos 4x}{8}', (3+4*cos(2*x)+cos(4*x))/8), O(r'\frac{3+4\cos 2x+\cos 4x}{4}', (3+4*cos(2*x)+cos(4*x))/4),
   O(r'\frac{3-4\cos 2x+\cos 4x}{8}', (3-4*cos(2*x)+cos(4*x))/8), O(r'\frac{1+2\cos 2x+\cos 4x}{8}', (1+2*cos(2*x)+cos(4*x))/8)],
  r"$\cos^4x=\left(\dfrac{1+\cos2x}{2}\right)^2=\dfrac{1+2\cos2x+\cos^22x}{4}$" "\n"
  r"و $\cos^22x=\dfrac{1+\cos4x}{2}$ ، إذن $\cos^4x=\dfrac{2+4\cos2x+1+\cos4x}{8}=\dfrac{3+4\cos2x+\cos4x}{8}$",
  truth=cos(x)**4),
Q('u2e2q8', L2, 'hard',
  F(r"قيمة المقدار: $«0»$ هي:", (r'2\sin\frac{5\pi}{12}\cos\frac{\pi}{12}', 2*sin(5*pi/12)*cos(pi/12))),
  [O(r'1+\frac{\sqrt{3}}{2}', 1+sqrt(3)/2), O(r'1-\frac{\sqrt{3}}{2}', 1-sqrt(3)/2), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2), O(r'1+\sqrt{3}', 1+sqrt(3))],
  r"$2\sin A\cos B=\sin(A+B)+\sin(A-B)$" "\n"
  r"$=\sin\frac{6\pi}{12}+\sin\frac{4\pi}{12}=\sin\frac{\pi}{2}+\sin\frac{\pi}{3}=1+\frac{\sqrt3}{2}$",
  truth=2*sin(5*pi/12)*cos(pi/12)),
Q('u2e2q9', L3, 'easy',
  F(r"حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هو:", (r'\cos^{2}x+2\cos x-3', cos(x)**2+2*cos(x)-3)),
  [O(st('0'), S_(0), 'set'), O(st(r'\pi'), S_(P), 'set'), O(st(r'\frac{\pi}{2}'), S_(P/2), 'set'), O(st(r'\frac{3\pi}{2}'), S_(3*P/2), 'set')],
  r"بالتحليل: $(\cos x+3)(\cos x-1)=0$" "\n"
  r"$\cos x=-3$ مرفوض (لأن $-1\le\cos x\le1$) ، و $\cos x=1 \Rightarrow x=0$",
  truth=lambda: sols(cos(x)**2+2*cos(x)-3, 0, 2*pi)),
Q('u2e2q10', L3, 'medium',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $\left(\frac{\pi}{2},\,\frac{3\pi}{2}\right)$ هي:", (r'3\tan^{2}x-1', 3*tan(x)**2-1)),
  [O(st(r'\frac{5\pi}{6}', r'\frac{7\pi}{6}'), S_(5*P/6, 7*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{7\pi}{6}'), S_(P/6, 7*P/6), 'set'),
   O(st(r'\frac{5\pi}{6}', r'\frac{11\pi}{6}'), S_(5*P/6, 11*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set')],
  r"$\tan^2x=\frac13 \Rightarrow \tan x=\pm\frac{1}{\sqrt3}$" "\n"
  r"في الفترة $\left(\frac{\pi}{2},\frac{3\pi}{2}\right)$: $\tan x=-\frac{1}{\sqrt3} \Rightarrow x=\frac{5\pi}{6}$ ، و $\tan x=\frac{1}{\sqrt3} \Rightarrow x=\frac{7\pi}{6}$",
  truth=lambda: sols(3*tan(x)**2-1, pi/2, 3*pi/2, closed_lo=False)),
Q('u2e2q11', L3, 'hard',
  F(r"حلول المعادلة: $«0»=0$ في الفترة $(\pi,\,2\pi)$ هي:", (r'2\sin x\cos x+\sqrt{2}\cos x', 2*sin(x)*cos(x)+sqrt(2)*cos(x))),
  [O(st(r'\frac{5\pi}{4}', r'\frac{3\pi}{2}', r'\frac{7\pi}{4}'), S_(5*P/4, 3*P/2, 7*P/4), 'set'), O(st(r'\frac{5\pi}{4}', r'\frac{7\pi}{4}'), S_(5*P/4, 7*P/4), 'set'),
   O(st(r'\frac{\pi}{2}', r'\frac{5\pi}{4}', r'\frac{7\pi}{4}'), S_(P/2, 5*P/4, 7*P/4), 'set'), O(st(r'\frac{3\pi}{4}', r'\frac{3\pi}{2}', r'\frac{7\pi}{4}'), S_(3*P/4, 3*P/2, 7*P/4), 'set')],
  r"بإخراج العامل المشترك: $\cos x(2\sin x+\sqrt2)=0$" "\n"
  r"$\cos x=0 \Rightarrow x=\frac{3\pi}{2}$ (في الفترة) ، أو $\sin x=-\frac{\sqrt2}{2} \Rightarrow x=\frac{5\pi}{4},\ \frac{7\pi}{4}$" "\n"
  r"تنبيه: لا نقسم على $\cos x$ حتى لا نفقد الحل $\frac{3\pi}{2}$",
  truth=lambda: sols(2*sin(x)*cos(x)+sqrt(2)*cos(x), pi, 2*pi, closed_lo=False)),
Q('u2e2q12', L3, 'medium',
  F(r"مجموعة حلّ المعادلة: $«0»=«1»$ في الفترة $[0,\,2\pi)$ هي:", (r'\sin\frac{x}{2}', sin(x/2)), (r'\cos\frac{x}{2}', cos(x/2))),
  [O(st(r'\frac{\pi}{2}'), S_(P/2), 'set'), O(st(r'\frac{\pi}{2}', r'\frac{5\pi}{2}'), S_(P/2, 5*P/2), 'set'),
   O(st(r'\frac{\pi}{4}'), S_(P/4), 'set'), O(st(r'\frac{\pi}{4}', r'\frac{5\pi}{4}'), S_(P/4, 5*P/4), 'set')],
  r"بالقسمة على $\cos\frac{x}{2}$: $\tan\frac{x}{2}=1$ ، وبما أن $0\le\frac{x}{2}<\pi$ فإن $\frac{x}{2}=\frac{\pi}{4}$ فقط" "\n"
  r"إذن $x=\frac{\pi}{2}$ ($\frac{5\pi}{2}$ خارج الفترة)",
  truth=lambda: sols(sin(x/2)-cos(x/2), 0, 2*pi)),
]

# ============================================================== Exam 3
al, be = symbols('alpha beta')
E3 = [
Q('u2e3q1', L1, 'easy',
  r"إذا كان $\cot\theta=\frac{3}{4}$ ، حيث $\pi<\theta<\frac{3\pi}{2}$ ، فإنّ قيمة $\sin\theta$ هي:",
  [O(r'-\frac{4}{5}', -R(4, 5)), O(r'\frac{4}{5}', R(4, 5)), O(r'-\frac{3}{5}', -R(3, 5)), O(r'\frac{3}{5}', R(3, 5))],
  r"$\cot\theta=\frac34 \Rightarrow \tan\theta=\frac43$ ، ومن مثلث قائم أضلاعه $3,\ 4,\ 5$: $|\sin\theta|=\frac45$" "\n"
  r"$\theta$ في الربع الثالث فالجيب سالب: $\sin\theta=-\frac45$",
  truth=sin(pi+atan(R(4, 3)))),
Q('u2e3q2', L1, 'medium',
  F(r"أبسط صورة للمقدار: $«0»$ هي:", (r'\cos(x+\frac{\pi}{6})-\cos(x-\frac{\pi}{6})', cos(x+pi/6)-cos(x-pi/6))),
  [O(r'-\sin x', -sin(x)), O(r'\sin x', sin(x)), O(r'-\sqrt{3}\sin x', -sqrt(3)*sin(x)), O(r'\sqrt{3}\cos x', sqrt(3)*cos(x))],
  r"بفك المقدارين: $\left(\cos x\cos\frac{\pi}{6}-\sin x\sin\frac{\pi}{6}\right)-\left(\cos x\cos\frac{\pi}{6}+\sin x\sin\frac{\pi}{6}\right)$" "\n"
  r"$=-2\sin x\sin\frac{\pi}{6}=-2\cdot\frac12\sin x=-\sin x$",
  truth=cos(x+pi/6)-cos(x-pi/6)),
Q('u2e3q3', L1, 'medium',
  F(r"أيّ الآتية مكافئ للمقدار: $«0»$ ؟", (r'\frac{1+\tan^{2}x}{1+\cot^{2}x}', (1+tan(x)**2)/(1+cot(x)**2))),
  [O(r'\tan^{2}x', tan(x)**2), O(r'\cot^{2}x', cot(x)**2), O('1', 1), O(r'\sec^{2}x', sec(x)**2)],
  r"$\dfrac{\sec^2x}{\csc^2x}=\dfrac{1/\cos^2x}{1/\sin^2x}=\dfrac{\sin^2x}{\cos^2x}=\tan^2x$",
  truth=(1+tan(x)**2)/(1+cot(x)**2)),
Q('u2e3q4', L1, 'hard',
  r"المقدار: $\sin(\alpha+\beta)\sin(\alpha-\beta)$ يساوي:",
  [O(r'\sin^{2}\alpha-\sin^{2}\beta', sin(al)**2-sin(be)**2, sym={'alpha': al, 'beta': be}),
   O(r'\sin^{2}\alpha+\sin^{2}\beta', sin(al)**2+sin(be)**2, sym={'alpha': al, 'beta': be}),
   O(r'\cos^{2}\alpha-\cos^{2}\beta', cos(al)**2-cos(be)**2, sym={'alpha': al, 'beta': be}),
   O(r'\sin^{2}\alpha-\cos^{2}\beta', sin(al)**2-cos(be)**2, sym={'alpha': al, 'beta': be})],
  r"$(\sin\alpha\cos\beta+\cos\alpha\sin\beta)(\sin\alpha\cos\beta-\cos\alpha\sin\beta)=\sin^2\alpha\cos^2\beta-\cos^2\alpha\sin^2\beta$" "\n"
  r"$=\sin^2\alpha(1-\sin^2\beta)-(1-\sin^2\alpha)\sin^2\beta=\sin^2\alpha-\sin^2\beta$" "\n"
  r"(لاحظ أن الخيار $\cos^2\alpha-\cos^2\beta$ يساوي $\sin^2\beta-\sin^2\alpha$ أي سالب الإجابة)",
  truth=sin(al+be)*sin(al-be)),
Q('u2e3q5', L2, 'easy',
  F(r"إذا كانت $0<x<\frac{\pi}{6}$ ، فإنّ أبسط صورة للمقدار $«0»$ هي:", (r'\sqrt{\frac{1+\cos 6x}{2}}', sqrt((1+cos(6*x))/2))),
  [O(r'\cos 3x', cos(3*x)), O(r'\cos 6x', cos(6*x)), O(r'\sin 3x', sin(3*x)), O(r'\cos 12x', cos(12*x))],
  r"من متطابقة نصف الزاوية: $\dfrac{1+\cos6x}{2}=\cos^23x$ ، فالمقدار $=|\cos3x|$" "\n"
  r"وبما أن $0<3x<\frac{\pi}{2}$ فإن $\cos3x>0$ ، إذن المقدار $=\cos3x$",
  truth=cos(3*x)),
Q('u2e3q6', L2, 'medium',
  r"إذا كان $\cos\theta=\frac{3}{5}$ ، حيث $\frac{3\pi}{2}<\theta<2\pi$ ، فإنّ قيمة $\tan2\theta$ هي:",
  [O(r'\frac{24}{7}', R(24, 7)), O(r'-\frac{24}{7}', -R(24, 7)), O(r'\frac{7}{24}', R(7, 24)), O(r'-\frac{7}{24}', -R(7, 24))],
  r"$\theta$ في الربع الرابع: $\sin\theta=-\frac45$ ، $\tan\theta=-\frac43$" "\n"
  r"$\tan2\theta=\dfrac{2\tan\theta}{1-\tan^2\theta}=\dfrac{-\frac83}{1-\frac{16}{9}}=\dfrac{-\frac83}{-\frac79}=\dfrac{24}{7}$",
  truth=tan(2*(2*pi-acos(R(3, 5))))),
Q('u2e3q7', L2, 'medium',
  F(r"المقدار $«0»$ يساوي:", (r'\cos 3x', cos(3*x))),
  [O(r'4\cos^{3}x-3\cos x', 4*cos(x)**3-3*cos(x)), O(r'3\cos x-4\cos^{3}x', 3*cos(x)-4*cos(x)**3),
   O(r'4\cos^{3}x+3\cos x', 4*cos(x)**3+3*cos(x)), O(r'\cos^{3}x-3\cos x', cos(x)**3-3*cos(x))],
  r"$\cos3x=\cos(2x+x)=\cos2x\cos x-\sin2x\sin x$" "\n"
  r"$=(2\cos^2x-1)\cos x-2\sin^2x\cos x=(2\cos^2x-1)\cos x-2(1-\cos^2x)\cos x=4\cos^3x-3\cos x$",
  truth=cos(3*x)),
Q('u2e3q8', L2, 'hard',
  r"قيمة المقدار: $\cos105^\circ+\cos15^\circ$ هي:",
  [O(r'\frac{\sqrt{2}}{2}', sqrt(2)/2), O(r'\frac{\sqrt{6}}{2}', sqrt(6)/2), O(r'-\frac{\sqrt{2}}{2}', -sqrt(2)/2), O(r'\frac{\sqrt{3}}{2}', sqrt(3)/2)],
  r"$\cos A+\cos B=2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$" "\n"
  r"$=2\cos60^\circ\cos45^\circ=2\cdot\frac12\cdot\frac{\sqrt2}{2}=\frac{\sqrt2}{2}$",
  truth=cos(deg(105))+cos(deg(15))),
Q('u2e3q9', L3, 'easy',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,\pi]$ هي:", (r'4\cos^{2}x-3', 4*cos(x)**2-3)),
  [O(st(r'\frac{\pi}{6}', r'\frac{5\pi}{6}'), S_(P/6, 5*P/6), 'set'), O(st(r'\frac{\pi}{6}', r'\frac{11\pi}{6}'), S_(P/6, 11*P/6), 'set'),
   O(st(r'\frac{\pi}{3}', r'\frac{2\pi}{3}'), S_(P/3, 2*P/3), 'set'), O(st(r'\frac{\pi}{6}'), S_(P/6), 'set')],
  r"$\cos^2x=\frac34 \Rightarrow \cos x=\pm\frac{\sqrt3}{2}$" "\n"
  r"في $[0,\pi]$: $\cos x=\frac{\sqrt3}{2} \Rightarrow x=\frac{\pi}{6}$ ، و $\cos x=-\frac{\sqrt3}{2} \Rightarrow x=\frac{5\pi}{6}$",
  truth=lambda: sols(4*cos(x)**2-3, 0, pi, closed_hi=True)),
Q('u2e3q10', L3, 'medium',
  F(r"عدد حلول المعادلة: $«0»=«1»$ في الفترة $[0,\,2\pi)$ هو:", (r'\sin 2x', sin(2*x)), (r'-\cos x', -cos(x))),
  [O('4', 4), O('2', 2), O('3', 3), O('6', 6)],
  r"$2\sin x\cos x+\cos x=0 \Rightarrow \cos x(2\sin x+1)=0$" "\n"
  r"$\cos x=0 \Rightarrow x=\frac{\pi}{2},\ \frac{3\pi}{2}$ ، و $\sin x=-\frac12 \Rightarrow x=\frac{7\pi}{6},\ \frac{11\pi}{6}$ ، إذن $4$ حلول.",
  truth=lambda: len(sols(sin(2*x)+cos(x), 0, 2*pi))),
Q('u2e3q11', L3, 'hard',
  F(r"مجموعة حلّ المعادلة: $«0»=0$ في الفترة $[0,\,2\pi)$ هي:", (r'\sec^{2}x-2\tan x', sec(x)**2-2*tan(x))),
  [O(st(r'\frac{\pi}{4}', r'\frac{5\pi}{4}'), S_(P/4, 5*P/4), 'set'), O(st(r'\frac{\pi}{4}'), S_(P/4), 'set'),
   O(st(r'\frac{\pi}{4}', r'\frac{3\pi}{4}'), S_(P/4, 3*P/4), 'set'), O(st(r'\frac{3\pi}{4}', r'\frac{7\pi}{4}'), S_(3*P/4, 7*P/4), 'set')],
  r"نعوّض $\sec^2x=1+\tan^2x$: $\tan^2x-2\tan x+1=0 \Rightarrow (\tan x-1)^2=0 \Rightarrow \tan x=1$" "\n"
  r"$x=\frac{\pi}{4}$ أو $x=\frac{5\pi}{4}$",
  truth=lambda: sols(sec(x)**2-2*tan(x), 0, 2*pi)),
Q('u2e3q12', L3, 'medium',
  F(r"مجموع حلول المعادلة: $«0»=\sqrt{3}$ في الفترة $[0,\,2\pi)$ هو:", (r'2\sin x', 2*sin(x))),
  [O(r'\pi', P), O(r'\frac{2\pi}{3}', 2*P/3), O(r'\frac{4\pi}{3}', 4*P/3), O(r'2\pi', 2*P)],
  r"$\sin x=\frac{\sqrt3}{2} \Rightarrow x=\frac{\pi}{3}$ أو $x=\frac{2\pi}{3}$ ، ومجموعهما $\pi$",
  truth=lambda: sum(sols(2*sin(x)-sqrt(3), 0, 2*pi))),
]

exams = [dict(id='u2-e1', title='الاختبار الأول', questions=E1),
         dict(id='u2-e2', title='الاختبار الثاني', questions=E2),
         dict(id='u2-e3', title='الاختبار الثالث', questions=E3)]
build(meta, exams, 'u2')
