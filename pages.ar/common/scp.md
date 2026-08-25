# scp

> نسخ آمن.
> انسخ الملفات بين الأجهزة باستخدام بروتوكول النسخ الآمن عبر SSH.
> لمزيد من التفاصيل: <https://man.openbsd.org/scp>.

- إنسخ ملفًا محليًا إلى مضيف بعيد:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- إستخدم منفذًا محددًا عند الاتصال بالمضيف البعيد:

`scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- إنسخ ملفًا من مضيف بعيد إلى مجلد محلي:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- إنسخ محتوى مجلد بشكل متكرر من مضيف بعيد إلى مجلد محلي:

`scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- إنسخ ملفًا بين مضيفين بعيدين مع تمرير النقل عبر المضيف المحلي:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}`

- إستخدم اسم مستخدم محدد للاتصال بالمضيف البعيد:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}`

- إستخدم مفتاح خاصًا محددًا للمصادقة مع المضيف البعيد:

`scp -i {{~/.ssh/private_key}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- إستخدم خادمًا وكيلًا محددًا عند الاتصال بالمضيف البعيد:

`scp -J {{proxy_username}}@{{proxy_host}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`
