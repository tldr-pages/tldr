# update-alternatives

> نگهداری آسان پیوندهای نمادین برای تعیین دستورهای پیش‌فرض.
> اطلاعات بیشتر: <https://manned.org/update-alternatives>.

- افزودن پیوند نمادین:

`sudo update-alternatives --install {{path/to/symlink}} {{command_name}} {{path/to/command_binary}} {{priority}}`

- پیکربندی پیوند نمادین برای `java`:

`sudo update-alternatives --config java`

- حذف پیوند نمادین:

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- نمایش اطلاعات دستور مشخص:

`update-alternatives --display {{java}}`

- نمایش همهٔ دستورها و انتخاب فعلی آن‌ها:

`update-alternatives --get-selections`
