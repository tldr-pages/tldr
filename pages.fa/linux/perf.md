# perf

> چارچوب اندازه‌گیری شمارنده‌های عملکرد لینوکس.
> اطلاعات بیشتر: <https://perfwiki.github.io/main/>.

- نمایش آمار پایهٔ شمارندهٔ عملکرد برای دستور:

`perf stat {{gcc hello.c}}`

- نمایش نمایهٔ بلادرنگ شمارندهٔ عملکرد در کل سیستم:

`sudo perf top`

- اجرای دستور و ثبت نمایهٔ آن در `perf.data`:

`sudo perf record {{command}}`

- ثبت نمایهٔ فرایند موجود در `perf.data`:

`sudo perf record {{[-p|--pid]}} {{process_id}}`

- خواندن `perf.data` (ایجادشده توسط `perf record`) و نمایش نمایه:

`sudo perf report`
