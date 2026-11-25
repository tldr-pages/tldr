# apparmor_parser

> بارگذاری، کامپایل و مدیریت پروفایل‌های امنیتی AppArmor.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_apparmor_parser.8>.

- بارگذاری یک پروفایل در هسته:

`sudo apparmor_parser {{[-a|--add]}} {{profile_file}}`

- جایگزینی یک پروفایل موجود:

`sudo apparmor_parser {{[-r|--replace]}} {{profile_file}}`

- حذف یک پروفایل از هسته:

`sudo apparmor_parser {{[-R|--remove]}} {{profile_name}}`

- بارگذاری یک پروفایل در حالت گزارش تخلف (تخلف‌ها را ثبت می‌کند اما مسدود نمی‌کند):

`sudo apparmor_parser {{[-C|--complain]}} {{[-r|--replace]}} {{path/to/profile}}`

- پیش‌پردازش یک پروفایل (حل کردن دستورهای include) و نوشتن حافظهٔ نهان دودویی در فایل:

`apparmor_parser {{[-p|--preprocess]}} {{[-o|--ofile]}} {{path/to/output.cache}} {{[-Q|--skip-kernel-load]}} {{path/to/profile}}`

- پیش‌پردازش و چاپ پروفایل دودویی در خروجی استاندارد `stdout` بدون بارگذاری:

`apparmor_parser {{[-p|--preprocess]}} {{[-S|--stdout]}} {{[-Q|--skip-kernel-load]}} {{path/to/profile}}`

- جایگزینی یک پروفایل بدون خواندن حافظهٔ نهان:

`sudo apparmor_parser {{[-r|--replace]}} {{[-T|--skip-read-cache]}} {{path/to/profile}}`

- جایگزینی یک پروفایل، بازسازی حافظهٔ نهان و نوشتن آن در یک دایرکتوری دلخواه:

`sudo apparmor_parser {{[-r|--replace]}} {{[-W|--write-cache]}} {{[-L|--cache-loc]}} /{{path/to/cache}} {{path/to/profile}}`
