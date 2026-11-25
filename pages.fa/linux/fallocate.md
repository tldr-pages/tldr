# fallocate

> رزرو یا آزاد کردن فضای دیسک برای فایل‌ها.
> این ابزار فضا را بدون صفر کردن تخصیص می‌دهد.
> اطلاعات بیشتر: <https://manned.org/fallocate>.

- رزرو یک فایل با اشغال ۷۰۰ MiB فضای دیسک:

`fallocate {{[-l|--length]}} 700M {{path/to/file}}`

- کوچک کردن یک فایل قبلاً تخصیص‌یافته به میزان ۲۰۰ MB:

`fallocate {{[-c|--collapse-range]}} {{[-l|--length]}} 200MB {{path/to/file}}`

- کاهش ۲۰ MB فضا پس از ۱۰۰ MiB در یک فایل:

`fallocate {{[-c|--collapse-range]}} {{[-o|--offset]}} 100M {{[-l|--length]}} 20M {{path/to/file}}`
