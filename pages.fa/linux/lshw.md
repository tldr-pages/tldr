# lshw

> فهرست کردن اطلاعات مفصل پیکربندی سخت‌افزار با کاربر root.
> همچنین : `inxi`, `hwinfo`, `dmidecode`.
> اطلاعات بیشتر: <https://ezix.org/project/wiki/HardwareLiSter>.

- اجرای رابط گرافیکی X11 (در صورت وجود):

`sudo lshw -X`

- فهرست کردن همهٔ سخت‌افزارها در قالب جدول:

`sudo lshw -short`

- فهرست کردن چند ردهٔ سخت‌افزار (همهٔ دیسک‌ها و کنترل‌کننده‌های ذخیره‌سازی) در قالب جدول:

`sudo lshw {{[-c|-class]}} disk {{[-c|-class]}} storage -short`

- ذخیرهٔ همهٔ واسط‌های شبکه در فایل HTML/XML/JSON:

`sudo lshw {{[-c|-class]}} network -{{html|xml|json}} >interfaces{{.html|.xml|.json}}`

- فهرست کردن واسط‌های شبکه بدون افشای اطلاعات حساس (آدرس IP، شماره‌سریال و غیره):

`sudo lshw {{[-c|-class]}} network -sanitize`

- فهرست کردن ردهٔ مشخص سخت‌افزار:

`sudo lshw {{[-c|-class]}} {{system|bridge|memory|processor|address|storage|disk|tape|bus|network|display|input|printer|multimedia|communication|power|volume|generic}}`
