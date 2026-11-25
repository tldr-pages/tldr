# expac

> ابزار استخراج داده از پایگاه‌های alpm با انعطاف‌پذیری مشابه printf برای ابزارهای مبتنی بر pacman.
> همچنین ببینید: `pacman`.
> اطلاعات بیشتر: <https://github.com/falconindy/expac#name>.

- فهرست کردن وابستگی‌های یک بسته:

`expac {{[-S|--sync]}} '%D' {{package}}`

- فهرست کردن وابستگی‌های اختیاری یک بسته:

`expac {{[-S|--sync]}} "%o" {{package}}`

- فهرست کردن اندازهٔ دانلود بسته‌ها بر حسب MiB:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' {{package1 package2 ...}}`

- فهرست کردن بسته‌های علامت‌گذاری‌شده برای ارتقا همراه با اندازهٔ دانلود:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' $(pacman -Qqu) | sort {{[-sh|--sort --human-numeric-sort]}}`

- فهرست کردن بسته‌های صریحاً نصب‌شده همراه با وابستگی‌های اختیاری آن‌ها:

`expac {{[-d|--delim]}} '\n\n' {{[-l|--listdelim]}} '\n\t' {{[-Q|--query]}} '%n\n\t%O' $(pacman -Qeq)`
