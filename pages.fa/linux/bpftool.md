# bpftool

> بررسی و تغییر سادهٔ برنامه‌ها و نگاشت‌های eBPF.
> اطلاعات بیشتر: <https://manned.org/bpftool>.

- فهرست کردن اطلاعات برنامه‌های بارگذاری‌شدهٔ `eBPF`:

`bpftool prog list`

- فهرست کردن اتصال‌های برنامه‌های `eBPF` در زیرسیستم شبکهٔ هسته:

`bpftool net list`

- فهرست کردن همهٔ پیوندهای فعال:

`bpftool link list`

- فهرست کردن همهٔ اتصال‌های `raw_tracepoint`، `tracepoint` و `kprobe` در سیستم:

`bpftool perf list`

- فهرست کردن داده‌های `BPF Type Format (BTF)`:

`bpftool btf list`

- فهرست کردن اطلاعات نگاشت‌های بارگذاری‌شده:

`bpftool map list`

- بررسی قابلیت‌های `eBPF` پشتیبانی‌شده توسط دستگاه شبکهٔ «eth0»:

`bpftool feature probe dev {{eth0}}`

- اجرای دستورها در حالت دسته‌ای از یک فایل:

`bpftool batch file {{myfile}}`
