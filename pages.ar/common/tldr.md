# tldr

> يعرض صفحات مساعدة مبسطة للأوامر في سطر الأوامر، مستمدة من مشروع tldr-pages.
> ملاحظة: الخيارات `--language` و `--list` ليست مطلوبة وفقًا للمواصفات، ولكن معظم العملاء يدعمونها.
> لمزيد من التفاصيل: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- عرض صفحة tldr لأمر معين (تلميح: هذا ما أوصلك إلى هنا!):

`tldr {{command}}`

- عرض صفحة tldr لأمر فرعي معين:

`tldr {{command}} {{subcommand}}`

- عرض صفحة tldr لأمر بلغة معينة (إن وجدت، وإلا سيتم الرجوع إلى الإنجليزية):

`tldr {{[-L|--language]}} {{language_code}} {{command}}`

- عرض صفحة tldr لأمر من نظام تشغيل معين:

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{command}}`

- تحديث ذاكرة التخزين المؤقت لصفحات tldr:

`tldr {{[-u|--update]}}`

- عرض قائمة بجميع الصفحات المتاحة للمنصة الحالية وللأوامر الشائعة:

`tldr {{[-l|--list]}}`

- عرض جميع الصفحات الفرعية المتاحة لأمر معين:

`tldr {{[-l|--list]}} | grep {{command}} | column`

- عرض صفحة tldr لأمر عشوائي:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
