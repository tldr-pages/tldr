# cgclassify

> انتقال وظایف در حال اجرا به `cgroups`.
> اطلاعات بیشتر: <https://manned.org/cgclassify>.

- انتقال فرایند با PID مشخص به گروه کنترلی student در سلسله‌مراتب CPU با `-g`:

`cgclassify -g {{cpu:student}} {{1234}}`

- انتقال فرایند با PID مشخص به گروه‌های کنترلی بر اساس فایل پیکربندی `/etc/cgrules.conf`:

`cgclassify {{1234}}`

- انتقال فرایند با PID مشخص به گروه کنترلی student در سلسله‌مراتب CPU با `-g`؛ توجه: سرویس `cgred`، گروه‌های `cgroups` آن PID و فرزندانش را بر اساس `/etc/cgrules.conf` تغییر نمی‌دهد:

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
