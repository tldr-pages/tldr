# modetest

> عیب‌یابی Direct Rendering Manager و Kernel Mode Setting.
> اطلاعات بیشتر: <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841850/Video_Mixer#modetest>.

- فهرست کردن اتصال‌دهنده‌ها و حالت‌های موجود آن‌ها:

`modetest -c`

- فهرست کردن اتصال‌دهنده‌ها و حالت‌های موجود آن‌ها برای درایور مشخص:

`modetest -M {{mgag200}} -c`

- تنظیم وضوح یک اتصال‌دهنده:

`sudo modetest -M {{mgag200}} -s {{connector_id}}:{{1600}}x{{1200}}`
