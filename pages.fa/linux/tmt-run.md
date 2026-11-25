# tmt run

> اجرای مراحل آزمون `tmt`. به‌طور پیش‌فرض همهٔ مراحل اجرا می‌شوند.
> اطلاعات بیشتر: <https://tmt.readthedocs.io/en/stable/stories/cli.html#run>.

- اجرای همهٔ مراحل آزمون برای هر طرح:

`tmt run`

- اجرای فقط مرحلهٔ کشف برای نمایش آزمون‌های قابل اجرا:

`tmt run discover {{[-v|--verbose]}}`

- اجرای همهٔ مراحل و تنظیم گزینه‌های مرحلهٔ فراهم‌سازی:

`tmt run {{[-a|--all]}} provision {{[-h|--how]}} {{container}} {{[-i|--image]}} {{fedora:rawhide}}`

- اجرای فقط طرح‌ها و آزمون‌های انتخاب‌شده:

`tmt run plan {{[-n|--name]}} {{/plan/name}} test {{[-n|--name]}} {{/test/name}}`

- نمایش نتایج آخرین اجرا در مرورگر وب:

`tmt run {{[-l|--last]}} report {{[-h|--how]}} {{html}} {{[-o|--open]}}`

- اجرای آزمون‌ها با زمینهٔ ارائه‌شده:

`tmt run {{[-c|--context]}} {{key=value}} {{[-c|--context]}} {{distro=fedora}}`

- اجرای تعاملی آزمون‌ها (اشکال‌زدایی کد آزمون در میانهٔ آزمون):

`tmt run {{[-a|--all]}} execute {{[-h|--how]}} {{tmt}} --interactive`

- شبیه‌سازی اجرا برای مشاهدهٔ اقدامات احتمالی با بیشترین جزئیات:

`tmt run {{[-n|--dry]}} {{[-vvv|--verbose --verbose --verbose]}}`
