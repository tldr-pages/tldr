# journalctl

> استعلم عن سجلات نظام التشغيل (systemd journal).
> انظر أيضًا: `dmesg`.
> لمزيد من التفاصيل: <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html>.

- [-n] اعرض السجلات الأحدث بعدد معين وتابع الرسائل الجديدة فور حدوثها:

`journalctl {{[-n|--lines]}} {{عدد_الأسطر}} {{[-f|--follow]}}`

- [-b] اعرض جميع الرسائل ذات مستوى الأولوية 3 (الأخطاء) الخاصة بجلسة التشغيل السابقة:

`journalctl {{[-b|--boot]}} -1 {{[-p|--priority]}} 3`

- [-u] اعرض جميع الرسائل الخاصة بوحدة (unit) معينة في النظام:

`journalctl {{[-u|--unit]}} {{اسم_الوحدة}}`

- [_] اعرض السجلات لوحدة معينة منذ آخر مرة تم تشغيلها فيها:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{اسم_الوحدة}})`

- [-S] تصفح الرسائل وضفّها ضمن نطاق زمني محدد (باستخدام طابع زمني أو كلمات دلالية):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow|...}} {{[-U|--until]}} "{{السنة-الشهر-اليوم الساعات:الدقائق:الثواني}}"`

- [_] اعرض جميع الرسائل الخاصة بمعرّف عملية (PID) محددة:

`journalctl _PID={{معرف_العملية}}`

- [/] اعرض جميع الرسائل الخاصة بملف تنفيذي معين:

`journalctl {{مسار/الملف_التنفيذي}}`

- [--] احذف سجلات النظام القديمة التي يتجاوز عمرها يومين:

`journalctl --vacuum-time 2d`
