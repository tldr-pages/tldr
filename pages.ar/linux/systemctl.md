# systemctl

> التحكم في مدير نظام systemd والخدمات.
> لمزيد من التفاصيل: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- عرض جميع الخدمات قيد التشغيل:

`systemctl status`

- عرض الوحدات الفاشلة:

`systemctl --failed`

- بدء/إيقاف/إعادة تشغيل/إعادة تحميل/عرض حالة خدمة:

`systemctl {{start|stop|restart|reload|status}} {{unit}}`

- تمكين/تعطيل وحدة ليتم تشغيلها عند بدء تشغيل النظام:

`systemctl {{enable|disable}} {{unit}}`

- إعادة تحميل systemd والبحث عن وحدات جديدة أو متغيرة:

`systemctl daemon-reload`

- التحقق مما إذا كانت الوحدة نشطة/مُمكّنة/فاشلة:

`systemctl {{is-active|is-enabled|is-failed}} {{unit}}`

- عرض جميع وحدات الخدمة/المقبس/التركيب التلقائي مع التصفية حسب الحالة (قيد التشغيل/فاشلة):

`systemctl list-units {{[-t|--type]}} {{service|socket|automount}} --state {{failed|running}}`

- عرض محتويات ومسار ملف الوحدة:

`systemctl cat {{unit}}`
