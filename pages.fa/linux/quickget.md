# quickget

> بارگیری و آماده‌سازی مواد لازم برای ساخت ماشین مجازی Quickemu.
> توجه: پارامتر «edition» گاهی اختیاری است.
> همچنین : `quickemu`.
> اطلاعات بیشتر: <https://github.com/quickemu-project/quickemu>.

- نمایش فهرست همهٔ سیستم‌عامل‌های مهمان، نسخه‌ها و گونه‌های پشتیبانی‌شده در قالب‌های مختلف:

`quickget {{--list|--list-csv|--list-json}}`

- بارگیری و ایجاد پیکربندی ماشین مجازی برای ساخت ماشین Quickemu برای یک سیستم‌عامل:

`quickget {{os}} {{release}} {{edition}}`

- بارگیری پیکربندی ماشین مجازی Windows 11 با درایورهای VirtIO برای Windows:

`quickget windows 11`

- بارگیری تصویر بازیابی macOS و ایجاد پیکربندی ماشین مجازی:

`quickget macos {{mojave|catalina|big-sur|monterey|ventura|sonoma}}`

- نمایش URL تصویر ISO یک سیستم‌عامل:

`quickget --url {{os}} {{release}} {{edition}}`

- بررسی موجود بودن فایل ISO برای سیستم‌عامل:

`quickget --check {{os}} {{release}} {{edition}}`

- بارگیری تصویر بدون ساخت هیچ پیکربندی ماشین مجازی:

`quickget --download {{os}} {{release}} {{edition}}`

- ایجاد پیکربندی ماشین مجازی برای تصویر سیستم‌عامل (فایل ISO از دایرکتوری مبدأ منتقل می‌شود):

`quickget --create-config {{os}} {{path/to/iso}}`
