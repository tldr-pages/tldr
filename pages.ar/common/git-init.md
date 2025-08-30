# git init

> يهيئ مستودع Git محلي جديد.
> لمزيد من التفاصيل: <https://git-scm.com/docs/git-init>.

- تهيئة مستودع محلي جديد:

`git init`

- تهيئة مستودع مع تحديد اسم الفرع الابتدائي:

`git init {{[-b|--initial-branch]}} {{branch_name}}`

- تهيئة مستودع يستخدم خوارزمية SHA256 لتنسيق تجزئة الكائنات (يتطلب إصدار Git 2.29 أو أحدث):

`git init --object-format sha256`

- تهيئة مستودع خال، مناسب للاستخدام كمستودع خارجي عبر SSH:

`git init --bare`
