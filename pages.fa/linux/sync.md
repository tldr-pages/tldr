# sync

> نوشتن همهٔ عملیات نوشتن در انتظار روی دیسک‌های مربوط.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- نوشتن همهٔ عملیات در انتظار روی همهٔ دیسک‌ها:

`sync`

- نوشتن همهٔ عملیات در انتظار یک فایل روی دیسک:

`sync {{path/to/file}}`

- نوشتن تغییرات و حذف حافظه‌های نهان فایل‌سیستم:

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`
