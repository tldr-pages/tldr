# swaks

> چاقوی سوئیسی SMTP، آزمونگر همه‌منظورهٔ تراکنش SMTP.
> اطلاعات بیشتر: <https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- تحویل ایمیل آزمایشی استاندارد به `user@example.com` روی پورت ۲۵ سرور `test-server.example.net`:

`swaks {{[-t|--to]}} {{user@example.com}} {{[-s|--server]}} {{test-server.example.net}}`

- تحویل ایمیل آزمایشی استاندارد با الزام احراز هویت CRAM-MD5 به‌عنوان کاربر `me@example.com`. سربرگ «X-Test» به بدنهٔ ایمیل افزوده می‌شود:

`swaks {{[-t|--to]}} {{user@example.com}} {{[-f|--from]}} {{me@example.com}} {{[-a|--auth]}} {{CRAM-MD5}} {{[-au|--auth-user]}} {{me@example.com}} --header-X-Test "{{test_email}}"`

- آزمودن ویروس‌یاب با EICAR در پیوست، بدون نمایش بخش DATA پیام:

`swaks {{[-t|--to]}} {{user@example.com}} --attach - {{[-s|--server]}} {{test-server.example.com}} {{[-n|--suppress-data]}} {{path/to/eicar.txt}}`

- آزمودن هرزنامه‌یاب با GTUBE در بدنهٔ ایمیل، مسیریابی‌شده از طریق رکوردهای MX برای `example.com`:

`swaks {{[-t|--to]}} {{user@example.com}} --body {{path/to/gtube_file}}`

- تحویل ایمیل آزمایشی استاندارد به `user@example.com` با پروتکل LMTP از طریق فایل سوکت دامنهٔ UNIX:

`swaks {{[-t|--to]}} {{user@example.com}} --socket {{/var/lda.sock}} --protocol {{LMTP}}`
