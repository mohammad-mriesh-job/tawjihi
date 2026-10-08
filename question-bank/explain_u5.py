"""Teaching explanations for unit 5 (attached by build() in qb.py).
wrong: {original option index: reason}; option 0 is the correct one as written in u5.py."""
from explain_common import E

POW = r"قاعدة القوة في التكامل: $\displaystyle\int x^n\,dx=\frac{x^{n+1}}{n+1}+C$ (نزيد الأس واحدًا ونقسم على الأس الجديد)، بشرط $n\neq-1$"
SUB = r"خطوات التكامل بالتعويض: نختار $u$ (غالبًا ما داخل القوس أو الجذر أو الأس، بحيث تظهر مشتقته في التكامل)، نحسب $du$ ، نحوّل التكامل كله إلى $u$ ، نكامل، ثم نرجع إلى $x$"
PARTS = r"التكامل بالأجزاء: $\displaystyle\int u\,dv=uv-\int v\,du$ ، ونختار $u$ الحدّ الذي يصبح أبسط بالاشتقاق ($\ln x$ أولًا، ثم كثير الحدود، ثم المثلثي أو الأسّي)"
FTC = r"التكامل المحدود: نجد الاقتران الأصلي $F$ ، ثم $\displaystyle\int_a^bf(x)\,dx=F(b)-F(a)$"
CHECK = r"للتحقّق من أيّ تكامل غير محدود: اشتقّي الناتج، فيجب أن يعطي المقدار الذي داخل التكامل."
SEP = r"المعادلة التفاضلية القابلة للفصل: نضع كل ما فيه $y$ مع $dy$ في طرف، وكل ما فيه $x$ مع $dx$ في الطرف الآخر، ثم نكامل الطرفين ونضيف ثابتًا واحدًا"
LOGD = r"إذا كان البسط مشتقة المقام: $\displaystyle\int\frac{g'(x)}{g(x)}\,dx=\ln|g(x)|+C$"
EKX = r"$\displaystyle\int e^{kx}\,dx=\frac{e^{kx}}{k}$ و $\displaystyle\int\cos kx\,dx=\frac{\sin kx}{k}$ و $\displaystyle\int\sin kx\,dx=-\frac{\cos kx}{k}$ (نقسم على معامل $x$)"
WASH = r"الحجم الدوراني حول المحور $x$: $V=\pi\displaystyle\int_a^b f(x)^2\,dx$ ، وبين منحنيين (طريقة الحلقات): $V=\pi\displaystyle\int_a^b\left(R^2-r^2\right)dx$ حيث $R$ البعيد عن المحور و $r$ القريب"
DIST = r"الإزاحة هي $\displaystyle\int v\,dt$ ، أما المسافة الكلية فهي $\displaystyle\int|v|\,dt$: نقسم الفترة عند أصفار $v$ ونجمع القيم المطلقة"
PFR = r"الكسور الجزئية: نحلّل المقام، نكتب كسرًا لكل عامل، نضرب في المقام، ونعوّض بأصفار العوامل لإيجاد الثوابت؛ وتكامل $\frac{A}{x-a}$ هو $A\ln|x-a|$"

AREA = r"المساحة بين منحنيين: نجد نقاط التقاطع (حدود التكامل)، نحدّد المنحنى الأعلى بتجربة نقطة بينهما، ثم نكامل (الأعلى − الأسفل)"

EXPLAIN = {
# ============================================================ الاختبار الأول
'u5e1q1': E(
    idea=r"تكامل مجموع ← نكامل كل حدّ وحده بقاعدته المعروفة.",
    steps=[
        "## القواعد",
        r"$\displaystyle\int e^x\,dx=e^x$ ، $\displaystyle\int\frac1x\,dx=\ln|x|$ ، $\displaystyle\int\sec^2x\,dx=\tan x$ (لأن مشتقة $\tan x$ هي $\sec^2x$)",
        "## حدًّا حدًّا",
        r"$\displaystyle\int2e^x\,dx=2e^x$",
        r"$\displaystyle\int-\frac3x\,dx=-3\ln|x|$",
        r"$\displaystyle\int\sec^2x\,dx=\tan x$",
        r"الناتج: $2e^x-3\ln|x|+\tan x+C$",
    ],
    wrong={
        1: r"تكامل $\frac1x$ هو $\ln|x|$؛ قاعدة القوة لا تصلح عند الأس $-1$ ، و $\frac{3}{x^2}$ ناتج اشتقاق لا تكامل.",
        2: r"$\displaystyle\int\sec^2x\,dx=+\tan x$.",
        3: r"$\displaystyle\int e^x\,dx=e^x$ دون ضرب في $x$.",
    },
    tip=CHECK,
),
'u5e1q2': E(
    idea=r"تكامل محدود فيه ثابت مجهول في الحدّ العلوي ← نكامل، نعوّض الحدّين، ونحلّ المعادلة الناتجة.",
    steps=[
        "## الاقتران الأصلي",
        EKX,
        r"$\displaystyle\int4e^{2x}\,dx=4\times\frac{e^{2x}}{2}=2e^{2x}$",
        "## التعويض بالحدّين",
        r"$\big[2e^{2x}\big]_0^{\ln a}=2e^{2\ln a}-2e^0$",
        r"$e^{2\ln a}=e^{\ln a^2}=a^2$ و $e^0=1$ ، إذن الناتج $2a^2-2$",
        "## حلّ المعادلة",
        r"$2a^2-2=30 \Rightarrow 2a^2=32 \Rightarrow a^2=16 \Rightarrow a=\pm4$",
        r"المعطى $a>0$ ، إذن $a=4$",
    ],
    wrong={
        1: r"تحقّقي: $2(2)^2-2=6\neq30$.",
        2: r"$16$ هي قيمة $a^2$ لا $a$.",
        3: r"تنتج من نسيان الحدّ السفلي $2e^0=2$: $2a^2=30$.",
    },
),
'u5e1q3': E(
    idea=r"معطى المشتقة ← نكامل لنحصل على $f$ مع ثابت، ثم النقطة تحدّد الثابت (انتبهي: $e^0=1$).",
    steps=[
        "## التكامل",
        r"$\displaystyle\int6x\,dx=3x^2$",
        r"$\displaystyle\int-e^{-x}\,dx=-\frac{e^{-x}}{-1}=e^{-x}$ (نقسم على معامل $x$ وهو $-1$)",
        r"$f(x)=3x^2+e^{-x}+C$",
        "## الثابت",
        r"$f(0)=0+e^0+C=1+C=4$ ، إذن $C=3$",
    ],
    wrong={
        1: r"إشارة $e^{-x}$: اشتقاق $-e^{-x}$ يعطي $+e^{-x}$ لا $-e^{-x}$.",
        2: r"$C\neq4$ لأن $e^0=1$ ليس صفرًا: $f(0)=1+4=5$.",
        3: r"نُسيت القسمة على الأس الجديد: $\int6x\,dx=3x^2$.",
    },
),
'u5e1q4': E(
    idea=r"في الأس $x^3$ ، ومشتقته $3x^2$ موجودة تقريبًا (لدينا $x^2$) ← تعويض $u=x^3$.",
    steps=[
        SUB,
        r"$u=x^3$ ، $du=3x^2\,dx$ ، إذن $x^2\,dx=\frac13du$",
        r"$\displaystyle\int e^{x^3}\,x^2\,dx=\frac13\int e^u\,du=\frac13e^u+C$",
        r"$\frac13e^{x^3}+C$",
        "## تحقّق",
        r"$\left(\frac13e^{x^3}\right)'=\frac13e^{x^3}\times3x^2=x^2e^{x^3}$ ✔",
    ],
    wrong={
        1: r"الضرب في $3$ للاشتقاق؛ في التكامل نقسم: $x^2dx=\frac13du$.",
        2: r"نُسي العامل $\frac13$؛ اشتقاق $e^{x^3}$ يعطي $3x^2e^{x^3}$.",
        3: r"لا يجوز تكامل كل عامل وحده ثم ضربهما.",
    },
),
'u5e1q5': E(
    idea=r"جذر لمقدار خطي و $x$ خارجه ← $u=x-1$ ، ونكتب $x=u+1$ ، فيصبح التكامل قوى لـ $u$.",
    steps=[
        SUB,
        r"$u=x-1$ ، $x=u+1$ ، $dx=du$",
        r"$\displaystyle\int(u+1)\sqrt u\,du=\int\left(u^{\frac32}+u^{\frac12}\right)du$ (لأن $u\cdot u^{\frac12}=u^{\frac32}$)",
        POW,
        r"$\dfrac{u^{\frac52}}{\frac52}+\dfrac{u^{\frac32}}{\frac32}=\frac25u^{\frac52}+\frac23u^{\frac32}$",
        r"نرجع إلى $x$: $\frac25(x-1)^{\frac52}+\frac23(x-1)^{\frac32}+C$",
    ],
    wrong={
        1: r"$x=u+1$ (لا $u-1$)، فالحدّان يُجمعان.",
        2: r"لا يجوز تكامل $x$ و $\sqrt{x-1}$ كلًّا وحده ثم ضربهما.",
        3: r"اشتقاق هذا البديل يعطي حدودًا إضافية؛ $x$ ليس ثابتًا لنُخرجه.",
    },
),
'u5e1q6': E(
    idea=PFR + r".",
    steps=[
        r"$\dfrac{5x+4}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}$ ، و $5x+4=A(x+2)+B(x-1)$",
        r"$x=1$: $9=3A$ ، إذن $A=3$",
        r"$x=-2$: $-6=-3B$ ، إذن $B=2$",
        r"$\displaystyle\int\left(\frac{3}{x-1}+\frac{2}{x+2}\right)dx=3\ln|x-1|+2\ln|x+2|+C$",
    ],
    wrong={
        1: r"الثابتان مبدّلان: $A=3$ فوق $(x-1)$.",
        2: r"من $-6=-3B$ تكون $B=+2$.",
        3: r"$\ln|(x-1)(x+2)|$ يحتاج بسطًا يساوي مشتقة المقام $2x+1$ ، و $5x+4$ ليس مضاعفًا لها.",
    },
),
'u5e1q7': E(
    idea=r"درجة البسط تساوي درجة المقام (كسر غير فعلي) ← نقسم أولًا، ثم نجزّئ الباقي.",
    steps=[
        "## أولًا: القسمة",
        r"$x^2+1=(x^2-1)+2$ ، إذن $\dfrac{x^2+1}{x^2-1}=1+\dfrac{2}{x^2-1}$",
        "## ثانيًا: التجزئة",
        r"$\dfrac{2}{(x-1)(x+1)}=\dfrac{A}{x-1}+\dfrac{B}{x+1}$ ، و $2=A(x+1)+B(x-1)$",
        r"$x=1$: $A=1$ ، و $x=-1$: $B=-1$",
        "## ثالثًا: التكامل والحدود",
        r"$\big[x+\ln|x-1|-\ln|x+1|\big]_2^3$",
        r"عند $3$: $3+\ln2-\ln4$ ، وعند $2$: $2+0-\ln3$",
        r"الفرق: $1+\ln2-\ln4+\ln3=1+\ln\dfrac{2\times3}{4}=1+\ln\dfrac32$",
    ],
    wrong={
        1: r"الحدّ اللوغاريتمي مقلوب؛ تحقّقي من الطرح: $\ln2+\ln3-\ln4=\ln\frac32$.",
        2: r"نُسي الحدّ $1$ الناتج من القسمة ($\int_2^31\,dx=1$).",
        3: r"نُسي الحدّ $-\ln4$.",
    },
),
'u5e1q8': E(
    idea=r"$x$ × أسّي ← بالأجزاء، مع $u=x$ (يصبح $1$ بالاشتقاق).",
    steps=[
        PARTS,
        r"$u=x$ ، $du=dx$ ، $dv=e^{3x}\,dx$ ، $v=\frac13e^{3x}$",
        r"$\dfrac x3e^{3x}-\displaystyle\int\frac13e^{3x}\,dx$",
        r"$\displaystyle\int\frac13e^{3x}\,dx=\frac13\times\frac13e^{3x}=\frac19e^{3x}$",
        r"الناتج: $\dfrac x3e^{3x}-\dfrac19e^{3x}+C$",
    ],
    wrong={
        1: r"تكامل $\frac13e^{3x}$ يقسم على $3$ مرة أخرى: $\frac19$.",
        2: r"عند التكامل نقسم على $3$ لا نضرب.",
        3: r"لا يجوز تكامل العاملين كلًّا وحده.",
    },
),
'u5e1q9': E(
    idea=r"$x$ × $\sec^2x$ ← بالأجزاء: $u=x$ ، و $dv=\sec^2x\,dx$ لأن تكامله معروف ($\tan x$).",
    steps=[
        PARTS,
        r"$u=x$ ، $du=dx$ ، $v=\tan x$",
        r"$x\tan x-\displaystyle\int\tan x\,dx$",
        r"$\displaystyle\int\tan x\,dx=\int\frac{\sin x}{\cos x}\,dx=-\ln|\cos x|$ (البسط سالب مشتقة المقام)",
        r"$x\tan x-(-\ln|\cos x|)=x\tan x+\ln|\cos x|+C$",
    ],
    wrong={
        1: r"ناقص في ناقص: $-(-\ln|\cos x|)=+\ln|\cos x|$.",
        2: r"$\ln|\sin x|$ هو تكامل $\cot x$ لا $\tan x$.",
        3: r"لا يجوز تكامل العاملين كلًّا وحده.",
    },
),
'u5e1q10': E(
    idea=r"المنطقة تحت المحور $x$ ← التكامل سالب، والمساحة قيمته المطلقة.",
    steps=[
        r"تقاطع المنحنى مع المحور: $x^2-4x=x(x-4)=0$ ، أي $x=0$ و $x=4$",
        r"بين $0$ و $4$ المنحنى تحت المحور (مثلًا $f(2)=-4$)",
        r"$\displaystyle\int_0^4(x^2-4x)\,dx=\left[\frac{x^3}{3}-2x^2\right]_0^4=\frac{64}{3}-32=-\frac{32}{3}$",
        r"المساحة: $\left|-\frac{32}{3}\right|=\frac{32}{3}$",
    ],
    wrong={
        1: r"المساحة لا تكون سالبة؛ نأخذ القيمة المطلقة.",
        2: r"تحقّقي: $\frac{64}{3}-32=-\frac{32}{3}$.",
        3: r"نُسي الحدّ $-2x^2$ (أي $-32$).",
    },
),
'u5e1q11': E(
    idea=WASH + r". تربيع الجذر يزيله، فيبقى $\cos x$.",
    steps=[
        r"$V=\pi\displaystyle\int_0^{\pi/2}\left(\sqrt{\cos x}\right)^2dx=\pi\int_0^{\pi/2}\cos x\,dx$",
        r"$\pi\big[\sin x\big]_0^{\pi/2}=\pi(1-0)=\pi$",
    ],
    wrong={
        1: r"تحقّقي: $\int_0^{\pi/2}\cos x\,dx=1$ ، فالحجم $\pi$.",
        2: r"تحقّقي: $\sin\frac{\pi}{2}=1$ لا $\frac12$.",
        3: r"$\pi$ مضروبة مرة واحدة فقط.",
    },
),
'u5e1q12': E(
    idea=r"فصل المتغيرات، ثم الشرط الأوّلي، ثم نعزل $y$.",
    steps=[
        SEP,
        r"$\dfrac{dy}{y^2}=x\,dx$",
        r"$\displaystyle\int y^{-2}\,dy=-y^{-1}=-\frac1y$ ، و $\displaystyle\int x\,dx=\frac{x^2}{2}$",
        r"$-\dfrac1y=\dfrac{x^2}{2}+C$",
        r"$y(0)=1$: $-1=0+C$ ، إذن $C=-1$",
        r"$-\dfrac1y=\dfrac{x^2}{2}-1=\dfrac{x^2-2}{2}$ ، نقلب الطرفين ونضرب في $-1$: $y=\dfrac{2}{2-x^2}$",
    ],
    wrong={
        1: r"الإشارة في المقام معكوسة؛ تحقّقي: اشتقاق $\frac{2}{2+x^2}$ سالب، بينما $xy^2$ موجبة لـ $x>0$.",
        2: r"تحقّقي: $y=\frac{1}{1-x^2}$ مشتقته $\frac{2x}{(1-x^2)^2}$ ، و $xy^2=\frac{x}{(1-x^2)^2}$.",
        3: r"اشتقاق $1-\frac{x^2}{2}$ يعطي $-x$ لا $xy^2$.",
    },
),
# ============================================================ الاختبار الثاني
'u5e2q1': E(
    idea=r"لا نكامل $\cot^2x$ مباشرة ← نحوّله بمتطابقة فيثاغورس: $\cot^2x=\csc^2x-1$.",
    steps=[
        r"من $1+\cot^2x=\csc^2x$: $\cot^2x=\csc^2x-1$",
        r"$\cot^2x+3=\csc^2x-1+3=\csc^2x+2$",
        r"$\displaystyle\int\csc^2x\,dx=-\cot x$ (لأن مشتقة $\cot x$ هي $-\csc^2x$)",
        r"$\displaystyle\int2\,dx=2x$",
        r"الناتج: $-\cot x+2x+C$",
    ],
    wrong={
        1: r"نُسي $-1$ من المتطابقة: $-1+3=2$.",
        2: r"تكامل $\csc^2x$ هو $-\cot x$.",
        3: r"$-\csc x$ ليس تكامل $\csc^2x$.",
    },
),
'u5e2q2': E(
    idea=r"أسّي أساسه $3$ والأس خطي $2x+1$ ← نقسم على $\ln3$ وعلى معامل $x$ وهو $2$.",
    steps=[
        r"اشتقاق $3^{2x+1}$ بالسلسلة: $3^{2x+1}\ln3\times2$",
        r"التكامل عكسه: $\displaystyle\int3^{2x+1}\,dx=\frac{3^{2x+1}}{2\ln3}+C$",
        "## تحقّق",
        r"$\left(\dfrac{3^{2x+1}}{2\ln3}\right)'=\dfrac{3^{2x+1}\times2\ln3}{2\ln3}=3^{2x+1}$ ✔",
    ],
    wrong={
        1: r"نُسيت القسمة على معامل $x$ وهو $2$.",
        2: r"هذه مشتقة $3^{2x+1}$ لا تكاملها.",
        3: r"نقسم على $\ln3$ مرة واحدة فقط.",
    },
),
'u5e2q3': E(
    idea=DIST + r".",
    steps=[
        "## إشارة السرعة",
        r"$v(t)=t^2-4t+3=(t-1)(t-3)$ ، وأصفارها $1$ و $3$",
        r"$v(0.5)>0$ و $v(2)=-1<0$: موجبة في $(0,1)$ وسالبة في $(1,3)$",
        "## كل جزء",
        r"الاقتران الأصلي: $\frac{t^3}{3}-2t^2+3t$",
        r"$[0,1]$: $\frac13-2+3=\frac43$",
        r"$[1,3]$: $(9-18+9)-\frac43=-\frac43$ ، والمسافة $\frac43$",
        r"المسافة الكلية: $\frac43+\frac43=\frac83\ \text{m}$",
    ],
    wrong={
        1: r"$0$ هي الإزاحة (الجسيم عاد إلى موقعه).",
        2: r"هذه مسافة جزء واحد فقط.",
        3: r"تحقّقي: كل جزء مسافته $\frac43$.",
    },
),
'u5e2q4': E(
    idea=r"$\cos x$ مشتقة ما داخل القوس ← تعويض $u=1+\sin x$.",
    steps=[
        SUB,
        r"$u=1+\sin x$ ، $du=\cos x\,dx$",
        r"$\displaystyle\int u^{-2}\,du=\frac{u^{-1}}{-1}=-\frac1u+C$",
        r"$-\dfrac{1}{1+\sin x}+C$",
    ],
    wrong={
        1: r"القسمة على الأس الجديد $-1$ تعطي إشارة سالبة.",
        2: r"$\ln$ لتكامل $u^{-1}$ ، والقوة هنا $-2$.",
        3: r"الأس يُرفع واحدًا ($-1$) لا يُخفض.",
    },
),
'u5e2q5': E(
    idea=r"$\dfrac{\sin x}{\cos^2x}=\dfrac{1}{\cos x}\cdot\dfrac{\sin x}{\cos x}=\sec x\tan x$ ، وتكامله $\sec x$.",
    steps=[
        r"$\dfrac{\sin x}{\cos^2x}=\sec x\tan x$ ، و $(\sec x)'=\sec x\tan x$",
        FTC,
        r"$\big[\sec x\big]_0^{\pi/3}=\sec\frac{\pi}{3}-\sec0=\dfrac{1}{1/2}-1=2-1=1$",
        "## طريقة أخرى بالتعويض",
        r"$u=\cos x$ ، $du=-\sin x\,dx$: $\displaystyle-\int u^{-2}\,du=\frac1u=\sec x$ ✔",
    ],
    wrong={
        1: r"نُسي طرح $\sec0=1$.",
        2: r"خطأ إشارة؛ $\sec$ يزداد من $1$ إلى $2$ فالتكامل موجب.",
        3: r"$\frac12$ هي $\cos\frac{\pi}{3}$ لا $\sec\frac{\pi}{3}$.",
    },
),
'u5e2q6': E(
    idea=PFR + r".",
    steps=[
        r"$x^2-1=(x-1)(x+1)$ ، و $3x+1=A(x+1)+B(x-1)$",
        r"$x=1$: $4=2A$ ، إذن $A=2$",
        r"$x=-1$: $-2=-2B$ ، إذن $B=1$",
        r"$2\ln|x-1|+\ln|x+1|+C$",
    ],
    wrong={
        1: r"الثابتان مبدّلان.",
        2: r"من $-2=-2B$ تكون $B=+1$.",
        3: r"اشتقاق $\frac32\ln|x^2-1|$ يعطي $\frac{3x}{x^2-1}$ لا $\frac{3x+1}{x^2-1}$.",
    },
),
'u5e2q7': E(
    idea=r"المقام $x(x^2+3)$: عامل خطي وتربيعي لا يتحلّل ← فوق التربيعي $Bx+C$ ، وتكامله $\ln$ بعد ملاحظة المشتقة.",
    steps=[
        r"$2x^2+3=A(x^2+3)+(Bx+C)x$",
        r"$x=0$: $3=3A$ ، إذن $A=1$",
        r"معامل $x^2$: $2=A+B$ ، إذن $B=1$ ؛ معامل $x$: $C=0$",
        r"$\displaystyle\int\left(\frac1x+\frac{x}{x^2+3}\right)dx$",
        r"$\displaystyle\int\frac{x}{x^2+3}\,dx=\frac12\int\frac{2x}{x^2+3}\,dx=\frac12\ln(x^2+3)$ (البسط نصف مشتقة المقام)",
        r"الناتج: $\ln|x|+\frac12\ln(x^2+3)+C$",
    ],
    wrong={
        1: r"نُسي العامل $\frac12$: البسط $x$ نصف مشتقة المقام $2x$.",
        2: r"$B=+1$ ، فالحدّ الثاني موجب.",
        3: r"$A=1$ (من $3=3A$) لا $2$.",
    },
),
'u5e2q8': E(
    idea=r"$\ln$ وحده ← بالأجزاء مع $u=\ln(2x)$ و $dv=dx$.",
    steps=[
        PARTS,
        r"$u=\ln(2x)$ ، $du=\dfrac{2}{2x}dx=\dfrac1xdx$ ، $dv=dx$ ، $v=x$",
        r"$x\ln(2x)-\displaystyle\int x\cdot\frac1x\,dx=x\ln(2x)-\int1\,dx=x\ln(2x)-x+C$",
    ],
    wrong={
        1: r"$du=\frac{2}{2x}dx=\frac1xdx$ ، فالحدّ الثاني $-x$ لا $-2x$.",
        2: r"هذه قريبة من مشتقة $\ln(2x)$ لا تكامله.",
        3: r"$v=x$ لا $2x$.",
    },
),
'u5e2q9': E(
    idea=r"$x^2$ × مثلثي ← بالأجزاء مرتين؛ كل مرة تُخفض قوة $x$.",
    steps=[
        "## المرة الأولى",
        r"$u=x^2$ ، $dv=\cos x\,dx$ ، $v=\sin x$: $x^2\sin x-\displaystyle\int2x\sin x\,dx$",
        "## المرة الثانية",
        r"$u=2x$ ، $dv=\sin x\,dx$ ، $v=-\cos x$: $\displaystyle\int2x\sin x\,dx=-2x\cos x+\int2\cos x\,dx=-2x\cos x+2\sin x$",
        "## التجميع",
        r"$x^2\sin x-(-2x\cos x+2\sin x)=x^2\sin x+2x\cos x-2\sin x+C$",
    ],
    wrong={
        1: r"الطرح يقلب إشارتي القوس: $-(-2x\cos x)=+2x\cos x$ ، و $-(+2\sin x)=-2\sin x$.",
        2: r"الحدّ الأخير $-2\sin x$.",
        3: r"الحدّ الأول $uv=x^2\sin x$ موجب.",
    },
    tip=CHECK,
),
'u5e2q10': E(
    idea=AREA + r".",
    steps=[
        r"التقاطع: $x^2-3=2x \Rightarrow x^2-2x-3=0 \Rightarrow (x-3)(x+1)=0$ ، أي $x=-1$ و $x=3$",
        r"نجرّب $x=0$: $f(0)=0$ و $g(0)=-3$ ، فالمستقيم $2x$ هو الأعلى",
        r"$\displaystyle\int_{-1}^3(2x-x^2+3)\,dx=\left[x^2-\frac{x^3}{3}+3x\right]_{-1}^3$",
        r"عند $3$: $9-9+9=9$ ، وعند $-1$: $1+\frac13-3=-\frac53$",
        r"المساحة: $9-\left(-\frac53\right)=\frac{32}{3}$",
    ],
    wrong={
        1: r"نصف الناتج؛ تحقّقي من الحدّ السفلي.",
        2: r"$9$ هي القيمة عند الحدّ العلوي فقط.",
        3: r"ضعف الناتج.",
    },
),
'u5e2q11': E(
    idea=WASH + r".",
    steps=[
        r"التقاطع: $\sqrt x=x$ عند $x=0$ و $x=1$",
        r"في $(0,1)$: $\sqrt x>x$ (مثلًا $\sqrt{0.25}=0.5>0.25$) ، فـ $R=\sqrt x$ و $r=x$",
        r"$V=\pi\displaystyle\int_0^1(x-x^2)\,dx=\pi\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1=\pi\left(\frac12-\frac13\right)=\frac{\pi}{6}$",
    ],
    wrong={
        1: r"هذا $\pi\int_0^1x^2\,dx$ (الحجم الداخلي وحده).",
        2: r"هذا $\pi\int_0^1x\,dx$ (الحجم الخارجي وحده).",
        3: r"تحقّقي: $\frac12-\frac13=\frac16$.",
    },
),
'u5e2q12': E(
    idea=r"$\frac{dP}{dt}=kP$ حلّها نمو أسّي: $P=P_0e^{kt}$ ، ومن المعلومة الثانية نجد $e^k$.",
    steps=[
        SEP,
        r"$\dfrac{dP}{P}=k\,dt \Rightarrow \ln P=kt+C \Rightarrow P=P_0e^{kt}$ ، و $P_0=200$",
        r"$P(3)=200e^{3k}=1600 \Rightarrow e^{3k}=8=2^3 \Rightarrow e^k=2$",
        r"$P(t)=200\cdot2^t$ (العدد يتضاعف كل ساعة)",
        r"$P(5)=200\times32=6400$",
    ],
    wrong={
        1: r"هذا $200\times2^4$ (بعد $4$ ساعات).",
        2: r"النمو أسّي لا خطّي.",
        3: r"هذا $200\times2^6$.",
    },
),
# ============================================================ الاختبار الثالث
'u5e3q1': E(
    idea=r"نقسم البسط على $x$ حدًّا حدًّا، فيصبح التكامل سهلًا.",
    steps=[
        r"$\dfrac{x+1}{x}=1+\dfrac1x$",
        r"$\displaystyle\int\left(1+\frac1x\right)dx=x+\ln x$",
        r"$\big[x+\ln x\big]_1^e=(e+\ln e)-(1+\ln1)=(e+1)-(1+0)=e$",
    ],
    wrong={
        1: r"نُسي الحدّ $\ln x$ (قيمته $1$).",
        2: r"نُسي طرح قيمة الحدّ السفلي $1$.",
        3: r"هذا $\int_1^e\frac1x\,dx$ فقط.",
    },
),
'u5e3q2': E(
    idea=r"تقليص القوة: $\cos^2x=\frac{1+\cos2x}{2}$.",
    steps=[
        r"$\displaystyle\int_0^{\pi/2}\frac{1+\cos2x}{2}\,dx=\left[\frac x2+\frac{\sin2x}{4}\right]_0^{\pi/2}$",
        r"عند $\frac{\pi}{2}$: $\frac{\pi}{4}+\frac{\sin\pi}{4}=\frac{\pi}{4}$ ، وعند $0$: $0$",
        r"$a\pi=\frac{\pi}{4}$ ، إذن $a=\frac14$",
    ],
    quick=r"متوسط $\cos^2$ على هذه الفترة $\frac12$ ، والطول $\frac{\pi}{2}$ ، فالتكامل $\frac{\pi}{4}$.",
    wrong={
        1: r"نُسيت القسمة على $2$ في المتطابقة.",
        2: r"$\cos^2x\ge0$ ، فالتكامل موجب.",
        3: r"التكامل $\frac{\pi}{4}$ لا $\pi$.",
    },
),
'u5e3q3': E(
    idea=r"الموقع = الموقع الابتدائي + تكامل السرعة، والسرعة متعددة القاعدة ← نقسم عند $t=2$.",
    steps=[
        r"$s(5)=0+\displaystyle\int_0^2 3t^2\,dt+\int_2^5 12\,dt$",
        r"$\big[t^3\big]_0^2=8$",
        r"$\displaystyle\int_2^5 12\,dt=12\times(5-2)=36$",
        r"$s(5)=8+36=44\ \text{m}$",
    ],
    wrong={
        1: r"هذا الجزء الثاني فقط.",
        2: r"$75$ هي قيمة $3t^2$ عند $t=5$ ، لكن بعد $t=2$ السرعة ثابتة $12$.",
        3: r"تحقّقي: $8+36=44$.",
    },
),
'u5e3q4': E(
    idea=LOGD + r". هنا $(e^x+3)'=e^x$ هو البسط.",
    steps=[
        r"$g(x)=e^x+3$ ، $g'(x)=e^x$",
        r"$\displaystyle\int\frac{e^x}{e^x+3}\,dx=\ln(e^x+3)+C$ (لا قيمة مطلقة لأن $e^x+3>0$)",
    ],
    wrong={
        1: r"لا يُضرب في $e^x$؛ البسط استُعمل كمشتقة.",
        2: r"هذا ليس تكاملًا؛ اشتقاقه سالب.",
        3: r"لا يجوز تقسيم الكسر على حدود المقام.",
    },
),
'u5e3q5': E(
    idea=r"$\sin2x$ قريب من مشتقة $1+\cos^2x$ ← تعويض، وانتبهي للإشارة.",
    steps=[
        r"$u=1+\cos^2x$ ، $du=2\cos x(-\sin x)\,dx=-\sin2x\,dx$",
        r"$\displaystyle\int\frac{\sin2x}{1+\cos^2x}\,dx=\int\frac{-du}{u}=-\ln|u|+C$",
        r"$-\ln(1+\cos^2x)+C$",
    ],
    wrong={
        1: r"مشتقة $\cos^2x$ سالبة: $-\sin2x$.",
        2: r"$du=-\sin2x\,dx$ تمامًا، فلا عامل $2$ إضافي.",
        3: r"لا قسمة على $2$: $2\sin x\cos x=\sin2x$.",
    },
),
'u5e3q6': E(
    idea=PFR + r" ، ثم نعوّض الحدّين ونجمع اللوغاريتمات.",
    steps=[
        r"$2x-1=A(x-2)+B(x-1)$",
        r"$x=1$: $1=-A$ ، إذن $A=-1$ ؛ $x=2$: $3=B$",
        r"$\big[-\ln|x-1|+3\ln|x-2|\big]_3^4$",
        r"عند $4$: $-\ln3+3\ln2$ ، وعند $3$: $-\ln2+0$",
        r"الفرق: $-\ln3+3\ln2+\ln2=4\ln2-\ln3=\ln\dfrac{16}{3}$",
    ],
    wrong={
        1: r"مقلوب الناتج (إشارة معكوسة).",
        2: r"نُسي $-\ln3$.",
        3: r"$\ln3$ يُطرح.",
    },
),
'u5e3q7': E(
    idea=r"كسر غير فعلي ← نقسم: $x^3=x(x^2-1)+x$ ، ثم الباقي بسطه نصف مشتقة مقامه.",
    steps=[
        r"$\dfrac{x^3}{x^2-1}=x+\dfrac{x}{x^2-1}$",
        r"$\displaystyle\int x\,dx=\frac{x^2}{2}$",
        r"$\displaystyle\int\frac{x}{x^2-1}\,dx=\frac12\ln|x^2-1|$",
        r"الناتج: $\dfrac{x^2}{2}+\dfrac12\ln|x^2-1|+C$",
    ],
    wrong={
        1: r"نُسي العامل $\frac12$.",
        2: r"الباقي $+x$ ، فالحدّ موجب.",
        3: r"هذا ليس تكاملًا صحيحًا؛ اشتقاقه لا يعطي المقدار.",
    },
),
'u5e3q8': E(
    idea=r"$x$ × مثلثي ← بالأجزاء مع $u=x$.",
    steps=[
        PARTS,
        r"$u=x$ ، $dv=\cos2x\,dx$ ، $v=\frac12\sin2x$",
        r"$\dfrac x2\sin2x-\displaystyle\int\frac12\sin2x\,dx$",
        r"$\displaystyle\int\frac12\sin2x\,dx=\frac12\times\left(-\frac{\cos2x}{2}\right)=-\frac14\cos2x$",
        r"$\dfrac x2\sin2x-\left(-\dfrac14\cos2x\right)=\dfrac x2\sin2x+\dfrac14\cos2x+C$",
    ],
    wrong={
        1: r"تكامل $\sin$ سالب، وناقص في ناقص موجب.",
        2: r"عند التكامل نقسم على $2$ لا نضرب.",
        3: r"لا يجوز تكامل العاملين كلًّا وحده.",
    },
),
'u5e3q9': E(
    idea=r"$x\ln x$ ← بالأجزاء مع $u=\ln x$ (لأنه يصبح أبسط بالاشتقاق).",
    steps=[
        PARTS,
        r"$u=\ln x$ ، $du=\frac1xdx$ ، $dv=x\,dx$ ، $v=\frac{x^2}{2}$",
        r"$\dfrac{x^2}{2}\ln x-\displaystyle\int\frac{x^2}{2}\cdot\frac1x\,dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}$",
        r"عند $e$: $\frac{e^2}{2}-\frac{e^2}{4}=\frac{e^2}{4}$ ، وعند $1$: $0-\frac14$",
        r"$\frac{e^2}{4}+\frac14=\dfrac{e^2+1}{4}$",
    ],
    wrong={
        1: r"قيمة الحدّ السفلي $-\frac14$ تُطرح فتصبح $+\frac14$.",
        2: r"نُسي الحدّ السفلي.",
        3: r"$\int\frac x2\,dx=\frac{x^2}{4}$ ، والمقام $4$.",
    },
),
'u5e3q10': E(
    idea=r"المسافة = مجموع المساحات بين منحنى السرعة ومحور $t$ ، **كلها موجبة**.",
    steps=[
        r"$[0,2]$: مثلث فوق المحور $\frac12\times2\times4=4$",
        r"$[2,4]$: مستطيل $2\times4=8$",
        r"$[4,5]$: مثلث $\frac12\times1\times4=2$",
        r"$[5,6]$: مثلث تحت المحور مساحته $2$ ، و $[6,8]$: مثلث تحت المحور مساحته $4$",
        r"المسافة: $4+8+2+2+4=20\ \text{m}$ (أما الإزاحة $14-6=8$)",
    ],
    wrong={
        1: r"$8$ هي الإزاحة.",
        2: r"تحقّقي: المساحات فوق $14$ وتحت $6$ ، ومجموعهما $20$.",
        3: r"تحقّقي من مجموع المساحات.",
    },
),
'u5e3q11': E(
    idea=r"المساحة = التكامل (المنحنى موجب) ← معادلة في $\ln a$.",
    steps=[
        r"$\displaystyle\int_1^a\frac6x\,dx=\big[6\ln x\big]_1^a=6\ln a-0$",
        r"$6\ln a=12 \Rightarrow \ln a=2 \Rightarrow a=e^2$",
    ],
    wrong={
        1: r"تحقّقي: $6\ln e=6\neq12$.",
        2: r"تحقّقي: $6\ln e^3=18\neq12$.",
        3: r"تحقّقي: $6\ln e^6=36\neq12$.",
    },
),
'u5e3q12': E(
    idea=r"$e^{x-y}=\dfrac{e^x}{e^y}$ ← نفصل المتغيرات، ونستعمل الشرط.",
    steps=[
        SEP,
        r"$\dfrac{dy}{dx}=\dfrac{e^x}{e^y} \Rightarrow e^y\,dy=e^x\,dx$",
        r"$e^y=e^x+C$",
        r"$y(0)=\ln2$: $e^{\ln2}=e^0+C$ ، أي $2=1+C$ ، إذن $C=1$",
        r"$e^y=e^x+1 \Rightarrow y=\ln(e^x+1)$",
    ],
    wrong={
        1: r"$C=1$ لا $2$ لأن $e^0=1$.",
        2: r"تحقّقي: $y'=1$ ، و $e^{x-y}=e^{-\ln2}=\frac12\neq1$.",
        3: r"هذا يساوي $\ln2$ ثابتًا، فمشتقته صفر لا $e^{x-y}$.",
    },
),
# ============================================================ الاختبار الرابع
'u5e4q1': E(
    idea=r"نكتب الجذرين كقوى: $\sqrt x=x^{\frac12}$ و $\frac{1}{\sqrt x}=x^{-\frac12}$ ، ثم قاعدة القوة.",
    steps=[
        POW,
        r"$\displaystyle\int x^{\frac12}\,dx=\frac{x^{\frac32}}{\frac32}=\frac23x^{\frac32}$",
        r"$\displaystyle\int x^{-\frac12}\,dx=\frac{x^{\frac12}}{\frac12}=2\sqrt x$",
        r"الناتج: $\frac23x^{\frac32}+2\sqrt x+C$",
    ],
    wrong={
        1: r"القسمة على $\frac32$ تعني الضرب في $\frac23$.",
        2: r"القسمة على $\frac12$ تعني الضرب في $2$.",
        3: r"الحدّ الثاني موجب.",
    },
),
'u5e4q2': E(
    idea=r"نفكّ المربّع، فيظهر $\sin^2+\cos^2=1$ و $2\sin x\cos x=\sin2x$.",
    steps=[
        r"$(\sin x+\cos x)^2=\sin^2x+2\sin x\cos x+\cos^2x=1+\sin2x$",
        r"$\displaystyle\int(1+\sin2x)\,dx=x-\frac12\cos2x+C$",
    ],
    wrong={
        1: r"تكامل $\sin2x$ سالب: $-\frac12\cos2x$.",
        2: r"نقسم على معامل $x$ وهو $2$.",
        3: r"قاعدة القوة لا تصلح لقوس داخله ليس $x$ وحده.",
    },
),
'u5e4q3': E(
    idea=r"نقسم كل حدّ في البسط على $e^x$.",
    steps=[
        r"$\dfrac{e^{2x}}{e^x}=e^x$ ، $\dfrac{1}{e^x}=e^{-x}$",
        r"$\displaystyle\int(e^x-e^{-x})\,dx=e^x-(-e^{-x})=e^x+e^{-x}+C$",
    ],
    wrong={
        1: r"$\int-e^{-x}\,dx=+e^{-x}$.",
        2: r"$\frac{1}{e^x}=e^{-x}$ وليس $1$.",
        3: r"$\frac{e^{2x}}{e^x}=e^x$.",
    },
),
'u5e4q4': E(
    idea=r"$\frac1x$ مشتقة $\ln x$ ← تعويض $u=\ln x$.",
    steps=[
        SUB,
        r"$u=\ln x$ ، $du=\frac1xdx$",
        r"$\displaystyle\int u^3\,du=\frac{u^4}{4}+C=\frac{(\ln x)^4}{4}+C$",
    ],
    wrong={
        1: r"نُسيت القسمة على الأس الجديد $4$.",
        2: r"هذا اشتقاق لا تكامل.",
        3: r"$\frac1x$ استُعمل في $du$ ، فلا يبقى.",
    },
),
'u5e4q5': E(
    idea=r"$x^3=x^2\cdot x$ ، و $x\,dx$ تأتي من $du$ ← $u=x^2+1$ ، و $x^2=u-1$.",
    steps=[
        SUB,
        r"$u=x^2+1$ ، $du=2x\,dx$ ، $x\,dx=\frac12du$ ، $x^2=u-1$",
        r"$\displaystyle\int x^2\sqrt{x^2+1}\,x\,dx=\frac12\int(u-1)u^{\frac12}\,du=\frac12\int\left(u^{\frac32}-u^{\frac12}\right)du$",
        r"$\frac12\left(\frac25u^{\frac52}-\frac23u^{\frac32}\right)=\frac15u^{\frac52}-\frac13u^{\frac32}$",
        r"$\frac15(x^2+1)^{\frac52}-\frac13(x^2+1)^{\frac32}+C$",
    ],
    wrong={
        1: r"$x^2=u-1$ ، فالحدّ الثاني سالب.",
        2: r"نُسي العامل $\frac12$ من $x\,dx=\frac12du$.",
        3: r"لا يجوز تكامل العاملين كلًّا وحده.",
    },
),
'u5e4q6': E(
    idea=PFR + r".",
    steps=[
        r"$x^2-4x=x(x-4)$ ، و $4=A(x-4)+Bx$",
        r"$x=0$: $4=-4A$ ، إذن $A=-1$",
        r"$x=4$: $4=4B$ ، إذن $B=1$",
        r"$-\ln|x|+\ln|x-4|+C=\ln|x-4|-\ln|x|+C$",
    ],
    wrong={
        1: r"الإشارتان معكوستان: $A=-1$.",
        2: r"الثابتان $\pm1$ لا $\pm4$.",
        3: r"اشتقاق $\ln|x^2-4x|$ يعطي $\frac{2x-4}{x^2-4x}$ لا $\frac{4}{x^2-4x}$.",
    },
),
'u5e4q7': E(
    idea=PFR + r" ، ثم الحدود.",
    steps=[
        r"$x^2+3x+2=(x+1)(x+2)$ ، و $x+3=A(x+2)+B(x+1)$",
        r"$x=-1$: $2=A$ ؛ $x=-2$: $1=-B$ ، إذن $B=-1$",
        r"$\big[2\ln|x+1|-\ln|x+2|\big]_0^1=(2\ln2-\ln3)-(0-\ln2)$",
        r"$3\ln2-\ln3=\ln\dfrac{8}{3}$",
    ],
    wrong={
        1: r"مقلوب الناتج.",
        2: r"نُسي $-\ln3$ وقيمة الحدّ السفلي.",
        3: r"نُسيت قيمة الحدّ السفلي ($+\ln2$).",
    },
),
'u5e4q8': E(
    idea=r"$x^2e^x$ ← بالأجزاء مرتين.",
    steps=[
        r"المرة الأولى: $u=x^2$ ، $v=e^x$: $x^2e^x-\displaystyle\int2xe^x\,dx$",
        r"المرة الثانية: $\displaystyle\int2xe^x\,dx=2xe^x-2e^x$",
        r"$x^2e^x-2xe^x+2e^x=e^x(x^2-2x+2)+C$",
    ],
    wrong={
        1: r"إشارة $2x$: الحدّ $-2xe^x$.",
        2: r"الحدّ الأخير $+2e^x$.",
        3: r"لا يجوز تكامل العاملين كلًّا وحده.",
    },
    tip=CHECK,
),
'u5e4q9': E(
    idea=r"أسّي × مثلثي ← بالأجزاء مرتين فيعود التكامل الأصلي $I$ ، ونحلّ معادلة.",
    steps=[
        r"$I=\displaystyle\int e^{2x}\cos x\,dx$",
        r"المرة الأولى ($u=e^{2x}$ ، $v=\sin x$): $I=e^{2x}\sin x-\displaystyle\int2e^{2x}\sin x\,dx$",
        r"المرة الثانية ($u=2e^{2x}$ ، $v=-\cos x$): $\displaystyle\int2e^{2x}\sin x\,dx=-2e^{2x}\cos x+4I$",
        r"$I=e^{2x}\sin x+2e^{2x}\cos x-4I$ ، فـ $5I=e^{2x}(2\cos x+\sin x)$",
        r"$I=\dfrac{e^{2x}}{5}(2\cos x+\sin x)+C$",
    ],
    wrong={
        1: r"إشارة $\sin x$ موجبة.",
        2: r"$1+4=5$ لا $3$.",
        3: r"المعاملان مبدّلان.",
    },
),
'u5e4q10': E(
    idea=AREA + r".",
    steps=[
        r"التقاطع: $6-x^2=x+4 \Rightarrow x^2+x-2=0 \Rightarrow x=-2,\ x=1$",
        r"عند $x=0$: $6>4$ ، فالقطع المكافئ هو الأعلى",
        r"$\displaystyle\int_{-2}^1(2-x-x^2)\,dx=\left[2x-\frac{x^2}{2}-\frac{x^3}{3}\right]_{-2}^1$",
        r"عند $1$: $2-\frac12-\frac13=\frac76$ ، وعند $-2$: $-4-2+\frac83=-\frac{10}{3}$",
        r"المساحة: $\frac76+\frac{10}{3}=\frac{27}{6}=\frac92$",
    ],
    wrong={
        1: r"ضعف الناتج.",
        2: r"هذه قيمة الحدّ العلوي فقط.",
        3: r"هذه قيمة الحدّ السفلي فقط.",
    },
),
'u5e4q11': E(
    idea=WASH + r".",
    steps=[
        r"التقاطع: $5-x^2=x+3 \Rightarrow x=-2,\ x=1$ ، وفيها $5-x^2\ge x+3\ge0$",
        r"$R=5-x^2$ ، $r=x+3$",
        r"$R^2-r^2=(25-10x^2+x^4)-(x^2+6x+9)=x^4-11x^2-6x+16$",
        r"$\left[\frac{x^5}{5}-\frac{11x^3}{3}-3x^2+16x\right]_{-2}^1=\frac{143}{15}-\left(-\frac{316}{15}\right)=\frac{459}{15}=\frac{153}{5}$",
        r"$V=\frac{153\pi}{5}$",
    ],
    wrong={
        1: r"هذا $\pi\times$ المساحة.",
        2: r"تحقّقي: $R^2-r^2$ لا $(R-r)^2$.",
        3: r"تحقّقي من التعويض بالحدّين.",
    },
),
'u5e4q12': E(
    idea=r"فصل المتغيرات، ثم الشرط الأوّلي.",
    steps=[
        SEP,
        r"$2y\,dy=(2x+1)\,dx$",
        r"$y^2=x^2+x+C$",
        r"$y(0)=3$: $9=C$",
        r"$y^2=x^2+x+9$",
    ],
    wrong={
        1: r"$y(0)=3$ يعني $y^2=9$ ، فـ $C=9$.",
        2: r"$\int2x\,dx=x^2$.",
        3: r"$\int2y\,dy=y^2$ لا $y$.",
    },
),
}
