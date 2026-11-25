# tuned

> سرویس تنظیم تطبیقی پویای سیستم.
> همچنین ببینید: `tuned-adm`.
> اطلاعات بیشتر: <https://manned.org/tuned>.

- شروع سرویس `tuned` در پیش‌زمینه:

`sudo tuned`

- شروع سرویس `tuned` در پس‌زمینه:

`sudo tuned {{[-d|--daemon]}}`

- شروع سرویس `tuned` با پروفایل مشخص:

`sudo tuned {{[-p|--profile]}} {{profile_name}}`

- شروع سرویس `tuned` با ثبت در فایل گزارش دلخواه:

`sudo tuned {{[-l|--log]}} {{path/to/log_file.log}}`

- شروع سرویس `tuned` با نوشتن شناسهٔ فرایند در فایل PID دلخواه:

`sudo tuned {{[-P|--pid]}} {{path/to/process_id_file.pid}}`

- شروع سرویس `tuned` با پیام‌های اشکال‌زدایی:

`sudo tuned {{[-D|--debug]}}`
