# تقرير جودة الأسئلة

## المصادر التي اعتمدنا عليها

| المصدر | ماذا أخذنا منه |
|---|---|
| **كتاب الطالب + كتاب التمارين** (الرياضيات، المسار الأكاديمي، الصف الثاني عشر، طبعة 2025، المركز الوطني لتطوير المناهج، الفصلان) | أسماء الوحدات والدروس الرسمية، المصطلحات والرموز (السعة الرئيسة $-\pi<\text{Arg}(z)\le\pi$، «الشعاع»، $X\sim Geo(p)$، $X\sim N(\mu,\sigma^2)$ ، $\langle\,\rangle$ و $\hat i,\hat j,\hat k$)، ونمط «اختبار نهاية الوحدة» |
| **الامتحان الوزاري 2 تموز 2026 – نموذج (1)** (50 فقرة، 3 ساعات، 12 صفحة) | توزيع الأسئلة على الوحدات، نمط الصياغة، مستوى الصعوبة، أنواع المشتّتات |
| **الامتحان التجريبي الموحّد 19 أيار 2026 – الفصل الثاني** (30 فقرة، 90 دقيقة) | نمط أسئلة التكامل والمتجهات والإحصاء |
| **امتحان 2025 (جيل 2007) – الورقة الثانية** | أسئلة التكامل والحركة والمساحات في السنة السابقة |
| ملفات ودورات الأساتذة المتاحة للعموم (سامر رشاد – جو أكاديمي، محمد صالح، فخري جرار ومحمد حميدي – وتد، جمعة عياش، محمد العبدالات – حصص) | ترتيب الدروس كما يُدرَّس، وأسلوب «ملفات الأسئلة الوزارية» و«الامتحانات النهائية» |

## ما تعلّمناه عن طريقة الوزارة

- **التوزيع (2026):** الوحدة 1: 3 فقرات · الوحدة 2: 5 · الوحدة 3: 10 · الوحدة 4: 7 · الوحدة 5: 12 · الوحدة 6: 8 · الوحدة 7: 5 (الامتحان التجريبي الشامل في الموقع يتبع هذا التوزيع نفسه).
- **الشكل:** البدائل مرقّمة a, b, c, d على ورقة الأسئلة (وتقابلها أ، ب، ج، د على ورقة القارئ الضوئي).
- **الأنماط المتكرّرة:** «إذا كان ... فإنّ قيمة الثابت ... هي»، ونصّ مشترك لفقرتين، وأسئلة تعتمد على شكل (منحنيان مستقيمان على شبكة، منطقة مظلّلة، منحنى سرعة–زمن، متوازي مستطيلات، متوازي أضلاع بمتجهات)، وجدول مختصر لقيم $P(Z<z)$ داخل السؤال، وحلول معادلات مثلثية في فترات مثل $(\pi,2\pi)$ مع بدائل خارج الفترة.
- **الصعوبة:** أعلى من التمارين المباشرة؛ تكاملات تجمع أكثر من طريقة، ومشتّتات مدروسة (خطأ إشارة، نسيان معامل، الخلط بين التباين والانحراف، الإزاحة بدل المسافة).

## ما تغيّر في بنك الأسئلة (الإصدار الثاني)

- أُعيدت كتابة **276 سؤالًا** في 23 اختبارًا على نمط الوزارة، **بأرقام جديدة**؛ ولا يوجد سؤال منسوخ من الكتاب (فُحصت كل الصيغ آليًّا مقابل نص الكتابين وكتابي التمارين، وما بقي من تطابقات هو مقادير عامة قصيرة مثل $\tan\theta=2$ تظهر في سياق مختلف تمامًا).
- أسماء الوحدات والدروس مطابقة للكتاب (مثلًا: الوحدة 3 «التفاضل وتطبيقاته» بخمسة دروس، والمماس والحركة ضمن دروسها).
- 14 سؤالًا بأشكال، وجداول $z$ داخل الأسئلة، والبدائل بالأحرف a–d.
- توزيع الصعوبة: 77 سهل، 124 متوسط، 75 صعب.

## كيف نضمن أن كل سؤال صحيح

كل سؤال يمرّ بثلاثة فحوص آلية قبل أن يصل إلى الموقع (`src/global/question-bank/qb.py`):

1. **الإجابة:** يحسب sympy الإجابة بشكل مستقل، ويجب أن تطابق البديل الصحيح فقط ولا تطابق أيّ بديل آخر.
2. **نص البدائل:** نص كل بديل كما يراه الطالب يُحلَّل ويُقارَن بالقيمة التي فُحصت، فأيّ خطأ مطبعي في بديل يوقف البناء.
3. **نص السؤال:** الصيغ داخل نص السؤال تُحلَّل وتُقارَن بالمقدار الذي حُسبت منه الإجابة.

إضافةً إلى ذلك: التكاملات غير المحددة تُفحص بالاشتقاق، وحلول المعادلات المثلثية تُوجد عدديًّا كلها داخل الفترة، وقيم جدول التوزيع الطبيعي تُحسب من الدالة الدقيقة وتُقرَّب لأربع منازل، وجميع الصيغ (2803 صيغة) تُعرض في KaTeX دون أخطاء.

5 أسئلة وصفية فقط (المناطق المظلّلة في المستوى المركّب، ووصف الشعاع، وشروط تجربة ذي الحدّين) لا يمكن فحصها آليًّا، وقد رُوجعت يدويًّا مع الأشكال. ثم قُرئت **جميع** الأسئلة وحلولها قراءةً بشرية للتأكد من وضوح الصياغة وعدم وجود لبس.

## الامتحانات التجريبية للفصل الأول — النماذج 1–5

**الشكل:** لم تنشر الوزارة امتحانًا تجريبيًّا للفصل الأول، فاعتمدنا شكل التجريبي الوزاري الرسمي للفصل الثاني (30 فقرة في 90 دقيقة)،
وتوزيع فقرات الفصل الأول في امتحان 2026 (الفقرات 1–25: 3·5·10·7) مُكبَّرًا إلى 30: **4 · 6 · 12 · 8**.

**التغطية:** 150 سؤالًا جديدًا تغطّي 87 نمطًا مختلفًا مجمّعة في 21 مهارة، ومنها كل أنماط فقرات الفصل الأول في امتحان 2026:

| فقرة 2026 | النمط | في النماذج |
|---|---|---|
| 1 | حل معادلة كثير حدود بمعلومية جذر | م1·1 ، م4·1 |
| 2 | تجزئة بعامل خطي مكرر | م1·3 ، م4·4 ، م5·4 |
| 3 | نظرية الباقي وإيجاد ثابت | م2·2 ، م4·2 ، م5·2 |
| 4 | نصف الزاوية مع تحديد الربع | م1·5 ، م3·7 ، م5·7 |
| 5 | أبسط صورة بالمجموع والفرق | م1·6 ، م3·6 ، م4·5 |
| 6 | مقدار مكافئ | م2·6 ، م4·6 |
| 7 | معادلة تربيعية في نسبة مع رفض حل | م1·9 (وتربيعية دون رفض: م2·10 ، م3·9) |
| 8 | معادلة فيها مقلوب نسبة في فترة مع بدائل خارجها | م1·10 ، م4·9 ، م5·10 |
| 9 | تركيب من الاقتران ومشتقته | م1·11 ، م3·12 |
| 10 | ثابت بمعلومية قيمة المشتقة | م1·12 ، م2·15 ، م3·15 ، م5·15 |
| 11 | تركيب المشتقات العليا | م1·13 ، م3·12 (ومشتقات عليا: م2·14 ، م4·12 ، م4·15) |
| 12 | معدل تغير في سياق حياتي | م1·18 ، م3·18 ، م4·18 ، م5·18 |
| 13 | لوغاريتم لأساس غير e لاقتران مركب | م1·14 ، م3·17 ، م5·17 |
| 14 | المشتقة من التمثيل البياني | فقرة 16 أو 17 في كل نموذج |
| 15 | مشتقة المعادلات الوسيطية | م1·19 ، م4·19 |
| 16 | اشتقاق ضمني فيه أسّي/لوغاريتم | م1·20 ، م2·20 ، م3·21 |
| 17 | مقطع مماس منحنى ضمني | م1·21 ، م5·21 |
| 18 | معدلات مرتبطة مع تحويل لترات | م1·22 ، م4·22 |
| 19 | الصورة المثلثية بشروط | م1·23 ، م3·23 |
| 20–21 | نص مشترك لعمليات على عددين | م1·24–25 ، م3·26–27 ، م4·24–25 ، م5·26–27 |
| 22 | ثابت يجعل العدد حقيقيًّا/تخيّليًّا | م1·26 ، م3·24 ، م5·25 |
| 23 | معادلة تربيعية بمعلومية جذر مركب | م2·26 ، م4·27 |
| 24 | الزاوية الصغرى بين عددين | م1·28 ، م3·28 |
| 25 | منطقة في المستوى المركب من شكل | الفقرة 30 في كل نموذج |

**واقعية الورقة:** ترتيب البدائل ثابت كالورقة المطبوعة، والإجابات الصحيحة موزّعة بالتساوي تقريبًا على a/b/c/d في كل نموذج (8·8·7·7)
دون تكرار الحرف نفسه ثلاث مرات متتالية، وكل نموذج يحوي شكلين، ونموذج (5) هو الأصعب.

**الصحة:** الفحوص الثلاثة نفسها (145 سؤالًا آليًّا + 5 أسئلة مناطق مُراجَعة يدويًّا مع أشكالها)، وفحص عدم التكرار مع بنك الوحدات وبين النماذج.

## الامتحانات التجريبية للفصل الأول — النماذج 6–10

**المراجع:** أوراق الوزارة الرسمية من أرشيفها (2020–2026، في `src/semesters/semester-1/previous-ministry/`). قُرئت فقرات الفصل الأول
واحدة واحدة في: ورقة 2 تموز 2026 لجيل 2008 (الفقرات 1–25 هي مخطّط الفصل الأول)، وورقة 2026 للمنهاج القديم، وأوراق 2023–2025
(الدورتان)، ودُوّن تحليل طريقة الوزارة في `previous-ministry/ANALYSIS.md`.

**كيف كُتبت:** كل فقرة من الفقرات الـ150 «أخت» لفقرة وزارية محدّدة: المهارة نفسها، وبنية النص نفسها، ونوع الاقتران والأرقام نفسه،
والصعوبة نفسها، وطريقة بناء البدائل نفسها، مع اقتران وأرقام جديدة. مثال: فقرة 2026 رقم 13 $f(x)=\log_3(2+\ln x)$ عند $e$ صارت
$f(x)=\log_2(3+\ln x)$ عند $e$ ، وبدائلها من المفتاحين نفسيهما ($e$ أو $\frac1e$ × قوة اللوغاريتم). الفقرة الوزارية التي بُنيت عليها
كل فقرة مكتوبة فوقها في `s1_papers_6_10.py` ، والجدول الكامل في القسم 9 من `ANALYSIS.md`. مصادرها: 2026 (77)، 2025 (20)،
2025 التكميلي (18)، 2023 (17)، 2024 (16)، 2024 التكميلي (14)، 2026 للمنهاج القديم (13) (بعض الفقرات لها نموذجان).

- **كل نموذج يغطّي أنماط فقرات الفصل الأول في امتحان 2026 بالترتيب نفسه**، والفقرات الباقية من أوراق 2023–2025 ضمن منهاج 2008
  (الحركة، ميل العمودي لـ $a^{x}$ ، إيجاد ثابت من $f'(a)$ ، لوغاريتم حاصل ضرب، الاشتقاق اللوغاريتمي، قاعدة السلسلة من جدول قيم،
  جسيم يتحرّك على منحنى، طريقان متعامدان، مربّع في المستوى المركب، المرافق من الشكل، أكبر سعة على دائرة، …). 69 نمطًا في
  21 مهارة، منها 13 نمطًا لا يوجد في النماذج 1–5. لم تُستعمل القيم القصوى والتقعّر والتحسين لأنها ليست في وحدات الفصل الأول لجيل 2008.
- **بدائل على طريقة الوزارة:** 97 فقرة بدائلها شبكة من «مفتاحين» لخطأين شائعين (الإشارة × المقلوب، المركز × نوع الخط، $\ln a$
  في البسط أو المقام × عامل السلسلة، تحويل الوحدات × القطر أو نصف القطر …)، والبقية قوائم قيم من النوع نفسه كما في الوزارة.
  كل بديل خطأ مشروح بالخطأ الذي يُنتجه، وإن لم يكن وراءه خطأ محدد يُفحص بالتعويض.
- **المناطق في المستوى المركب مفحوصة آليًّا:** كل بديل شرط على $z$ ، والشكل يُرسم من شرط البديل الصحيح، ويُفحص أن كل بديل خطأ يختلف
  عنه داخل المستوى أو على الحدود (المتقطّع والمتصل).
- **17 شكلًا كما في الأوراق الوزارية:** منحنيا اقترانين على شبكة، منحنى اقتران واحد، خزّان أسطواني، طائرة مُسيّرة، مثلث متطابق الضلعين،
  نقطة في المستوى المركب، مربّع، عمود منصّف، ومناطق (قرص مع زاوية، حلقة، زاوية، قرص مع عمود منصّف، قرص).

**الصعوبة:** 43 سهلًا · 90 متوسطًا · 17 صعبًا (النماذج 1–5: 31 · 79 · 40). النماذج الجديدة أقرب إلى مستوى الورقة الوزارية: فقرات
2026 في معظمها خطوة أو خطوتان مع فخّ واحد، والصعوبة فيها من دقة البدائل لا من طول الحل.

**واقعية الورقة:** الإجابات الصحيحة موزّعة 8·8·7·7 على a/b/c/d في كل نموذج.

**الصحة:** الفحوص الثلاثة لكل الأسئلة الـ150 آليًّا (لا يوجد سؤال يدوي) مع فحص المناطق، و3293 صيغة في النماذج الخمسة (الأسئلة والبدائل
والحلول والشروح) تُعرض في KaTeX دون أخطاء. وقورنت النصوص بالنماذج 1–5 وبنك الوحدات، فاستُبدلت 6 فقرات كانت تعيد صيغة أو سياقًا
مستعملًا بأرقام جديدة.

**لا تتأثر محاولات الطلاب السابقة:** النماذج 6–10 أُضيفت بعد النماذج 1–5، فبقيت أسئلة النماذج 1–5 وترتيب بدائلها كما هي تمامًا.

## الامتحانات التجريبية للفصل الثاني (5 نماذج)

**الشكل:** مطابق للامتحان التجريبي الوزاري الموحّد للفصل الثاني (19 أيار 2026): 30 فقرة في 90 دقيقة، الوحدة 5 في الفقرات 1–16،
والوحدة 6 في 17–25، والوحدة 7 في 26–30، مع جدول مختصر لقيم $P(Z<z)$ يخدم آخر فقرتين أو ثلاث (كما في الفقرات 48–50 من امتحان 2026).

**التغطية:** 150 سؤالًا جديدًا تغطّي 80 نمطًا مجمّعة في 17 مهارة، ومنها كل أنماط فقرات الفصل الثاني في امتحان 2026:

| فقرة 2026 | النمط | في النماذج |
|---|---|---|
| 26 | تكامل ظل/ظل تمام/قاطع تمام لزاوية مضاعفة | م1·1 ، م4·1 ، م5·1 |
| 27 | تكامل الاقتران الأسي لأساس غير e | م1·2 ، م2·6 ، م3·2 ، م4·2 |
| 28 | تكامل محدود بتقليص القوة = $a\pi$ | م1·3 (وتقليص القوة: م5·3 ، ضعف الزاوية: م2·3 ، م3·3) |
| 29 | الاقتران بمعلومية مشتقته ونقطة | م1·4 ، م2·5 ، م3·4 ، م4·4 ، م5·4 (من المشتقة الثانية) |
| 30 | المسافة الكلية من سرعة مثلثية/كثيرة حدود | م1·5 ، م3·5 ، م4·5 ، م5·5 |
| 31 | تبسيط ثم تعويض | م3·8 |
| 32 | قوى الاقترانات المثلثية بالتعويض | م1·7 ، م2·7 ، م3·7 ، م4·7 ، م5·9 |
| 33 | كسور جزئية بعامل تربيعي | م1·11 |
| 34 | تعويض ثم تكامل بالأجزاء | م1·13 ، م2·13 ، م5·12 |
| 35 | المساحة وإيجاد ثابت | م1·14 |
| 36 | حجم دوراني من شكل | م1·15 (وطريقة الحلقات: م3·15 ، م5·15) |
| 37 | معادلة تفاضلية بفصل المتغيرات ومتطابقات | م1·16 ، م4·16 ، م5·16 |
| 38 | معادلة مستقيم بمعلومية متجه موقع ومتجه اتجاه | م1·17 ، م3·21 ، م4·17 |
| 39–40 | نص مشترك: نقطة ومتجه موقع، ثم ثابت | م1·18–19 ، م4·18–19 |
| 41 | متوازي مستطيلات/مكعب من شكل | م1·20 ، م3·18 ، م5·18 |
| 42 | الاستقامة والتوازي وإيجاد ثابت | م1·21 ، م2·19 ، م4·23 |
| 43 | ضرب قياسي لمتجهات بين ثلاث نقاط | م2·25 |
| 44 | متوازي أضلاع/مثلث بمتجهات ونسبة من شكل | م5·19 ، م2·18 ، م3·20 ، م4·20 |
| 45 | مساحة مثلث/زاوية فيه بالضرب القياسي | م1·25 ، م4·25 |
| 46 | التوزيع الهندسي: نسبة احتمالين | م1·26 ، م5·26 |
| 47 | ذو الحدين في سياق ضبط الجودة | م1·27 (و«على الأكثر»: م4·27) |
| 48 | احتمال طبيعي باستعمال الجدول | م1·28 ، م2·29 ، م3·28 ، م4·29 ، م5·30 |
| 49 | فترة متماثلة وإيجاد ثابت | م1·29 ، م5·28 |
| 50 | الانحراف المعياري من نسبة مئوية | م1·30 ، م2·30 ، م5·29 |

وأنماط التجريبي الموحّد غير الموجودة في امتحان 2026 ممثَّلة أيضًا: الموقع من سرعة متعددة القاعدة (م2·4)، الحركة من منحنى
السرعة–الزمن (م2·14 ، م4·14)، مساحة مظلّلة من شكل (م3·14 ، م5·14)، الحل الخاص لمعادلة تفاضلية (م2·16 ، م3·16)،
تقاطع مستقيم مع مستوى إحداثي (م2·21)، نقطة تقاطع مستقيمين (م1·23 ، م4·22)، مسقط العمود (م2·23 ، م5·23)،
مساحة من منحنى التوزيع الطبيعي (م2·28 ، م4·28)، وإيجاد $\mu$ و/أو $\sigma$ (م3·30 ، م4·30).

**ليست نسخًا:** قورن كل سؤال بامتحان 2026 والتجريبي الموحّد وبنك الوحدات والكتاب. كل سؤال كان مجرد تغيير أرقام في سؤال رسمي
(مثل $\int\cot\frac{x}{2}$ ← $\int\cot\frac{x}{3}$) أُعيدت كتابته بفكرة أو بنية مختلفة للمهارة نفسها (19 سؤالًا، و9 أسئلة أخرى لتشابهها مع بنك الوحدات)، وفُحصت الصيغ آليًّا
حتى بعد استبدال الأرقام، فلا يوجد تطابق مع أيّ مصدر.

**واقعية الورقة:** الإجابات الصحيحة موزّعة 8·8·7·7 على a/b/c/d في كل نموذج، ولكل نموذج شكلان أو أكثر (منحنى سرعة–زمن،
منطقة مظلّلة، مثلث/متوازي أضلاع بمتجهات، متوازي مستطيلات، منحنى طبيعي)، ونموذج (5) هو الأصعب.

**الصحة:** الفحوص الثلاثة نفسها لكل الأسئلة الـ150 (كلها آليًّا، ولا يوجد سؤال يدوي)، والمعادلات التفاضلية تُفحص بالتعويض في المعادلة
والشرط الأوّلي، وجميع الصيغ تُعرض في KaTeX دون أخطاء.

## الشرح المفصّل في كل الوحدات والنماذج (تشرين الأول 2026)

أُعيدت كتابة الشرح بعد التسليم بالطريقة المعتادة البسيطة في الوحدات 3 و4 و5 و6 و7 وفي نماذج الفصل الأول 6–10، وأُكملت الأسئلة التي كان شرحها قصيرًا في باقي النماذج: «ماذا يطلب السؤال؟» ثم مراحل معنونة، وكل خطوة حسابية مكتوبة (التعويض بالقيم، توحيد المقامات، الإشارات حسب الربع، $e^0=1$ و $\ln1=0$…)، وتحقّق بالاشتقاق أو بالتعويض حيث يفيد. متوسط الخطوات المرقّمة لكل سؤال: الوحدة 3: 6.3 · الوحدة 4: 5.3 · الوحدة 5: 6.0 · الوحدة 6: 4.4 (مع مراحل معنونة) · الوحدة 7: 5.5 · نماذج الفصل الأول: 4.8 · نماذج الفصل الثاني: 4.7، ولا يوجد سؤال بخطوتين أو أقل. لم يتغيّر أيّ سؤال أو بديل أو ترتيب (فُحصت بيانات الأسئلة في كل ملف مولّد مقابل الإصدار السابق)، وجميع الصيغ تُعرض في KaTeX دون أخطاء.

## الوحدة 5 (التكامل) — الاختبارات 5–10

**الشكل:** 12 فقرة في كل اختبار بترتيب فقرات التكامل في ورقة 2026 (الفقرات 26–37): تكامل اقترانات خاصة والحركة، ثم التعويض،
ثم الكسور الجزئية، ثم الأجزاء، ثم المساحات والحجوم، ثم المعادلات التفاضلية. أصبح للوحدة 10 اختبارات (120 سؤالًا).

**طريقة الكتابة:** كل فقرة «أخت» لفقرة وزارية مسمّاة (المصدر مكتوب في تعليق فوق كل `Q(...)` في
`src/semesters/semester-2/unit-5/u5_exams_5_10.py`): المهارة وبنية النصّ ونوع الاقتران والصعوبة نفسها، وتتغيّر الأرقام والاقتران،
والبدائل شبكة 2×2 من خطأين شائعين (إشارة، نسيان معامل السلسلة، الضرب بدل القسمة، الإزاحة بدل المسافة، نسيان الحدّ السفلي…)
أو قائمة قيم من النوع نفسه. النماذج المستعملة: 2026 — 17، 2025 — 10، 2024 — 10، 2024 التكميلي — 9، 2023 — 9،
2023 التكميلي — 9، 2026 المعيدون — 8، 2025 التكميلي — 7. سياقان جديدان (سعر قطعة، أعداد الأسماك) لم يُستعملا في أي بنك آخر،
ولا تتكرّر أي صيغة من نصوص الأسئلة مع الاختبارات 1–4 أو نماذج الفصل الثاني.

**الصعوبة:** 16 سهلًا · 41 متوسطًا · 15 صعبًا.

**الشرح:** كل أسئلة الوحدة الـ120 (القديمة والجديدة) لها شرح مفصّل بالطريقة المعتادة في الكتاب: مراحل معنونة، وكل خطوة حسابية
مكتوبة (التعويض بالحدود، توحيد المقامات، قيم $e^0$ و $\ln1$…)، وتحقّق بالاشتقاق أو بالتعويض، وسبب خطأ كل بديل باسم الخطأ الذي
بُني منه. «الطريقة الأسرع» تظهر فقط حين توجد طريقة حقيقية أقصر.

**العرض:** أثناء الحلّ لا يظهر اسم الدرس ولا مستوى الصعوبة (ولا توزيع الصعوبة في صفحة الوحدة)؛ يظهران في المراجعة بعد التسليم
مع جدول النتيجة حسب الدرس وحسب مستوى السؤال.

**الصحة:** الفحوص الثلاثة لكل الأسئلة الـ72 الجديدة آليًّا (لا سؤال يدوي)، وجميع صيغ الوحدة (3398 صيغة) تُعرض في KaTeX دون أخطاء،
وأسئلة الاختبارات 1–4 لم تتغيّر (تغيّر شرحها فقط).

| الفقرة | النموذج الوزاري · شبكة البدائل |
|---|---|
| u5e5q1 | 2026 #26: integral of cot(x/2); options = ln\|sin\| vs -ln\|cos\| x coefficient 2 vs 1/2 |
| u5e5q2 | 2026 #27: a^(linear) divided by ln a; options = exponent (extra 1/2 or not) x ln a vs (ln a)^2 |
| u5e5q3 | 2026 #28: integral of sin^2 over an interval = a pi; options = +-1/2, +-1/4 (power reduction, missing 1/2) |
| u5e5q4 | 2026 #29: dy/dx = e^(kx) - e^(-x), curve through (0, c); options = sign of the e^(-x) term x sign of the constant |
| u5e5q5 | 2026 #30: v = k sin(t), total distance over several arches; options = distance, displacement, arch-count and chain slips |
| u5e5q6 | 2026 #31: x^n (1 + c/x)^n simplifies to (x + c)^n; options = (x+c)^(n+1)/(n+1), (x+c)^n/n, term-by-term slips |
| u5e5q7 | 2026 #32: sin^2(kx)/cos^4(kx) = tan^2 sec^2; options = sign x cot vs csc (the cot/csc version) |
| u5e5q8 | 2026 #33: (x^2 + a)/(x^3 + bx) = A/x + Bx/(x^2 + b); options = sign of A x the 1/2 from the ln(x^2 + b) term |
| u5e5q9 | 2026 #34: sec^2(sqrt x) by substitution then parts; options = signs of the two terms (csc^2 version) |
| u5e5q10 | 2024s #8 / 2026 #35: shaded area under k/(x + c) equals a logarithm -> k; options = ratio of logs vs of numbers x inverted |
| u5e5q11 | 2026 #36: volume of the region under a root of (x times exponential); options = sign of 1 x the parts sign slip |
| u5e5q12 | 2026 #37: dy/dx = 1/(trig^2 x . trig^2 y); options = 1/2 vs 1/4 sin 2y x its sign |
| u5e6q1 | 2026r #2: Pythagorean quotient whose denominator is 1; options = sign of the trig term x sign of x |
| u5e6q2 | 2026r #1: k e^(mx) + a^(nx); options = coefficient of e (divided vs multiplied) x chain factor in a^(nx) |
| u5e6q3 | 2025 #4: integral from a to 2a of (x + c)/x equals a logarithm -> a; options = coefficient of ln dropped x [x] read as 2a |
| u5e6q4 | 2024 #5: f'(x) = (p e^x + q)^2 and f(0) -> f; options = 1/2 kept in e^(2x) x the constant integrated to a multiple of x |
| u5e6q5 | 2026r #5: v = k trig(t/n), total distance on an interval where v changes sign once |
| u5e6q6 | 2026r #9 / 2024s #10: definite integral of x times a root of (x + c); options = sign x (x = u - c vs u + c) |
| u5e6q7 | 2026r #10 / 2024 #7: odd power of sin times a power of cos; options = signs of the two terms |
| u5e6q8 | 2026r #7 / 2025s #10: (px + q)/(x^2 - cx); options = constants swapped x sign of the second |
| u5e6q9 | 2024 #10: ln of a root of x by parts; options = sign of the x term x the 1/n factor on it |
| u5e6q10 | 2025 #3: area under c - a^x in the first quadrant (figure); options = divide vs multiply by ln a x lower limit kept |
| u5e6q11 | 2026 #36: volume about the x-axis of an exponential on [0, ln c]; options = square kept, 1/2 kept, lower limit kept |
| u5e6q12 | 2026r #12: dy/dx = y times a polynomial, through a point; options = 1/2 kept x sign of the constant |
| u5e7q1 | 2024s #2: 1/(sin^2 cos^2) through the double angle; options = sign x tan vs cot |
| u5e7q2 | 2025s #1: k root(x) - a^(-x); options = power-rule coefficient (divide vs multiply) x sign of the a^(-x) term |
| u5e7q3 | 2024s #5 / 2023 #4: definite integral of \|linear\| across its zero; options = no absolute value, one triangle, missing 1/2 |
| u5e7q4 | 2024 #6: displacement for v = k trig(t/n); options = sign x chain factor (multiplied instead of divided) |
| u5e7q5 | 2025 #8: price rate p'(x) = k x / root(x^2 + c) and one price -> P(x); options = coefficient (1/2 slip) x sign of the constant |
| u5e7q6 | 2025 #6: root(a x^2 - x^4) on a negative interval (\|x\| = -x); options = sign (\|x\| = x slip) x the missing 1/2 |
| u5e7q7 | 2025 #2: improper fraction over a linear factor; options = quotient term halved or not x sign of the ln term |
| u5e7q8 | 2023 #9: k x^n ln x by parts; options = power of x in the first term x sign of the second |
| u5e7q9 | 2023 #10: k x trig(kx) by parts; options = sign of the first term x sign of the second |
| u5e7q10 | 2025s #3: area under x(x - c)^2 between its zeros (figure); options = expansion slips |
| u5e7q11 | 2026 #36 family (washers, figure): volume between a line and a parabola; options = squared difference, pi x area, x^2 not squared |
| u5e7q12 | 2025 #12: dy/dx = ((linear) trig y)^2 / (linear), through a point; options = tan vs -cot x sign of the constant |
| u5e8q1 | 2025 #1: a quotient that collapses with sum-to-product; options = sign x sin vs cos |
| u5e8q2 | 2024 #1: a^(-x) plus a trig function of -x; options = sign of each term |
| u5e8q3 | 2025s #2: \|linear\| / (its negative) on an interval where the sign is fixed; options = sign x answering the integrand value |
| u5e8q4 | 2024s #6: population changing at k e^(rt), initial count -> P(t); options = decimal slip in k/r x constant adjusted or not |
| u5e8q5 | 2024s #7: position after a time for v = k sin(t/n), given the start; options = start added or not x chain slip |
| u5e8q6 | 2025 #7: e^(nx) times a power of (1 - c e^(-x)) becomes e^x (e^x - c)^k; options = which bracket x sign |
| u5e8q7 | 2024s #9: f'/f^n with a trig inner function; options = sign x 1/(n-1) vs (n-1) |
| u5e8q8 | 2025 #10: 1/(x^2 (x - c)) with a repeated factor; options = sign of the logs x sign of 1/x |
| u5e8q9 | 2023s #11: integral of x f'(x) from given values by parts; options = subtract vs add the integral x f(b) vs b f(b) |
| u5e8q10 | 2026 #35 / 2026r #6: shaded area under c/(x - h) from a fixed line to a equals k -> a (figure); options = coefficient x shift |
| u5e8q11 | 2026 #36: volume of a squared trig function on a special interval; options = pi kept x tan of the right angle |
| u5e8q12 | 2025s #12: x dy/dx = (power of y)(linear), through (1, 1); options = sign of the y side x sign of the constant |
| u5e9q1 | 2023 #2: 1/trig^2(kx) plus a constant; options = tan vs -cot x the constant integrated to cx or left as c |
| u5e9q2 | 2023 #1: integral of (a^c)^x on [0, 1]; options = lower limit subtracted or not x the factor c in the denominator |
| u5e9q3 | 2023s #4: definite integral of a piecewise function across its break; options = one piece only, chain slip |
| u5e9q4 | 2023 #5: f' a quotient by a power of x, and f(1) -> f; options = power rule (divided or not) x sign of the 1/x term |
| u5e9q5 | 2025s #7: position from v = c - (linear)^2 and the initial position; options = start added or not x chain slip |
| u5e9q6 | 2023s #7: (linear) times a cube root of a quadratic whose derivative is a multiple of it; options = sign x cube vs fourth root |
| u5e9q7 | 2023s #8: a power of a trig function times sin 2x; options = sign x the 2 of sin 2x |
| u5e9q8 | 2024 #9: c/((x - p)(x + q)); options = difference vs sum of logs, ln of the product |
| u5e9q9 | 2023 #11: definite integral of x a^x by parts; options = sign of the second term x lower limit kept |
| u5e9q10 | 2024 #12 / 2023 #12: velocity-time graph, start given -> final position; options = displacement vs distance x start added or not |
| u5e9q11 | 2026 #36: volume of the root of a trig function; options = sign (ln cos) x ln root 2 vs ln 2 |
| u5e9q12 | 2024 #13: dy/dx = e^(px + y) through the origin; options = 1/p kept x sign |
| u5e10q1 | 2023s #2: trig of (c - kx); options = sign x divide vs multiply by k |
| u5e10q2 | 2024s #1: integral of (1/a)^(linear); options = sign (ln of 1/a) x chain factor |
| u5e10q3 | 2024 #3: integral of 1/(a + x/k) from 0 to ma, a > 0; options = factor k kept x limits reversed |
| u5e10q4 | 2023s #5: f' = e^x -+ e^(-x) and a point -> f; options = sign of e^(-x) x the constant (e^0 = 1) |
| u5e10q5 | 2023 #6: displacement for v = k t/(t^2 + c); options = sign x the 1/2 from du = 2t dt |
| u5e10q6 | 2024 #8: definite integral of k x (1 - x)^n by substitution; options = sign (limits) x (x = 1 - u vs 1 + u) |
| u5e10q7 | 2024s #11: (px + q)/(cx - x^2); options = sign of the second log, ln of the denominator |
| u5e10q8 | 2025s #5: improper fraction integrated into a given form -> a constant; options = quotient coefficient slips |
| u5e10q9 | 2023s #9 family: definite integral of x trig x by parts; options = sign of the second term, lower limit |
| u5e10q10 | 2023s #12: velocity-time graph starting above the axis, start given -> final position |
| u5e10q11 | 2025 #3 family (figure): area between a parabola and a line; options = intersection sign slip x integral of x slip |
| u5e10q12 | 2023s #13: dy/dx = trig + x e^(x^2) with an initial value; options = sign of ln\|cos x\| x the constant (e^0 = 1) |

## الوحدة 6 (المتجهات) — الاختبارات 4–8

**الشكل:** 12 فقرة في كل اختبار: 6 على المتجهات في الفضاء، و3 على المستقيمات في الفضاء، و3 على الضرب القياسي. الوزارة تميل إلى
الدرس الأول (فقرات المتجهات 38–45 في ورقة 2026: 5 · 1 · 2)، واخترنا توزيعًا أعدل على الدروس الثلاثة. أصبح للوحدة 8 اختبارات
(96 سؤالًا). الملف يسرد الفقرات درسًا درسًا، أمّا الطالبة فترى الأسئلة بترتيب جديد في كل محاولة (كل اختبارات الوحدات)،
حتى لا يدلّ موضع السؤال على درسه.

**طريقة الكتابة:** كل فقرة «أخت» لفقرة وزارية مسمّاة (المصدر مكتوب في تعليق فوق كل `Q(...)` في
`src/semesters/semester-2/unit-6/u6_exams_4_8.py`)، والبدائل شبكة 2×2 من خطأين شائعين (ترتيب الطرح $B-A$ أو $A-B$ ، طرح عدد
سالب، النسبة $k$ أو $\frac1k$ وإشارتها، المنتصف الخطأ $2A-B$ ، مكان المركبة الغائبة في $\hat{i},\hat{j},\hat{k}$ ، الجذر أو
مربّعه، الوتر بدل ضلع القائمة، الجذر المرفوض…) أو قائمة قيم من النوع نفسه. النماذج المستعملة: 2026 — 17، 2025 — 7،
2025 التكميلي — 8، 2024 التكميلي — 7، 2026 المعيدون — 6، 2023 — 6، 2024 — 5، 2023 التكميلي — 4. لا تتكرّر نقطة أو صيغة
أو مجموعة بدائل من الاختبارات 1–3 أو من فقرات المتجهات في نماذج الفصل الثاني (فُحص ذلك آليًّا؛ المشترك فقط عبارات عامة مثل
الشرط $\overrightarrow{AB}=\overrightarrow{BD}$ نفسه ومجموعة الزوايا الخاصة).

**الأشكال:** 10 أشكال: متوازي مستطيلات ومكعّب برسم الوزارة (الرأس $O$ في الخلف وأحرفه الثلاثة منقّطة، $x$ إلى أسفل اليسار
و $y$ إلى أسفل اليمين، والرؤوس $A$–$G$ كما في الفقرة 2026 #41)، ومتوازيات أضلاع ومثلث لمسائل النسبة مرسومة من معاملات
$\vec{\mathbf{a}}$ و $\vec{\mathbf{b}}$ نفسها التي في السؤال، وأربعة أشكال صغيرة لإشارة الضرب القياسي.

**الصعوبة:** 20 سهلًا · 25 متوسطًا · 15 صعبًا (4 · 5 · 3 في كل اختبار).

**الشرح:** لكل سؤال شرح مفصّل بالطريقة المعتادة: مراحل معنونة، وكل خطوة حسابية مكتوبة، وتحقّق بالتعويض أو بمسار آخر في
الشكل، وسبب خطأ كل بديل باسم الخطأ الذي بُني منه (متوسط 9.4 خطوة لكل سؤال). العبارات المشتركة في `explain_u6_common.py`.

**الصحة:** الفحوص الثلاثة لكل الأسئلة الـ60 الجديدة آليًّا (لا سؤال يدوي؛ أُضيف إلى `qb.py` نوع البديل `ijk` لفحص البدائل
المكتوبة بـ $\hat{i},\hat{j},\hat{k}$)، وفُحصت 203 مساواة داخل الشرح آليًّا، وجميع صيغ الوحدة (3042 صيغة) تُعرض في KaTeX دون
أخطاء، وأسئلة الاختبارات 1–3 لم تتغيّر.

| الفقرة | النموذج الوزاري · شبكة البدائل |
|---|---|
| u6e4q1 | 2026r #17: displacement from A to B in context; options = order (B - A or A - B) x sign slip with a negative coordinate |
| u6e4q2 | 2026 #39: AB = BD -> position vector of D; options = 2B - A, 2A - B, B - A (the vector AB itself), -(2B - A) |
| u6e4q3 | 2026 #40: \|AC\| = sqrt(n) with alpha < 0; options = +-3, +-7 (the other root, and the (alpha + 2) sign slip) |
| u6e4q4 | 2026 #41: cuboid in the ministry's drawing, vertex B given, midpoint of a segment joining two vertices; options = one vertex misread each time (A read as E, A read as D, G read as O) |
| u6e4q5 | 2026 #42: collinear points, AB and AC given, the unknown inside AC; options = sign of the ratio x moving the constant |
| u6e4q6 | 2026r #18: parallelogram, a point on a side in a given ratio, Z on a produced side, k from the given vector; options = k, 1/k (the ratio read the other way) and small values of the same kind |
| u6e4q7 | 2023 #18: a point with one unknown coordinate lies on a line; options = t right or sign-slipped, x the line's point added or forgotten |
| u6e4q8 | 2024s #18 (2026 #38 family): line parallel to v through a position vector with a missing component; options = point and direction swapped x the missing component put in the wrong place |
| u6e4q9 | 2024 #19: point where a line meets the xz plane; options = the right plane, the yz plane, the xy plane, t sign slip |
| u6e4q10 | 2026 #43 family: AB and CB given -> AB . AC; options = right AC, AC = AB + CB (sign slip), CB used as AC, sign |
| u6e4q11 | 2025 #20: angle from the magnitudes and the dot product; options = cos = -sqrt3/2 or -1/2, x obtuse or acute |
| u6e4q12 | 2026 #45: triangle from BA and BC (right angle not stated); options = 1/2\|BA\|\|BC\|, without 1/2, and the hypotenuse AC taken as a side (with and without 1/2) |
| u6e5q1 | 2025s #14: 2f - g with i, j, k; options = 2f - g, 2f + g, sign slip in the k component, f - 2g |
| u6e5q2 | 2026r #13: midpoint and one end -> the other end; options = 2N - A, 2A - N, and their negatives |
| u6e5q3 | 2025 #14: unit vector in the direction of GH; options = GH or HG, x divided by \|GH\| or by \|GH\|^2 |
| u6e5q4 | 2025 #18: parallel vectors with one unknown; options = the ratio or its reciprocal, x sign |
| u6e5q5 | 2025 #15: point dividing a segment, TN = 1/3 NM; options = 1/4 or 1/3 of TM, x measured from T or from M |
| u6e5q6 | 2025s #19: parallelogram, N on a diagonal in a given ratio, GN = k(...); options = k, -k, 1/k, -1/k |
| u6e5q7 | 2024 #19 / 2025s #17: point where a line meets the xy plane; options = the right plane, the xz plane, the yz plane, t sign slip |
| u6e5q8 | 2025 #19: cube in the ministry's drawing, line through a vertex and the centre; options = direction M - A or the position vector of M, x through A or through the misread vertex C |
| u6e5q9 | 2024s #19: a point whose coordinates contain the unknown lies on a line; options = a, the parameter t, t = a - 3 sign slip, t taken equal to a |
| u6e5q10 | 2026r #19: perpendicular vectors, quadratic in alpha; options = right factor pair or the other pair of 18, x sign |
| u6e5q11 | 2026r #20: distance from a point to a line, foot given; options = \|PF\| or \|PF\|^2, x sign slip with a negative coordinate |
| u6e5q12 | 2023s #19: u . c with u = AB; options = AB or BA, x A + B used instead of B - A |
| u6e6q1 | 2023s #14: a point in a coordinate plane; options = points with the same numbers in the three planes |
| u6e6q2 | 2025 #16: p a - q b equals a given vector -> p + q; options = right, q sign flipped, a and b swapped, same kind |
| u6e6q3 | 2024s #15: \|PQ\| = \|QR\| -> values of k; options = right roots, (k + 3) sign slip, the other components of QR forgotten (x sign) |
| u6e6q4 | 2026 #41: cuboid in the ministry's drawing, vertex B given, vector between two vertices; options = order x C misread as B |
| u6e6q5 | 2026 #42: collinear points, AB and AC given, the unknown inside AB; options = sign of the ratio x moving the constant |
| u6e6q6 | 2024s #16: triangle, P on AB in a given ratio, PO = k(...); options = k, -k, 1/k, -1/k (P's ratio 1:2 here, 2:1 there) |
| u6e6q7 | 2024s #19: a point whose coordinates all contain the unknown lies on a line; options = a, the parameter t, t = 3a - 5 sign slip, t taken equal to a |
| u6e6q8 | 2026 #38: line parallel to v through a position vector with a missing component (k); options as in 2026 #38 |
| u6e6q9 | 2025s #17: point where a line meets the yz plane; options = right point, x merely set to 0, t sign slip (with and without x = 0) |
| u6e6q10 | 2023 #19: perpendicular vectors, linear in c; options = +-3, +-1 (sign slip in one product) |
| u6e6q11 | 2024s #20: \|b\| from the angle, the dot product and \|a\|; options = divide or multiply by cos, x cos 30 or 1/2 |
| u6e6q12 | 2025s #20: distance from a point to a line (foot found first); options = \|PF\| or \|PF\|^2, x the line's own point used for the foot |
| u6e7q1 | 2024s #14: magnitude of the position vector of a midpoint; options = \|OM\|, \|OA + OB\| (not halved), half of \|AB\|, \|AB\| |
| u6e7q2 | 2025s #13: midpoint with unknowns in both points; options = n right or not doubled, x sign slip when moving -3 |
| u6e7q3 | 2024 #20: parallel vectors with two unknowns -> a + b; options = sign of the ratio x moving the constants |
| u6e7q4 | 2026 #44 (asked the other way): parallelogram, Y the midpoint of a diagonal, Z on a produced side in a given ratio -> YZ; options = MZ right or the ratio read the other way, x YZ or ZY |
| u6e7q5 | 2024 #18: vector of a given magnitude opposite to a vector in i, j, k; options = opposite or same direction, x normalised or not |
| u6e7q6 | 2023 #17: PF = 2/3 PQ -> F; options = 2/3 or 1/3 of PQ, x added to P or not |
| u6e7q7 | 2026 #38: line parallel to v (v has a missing component, j) through a position vector; options = point and direction swapped x the zero of v put in the wrong place |
| u6e7q8 | 2023 #18: a point with an unknown coordinate lies on a line; options = t right or slipped, x 2a divided by 2 or not |
| u6e7q9 | 2023s #18: general point of a segment, PF = t PQ; options = start at P or at Q, x direction PQ or QP |
| u6e7q10 | 2023 #20: which figure shows u . v > 0 (sign of the dot product from the angle); options = the four panels |
| u6e7q11 | 2026 #43: three points, two side vectors given -> dot product; options = +-(right value), +-(KL . ML used directly) |
| u6e7q12 | 2026 #45: right triangle from its vertices (the right angle is at C, not at B); options = 1/2 x the legs, without 1/2, and the hypotenuse AB taken as a leg (with and without 1/2) |
| u6e8q1 | 2024 #17: position vector of a midpoint, given with i, j, k; options = sum or difference, x halved or not |
| u6e8q2 | 2025s #16: GH = HD -> D; options = 2H - G, 2G - H and their negatives |
| u6e8q3 | 2023s #15: \|AB\| = 13 with an unknown coordinate -> its values; options = right roots, (7 + k) slip, the other components forgotten (x sign) |
| u6e8q4 | 2026 #42: collinear with AB and BC (not AC) given; options = sign of the ratio x the ratio inverted |
| u6e8q5 | 2025s #18: parallel vectors with the unknown in two components; options = right root, the root that fails the first component, and their negatives |
| u6e8q6 | 2026 #44: parallelogram, Y the midpoint of a diagonal, Z on a produced side, k from the given vector; options = k, 1/k (the ratio read the other way) and values of the same kind |
| u6e8q7 | 2026 #38: line parallel to v through a position vector with a missing component (j); options as in 2026 #38 |
| u6e8q8 | 2023 #18: a point with two unknown coordinates lies on a line -> a + b; options = t = -3 (right), 3, -2, 2 |
| u6e8q9 | 2025 #19: cuboid in the ministry's drawing, line through two vertices; options = direction GA or GB (misread vertex), x point and direction in the right order or swapped |
| u6e8q10 | 2026r #19: perpendicular vectors, quadratic in alpha; options = right factor pair or the other pair of 15, x sign |
| u6e8q11 | 2025s #20: distance from a point to a line, foot given with fractions; options = \|PF\| or \|PF\|^2, x sign slip in y |
| u6e8q12 | 2026 #43: three points, two side vectors given -> dot product; options = +-(right value), +-(RS . TS used directly) |

## الوحدة 7 (الإحصاء والاحتمالات) — الاختبارات 4–8

**الشكل:** 12 فقرة في كل اختبار: 6 على التوزيع الهندسي وتوزيع ذي الحدّين، و6 على التوزيع الطبيعي (توزيع متوازن على الدرسين كما
في الاختبارات 1–3). أصبح للوحدة 8 اختبارات (96 سؤالًا)، وترتيب الأسئلة يتغيّر في كل محاولة.

**طريقة الكتابة:** كل فقرة «أخت» لفقرة وزارية مسمّاة (المصدر مكتوب في تعليق فوق كل `Q(...)` في
`src/semesters/semester-2/unit-7/u7_exams_4_8.py`)، والبدائل شبكة 2×2 من خطأين شائعين ($p$ أو $1-p$ أو مقلوبهما، التوقّع بدل
التباين أو الانحراف المعياري، نسيان المتممة، القسمة على التباين بدل الانحراف المعياري، جهة $z$ ، إهمال إشارة القيمة السالبة،
نسيان القسمة على $2$ في الفترة المتماثلة، القيمة الأقرب في الجدول…) أو قائمة قيم من النوع نفسه. قيم جدول التوزيع الطبيعي هي
قيم الوزارة بأربع منازل، وتُعطى في نص السؤال كما تفعل الوزارة، وتُحسب الإجابة منها. النماذج المستعملة: 2026 — 14، 2025 — 9،
2026 المعيدون — 8، 2024 التكميلي — 8، 2024 — 6، 2025 التكميلي — 5، 2023 — 5، 2023 التكميلي — 5. لا تتكرّر صيغة أو مجموعة
بدائل من الاختبارات 1–3 أو من فقرات الوحدة في نماذج الفصل الثاني (فُحص ذلك آليًّا؛ المشترك فقط رموز عامة مثل
$X\sim Geo(p)$ وجداول قيم $z$ المعتادة).

**الأشكال:** 8 أشكال: ثلاث مناطق مظلّلة أسفل المنحنى المعياري، وشكل القاعدة التجريبية كما تضعه الوزارة ملحوظةً
($34\%$ ، $13.5\%$ ، $2.35\%$ ، $0.15\%$) في أربعة أسئلة، ومنحنى عليه طرفان نسبة كلّ منهما $2.5\%$.

**الصعوبة:** 20 سهلًا · 25 متوسطًا · 15 صعبًا (4 · 5 · 3 في كل اختبار).

**الشرح:** لكل سؤال شرح مفصّل بالطريقة المعتادة: مراحل معنونة، وكل خطوة حسابية مكتوبة (مع خمس منازل عشرية في الحسابات الوسيطة
لذي الحدّين)، وسبب خطأ كل بديل باسم الخطأ الذي بُني منه (متوسط 6.8 خطوة لكل سؤال). العبارات المشتركة في `explain_u7_common.py`.

**الصحة:** الفحوص الثلاثة لكل الأسئلة الـ60 الجديدة آليًّا (لا سؤال يدوي؛ سؤالا «أيّ التجارب…» يُفحصان بخاصية تصنيف البدائل)،
وفُحصت 171 مساواة داخل الشرح آليًّا، وجميع صيغ الوحدة (2651 صيغة) تُعرض في KaTeX دون أخطاء، وأسئلة الاختبارات 1–3 لم تتغيّر.

| الفقرة | النموذج الوزاري · شبكة البدائل |
|---|---|
| u7e4q1 | 2026 #46: ratio of two geometric probabilities -> E(X); options = 1/p, p, 1 - p, 1/(1 - p) |
| u7e4q2 | 2026 #47: quality control, reject when 2 or more defective; options = P(X >= 2), P(X = 0), 1 - P(X = 0), P(X <= 1) |
| u7e4q3 | 2026r #22: n from E(X) and Var(X); options = n, E/(1 - p) (p and 1 - p swapped), Var/p, E/(p(1 - p)) |
| u7e4q4 | 2024s #21: a die thrown until a given outcome; options = (1-p)^2 p, p^2 (1-p) (swapped), (1-p)^2 (p forgotten), (1-p)^3 |
| u7e4q5 | 2024 #22: P(X = 1) = P(X = 2) -> Var(X); options = Var, E, sigma, p(1 - p) |
| u7e4q6 | 2025 #21: which experiment is geometric; options = geometric, binomial, drawing together, measuring |
| u7e4q7 | 2026 #48: P(X < a) for N(mu, sigma^2); options = complement or not x sigma or the variance used in z |
| u7e4q8 | 2026 #49: P(-k/c < Z < k/c) given -> k; options = right table entry times c, neighbouring entries, z divided by c |
| u7e4q9 | 2026 #50: sigma from the percentage above a value (closest table entry); options = sigma, z, d.z, z/d |
| u7e4q10 | 2026r #23: shaded area between a negative and a positive z (figure); options = right, sign ignored, and their complements |
| u7e4q11 | 2024s #23 / 2023 #24: probability between two values by the empirical rule (figure); options = right sum and misplaced bounds |
| u7e4q12 | 2025 #24: P(X < mu - k) given -> P(mu - k < X < mu + k); options = 1 - 2a, 1 - a, a, 2a |
| u7e5q1 | 2025 #22: P(X > k) given -> E(X); options = 1/p, 1/(1 - p), p, 1 - p |
| u7e5q2 | 2025s #22: E(X) and p -> Var(X); options = E(1 - p), Ep, p(1 - p), n(1 - p) |
| u7e5q3 | 2023 #22: at least n - 1 successes in n trials, written in powers (n(1 - p) = 1 collapses the binomial coefficient); options = the right sum, all successes only, one term without its coefficient, the failure power added |
| u7e5q4 | 2026r #21: trials until the first success in context; options = (1-p)^3 p, (1-p)^4, p^3 (1-p), (1-p)^3 |
| u7e5q5 | 2024s #22: Var of a given binomial; options = Var, E, sigma, p(1 - p) |
| u7e5q6 | 2023 #23: Var given -> the two possible p; options = pairs p, 1 - p |
| u7e5q7 | 2026r #24: P(Z > z) given -> P(-z < Z < z); options = 1 - 2a, 1 - a, a, 2a |
| u7e5q8 | 2026r #25: x from P(X > x); options = mu + z sigma, mu - z sigma, z, mu + z sigma^2 |
| u7e5q9 | 2025s #25: sigma from the interval holding 95% (empirical rule, figure); options = sigma, sigma^2, 2 sigma, 4 sigma |
| u7e5q10 | 2024 #25: P(a < Z < b) with a < 0 < b; options = right, sign ignored, and their complements |
| u7e5q11 | 2025 #25: x from P(mu < X < x) (closest table entry); options = right, the other entry, P(Z < z) = 0.3 read, the probability used as z |
| u7e5q12 | 2023s #25: X ~ N(mu, mu^2/9) -> P(X > 1.5 mu); options = 1 - P(Z<1.5), P(Z<1.5), and both with sigma = mu |
| u7e6q1 | 2023s #23: E(X) of a geometric variable; options = 1/p, 1/(1 - p), p, 1 - p (decimals) |
| u7e6q2 | 2026 #47: acceptance with at most one defective; options = P(X <= 1), P(X = 0), 1 - P(X <= 1), P(X = 1) |
| u7e6q3 | 2026 #46: ratio of consecutive geometric probabilities -> E(X); options = 1/p, p, 1 - p, 1/(1 - p) |
| u7e6q4 | 2023 #22: at least n - 1 successes, written in powers; options = the right sum, all successes, one term, the coefficient n kept |
| u7e6q5 | 2026r #22: n from E(X) and Var(X); options = n, E/(1 - p), E/(p(1 - p)), Var/p |
| u7e6q6 | 2024 #22: P(X = 3) = P(X = 4) -> Var(X); options = Var, E, p(1 - p), p |
| u7e6q7 | 2025s #23: probability above a value in context; options = 1 - P(Z<z), P(Z<z), P(Z<z) - 0.5, 0.5 + (1 - P(Z<z)) |
| u7e6q8 | 2026 #49: P(-k/c < Z < k/c) given -> k; options = right z or the unhalved one, x times c or divided by c |
| u7e6q9 | 2024s #24: shaded area between two negative z (figure); options = right, sign slip, sum of the tails, complement |
| u7e6q10 | 2025s #24: P(X > mu + k) given -> P(X < mu - k) by symmetry; options = a, 1 - a, 1 - 2a, 2a |
| u7e6q11 | 2023s #24: percentage between two values by the empirical rule (figure); options = mu..mu+3s, mu..mu+2s, mu..mu+s, 50% |
| u7e6q12 | 2024s #25: x from P(X < x) below the mean (closest table entry); options = mu - z sigma, mu + z sigma, mu - z, mu - z sigma^2 |
| u7e7q1 | 2025 #22: P(X > k) given -> P(X = k); options = (1-p)p, (1-p)^2 p, p^2, 1 - p |
| u7e7q2 | 2026 #47: reject when at least one is defective; options = P(X >= 1), P(X = 0), P(X = 1), P(X >= 2) |
| u7e7q3 | 2025 #21: which experiment is binomial; options = binomial, geometric, drawing together, measuring |
| u7e7q4 | 2023 #23: Var given with p > 0.5 -> E(X); options = E for each root x E or p |
| u7e7q5 | 2024s #22: Var of a given binomial; options = Var, E, sigma, p(1 - p) |
| u7e7q6 | 2023s #23: E(X) of a geometric variable; options = 1/p, 1/(1 - p), p, 1 - p (decimals) |
| u7e7q7 | 2026 #50: sigma from the percentage below a value (closest table entry); options = sigma, z, d.z, z/d |
| u7e7q8 | 2026r #24: P(Z > z) given -> P(-z < Z < z); options = 1 - 2a, 1 - a, a, 2a |
| u7e7q9 | 2025 #23: sigma from a curve whose 2.5% tails are marked (figure); options = sigma, 2 sigma, 4 sigma, sigma/2 |
| u7e7q10 | 2024 #25: P(a < Z < b) with a < 0 < b; options = right, sign ignored, and their complements |
| u7e7q11 | 2024 #24: X ~ N(mu, (2 mu)^2) and a z-score -> sigma; options = sigma, mu, sigma^2, x |
| u7e7q12 | 2025 #25: x from P(x < X < mu); options = mu - z sigma, mu + z sigma, mu - z, mu - z sigma^2 |
| u7e8q1 | 2026 #46: ratio of geometric probabilities two apart -> E(X); options = 1/p, p, 1 - p, 1/(1 - p) (decimals) |
| u7e8q2 | 2026r #21: testing chips until the first defective; options = (1-p)^3 p, (1-p)^4, p^3 (1-p), (1-p)^3 |
| u7e8q3 | 2025 #22: P(X > k) given -> P(X <= 3); options = 1 - (1-p)^3, (1-p)^3, (1-p)^2 p, 1 - (1-p)^2 |
| u7e8q4 | 2025s #22: E(X) and p -> Var(X); options = E(1 - p), Ep, p(1 - p), n(1 - p) |
| u7e8q5 | 2023 #22: at least n - 1 successes, written in powers; options = the right sum, all successes, one term, the failure power added |
| u7e8q6 | 2023s #23: E(X) of a geometric variable; options = 1/p, 1/(1 - p), p, 1 - p (decimals) |
| u7e8q7 | 2026 #48: P(X > a) with a below the mean; options = P(Z<z), its complement, and both with the variance used in z |
| u7e8q8 | 2026 #49: P(-k/c < Z < k/c) given -> k; options = right z or the unhalved one, x times c or divided by c |
| u7e8q9 | 2026 #50: sigma from a small percentage above a value; options = sigma, z, d.z, z/d |
| u7e8q10 | 2024 #23: one-sided empirical-rule percentage, "above the mean by at most one sigma" (figure); options = 34%, 68%, 16%, 50% |
| u7e8q11 | 2024s #24: shaded area between two negative z (figure); options = right, sum of the two areas, and complements |
| u7e8q12 | 2024s #25 / 2026r #25: x from P(X > x); options = mu + z sigma, mu - z sigma, mu + z, mu + z sigma^2 |
