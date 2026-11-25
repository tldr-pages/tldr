# bindfs

> سوار کردن یک دایرکتوری در محلی دیگر با مجوزهای متفاوت.
> اطلاعات بیشتر: <https://bindfs.org/docs/bindfs.1.html>.

- سوار کردن یک دایرکتوری با همان مجوزها:

`sudo bindfs {{path/to/directory}} {{path/to/mount_point}}`

- نگاشت اشیای سیستم فایل متعلق به `user1` به مالکیت `user2` (برای فایل‌های تازه‌ساخته‌شده به‌صورت معکوس نیز اعمال می‌شود):

`sudo bindfs --map={{user1}}/{{user2}} {{path/to/directory}} {{path/to/mount_point}}`

- پیاده کردن یک دایرکتوری:

`sudo umount {{path/to/mount_point}}`
