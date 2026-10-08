"""Explanations: semester-2 mock paper 4 (n4q1..n4q30). wrong keys = option index as written in mock_s2.py (0 = correct)."""
from explain_common import E
from explain_u5 import POW, SUB, PARTS, FTC, CHECK, SEP
from explain_u6 import VEC, MAG, PAR, LINE, REL, DOT
from explain_u7 import GEO, BIN, STD, SYM

EXPLAIN = {
'n4q1': E(
    idea=r"$\tan=\frac{\sin}{\cos}$ ، والبسط $\sin2x$ قريب من مشتقة المقام $\cos2x$ ← تعويض $u=\cos2x$ فينتج $\ln$.",
    steps=[
        r"$\tan2x=\dfrac{\sin2x}{\cos2x}$",
        SUB,
        r"$u=\cos2x$ ، $du=-2\sin2x\,dx$ ، إذن $\sin2x\,dx=-\frac12du$",
        r"$\displaystyle\int\frac{\sin2x}{\cos2x}\,dx=-\frac12\int\frac{du}{u}=-\frac12\ln|u|+C$",
        r"$-\frac12\ln|\cos2x|+C$",
    ],
    wrong={
        1: r"نُسيت الإشارة السالبة من $du=-2\sin2x\,dx$.",
        2: r"نقسم على $2$ لا نضرب فيه.",
        3: r"$\ln|\sin2x|$ يأتي من تكامل $\cot2x$ لا $\tan2x$.",
    },
    tip=CHECK,
),
'n4q2': E(
    idea=r"لا نكامل القوس المربّع مباشرة ← نفكّ المربّع أولًا: $(a+b)^2=a^2+2ab+b^2$ ، ونلاحظ أن $3^x\cdot3^{-x}=1$.",
    steps=[
        "## أولًا: فكّ المربّع",
        r"$(3^x)^2=3^{2x}=9^x$ ، $2\cdot3^x\cdot3^{-x}=2\cdot3^0=2$ ، $(3^{-x})^2=9^{-x}$",
        r"المقدار: $9^x+2+9^{-x}$",
        "## ثانيًا: التكامل حدًّا حدًّا",
        r"$\displaystyle\int9^x\,dx=\frac{9^x}{\ln9}$",
        r"$\displaystyle\int2\,dx=2x$",
        r"$\displaystyle\int9^{-x}\,dx=\frac{9^{-x}}{-\ln9}=-\frac{9^{-x}}{\ln9}$ (معامل $x$ في الأس $-1$)",
        r"الناتج: $\dfrac{9^x}{\ln9}+2x-\dfrac{9^{-x}}{\ln9}+C$",
    ],
    wrong={
        1: r"تكامل $9^{-x}$ سالب، لأننا نقسم على معامل $x$ وهو $-1$.",
        2: r"نُسي الحدّ الأوسط $2$ في فكّ المربّع: $(a+b)^2\neq a^2+b^2$.",
        3: r"قاعدة القوة لا تصلح لقوس داخله ليس $x$ وحده؛ اشتقاق هذا البديل يُنتج عاملًا إضافيًّا.",
    },
),
'n4q3': E(
    idea=r"تكامل محدود لمجموع حدّين ← نكامل كلًّا منهما، ونعوّض بعناية في $\cos2x$.",
    steps=[
        r"$\displaystyle\int\cos x\,dx=\sin x$ ، و $\displaystyle\int\sin2x\,dx=-\frac12\cos2x$",
        FTC,
        r"عند $\frac{\pi}{2}$: $\sin\frac{\pi}{2}-\frac12\cos\pi=1-\frac12(-1)=\frac32$",
        r"عند $0$: $\sin0-\frac12\cos0=0-\frac12=-\frac12$",
        r"الفرق: $\frac32-\left(-\frac12\right)=2$",
    ],
    wrong={
        1: r"هذا $\int_0^{\pi/2}\cos x\,dx$ فقط؛ نُسي الحدّ $\sin2x$ (وتكامله يساوي $1$ أيضًا).",
        2: r"تنتج من نسيان $\frac12$ في تكامل $\sin2x$.",
        3: r"الاقترانان موجبان في الفترة، فالتكامل موجب.",
    },
),
'n4q4': E(
    idea=r"نكامل المشتقة، ثم النقطة $(0,5)$ تحدّد الثابت.",
    steps=[
        r"$\displaystyle\int2\cos2x\,dx=2\times\frac{\sin2x}{2}=\sin2x$",
        r"$\displaystyle\int3x^2\,dx=x^3$",
        r"$f(x)=\sin2x-x^3+C$",
        r"$f(0)=\sin0-0+C=C=5$",
        r"$f(x)=\sin2x-x^3+5$",
    ],
    wrong={
        1: r"عند التكامل نقسم على $2$: $2\cos2x$ تكامله $\sin2x$ لا $4\sin2x$.",
        2: r"تكامل $\cos$ هو $+\sin$.",
        3: r"تحقّقي: $f(0)=4\neq5$.",
    },
),
'n4q5': E(
    idea=r"المسافة = $\int|v|$ ← نقسم الفترة حيث $\sin t$ يغيّر إشارته ($t=\pi$).",
    steps=[
        "## أولًا: إشارة السرعة",
        r"$\sin t\ge0$ في $[0,\pi]$ (الربعان الأول والثاني) ، و $\sin t<0$ في $\left(\pi,\frac{3\pi}{2}\right]$ (الربع الثالث)",
        "## ثانيًا: كل جزء",
        r"الاقتران الأصلي: $-2\cos t$",
        r"$[0,\pi]$: $-2\cos\pi-(-2\cos0)=2+2=4$",
        r"$\left[\pi,\frac{3\pi}{2}\right]$: $-2\cos\frac{3\pi}{2}-(-2\cos\pi)=0-2=-2$ ، والمسافة $2$",
        r"المسافة الكلية: $4+2=6\ \text{m}$",
    ],
    wrong={
        1: r"$2$ هي الإزاحة ($4-2$)، لا المسافة.",
        2: r"هذه مسافة الجزء الأول فقط.",
        3: r"الجزء الثاني ربع دورة فقط، ومسافته $2$ لا $4$.",
    },
),
'n4q6': E(
    idea=r"البسط $2x+1$ هو بالضبط مشتقة ما داخل القوس ← تعويض $u=x^2+x+3$.",
    steps=[
        SUB,
        r"$u=x^2+x+3$ ، $du=(2x+1)\,dx$",
        r"$\displaystyle\int u^{-2}\,du=\frac{u^{-1}}{-1}=-\frac1u+C$",
        r"$-\dfrac{1}{x^2+x+3}+C$",
    ],
    wrong={
        1: r"القسمة على الأس الجديد $-1$ تعطي إشارة سالبة.",
        2: r"$\ln$ لتكامل $u^{-1}$ ، والقوة هنا $-2$.",
        3: r"الأس يُرفع ($-2+1=-1$) لا يُخفض.",
    },
),
'n4q7': E(
    idea=r"قوة فردية لـ $\sin$ ← نفصل $\sin x$ واحدة، ونحوّل $\sin^2x$ إلى $1-\cos^2x$ ، ثم $u=\cos x$.",
    steps=[
        r"$\sin^3x=\sin^2x\cdot\sin x=(1-\cos^2x)\sin x$",
        r"$u=\cos x$ ، $du=-\sin x\,dx$ ، إذن $\sin x\,dx=-du$",
        r"$\displaystyle\int(1-u^2)(-du)=-\int(1-u^2)\,du=-\left(u-\frac{u^3}{3}\right)=-u+\frac{u^3}{3}$",
        r"$-\cos x+\dfrac{\cos^3x}{3}+C$",
    ],
    wrong={
        1: r"نُسيت الإشارة السالبة من $du=-\sin x\,dx$.",
        2: r"$-\left(-\frac{u^3}{3}\right)=+\frac{u^3}{3}$.",
        3: r"اشتقاق $\frac{\sin^4x}{4}$ يعطي $\sin^3x\cos x$ لا $\sin^3x$.",
    },
),
'n4q8': E(
    idea=r"جذر لمقدار خطي و $x$ في البسط ← $u=x+4$ ، ونكتب $x=u-4$ ، ثم نقسم كل حدّ على $\sqrt u$.",
    steps=[
        r"$u=x+4$ ، $x=u-4$ ، $dx=du$",
        r"$\displaystyle\int\frac{u-4}{\sqrt u}\,du=\int\left(u^{\frac12}-4u^{-\frac12}\right)du$",
        POW,
        r"$\displaystyle\int u^{\frac12}\,du=\frac{u^{\frac32}}{\frac32}=\frac23u^{\frac32}$",
        r"$\displaystyle\int4u^{-\frac12}\,du=4\times\frac{u^{\frac12}}{\frac12}=8u^{\frac12}$",
        r"الناتج: $\frac23(x+4)^{\frac32}-8\sqrt{x+4}+C$",
    ],
    wrong={
        1: r"الحدّ الثاني سالب لأن $x=u-4$.",
        2: r"القسمة على $\frac12$ تضاعف: $4\times2=8$.",
        3: r"اشتقاق هذا البديل لا يعطي $\frac{x}{\sqrt{x+4}}$.",
    },
),
'n4q9': E(
    idea=r"البسط $\cos x$ مشتقة المقام $1+\sin x$ ← التكامل $\ln$ المقام، مع تغيير الحدود.",
    steps=[
        r"$u=1+\sin x$ ، $du=\cos x\,dx$",
        r"الحدود: $x=0$ ← $u=1$ ، و $x=\frac{\pi}{6}$ ← $u=1+\frac12=\frac32$",
        r"$\displaystyle\int_1^{3/2}\frac{du}{u}=\big[\ln u\big]_1^{3/2}=\ln\frac32-\ln1=\ln\frac32$",
    ],
    wrong={
        1: r"الحدّان معكوسان: العلوي $\frac32$ والسفلي $1$.",
        2: r"عند $x=\frac{\pi}{6}$: $u=1+\sin\frac{\pi}{6}=\frac32$ لا $3$.",
        3: r"هذا $\int_0^{\pi/6}\cos x\,dx$؛ نُسي المقام.",
    },
),
'n4q10': E(
    idea=r"عاملان خطيان ← كسران جزئيان، نجد الثابتين بالتعويض بصفري العاملين.",
    steps=[
        r"$x+9=A(x+1)+B(x-3)$",
        r"$x=3$: $12=4A$ ، إذن $A=3$",
        r"$x=-1$: $8=-4B$ ، إذن $B=-2$",
        r"$\displaystyle\int\left(\frac{3}{x-3}-\frac{2}{x+1}\right)dx=3\ln|x-3|-2\ln|x+1|+C$",
    ],
    wrong={
        1: r"الثابتان مبدّلان.",
        2: r"من $8=-4B$ تكون $B=-2$ سالبة.",
        3: r"العاملان $(x-3)$ و $(x+1)$ لا $(x+3)$ و $(x-1)$.",
    },
),
'n4q11': E(
    idea=r"عامل خطي وعامل مكرّر ← ثلاثة كسور: $\frac Ax+\frac{B}{x-1}+\frac{D}{(x-1)^2}$.",
    steps=[
        "## أولًا: الثوابت",
        r"$2x^2-x+1=A(x-1)^2+Bx(x-1)+Dx$",
        r"$x=0$: $1=A(1)$ ، إذن $A=1$",
        r"$x=1$: $2-1+1=D$ ، إذن $D=2$",
        r"معامل $x^2$: $2=A+B$ ، إذن $B=1$",
        "## ثانيًا: التكامل",
        r"$\displaystyle\int\frac1x\,dx=\ln|x|$ ، $\displaystyle\int\frac{1}{x-1}\,dx=\ln|x-1|$",
        r"$\displaystyle\int2(x-1)^{-2}\,dx=2\times\frac{(x-1)^{-1}}{-1}=-\frac{2}{x-1}$",
        r"الناتج: $\ln|x|+\ln|x-1|-\dfrac{2}{x-1}+C$",
    ],
    wrong={
        1: r"تكامل $(x-1)^{-2}$ سالب: $-(x-1)^{-1}$.",
        2: r"$B=2-A=1$ موجب.",
        3: r"$B$ و $D$ مبدّلان: $D=2$ (من $x=1$) و $B=1$.",
    },
),
'n4q12': E(
    idea=r"$x$ × أسّي ← بالأجزاء مع $u=x$. انتبهي: تكامل $e^{-x}$ هو $-e^{-x}$.",
    steps=[
        PARTS,
        r"$u=x$ ، $du=dx$ ، $dv=e^{-x}\,dx$ ، $v=-e^{-x}$",
        r"$x(-e^{-x})-\displaystyle\int(-e^{-x})\,dx=-xe^{-x}+\int e^{-x}\,dx$",
        r"$\displaystyle\int e^{-x}\,dx=-e^{-x}$ ، فالناتج: $-xe^{-x}-e^{-x}+C$",
        "## تحقّق",
        r"$(-xe^{-x}-e^{-x})'=-e^{-x}+xe^{-x}+e^{-x}=xe^{-x}$ ✔",
    ],
    wrong={
        1: r"$\int e^{-x}\,dx=-e^{-x}$ سالب.",
        2: r"$v=-e^{-x}$ ، فالحدّ الأول $-xe^{-x}$.",
        3: r"لا يجوز تكامل كل عامل وحده.",
    },
),
'n4q13': E(
    idea=r"لا يوجد عامل آخر مع $\sin(\ln x)$ ← نأخذ $dv=dx$ ، ونكرّر الأجزاء فيعود التكامل الأصلي $I$.",
    steps=[
        r"$I=\displaystyle\int\sin(\ln x)\,dx$",
        "## المرة الأولى",
        r"$u=\sin(\ln x)$ ، $du=\cos(\ln x)\cdot\frac1x\,dx$ ، $v=x$",
        r"$I=x\sin(\ln x)-\displaystyle\int x\cos(\ln x)\frac1x\,dx=x\sin(\ln x)-\int\cos(\ln x)\,dx$",
        "## المرة الثانية",
        r"$u=\cos(\ln x)$ ، $du=-\sin(\ln x)\cdot\frac1x\,dx$ ، $v=x$",
        r"$\displaystyle\int\cos(\ln x)\,dx=x\cos(\ln x)+\int\sin(\ln x)\,dx=x\cos(\ln x)+I$",
        "## حلّ المعادلة",
        r"$I=x\sin(\ln x)-x\cos(\ln x)-I$ ، إذن $2I=x\big(\sin(\ln x)-\cos(\ln x)\big)$",
        r"$I=\dfrac x2\big(\sin(\ln x)-\cos(\ln x)\big)+C$",
    ],
    wrong={
        1: r"الحدّ $\cos(\ln x)$ يُطرح.",
        2: r"الإشارتان معكوستان؛ معامل $\sin(\ln x)$ موجب.",
        3: r"هذا يعامل $\ln x$ كأنه $x$؛ لكن مشتقة $\ln x$ هي $\frac1x$ وليست $1$.",
    },
),
'n4q14': E(
    idea=r"المسافة = مجموع المساحات بين المنحنى ومحور $t$ ، **كلها موجبة** (فوق المحور أو تحته).",
    steps=[
        r"$[0,2]$ (فوق): مثلث $\frac12\times2\times4=4$",
        r"$[2,4]$ (تحت): مثلث $\frac12\times2\times2=2$",
        r"$[4,6]$ (تحت): مستطيل $2\times2=4$",
        r"$[6,7]$ (تحت): مثلث $\frac12\times1\times2=1$",
        r"المسافة: $4+2+4+1=11\ \text{m}$",
        r"(للمقارنة: الإزاحة $4-(2+4+1)=-3$)",
    ],
    wrong={
        1: r"$3$ هي القيمة المطلقة للإزاحة.",
        2: r"$-3$ هي الإزاحة؛ والمسافة لا تكون سالبة.",
        3: r"هذه المساحة تحت المحور فقط.",
    },
),
'n4q15': E(
    idea=r"المنحنيان يتقاطعان داخل الفترة ← نقسم عند التقاطع، وفي كل جزء نطرح الأسفل من الأعلى.",
    steps=[
        "## أولًا: نقطة التقاطع",
        r"$\sin x=\cos x$ عند $x=\frac{\pi}{4}$ (كلاهما $\frac{\sqrt2}{2}$)",
        r"في $\left[0,\frac{\pi}{4}\right]$: $\cos x\ge\sin x$ (عند $0$: $1>0$) ، وفي $\left[\frac{\pi}{4},\frac{\pi}{2}\right]$: $\sin x\ge\cos x$",
        "## ثانيًا: الجزء الأول",
        r"$\displaystyle\int_0^{\pi/4}(\cos x-\sin x)\,dx=\big[\sin x+\cos x\big]_0^{\pi/4}=\left(\frac{\sqrt2}{2}+\frac{\sqrt2}{2}\right)-(0+1)=\sqrt2-1$",
        "## ثالثًا: الجزء الثاني",
        r"$\displaystyle\int_{\pi/4}^{\pi/2}(\sin x-\cos x)\,dx=\big[-\cos x-\sin x\big]_{\pi/4}^{\pi/2}=(0-1)-(-\sqrt2)=\sqrt2-1$",
        r"المساحة: $2(\sqrt2-1)=2\sqrt2-2$",
    ],
    wrong={
        1: r"نُسي طرح $1$ في كل جزء (قيمة الحدّ $\sin x+\cos x$ عند $0$).",
        2: r"هذا جزء واحد فقط؛ المنطقة جزءان متساويان.",
        3: r"تنتج من تكامل $\cos x-\sin x$ على الفترة كلها دون تقسيم، فيلغي الجزءان أحدهما الآخر.",
    },
),
'n4q16': E(
    idea=r"فصل المتغيرات: نقسم على $e^y$ ، أي نضرب في $e^{-y}$.",
    steps=[
        SEP,
        r"$\dfrac{dy}{e^y}=\cos x\,dx$ ، أي $e^{-y}\,dy=\cos x\,dx$",
        r"$\displaystyle\int e^{-y}\,dy=-e^{-y}$ (معامل $y$ في الأس $-1$)",
        r"$\displaystyle\int\cos x\,dx=\sin x$",
        r"$-e^{-y}=\sin x+C$",
    ],
    wrong={
        1: r"تكامل $e^{-y}$ سالب: $-e^{-y}$.",
        2: r"$e^y$ في الطرف الأيمن يُنقل بالقسمة فيصبح $e^{-y}$.",
        3: r"تكامل $\cos x$ هو $+\sin x$.",
    },
),
'n4q17': E(
    idea=r"مستقيمان متوازيان ← لهما متجه الاتجاه نفسه (أو أيّ مضاعف له). النقطة من المعطى.",
    steps=[
        LINE,
        r"اتجاه المستقيم المعطى $\langle 2,-1,0\rangle$ ، وأيّ مضاعف يصلح، مثل $-2\langle 2,-1,0\rangle=\langle -4,2,0\rangle$",
        r"النقطة $(-1,0,2)$",
        r"$\vec{\mathbf{r}}=\langle -1,0,2\rangle+t\langle -4,2,0\rangle$",
    ],
    wrong={
        1: r"$\langle 3,1,-4\rangle$ نقطة على المستقيم المعطى، لا اتجاهه.",
        2: r"النقطة والاتجاه خاطئان: المستقيم المطلوب يمرّ بـ $(-1,0,2)$ واتجاهه $\langle 2,-1,0\rangle$.",
        3: r"النقطة والاتجاه مبدّلان.",
    },
),
'n4q18': E(
    idea=r"متجه الوحدة = المتجه ÷ مقداره.",
    steps=[
        VEC,
        r"$\overrightarrow{PQ}=\langle 3-1,\ 4-0,\ 0-(-2)\rangle=\langle 2,4,2\rangle$",
        r"$|\overrightarrow{PQ}|=\sqrt{4+16+4}=\sqrt{24}=2\sqrt6$",
        r"$\dfrac{\langle 2,4,2\rangle}{2\sqrt6}=\left\langle \frac{1}{\sqrt6},\frac{2}{\sqrt6},\frac{1}{\sqrt6}\right\rangle=\left\langle \frac{\sqrt6}{6},\frac{\sqrt6}{3},\frac{\sqrt6}{6}\right\rangle$",
    ],
    wrong={
        1: r"مقدار $\langle 1,2,1\rangle$ هو $\sqrt6$ ، فهو ليس متجه وحدة.",
        2: r"قُسم على $6$ بدل $\sqrt6$.",
        3: r"هذا في عكس اتجاه $\overrightarrow{PQ}$.",
    },
),
'n4q19': E(
    idea=r"التعامد ⟺ الضرب القياسي صفر.",
    steps=[
        r"$\overrightarrow{PR}=\langle \beta-1,\ 2-0,\ 1-(-2)\rangle=\langle \beta-1,\ 2,\ 3\rangle$",
        r"$\overrightarrow{PQ}=\langle 2,4,2\rangle$",
        DOT,
        r"$2(\beta-1)+4(2)+2(3)=2\beta-2+8+6=2\beta+12=0$ ، إذن $\beta=-6$",
    ],
    wrong={
        1: r"خطأ إشارة: $2\beta=-12$.",
        2: r"تنتج من نسيان $-1$ في $\beta-1$.",
        3: r"تحقّقي: $\beta=-4$ يعطي $-10+8+6=4\neq0$.",
    },
),
'n4q20': E(
    idea=r"$\overrightarrow{MN}=\overrightarrow{ON}-\overrightarrow{OM}$ ← نعبّر عن كلٍّ منهما بدلالة $\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$.",
    steps=[
        "## أولًا: ON",
        r"$ON:NB=3:1$ ، فـ $ON$ ثلاثة أرباع $OB$: $\overrightarrow{ON}=\frac34(4\vec{\mathbf{b}})=3\vec{\mathbf{b}}$",
        "## ثانيًا: OM",
        r"متجه موقع المنتصف = نصف مجموع متجهي موقع الطرفين: $\overrightarrow{OM}=\frac12(6\vec{\mathbf{a}}+4\vec{\mathbf{b}})=3\vec{\mathbf{a}}+2\vec{\mathbf{b}}$",
        "## ثالثًا: MN",
        r"$\overrightarrow{MN}=3\vec{\mathbf{b}}-(3\vec{\mathbf{a}}+2\vec{\mathbf{b}})=-3\vec{\mathbf{a}}+\vec{\mathbf{b}}$",
    ],
    wrong={
        1: r"هذا $\overrightarrow{NM}$ (الاتجاه معكوس).",
        2: r"$3\vec{\mathbf{b}}-2\vec{\mathbf{b}}=+\vec{\mathbf{b}}$.",
        3: r"هذا $\overrightarrow{ON}-\overrightarrow{OA}$ ، أي $\overrightarrow{AN}$ لا $\overrightarrow{MN}$.",
    },
),
'n4q21': E(
    idea=r"متجه بمقدار معلوم واتجاه معلوم = المقدار × متجه الوحدة في ذلك الاتجاه.",
    steps=[
        MAG,
        r"$|\langle 2,-1,2\rangle|=\sqrt{4+1+4}=3$",
        r"متجه الوحدة في عكس الاتجاه: $-\frac13\langle 2,-1,2\rangle=\left\langle -\frac23,\frac13,-\frac23\right\rangle$",
        r"نضرب في $6$: $\langle -4,2,-4\rangle$",
    ],
    wrong={
        1: r"هذا في اتجاه المتجه نفسه، والمطلوب عكسه.",
        2: r"لم يُقسم على المقدار $3$ أولًا؛ مقدار هذا المتجه $18$.",
        3: r"مقدار هذا المتجه $3$ لا $6$.",
    },
),
'n4q22': E(
    idea=r"نساوي الإحداثيات. المركبة $y$ في $l_2$ ثابتة ($-2$) ، فتعطي $t$ مباشرة.",
    steps=[
        r"$x$: $3+t=-4+2s$ ، $y$: $-1+t=-2$ ، $z$: $4-2t=3+s$",
        r"من $y$: $t=-1$",
        r"من $x$: $3-1=-4+2s$ ، إذن $2s=6$ و $s=3$",
        r"تحقّق $z$: $4-2(-1)=6$ و $3+3=6$ ✔",
        r"النقطة: $(3-1,\ -1-1,\ 4+2)=(2,-2,6)$",
    ],
    wrong={
        1: r"هذه نقطة على $l_1$ عند $t=1$ ، لكنها ليست على $l_2$ (مركبة $y$ فيه دائمًا $-2$).",
        2: r"هذه نقطة على $l_2$ عند $s=1$ ، لكنها ليست على $l_1$.",
        3: r"المركبة الثالثة: $4-2(-1)=6$ لا $2$.",
    },
),
'n4q23': E(
    idea=r"التوازي ⟺ متجها الاتجاه مضاعفان ← نجد المضاعف من المركبة المعلومة في الاثنين.",
    steps=[
        PAR,
        r"$\langle 2,a,-4\rangle=k\langle -1,3,b\rangle$",
        r"الأولى: $2=-k$ ، إذن $k=-2$",
        r"الثانية: $a=-2\times3=-6$",
        r"الثالثة: $-4=-2b$ ، إذن $b=2$",
        r"$a+b=-6+2=-4$",
    ],
    wrong={
        1: r"إشارة معكوسة؛ $k$ سالب.",
        2: r"من $-4=-2b$ تكون $b=+2$.",
        3: r"تنتج من أخذ $k=+2$؛ لكن $2=k(-1)$.",
    },
),
'n4q24': E(
    idea=r"نفكّ الضرب القياسي مثل ضرب قوسين جبريين، مع $\vec{\mathbf{a}}\cdot\vec{\mathbf{a}}=|\vec{\mathbf{a}}|^2$ و $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=\vec{\mathbf{b}}\cdot\vec{\mathbf{a}}$.",
    steps=[
        r"$(2\vec{\mathbf{a}}-\vec{\mathbf{b}})\cdot(\vec{\mathbf{a}}+3\vec{\mathbf{b}})=2\vec{\mathbf{a}}\cdot\vec{\mathbf{a}}+6\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}-\vec{\mathbf{b}}\cdot\vec{\mathbf{a}}-3\vec{\mathbf{b}}\cdot\vec{\mathbf{b}}$",
        r"نجمع الحدّين الأوسطين: $6\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}-\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=5\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}$",
        r"المقدار: $2|\vec{\mathbf{a}}|^2+5\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}-3|\vec{\mathbf{b}}|^2$",
        r"نعوّض: $2(4)+5(-1)-3(9)=8-5-27=-24$",
    ],
    wrong={
        1: r"تحقّقي من فكّ الأقواس: الحدود الأربعة $2|\vec{\mathbf{a}}|^2$ ، $6\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}$ ، $-\vec{\mathbf{b}}\cdot\vec{\mathbf{a}}$ ، $-3|\vec{\mathbf{b}}|^2$.",
        2: r"تنتج من أخذ $\vec{\mathbf{a}}\cdot\vec{\mathbf{b}}=+1$: $8+5-27$.",
        3: r"$-3|\vec{\mathbf{b}}|^2=-27$ يجعل الناتج سالبًا.",
    },
),
'n4q25': E(
    idea=r"الزاوية $ABC$ رأسها $B$ ← نستعمل المتجهين **الخارجين من $B$**: $\overrightarrow{BA}$ و $\overrightarrow{BC}$.",
    steps=[
        r"$\overrightarrow{BA}=A-B=\langle 1,0,1\rangle$ ، $\overrightarrow{BC}=C-B=\langle 0,-1,-1\rangle$",
        r"الضرب القياسي: $0+0-1=-1$",
        r"المقداران: $\sqrt2$ و $\sqrt2$",
        r"$\cos\theta=\dfrac{-1}{\sqrt2\times\sqrt2}=-\dfrac12$",
        r"جيب التمام سالب، فالزاوية منفرجة: $\theta=\pi-\frac{\pi}{3}=\frac{2\pi}{3}$",
    ],
    wrong={
        1: r"تنتج من استعمال $\overrightarrow{AB}$ بدل $\overrightarrow{BA}$ (أو إهمال الإشارة)؛ زاوية المثلث هنا منفرجة.",
        2: r"$\cos\frac{5\pi}{6}=-\frac{\sqrt3}{2}\neq-\frac12$.",
        3: r"$\cos\frac{\pi}{6}=\frac{\sqrt3}{2}$ ، وجيب التمام هنا سالب.",
    },
),
'n4q26': E(
    idea=r"$X\ge3$ يعني أن أول محاولتين فشل ← $(1-p)^2$.",
    steps=[
        GEO,
        r"$\frac1p=4$ ، إذن $p=\frac14$ و $1-p=\frac34$",
        r"$P(X\ge3)=P(X>2)=\left(\frac34\right)^2=\frac{9}{16}$",
    ],
    wrong={
        1: r"هذا $\left(\frac34\right)^3=P(X\ge4)$.",
        2: r"هذا $1-\frac{9}{16}=P(X\le2)$.",
        3: r"هذا $P(X=3)$ فقط.",
    },
),
'n4q27': E(
    idea=r"«على الأكثر مرة» ← $X=0$ أو $X=1$.",
    steps=[
        BIN,
        r"$X\sim B(5,\ 0.2)$",
        r"$P(X=0)=(0.8)^5=0.32768$",
        r"$P(X=1)=\binom51(0.2)(0.8)^4=5\times0.2\times0.4096=0.4096$",
        r"$P(X\le1)=0.32768+0.4096\approx0.7373$",
    ],
    wrong={
        1: r"هذا $P(X\ge2)$ (المتممة).",
        2: r"هذا $P(X=1)$ فقط.",
        3: r"هذا $P(X=0)$ فقط.",
    },
),
'n4q28': E(
    idea=r"المظلّل طرفان متماثلان ← كلٌّ منهما $0.0107$.",
    steps=[
        SYM,
        r"$P(Z>2.3)=P(Z<-2.3)=0.0107$ (بالتماثل)",
        r"المظلّل: $0.0107+0.0107=0.0214$",
    ],
    wrong={
        1: r"هذا طرف واحد؛ المظلّل طرفان.",
        2: r"هذا الجزء غير المظلّل (الوسط).",
        3: r"هذا $P(0<Z<2.3)$.",
    },
),
'n4q29': E(
    idea=r"الفترة متماثلة حول الوسط ($200\pm24$) ← $P(-c<Z<c)=2P(Z<c)-1$.",
    steps=[
        STD,
        r"$\sigma=\sqrt{400}=20$",
        r"$z=\dfrac{176-200}{20}=-1.2$ و $z=\dfrac{224-200}{20}=1.2$",
        r"$2(0.8849)-1=0.7698$",
    ],
    wrong={
        1: r"هذا نصف المساحة (من $0$ إلى $1.2$).",
        2: r"هذا $P(Z<1.2)$ فقط.",
        3: r"هذا $P(-1<Z<1)$؛ لكن $z=\frac{24}{20}=1.2$.",
    },
),
'n4q30': E(
    idea=r"مجهولان ← معادلتان: كل احتمال يعطي قيمة $z$ ، وكل $z$ يعطي معادلة $\frac{x-\mu}{\sigma}=z$.",
    steps=[
        "## المعادلة الأولى",
        r"$P(X<70)=0.8413=P(Z<1)$ ، إذن $\dfrac{70-\mu}{\sigma}=1$ ، أي $70-\mu=\sigma$",
        "## المعادلة الثانية",
        r"$0.0668<0.5$ ، فـ $z$ سالبة: $0.0668=1-0.9332=P(Z<-1.5)$",
        r"$\dfrac{45-\mu}{\sigma}=-1.5$ ، أي $45-\mu=-1.5\sigma$",
        "## الحلّ",
        r"نطرح الثانية من الأولى: $70-45=\sigma+1.5\sigma$ ، أي $25=2.5\sigma$ ، إذن $\sigma=10$",
        r"$\mu=70-10=60$",
    ],
    wrong={
        1: r"تحقّق المعادلة الأولى فقط: $\frac{45-50}{20}=-0.25\neq-1.5$.",
        2: r"تحقّق الأولى فقط: $\frac{45-55}{15}\approx-0.67\neq-1.5$.",
        3: r"تحقّق الأولى فقط: $\frac{45-62.5}{7.5}\approx-2.33\neq-1.5$.",
    },
    tip=r"في أسئلة المجهولين، عوّضي كل بديل في المعادلتين معًا؛ كثير من البدائل يحقّق واحدة فقط.",
),
}
