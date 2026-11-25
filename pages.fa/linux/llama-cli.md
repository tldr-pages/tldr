# llama-cli

> رابط خط فرمان برای استنتاج مدل‌های زبانی بزرگ.
> اطلاعات بیشتر: <https://github.com/ggml-org/llama.cpp#llama-cli>.

- شروع مدل زبانی و رابط:

`llama-cli {{[-m|--model]}} {{path/to/model}}`

- شروع با اندازهٔ زمینهٔ تنظیم‌شده در اعلان:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-c|--ctx-size]}} {{number}}`

- شروع با تعیین تعداد لایه‌های بارسپاری‌شده به GPU:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-ngl|--n-gpu-layers]}} {{auto|all|number}}`

- شروع با ارسال محتوای فایل به‌عنوان اعلان سیستمی:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-sysf|--system-prompt-file]}} {{path/to/prompt}}`

- شروع با ارسال محتوای فایل به‌عنوان اولین اعلان:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-f|--file]}} {{path/to/prompt}}`
