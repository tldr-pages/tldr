# fold

> شکستن خط‌های طولانی برای دستگاه‌های خروجی با عرض ثابت.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- شکستن خط‌ها در عرض ثابت:

`fold {{[-w|--width]}} {{width}} {{path/to/file}}`

- محاسبهٔ عرض بر حسب بایت (پیش‌فرض محاسبه بر حسب ستون است):

`fold {{[-b|--bytes]}} {{[-w|--width]}} {{width_in_bytes}} {{path/to/file}}`

- شکستن خط پس از آخرین فضای خالی در محدودهٔ عرض:

`fold {{[-s|--spaces]}} {{[-w|--width]}} {{width}} {{path/to/file}}`
