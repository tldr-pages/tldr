# distrobox-export

> صادر کردن برنامه، سرویس یا فایل دودویی از کانتینر به سیستم‌عامل میزبان.
> همچنین ببینید: `distrobox`.
> اطلاعات بیشتر: <https://distrobox.it/usage/distrobox-export/>.

- صادر کردن برنامه از کانتینر به میزبان (ورودی میزکار و نماد آن در فهرست برنامه‌های سیستم میزبان ظاهر می‌شوند):

`distrobox-export {{[-a|--app]}} {{package}} {{[-ef|--extra-flags]}} "--foreground"`

- صادر کردن فایل دودویی از کانتینر به میزبان:

`distrobox-export {{[-b|--bin]}} {{path/to/binary}} {{[-ep|--export-path]}} {{path/to/binary_on_host}}`

- صادر کردن فایل دودویی از کانتینر به میزبان (برای مثال در `$HOME/.local/bin`):

`distrobox-export {{[-b|--bin]}} {{path/to/binary}} {{[-ep|--export-path]}} {{path/to/export}}`

- صادر کردن سرویس از کانتینر به میزبان (`--sudo` سرویس را با دسترسی ریشه درون کانتینر اجرا می‌کند):

`distrobox-export --service {{package}} {{[-ef|--extra-flags]}} "--allow-newer-config" {{[-S|--sudo]}}`

- حذف یا لغو صدور یک برنامهٔ صادرشده:

`distrobox-export {{[-a|--app]}} {{package}} {{[-d|--delete]}}`
