# fzf

> أداة بحث تقريبي (fuzzy) لسطر الأوامر.
> مشابهة لـ `sk`.
> لمزيد من التفاصيل: <https://github.com/junegunn/fzf>.

- تشغيل `fzf` على جميع الملفات داخل مُجَلَّد معين:

`find {{path/to/directory}} -type f | fzf`

- تشغيل `fzf` للبحث في العمليات الجارية في الخلفية:

`ps aux | fzf`

- تحديد ملفات متعددة باستخدام `<Shift Tab>` وحفظها في ملف:

`find {{path/to/directory}} -type f | fzf --multi > {{path/to/file}}`

- تشغيل `fzf` مع نص بحثي محدد:

`fzf --query "{{query}}"`

- تشغيل `fzf` على الإدخالات التي تبدأ بـ "core" وتنتهي بـ "go" أو "rb" أو "py":

`fzf --query "^core go$ | rb$ | py$"`

- تشغيل `fzf` على الإدخالات التي لا تطابق "pyc" وتطابق تمامًا "travis":

`fzf --query "!pyc 'travis"`
