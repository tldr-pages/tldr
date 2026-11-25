# scriptlive

> اجرای بلادرنگ typescript ایجادشده توسط دستور `script`.
> همچنین ببینید: `script`.
> اطلاعات بیشتر: <https://manned.org/scriptlive>.

- اجرای بلادرنگ typescript:

`scriptlive {{path/to/timing_file}} {{path/to/typescript}}`

- اجرای typescript با دو برابر سرعت اصلی:

`scriptlive {{path/to/timing_file}} {{path/to/typescript}} --divisor 2`

- اجرای typescript ایجادشده با گزینهٔ `--log-in` دستور `script`:

`scriptlive --log-in {{path/to/stdin_log_file}} {{path/to/typescript}}`

- اجرای typescript با حداکثر ۲ ثانیه انتظار بین هر دستور:

`scriptlive {{path/to/timing_file}} {{path/to/typescript}} --maxdelay 2`
