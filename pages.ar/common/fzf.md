# fzf

> أداة بحث تقريبي (fuzzy) لسطر الأوامر.
> مشابهة لـ `sk`.
> لمزيد من التفاصيل: <https://github.com/junegunn/fzf#usage>.

- تشغيل `fzf` على جميع الملفات داخل المجلد المحدد:

`find {{path/to/directory}} -type f | fzf`

- تشغيل `fzf` للعمليات الجارية:

`ps aux | fzf`

- تحديد ملفات متعددة باستخدام `<Shift Tab>` وكتابتها إلى ملف:

`find {{path/to/directory}} -type f | fzf {{[-m|--multi]}} > {{path/to/file}}`

- تشغيل `fzf` مع نص بحثي محدد:

`fzf {{[-q|--query]}} "{{query}}"`

- تشغيل `fzf` على إدخالات تبدأ بـ `core` وتنتهي بـ `go` أو `rb` أو `py`:

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- تشغيل `fzf` على إدخالات لا تطابق `pyc` وتحتوي على `travis`:

`fzf {{[-q|--query]}} '!pyc travis'`
