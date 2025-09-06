# fzf

> أداة بحث تقريبي (fuzzy) لسطر الأوامر.
> مشابهة لـ `sk`.
> لمزيد من التفاصيل: <https://github.com/junegunn/fzf>.

- تشغيل `fzf` على جميع الملفات داخل مُجَلَّد معين:

`find {{path/to/directory}} -type f | fzf`

- تشغيل `fzf` للبحث في العمليات الجارية في الخلفية:

`ps aux | fzf`

- تحديد ملفات متعددة باستخدام `<Shift Tab>` وحفظها في ملف:

`find {{path/to/directory}} -type f | fzf {{[-m|--multi]}} > {{path/to/file}}`

- تشغيل `fzf` مع نص بحثي محدد:

`fzf {{[-q|--query]}} "{{query}}"`

- تشغيل `fzf` على الإدخالات التي تبدأ بـ "core" وتنتهي بـ "go" أو "rb" أو "py":

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- تشغيل `fzf` على الإدخالات التي لا تطابق "pyc" وتطابق تمامًا "travis":

`fzf {{[-q|--query]}} "!pyc 'travis"`
