# bwrap

> اجرای برنامه‌ها در یک محیط ایزولهٔ سبک.
> اطلاعات بیشتر: <https://manned.org/bwrap>.

- اجرای یک برنامه در محیط فقط‌خواندنی:

`bwrap --ro-bind / / {{/bin/bash}}`

- دادن دسترسی به دستگاه‌ها و اطلاعات فرایند به محیط و ایجاد یک `tmpfs` برای آن:

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp {{/bin/bash}}`
