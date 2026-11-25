# trace-cmd record

> ضبط رویدادهای ردیابی هسته.
> همچنین ببینید: `trace-cmd list`, `trace-cmd report`.
> اطلاعات بیشتر: <https://manned.org/trace-cmd-record>.

- ضبط ردیابی با افزونهٔ مشخص:

`sudo trace-cmd record -p {{plugin}}`

- ضبط ردیابی فایل اجرایی مشخص:

`sudo trace-cmd record -F {{executable}}`

- ضبط ردیابی تابع مشخص:

`sudo trace-cmd record -g {{function}}`

- مستثنا کردن تابع مشخص از ردیابی:

`sudo trace-cmd record -n {{function}}`

- محدود کردن عمق گراف فراخوانی تابع:

`sudo trace-cmd record --max-graph-depth {{depth}}`

- ضبط ردیابی از شناسهٔ فرایند مشخص:

`sudo trace-cmd record -P {{process_id}}`
