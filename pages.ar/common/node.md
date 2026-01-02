# node

> بيئة تشغيل JavaScript للخادم (Node.js).
> لمزيد من التفاصيل: <https://nodejs.org/docs/latest/api/cli.html#options>.

- تشغيل ملف JavaScript:

`node {{path/to/file}}`

- بدء REPL (وحدة تحكم تفاعلية):

`node`

- تنفيذ الملف المحدد مع إعادة تشغيل العملية عند تغيير ملف مستورد (يتطلب Node.js إصدار 18.11+):

`node --watch {{path/to/file}}`

- تنفيذ كود JavaScript من سطر الأوامر:

`node {{[-e|--eval]}} "{{code}}"`

- تنفيذ وطباعة النتيجة، مفيد لطباعة إصدارات تبعيات node:

`node {{[-p|--print]}} "process.versions"`

- تفعيل المصحح (inspector)، مع إيقاف التنفيذ حتى يتم الاتصال بمصحح الأخطاء (debugger) بمجرد تحليل الكود المصدري بالكامل:

`node --no-lazy --inspect-brk {{path/to/file}}`
