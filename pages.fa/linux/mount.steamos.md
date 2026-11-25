# mount.steamos

> سوار یا پیاده کردن پارتیشن‌های فایل‌سیستم SteamOS.
> اطلاعات بیشتر: <https://gitlab.com/users/evlaV/projects>.

- سوار کردن همهٔ پارتیشن‌های لازم از دستگاه در دایرکتوری مقصد:

`sudo mount.steamos {{/dev/sdX}} {{/mnt}}`

- سوار کردن با گزینه‌های مستثنا کردن پارتیشن‌های مشخص (مانند `/home` و overlayها):

`sudo mount.steamos {{[-o|--options]}} nohome,nooverlay {{/dev/sdX}} {{/mnt}}`

- پیاده کردن همهٔ پارتیشن‌های سوارشده زیر دایرکتوری مقصد:

`sudo mount.steamos -u {{/mnt}}`

- نمایش راهنما:

`mount.steamos {{[-h|--help]}}`
