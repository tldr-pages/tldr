# ptx

> تولید نمایهٔ جایگشتی واژه‌ها از فایل‌های متنی.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- تولید نمایهٔ جایگشتی که نخستین فیلد هر خط ارجاع نمایه است:

`ptx {{[-r|--references]}} {{path/to/file}}`

- تولید نمایهٔ جایگشتی با ارجاع‌های نمایهٔ تولیدشده به‌صورت خودکار:

`ptx {{[-A|--auto-reference]}} {{path/to/file}}`

- تولید نمایهٔ جایگشتی با عرض ثابت:

`ptx {{[-w|--width]}} {{width_in_columns}} {{path/to/file}}`

- تولید نمایهٔ جایگشتی با فهرست واژه‌های فیلترشده:

`ptx {{[-o|--only-file]}} {{path/to/filter}} {{path/to/file}}`

- تولید نمایهٔ جایگشتی با رفتارهای سبک SYSV:

`ptx {{[-G|--traditional]}} {{path/to/file}}`
