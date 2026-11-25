# objcopy

> کپی محتویات فایل شیء در فایل دیگر.
> اطلاعات بیشتر: <https://manned.org/objcopy>.

- کپی داده‌ها در فایل دیگر:

`objcopy {{path/to/source_file}} {{path/to/target_file}}`

- تبدیل فایل‌های شیء از یک قالب به قالب دیگر:

`objcopy --input-target={{input_format}} --output-target {{output_format}} {{path/to/source_file}} {{path/to/target_file}}`

- حذف همهٔ اطلاعات نمادها از فایل:

`objcopy --strip-all {{path/to/source_file}} {{path/to/target_file}}`

- حذف اطلاعات اشکال‌زدایی از فایل:

`objcopy --strip-debug {{path/to/source_file}} {{path/to/target_file}}`

- کپی بخش مشخص از فایل مبدأ در فایل مقصد:

`objcopy --only-section {{section}} {{path/to/source_file}} {{path/to/target_file}}`
