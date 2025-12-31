# node

> یک runtime برای اجرای جاوا اسکریپت. (Node.js)
> اطلاعات بیشتر: <https://nodejs.org/docs/latest/api/cli.html#options>.

- اجرای یک فایل جاوااسکریپت:

`node {{path/to/file}}`

- شروع یک REPL (پوسته تعاملی):

`node`

- اجرای فایل مشخص‌شده و راه‌اندازی مجدد فرآیند هنگام تغییر در یک فایل وارد شده (نیازمند نسخه Node.js 18.11+):

`node --watch {{path/to/file}}`

- ارزیابی کد جاوااسکریپت با ارسال آن به‌عنوان یک آرگومان:

`node {{[-e|--eval]}} "{{code}}"`

- ارزیابی و چاپ نتیجه، مفید برای چاپ نسخه‌های وابستگی‌های Node:

`node {{[-p|--print]}} "process.versions"`

- فعال کردن حالت Inspector، توقف اجرای برنامه تا زمانی که دیباگر به کد متصل شود و کد کاملاً تحلیل شود:

`node --no-lazy --inspect-brk {{path/to/file}}`
