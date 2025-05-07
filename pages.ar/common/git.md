# git

> نظام تحكم في الإصدارات.
> بعض الأوامر الفرعية مثل `commit` و `add` و `branch` و `checkout` و `push`، وغيرها، لديها وثائق استخدام خاصة بها.
> لمزيد من التفاصيل: <https://git-scm.com/docs/git>.

- تنفيذ أمر فرعي في Git:

`git {{subcommand}}`

- تنفيذ أمر فرعي في Git على مسار مستودع مخصص:

`git -C {{path/to/repo}} {{subcommand}}`

- تنفيذ أمر فرعي في Git مع ضبط إعداد معين:

`git -c '{{config.key}}={{value}}' {{subcommand}}`

- عرض المساعدة:

`git --help`

- عرض المساعدة لأمر فرعي محدد (مثل `clone` أو `add` أو `push` أو `log`، إلخ):

`git help {{subcommand}}`

- عرض رقم الإصدار:

`git --version`
