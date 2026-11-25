# semanage

> ابزار مدیریت سیاست پایدار SELinux.
> برخی زیردستورها مانند `boolean`، `fcontext` و `port` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://manned.org/semanage>.

- تنظیم یا لغو مقدار بولی SELinux. مقادیر بولی به مدیر اجازه می‌دهند نحوهٔ تأثیر قوانین سیاست بر انواع فرایند محدودشده (دامنه‌ها) را سفارشی کند:

`sudo semanage boolean {{[-m|--modify]}} {{--on|--off}} {{haproxy_connect_any}}`

- افزودن قانون کاربری برچسب‌گذاری زمینهٔ فایل. زمینهٔ فایل مشخص می‌کند دامنه‌های محدودشده به چه فایل‌هایی اجازهٔ دسترسی دارند:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '/mnt/share(/.*)?'`

- افزودن قانون کاربری برچسب‌گذاری پورت. برچسب پورت مشخص می‌کند دامنه‌های محدودشده مجاز به گوش دادن به چه پورت‌هایی هستند:

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- تنظیم یا لغو حالت permissive برای دامنهٔ محدودشده. حالت permissive به تفکیک دامنه در مقایسه با `setenforce` کنترل دقیق‌تری فراهم می‌کند:

`sudo semanage permissive {{--add|--delete}} {{httpd_t}}`

- خروجی سفارشی‌سازی‌های محلی در مخزن پیش‌فرض:

`sudo semanage export {{[-f|--output_file]}} {{path/to/file}}`

- وارد کردن فایل تولیدشده توسط `semanage export` به سفارشی‌سازی‌های محلی (احتیاط: ممکن است سفارشی‌سازی‌های فعلی حذف شوند!):

`sudo semanage import {{[-f|--input_file]}} {{path/to/file}}`
