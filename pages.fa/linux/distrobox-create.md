# distrobox-create

> ایجاد یک کانتینر Distrobox.
> کانتینر ایجادشده به‌طور نزدیک با میزبان یکپارچه می‌شود و امکان اشتراک دایرکتوری `$HOME` کاربر، فضای ذخیره‌سازی خارجی، دستگاه‌های USB خارجی، برنامه‌های گرافیکی (X11/Wayland) و صدا را فراهم می‌کند.
> همچنین ببینید: `distrobox`.
> اطلاعات بیشتر: <https://distrobox.it/usage/distrobox-create/>.

- ایجاد یک کانتینر Distrobox با استفاده از تصویر اوبونتو:

`distrobox-create {{container_name}} {{[-i|--image]}} {{ubuntu:latest}}`

- رونوشت‌گیری از یک کانتینر Distrobox:

`distrobox-create {{[-c|--clone]}} {{container_name}} {{cloned_container_name}}`
