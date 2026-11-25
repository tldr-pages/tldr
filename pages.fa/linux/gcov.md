# gcov

> ابزار تحلیل پوشش کد و پروفایل‌سازی که بخش‌های آزموده‌نشدهٔ برنامه را پیدا می‌کند.
> همچنین نسخه‌ای از کد منبع را همراه با فراوانی اجرای بخش‌های کد نمایش می‌دهد.
> اطلاعات بیشتر: <https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>.

- تولید گزارش پوشش با نام `file.cpp.gcov`:

`gcov {{path/to/file.cpp}}`

- نوشتن تعداد اجرای جداگانه برای هر بلوک پایه:

`gcov {{[-a|--all-blocks]}} {{path/to/file.cpp}}`

- نوشتن فراوانی شاخه‌ها در فایل خروجی و چاپ اطلاعات خلاصه در خروجی استاندارد `stdout` به‌صورت درصد:

`gcov {{[-b|--branch-probabilities]}} {{path/to/file.cpp}}`

- نوشتن فراوانی شاخه‌ها به‌صورت تعداد شاخه‌های طی‌شده به جای درصد:

`gcov {{[-c|--branch-counts]}} {{path/to/file.cpp}}`

- ایجاد نکردن فایل خروجی `gcov`:

`gcov {{[-n|--no-output]}} {{path/to/file.cpp}}`

- نوشتن خلاصه‌ها در سطح فایل و همچنین سطح تابع:

`gcov {{[-f|--function-summaries]}} {{path/to/file.cpp}}`
