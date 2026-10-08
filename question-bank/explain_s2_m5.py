"""Explanations: semester-2 mock paper 5 (n5q1..n5q30). wrong keys = option index as written in mock_s2.py (0 = correct)."""
from explain_common import E
from explain_u5 import POW, SUB, PARTS, FTC, CHECK, SEP
from explain_u6 import VEC, MAG, PAR, LINE, REL, DOT
from explain_u7 import GEO, BIN, STD, SYM

EXPLAIN = {
'n5q1': E(
    idea=r"$1+\tan^2u=\sec^2u$ (متطابقة فيثاغورس) ← المقدار كله $\sec^23x$ ، وتكامله $\tan$ مقسومًا على $3$.",
    steps=[
        r"$1+\tan^23x=\sec^23x$",
        r"مشتقة $\tan3x$ هي $3\sec^23x$ ، فتكامل $\sec^23x$ هو $\frac13\tan3x$",
        r"$\displaystyle\int\sec^23x\,dx=\frac13\tan3x+C$",
    ],
    wrong={
        1: r"نُسيت القسمة على معامل $x$ وهو $3$.",
        2: r"الضرب في $3$ يحدث في الاشتقاق، أما التكامل فيقسم.",
        3: r"$1+\tan^23x$ مقدار واحد يساوي $\sec^23x$؛ لا نكامل $1$ وحده ثم $\tan^2$ كأنه $\sec^2$.",
    },
    tip=CHECK,
),
'n5q2': E(
    idea=r"نكامل ونعوّض، فيظهر $e^{\ln a}=a$ و $e^{-\ln a}=\frac1a$ ، فتنتج معادلة تربيعية في $a$.",
    steps=[
        "## أولًا: التكامل",
        r"$\displaystyle\int(e^x+e^{-x})\,dx=e^x-e^{-x}$ (تكامل $e^{-x}$ هو $-e^{-x}$)",
        "## ثانيًا: التعويض",
        r"عند $\ln a$: $e^{\ln a}-e^{-\ln a}=a-\frac1a$",
        r"عند $0$: $e^0-e^0=0$",
        r"$a-\dfrac1a=\dfrac83$",
        "## ثالثًا: الحلّ",
        r"نضرب في $3a$: $3a^2-3=8a$ ، أي $3a^2-8a-3=0$",
        r"نحلّل: $(3a+1)(a-3)=0$ ، إذن $a=3$ أو $a=-\frac13$",
        r"الشرط $a>1$ ، إذن $a=3$",
    ],
    wrong={
        1: r"تحقّقي: $\frac13-3=-\frac83\neq\frac83$ ، كما أن $\frac13<1$.",
        2: r"تحقّقي: $9-\frac19=\frac{80}{9}\neq\frac83$.",
        3: r"$a=e^3$ يعطي $e^3-e^{-3}\approx20$؛ لا نخلط بين $a$ و $\ln a$.",
    },
),
'n5q3': E(
    idea=r"لا نكامل $\cos^2$ مباشرة ← تقليص القوة: $\cos^2u=\frac{1+\cos2u}{2}$.",
    steps=[
        r"$\cos^23x=\dfrac{1+\cos6x}{2}=\frac12+\frac12\cos6x$",
        r"$\displaystyle\int\frac12\,dx=\frac x2$",
        r"$\displaystyle\int\frac12\cos6x\,dx=\frac12\times\frac{\sin6x}{6}=\frac{\sin6x}{12}$",
        r"الناتج: $\dfrac x2+\dfrac{\sin6x}{12}+C$",
    ],
    wrong={
        1: r"الإشارة السالبة في صيغة $\sin^2$؛ أما $\cos^2$ ففيها $+\cos2u$.",
        2: r"نُسي العامل $\frac12$: $\frac12\times\frac16=\frac{1}{12}$.",
        3: r"قاعدة القوة لا تصلح هنا؛ اشتقاق هذا البديل يعطي $-\cos^23x\sin3x$.",
    },
),
'n5q4': E(
    idea=r"من المشتقة الثانية نكامل مرتين، ونستعمل شرطًا لكل ثابت. انتبهي: $e^0=1$ ليس صفرًا.",
    steps=[
        "## التكامل الأول",
        r"$f'(x)=\displaystyle\int(6x+e^x)\,dx=3x^2+e^x+C_1$",
        r"$f'(0)=0+1+C_1=2$ ، إذن $C_1=1$",
        "## التكامل الثاني",
        r"$f(x)=\displaystyle\int(3x^2+e^x+1)\,dx=x^3+e^x+x+C_2$",
        r"$f(0)=0+1+0+C_2=3$ ، إذن $C_2=2$",
        r"$f(x)=x^3+e^x+x+2$",
    ],
    wrong={
        1: r"تنتج من اعتبار $C_1=2$؛ لكن $f'(0)=e^0+C_1=1+C_1$.",
        2: r"تنتج من اعتبار $C_2=3$؛ لكن $f(0)=e^0+C_2=1+C_2$.",
        3: r"نُسي الثابت $C_1$ ، فلم يظهر الحدّ $x$.",
    },
),
'n5q5': E(
    idea=r"المسافة = $\int|v|$ ← نقسم الفترة عند تغيّر إشارة السرعة.",
    steps=[
        r"$v=3t(2-t)=0$ عند $t=0$ و $t=2$",
        r"$v>0$ في $(0,2)$ ، و $v<0$ في $(2,3]$ (مثلًا $v(3)=-9$)",
        r"الاقتران الأصلي: $3t^2-t^3$",
        r"$[0,2]$: $(12-8)-0=4$",
        r"$[2,3]$: $(27-27)-4=-4$ ، والمسافة $4$",
        r"المسافة الكلية: $4+4=8\ \text{m}$",
    ],
    wrong={
        1: r"$0$ هي الإزاحة؛ الجسم عاد إلى مكانه.",
        2: r"هذه مسافة جزء واحد فقط.",
        3: r"تحقّقي: كل جزء مسافته $4$ ، والمجموع $8$.",
    },
),
'n5q6': E(
    idea=r"داخل الجذر $1+\sqrt x$ ، ومشتقته $\frac{1}{2\sqrt x}$ موجودة تقريبًا ← تعويض $u=1+\sqrt x$.",
    steps=[
        SUB,
        r"$u=1+\sqrt x$ ، $du=\dfrac{dx}{2\sqrt x}$ ، إذن $\dfrac{dx}{\sqrt x}=2\,du$",
        r"$\displaystyle\int\sqrt u\cdot2\,du=2\int u^{\frac12}\,du=2\times\frac{u^{\frac32}}{\frac32}=\frac43u^{\frac32}$",
        r"$\frac43(1+\sqrt x)^{\frac32}+C$",
    ],
    wrong={
        1: r"نُسي العامل $2$ من $\frac{dx}{\sqrt x}=2\,du$.",
        2: r"نضرب في $2$ لا نقسم عليه.",
        3: r"الأس يُرفع إلى $\frac32$ ، لا يبقى $\frac12$.",
    },
),
'n5q7': E(
    idea=r"$\sin2x=2\sin x\cos x$ هو بالضبط مشتقة $1+\sin^2x$ ← تعويض.",
    steps=[
        r"$u=1+\sin^2x$ ، $du=2\sin x\cos x\,dx=\sin2x\,dx$",
        r"$\displaystyle\int\frac{du}{\sqrt u}=\int u^{-\frac12}\,du=2u^{\frac12}+C$",
        r"$2\sqrt{1+\sin^2x}+C$",
    ],
    wrong={
        1: r"نُسي العامل $2$ الناتج من القسمة على $\frac12$.",
        2: r"القسمة على $\frac12$ ضرب في $2$ لا في $\frac12$.",
        3: r"$\ln$ لتكامل $u^{-1}$ ، وهنا $u^{-\frac12}$.",
    },
),
'n5q8': E(
    idea=r"تعويض $u=2x-1$ مع كتابة $x$ بدلالة $u$ وتغيير الحدود.",
    steps=[
        "## التعويض",
        r"$u=2x-1$ ، $x=\frac{u+1}{2}$ ، $dx=\frac{du}{2}$",
        r"الحدود: $x=1$ ← $u=1$ ، و $x=5$ ← $u=9$",
        r"$\displaystyle\int_1^9\frac{\frac{u+1}{2}}{\sqrt u}\cdot\frac{du}{2}=\frac14\int_1^9\left(u^{\frac12}+u^{-\frac12}\right)du$",
        "## التكامل",
        r"$\frac14\left[\frac23u^{\frac32}+2u^{\frac12}\right]_1^9$",
        r"عند $9$: $\frac23(27)+2(3)=18+6=24$ ، وعند $1$: $\frac23+2=\frac83$",
        r"$\frac14\left(24-\frac83\right)=\frac14\times\frac{64}{3}=\frac{16}{3}$",
    ],
    wrong={
        1: r"العامل $\frac14$ (نصف من $x$ ونصف من $dx$)؛ هنا استُعمل $\frac12$ فقط.",
        2: r"تحقّقي من التعويض بالحدّين: $24-\frac83=\frac{64}{3}$.",
        3: r"تحقّقي: $\frac14\times\frac{64}{3}=\frac{16}{3}$.",
    },
),
'n5q9': E(
    idea=r"$\tan^3x=\tan x\cdot\tan^2x$ ، و $\tan^2x=\sec^2x-1$ ← حدّ يُكامل بالتعويض، وحدّ $\tan x$ المعروف.",
    steps=[
        r"$\tan^3x=\tan x(\sec^2x-1)=\tan x\sec^2x-\tan x$",
        "## الحدّ الأول",
        r"$u=\tan x$ ، $du=\sec^2x\,dx$: $\displaystyle\int u\,du=\frac{u^2}{2}=\frac{\tan^2x}{2}$",
        "## الحدّ الثاني",
        r"$\displaystyle\int\tan x\,dx=\int\frac{\sin x}{\cos x}\,dx=-\ln|\cos x|$",
        r"الناتج: $\dfrac{\tan^2x}{2}-(-\ln|\cos x|)=\dfrac{\tan^2x}{2}+\ln|\cos x|+C$",
    ],
    wrong={
        1: r"نطرح $\int\tan x\,dx=-\ln|\cos x|$ ، فتصبح الإشارة موجبة.",
        2: r"قاعدة القوة لا تصلح لـ $\tan^3x$ دون وجود $\sec^2x$.",
        3: r"$\ln|\sin x|$ هو تكامل $\cot x$.",
    },
),
'n5q10': E(
    idea=r"كسر غير فعلي ← نقسم أولًا. الباقي $\frac{x}{x^2-1}$ بسطه نصف مشتقة مقامه.",
    steps=[
        "## القسمة",
        r"$x(x^2-1)=x^3-x$ ، و $x^3-2x-(x^3-x)=-x$",
        r"$\dfrac{x^3-2x}{x^2-1}=x-\dfrac{x}{x^2-1}$",
        "## التكامل",
        r"$\displaystyle\int x\,dx=\frac{x^2}{2}$",
        r"مشتقة $x^2-1$ هي $2x$ ، فـ $\displaystyle\int\frac{x}{x^2-1}\,dx=\frac12\ln|x^2-1|$",
        r"الناتج: $\dfrac{x^2}{2}-\dfrac12\ln|x^2-1|+C$",
    ],
    wrong={
        1: r"الباقي $-x$ سالب، فالحدّ اللوغاريتمي يُطرح.",
        2: r"البسط $x$ نصف المشتقة $2x$ ، فيظهر العامل $\frac12$.",
        3: r"تجزئة $-\frac{x}{x^2-1}$ تعطي $-\frac{1/2}{x-1}-\frac{1/2}{x+1}$ ، فكلا الحدّين سالب.",
    },
),
'n5q11': E(
    idea=r"$x^3-x=x(x-1)(x+1)$: ثلاثة عوامل خطية مختلفة ← ثلاثة كسور، والتعويض بالأصفار يعطي الثوابت مباشرة.",
    steps=[
        r"$x^2+2=A(x-1)(x+1)+Bx(x+1)+Dx(x-1)$",
        r"$x=0$: $2=A(-1)(1)$ ، إذن $A=-2$",
        r"$x=1$: $3=B(1)(2)$ ، إذن $B=\frac32$",
        r"$x=-1$: $3=D(-1)(-2)$ ، إذن $D=\frac32$",
        r"$\displaystyle\int=-2\ln|x|+\frac32\ln|x-1|+\frac32\ln|x+1|$",
        r"من خصائص اللوغاريتم: $\ln|x-1|+\ln|x+1|=\ln|x^2-1|$ ، فالناتج: $-2\ln|x|+\frac32\ln|x^2-1|+C$",
    ],
    wrong={
        1: r"الإشارتان معكوستان: $A=-2$ و $B=D=\frac32$.",
        2: r"من $3=2B$ تكون $B=\frac32$ لا $3$.",
        3: r"$D=+\frac32$: عند $x=-1$ الحاصل $(-1)(-2)=+2$.",
    },
),
'n5q12': E(
    idea=r"$\sqrt x$ في الأس ← $u=\sqrt x$ ، فيظهر $ue^u$ ونكامله بالأجزاء.",
    steps=[
        r"$u=\sqrt x$ ، $x=u^2$ ، $dx=2u\,du$",
        r"$\displaystyle\int e^u\cdot2u\,du=2\int ue^u\,du$",
        PARTS,
        r"$\displaystyle\int ue^u\,du=ue^u-\int e^u\,du=ue^u-e^u$",
        r"$2(ue^u-e^u)+C=2\sqrt xe^{\sqrt x}-2e^{\sqrt x}+C$",
    ],
    wrong={
        1: r"$-\int e^u\,du=-e^u$ ، فالحدّ الثاني سالب.",
        2: r"نُسي العامل $2$ من $dx=2u\,du$.",
        3: r"نُسيت خطوة الأجزاء؛ اشتقاق هذا البديل يعطي $\frac{e^{\sqrt x}}{\sqrt x}$.",
    },
),
'n5q13': E(
    idea=r"$x^2e^x$ ← بالأجزاء مرتين (كل مرة تُخفض قوة $x$ واحدًا).",
    steps=[
        "## المرة الأولى",
        r"$u=x^2$ ، $dv=e^x\,dx$: $\displaystyle\int x^2e^x\,dx=x^2e^x-2\int xe^x\,dx$",
        "## المرة الثانية",
        r"$\displaystyle\int xe^x\,dx=xe^x-e^x$",
        r"$x^2e^x-2(xe^x-e^x)=e^x(x^2-2x+2)$",
        "## التعويض",
        r"عند $1$: $e(1-2+2)=e$ ، وعند $0$: $1\times(0-0+2)=2$",
        r"$e-2$",
    ],
    wrong={
        1: r"الإشارات داخل القوس: $x^2-2x+2$ لا $x^2+2x+2$.",
        2: r"نُسي طرح قيمة الحدّ السفلي $2$.",
        3: r"قيمة الحدّ السفلي $e^0(0-0+2)=2$ لا $1$.",
    },
),
'n5q14': E(
    idea=r"المنطقة تبدأ من تقاطع المنحنى مع المحور ($\ln x=0$ عند $x=1$) إلى $x=e$ ، وتكامل $\ln x$ بالأجزاء.",
    steps=[
        r"$\ln x=0$ عند $x=1$ ، فالحدود من $1$ إلى $e$ ، والمنحنى فوق المحور",
        r"بالأجزاء ($u=\ln x$ ، $dv=dx$): $\displaystyle\int\ln x\,dx=x\ln x-x$",
        r"عند $e$: $e\ln e-e=e-e=0$",
        r"عند $1$: $1\times0-1=-1$",
        r"المساحة: $0-(-1)=1$",
    ],
    wrong={
        1: r"$e-1$ هو عرض الفترة، لا المساحة.",
        2: r"نُسي الحدّ $-x$ في ناتج الأجزاء.",
        3: r"تحقّقي من التعويض: $[x\ln x-x]_1^e=0-(-1)=1$.",
    },
),
'n5q15': E(
    idea=r"المنطقة بين منحنيين ← طريقة الحلقات: $\pi\int(R^2-r^2)\,dx$ ، والحدود من التقاطع.",
    steps=[
        r"التقاطع: $\sqrt x=x^2$ عند $x=0$ و $x=1$",
        r"في $[0,1]$: $\sqrt x\ge x^2$ (عند $\frac14$: $\frac12>\frac{1}{16}$) ، فـ $R=\sqrt x$ و $r=x^2$",
        r"$V=\pi\displaystyle\int_0^1\left(x-x^4\right)dx=\pi\left[\frac{x^2}{2}-\frac{x^5}{5}\right]_0^1=\pi\left(\frac12-\frac15\right)=\frac{3\pi}{10}$",
    ],
    wrong={
        1: r"هذا $\pi\int(R-r)^2\,dx$؛ لكن $(R-r)^2\neq R^2-r^2$.",
        2: r"هذا $\pi\times$ المساحة بين المنحنيين.",
        3: r"$R^2$ و $r^2$ يُطرحان لا يُجمعان.",
    },
),
'n5q16': E(
    idea=r"نفصل المتغيرات فيصبح $\cos^2y\,dy=\sin^2x\,dx$ ، ونكامل كلًّا منهما بتقليص القوة.",
    steps=[
        SEP,
        r"$\cos^2y\,dy=\sin^2x\,dx$",
        r"$\cos^2y=\dfrac{1+\cos2y}{2}$ ، فتكامله $\dfrac y2+\dfrac{\sin2y}{4}$",
        r"$\sin^2x=\dfrac{1-\cos2x}{2}$ ، فتكامله $\dfrac x2-\dfrac{\sin2x}{4}$",
        r"$\dfrac y2+\dfrac{\sin2y}{4}=\dfrac x2-\dfrac{\sin2x}{4}+C$",
    ],
    wrong={
        1: r"الصيغتان مبدّلتان: $\cos^2$ معه $+$ ، و $\sin^2$ معه $-$.",
        2: r"بعد الفصل $\cos^2y$ في البسط مع $dy$ ، وتكامله ليس $\tan y$.",
        3: r"تكامل $\sin^2x$ فيه $-\frac{\sin2x}{4}$.",
    },
),
'n5q17': E(
    idea=r"$AC:CB=2:1$ ← $C$ على ثلثي الطريق من $A$ إلى $B$: $C=A+\frac23\overrightarrow{AB}$.",
    steps=[
        r"$\overrightarrow{AB}=\langle 3-1,\ -1+2,\ 1-3\rangle=\langle 2,1,-2\rangle$",
        r"$\overrightarrow{AC}=\frac23\overrightarrow{AB}=\left\langle \frac43,\frac23,-\frac43\right\rangle$",
        r"$C=\left(1+\frac43,\ -2+\frac23,\ 3-\frac43\right)=\left(\frac73,-\frac43,\frac53\right)$",
    ],
    wrong={
        1: r"هذا $A+\frac13\overrightarrow{AB}$ ، أي $AC:CB=1:2$.",
        2: r"هذا منتصف $\overline{AB}$.",
        3: r"هذا $A+2\overrightarrow{AB}$ ، نقطة خارج القطعة.",
    },
),
'n5q18': E(
    idea=r"في المكعب الذي طول حرفه $4$ نقرأ إحداثيات $P$ و $V$ ، ثم المتجه ومقداره.",
    steps=[
        r"$P$ على المحور $x$: $P(4,0,0)$",
        r"$V$ فوق $R$ ($R$ على المحور $y$): $V(0,4,4)$",
        r"$\overrightarrow{PV}=\langle -4,4,4\rangle$ ، و $|\overrightarrow{PV}|=\sqrt{48}=4\sqrt3$",
        r"متجه الوحدة: $\dfrac{\langle -4,4,4\rangle}{4\sqrt3}=\left\langle -\frac{1}{\sqrt3},\frac{1}{\sqrt3},\frac{1}{\sqrt3}\right\rangle=\left\langle -\frac{\sqrt3}{3},\frac{\sqrt3}{3},\frac{\sqrt3}{3}\right\rangle$",
    ],
    wrong={
        1: r"هذا في اتجاه $\overrightarrow{VP}$ (معكوس).",
        2: r"مقداره $\sqrt3$ ، فهو ليس متجه وحدة.",
        3: r"$V$ في الأعلى، فالمركبة الثالثة موجبة.",
    },
),
'n5q19': E(
    idea=r"نعبّر عن $\overrightarrow{YZ}$ بدلالة $k$ ، ثم نساوي معامل $\vec{\mathbf{a}}$ بالمعطى.",
    steps=[
        "## أولًا: UY",
        r"$\overrightarrow{UW}=\overrightarrow{UV}+\overrightarrow{VW}=2\vec{\mathbf{a}}+6\vec{\mathbf{b}}$ ، و $Y$ منتصفه: $\overrightarrow{UY}=\vec{\mathbf{a}}+3\vec{\mathbf{b}}$",
        "## ثانيًا: UZ",
        r"$\overrightarrow{XW}=\overrightarrow{UV}=2\vec{\mathbf{a}}$ (ضلعان متقابلان)",
        r"$XW:WZ=k:1$ ، فـ $\overrightarrow{WZ}=\frac1k\overrightarrow{XW}=\frac2k\vec{\mathbf{a}}$",
        r"$\overrightarrow{UZ}=\overrightarrow{UX}+\overrightarrow{XW}+\overrightarrow{WZ}=6\vec{\mathbf{b}}+2\vec{\mathbf{a}}+\frac2k\vec{\mathbf{a}}$",
        "## ثالثًا: YZ",
        r"$\overrightarrow{YZ}=\overrightarrow{UZ}-\overrightarrow{UY}=\left(1+\frac2k\right)\vec{\mathbf{a}}+3\vec{\mathbf{b}}$",
        r"$1+\frac2k=\frac32 \Rightarrow \frac2k=\frac12 \Rightarrow k=4$",
    ],
    wrong={
        1: r"$k=2$ يعطي معامل $\vec{\mathbf{a}}$ يساوي $1+1=2\neq\frac32$.",
        2: r"النسبة مقلوبة؛ $k=\frac14$ يجعل $WZ$ أطول من $XW$ أربع مرات.",
        3: r"$k=3$ يعطي $1+\frac23=\frac53\neq\frac32$.",
    },
),
'n5q20': E(
    idea=r"التعامد ← الضرب القياسي صفر؛ نوزّع الضرب: $(\vec{\mathbf{u}}+k\vec{\mathbf{v}})\cdot\vec{\mathbf{v}}=\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}+k|\vec{\mathbf{v}}|^2$.",
    steps=[
        r"$\vec{\mathbf{u}}\cdot\vec{\mathbf{v}}=2-1+0=1$",
        r"$|\vec{\mathbf{v}}|^2=1+1+0=2$",
        r"$1+2k=0$ ، إذن $k=-\frac12$",
    ],
    wrong={
        1: r"خطأ إشارة: $2k=-1$.",
        2: r"$|\vec{\mathbf{v}}|^2=2$ لا $1$.",
        3: r"تحقّقي: $1+2(2)=5\neq0$.",
    },
),
'n5q21': E(
    idea=r"نفحص التوازي، ثم نحلّ معادلات الإحداثيات بحثًا عن نقطة مشتركة.",
    steps=[
        REL,
        r"$\langle 1,1,0\rangle$ و $\langle 0,1,0\rangle$ غير متوازيين (الأول له مركبة $x$ والثاني لا)",
        r"$x$: $1+t=2$ ، إذن $t=1$",
        r"$y$: $t=3+s$ ، إذن $s=-2$",
        r"$z$: $1=1$ متحقّقة دائمًا ✔",
        r"يوجد حلّ، فهما متقاطعان في $(2,1,1)$",
    ],
    wrong={
        1: r"متجها الاتجاه غير متوازيين.",
        2: r"المعادلات الثلاث لها حلّ، فيوجد تقاطع.",
        3: r"المنطبقان متوازيان، وهذان ليسا كذلك.",
    },
),
'n5q22': E(
    idea=r"بُعد نقطة عن مستقيم = طول العمود منها إليه ← نجد مسقط العمود $Q$ ، ثم $|\overrightarrow{PQ}|$.",
    steps=[
        r"$Q=(2+t,\ -1-t,\ t)$ ، و $\overrightarrow{PQ}=\langle t-3,\ -3-t,\ t-3\rangle$",
        r"$\overrightarrow{PQ}\cdot\langle 1,-1,1\rangle=(t-3)+(3+t)+(t-3)=3t-3=0$ ، إذن $t=1$",
        r"$Q=(3,-2,1)$ ، و $\overrightarrow{PQ}=\langle -2,-4,-2\rangle$",
        r"البعد: $\sqrt{4+16+4}=\sqrt{24}=2\sqrt6$",
    ],
    wrong={
        1: r"$\sqrt{24}=2\sqrt6$ لا $\sqrt6$.",
        2: r"هذا مربّع البعد.",
        3: r"البعد أقصر مسافة، وهي $\sqrt{24}$ عند مسقط العمود؛ $\sqrt{29}$ أكبر منها.",
    },
),
'n5q23': E(
    idea=r"$D$ نقطة على المستقيم، و $\overrightarrow{OD}$ عمودي على اتجاهه ← الضرب القياسي صفر يعطي $t$.",
    steps=[
        r"$\overrightarrow{OD}=\langle 5+t,\ 1+t,\ 2t\rangle$",
        r"$\overrightarrow{OD}\cdot\langle 1,1,2\rangle=5+t+1+t+4t=6+6t=0$ ، إذن $t=-1$",
        r"$D=(4,0,-2)$ ، وتحقّق: $4+0-4=0$ ✔",
    ],
    wrong={
        1: r"نقطة على المستقيم ($t=1$)، لكن $6+2+4=12\neq0$.",
        2: r"نقطة على المستقيم ($t=0$)، لكن $5+1+0=6\neq0$.",
        3: r"نقطة على المستقيم ($t=-2$)، لكن $3-1-8=-6\neq0$.",
    },
),
'n5q24': E(
    idea=r"مقدار المجموع معلوم ← نربّعه ونفكّه: $|\vec{\mathbf{a}}+\vec{\mathbf{b}}|^2=|\vec{\mathbf{a}}|^2+2\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}+|\vec{\mathbf{b}}|^2$ ، فنجد الضرب القياسي ثم الزاوية.",
    steps=[
        r"$(2\sqrt7)^2=28$ ، إذن $28=4+2\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}+16$",
        r"$2\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=8$ ، إذن $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=4$",
        r"$\cos\theta=\dfrac{4}{2\times4}=\dfrac12$ ، إذن $\theta=\frac{\pi}{3}$",
    ],
    wrong={
        1: r"الضرب القياسي موجب ($4$) ، فالزاوية حادة.",
        2: r"$\cos\frac{\pi}{6}=\frac{\sqrt3}{2}\neq\frac12$.",
        3: r"$\cos\frac{\pi}{4}=\frac{\sqrt2}{2}\neq\frac12$.",
    },
),
'n5q25': E(
    idea=r"نكتب $\cos\frac{\pi}{4}$ بقانون الزاوية، فتنتج معادلة في $k$.",
    steps=[
        r"الضرب القياسي: $1+0+1=2$",
        r"المقداران: $\sqrt{2+k^2}$ و $\sqrt2$",
        r"$\dfrac{2}{\sqrt{2+k^2}\cdot\sqrt2}=\dfrac{1}{\sqrt2}$ ، إذن $\sqrt{2+k^2}=2$",
        r"$2+k^2=4 \Rightarrow k^2=2 \Rightarrow k=\sqrt2$ (لأن $k>0$)",
    ],
    wrong={
        1: r"$2$ هي $k^2$ لا $k$.",
        2: r"تحقّقي: $k=\sqrt6$ يعطي $\cos\theta=\frac{2}{\sqrt8\sqrt2}=\frac12$ ، أي $\frac{\pi}{3}$.",
        3: r"تحقّقي: $k=1$ يعطي $\cos\theta=\frac{2}{\sqrt3\sqrt2}\neq\frac{1}{\sqrt2}$.",
    },
),
'n5q26': E(
    idea=r"نسبة احتمالين هندسيين ← تُختصر $p$ وتبقى قوة لـ $(1-p)$.",
    steps=[
        GEO,
        r"$\dfrac{(1-p)^2p}{(1-p)^5p}=\dfrac{1}{(1-p)^3}=\dfrac{64}{27}$",
        r"$(1-p)^3=\frac{27}{64}$ ، فـ $1-p=\frac34$ ، إذن $p=\frac14$",
        r"$E(X)=\frac1p=4$",
    ],
    wrong={
        1: r"$\frac43$ هي $\frac{1}{1-p}$.",
        2: r"$\frac14$ هي $p$.",
        3: r"$\frac34$ هي $1-p$.",
    },
),
'n5q27': E(
    idea=r"نساوي الاحتمالين بالقانون، ونقسم على العوامل المشتركة $p(1-p)^3$ ، فتنتج معادلة خطية في $p$.",
    steps=[
        BIN,
        r"$\binom51p(1-p)^4=\binom52p^2(1-p)^3$ ، أي $5p(1-p)^4=10p^2(1-p)^3$",
        r"نقسم على $p(1-p)^3$ (لا تساوي صفرًا): $5(1-p)=10p$",
        r"$5-5p=10p \Rightarrow 15p=5 \Rightarrow p=\frac13$",
        r"$\text{Var}(X)=5\times\frac13\times\frac23=\frac{10}{9}$",
    ],
    wrong={
        1: r"$\frac53$ هو التوقّع $np$ لا التباين.",
        2: r"التباين $np(1-p)$ ، و $5\times\frac13\times\frac23=\frac{10}{9}$.",
        3: r"$\frac23$ هي $1-p$.",
    },
),
'n5q28': E(
    idea=r"فترة متماثلة ← $2P(Z<c)-1$.",
    steps=[
        r"$2P\left(Z<\frac{k}{20}\right)-1=0.1586$ ، إذن $P\left(Z<\frac{k}{20}\right)=\frac{1.1586}{2}=0.5793$",
        r"من الجدول: $\frac{k}{20}=0.2$ ، إذن $k=4$",
    ],
    wrong={
        1: r"$\frac{k}{20}=0.2$ يعطي $k=4$ لا $2$.",
        2: r"$0.2$ هي $\frac{k}{20}$.",
        3: r"$k=5$ يعطي $z=0.25$ و $2(0.5987)-1=0.1974\neq0.1586$.",
    },
),
'n5q29': E(
    idea=r"النسبة فوق قيمة ← $P(X<535)$ ، ثم $z$ من الجدول، ثم $\sigma$.",
    steps=[
        r"$P(X>535)=0.0401$ ، إذن $P(X<535)=0.9599$ ، ومن الجدول $z=1.75$",
        STD,
        r"$\dfrac{535-500}{\sigma}=1.75 \Rightarrow \sigma=\dfrac{35}{1.75}=20\ \text{mm}$",
    ],
    wrong={
        1: r"$35$ هو $x-\mu$؛ يجب قسمته على $1.75$.",
        2: r"$400$ هو التباين $\sigma^2$.",
        3: r"$1.75$ هي $z$.",
    },
),
'n5q30': E(
    idea=r"«خارج الفترة» = الطرف الأيسر + الطرف الأيمن.",
    steps=[
        r"$P(Z<-0.25)=1-P(Z<0.25)=1-0.5987=0.4013$ (بالتماثل)",
        r"$P(Z>1.75)=1-0.9599=0.0401$",
        r"المجموع: $0.4013+0.0401=0.4414$",
    ],
    wrong={
        1: r"هذا احتمال **داخل** الفترة.",
        2: r"هذا $P(0.25<Z<1.75)$؛ أُخذت $-0.25$ كأنها $+0.25$.",
        3: r"هذا $P(0<Z<1.75)$.",
    },
),
}
