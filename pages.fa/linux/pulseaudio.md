# pulseaudio

> سرویس و مدیر سیستم صوتی PulseAudio.
> اطلاعات بیشتر: <https://manned.org/pulseaudio>.

- بررسی در حال اجرا بودن PulseAudio (کد خروج غیرصفر یعنی در حال اجرا نیست):

`pulseaudio --check`

- شروع سرویس PulseAudio در پس‌زمینه:

`pulseaudio --start`

- پایان دادن به سرویس PulseAudio در حال اجرا:

`pulseaudio {{[-k|--kill]}}`

- فهرست کردن ماژول‌های موجود:

`pulseaudio --dump-modules`

- بارگذاری ماژول در سرویس در حال اجرا با آرگومان‌های مشخص:

`pulseaudio {{[-L|--load]}} "{{module_name}} {{arguments}}"`
