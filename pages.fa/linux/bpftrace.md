# bpftrace

> زبان سطح‌بالای ردیابی برای eBPF در لینوکس.
> اطلاعات بیشتر: <https://github.com/bpftrace/bpftrace/blob/master/man/adoc/bpftrace.adoc>.

- فهرست کردن همهٔ نقاط کاوش موجود:

`sudo bpftrace -l`

- اجرای یک برنامهٔ تک‌خطی (برای مثال شمارش فراخوانی‌های سیستم به تفکیک برنامه):

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }}}'`

- اجرای یک برنامه از فایل:

`sudo bpftrace {{path/to/file}}`

- ردیابی یک برنامه بر اساس PID:

`sudo bpftrace -e '{{tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }}}'`

- شبیه‌سازی اجرای برنامه و نمایش خروجی در قالب eBPF:

`sudo bpftrace -d -e '{{one_line_program}}'`

- نمایش نسخه:

`bpftrace {{[-V|--version]}}`
