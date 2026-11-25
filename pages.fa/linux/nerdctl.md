# nerdctl

> رابط خط فرمان سازگار با Docker برای containerd.
> اطلاعات بیشتر: <https://github.com/containerd/nerdctl/blob/main/docs/command-reference.md>.

- فهرست کردن همهٔ کانتینرها (در حال اجرا و متوقف‌شده):

`nerdctl ps {{[-a|--all]}}`

- شروع کانتینر از تصویر با نام دلخواه:

`nerdctl run --name {{container_name}} {{image}}`

- شروع یا توقف کانتینر موجود:

`nerdctl {{start|stop}} {{container_name}}`

- دریافت تصویر از رجیستری کانتینر:

`nerdctl pull {{image}}`

- نمایش فهرست تصاویر بارگیری‌شده:

`nerdctl images`

- باز کردن tty تعاملی با پوستهٔ Bourne (`sh`) داخل کانتینر در حال اجرا:

`nerdctl exec {{[-it|--interactive --tty]}} {{container_name}} sh`

- حذف کانتینرهای متوقف‌شده:

`nerdctl rm {{container1 container2 ...}}`

- دریافت و دنبال کردن گزارش‌های کانتینر:

`nerdctl logs {{[-f|--follow]}} {{container_name}}`
