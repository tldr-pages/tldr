# dnf reposync

> همگام‌سازی بسته‌ها و فرادادهٔ مخزن راه دور DNF در یک دایرکتوری محلی.
> به‌صورت پیش‌فرض بخشی از `dnf` نیست، اما از طریق `dnf-plugins-core` پشتیبانی می‌شود.
> اطلاعات بیشتر: <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>.

- همگام‌سازی همهٔ بسته‌های مخزن با شناسهٔ `repo_name` در زیردایرکتوری `repo_name` از دایرکتوری کاری فعلی:

`dnf reposync --repoid {{repo_name}}`

- همگام‌سازی همهٔ بسته‌ها و تعیین محل ذخیرهٔ دلخواه:

`dnf reposync --repoid {{repo_name}} {{[-p|--download-path]}} {{path/to/directory}}`

- همگام‌سازی همهٔ بسته‌ها و فراداده:

`dnf reposync --repoid {{repo_name}} --download-metadata`

- دانلود فقط جدیدترین بسته‌های هر مخزن:

`dnf reposync --repoid {{repo_name}} {{[-n|--newest-only]}}`

- فقط چاپ URL مواردی که دانلود می‌شوند، بدون دانلود:

`dnf reposync --repoid {{repo_name}} {{[-u|--urls]}}`

- تلاش برای تنظیم زمان فایل‌های دانلودشده مطابق زمان فایل‌های راه دور:

`dnf reposync --repoid {{repo_name}} --remote-time`
