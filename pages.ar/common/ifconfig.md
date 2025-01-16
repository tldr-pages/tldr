# ifconfig

> مُكوِّن واجهة الشبكة.
> لمزيد من التفاصيل: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- عرض إعدادات الشبكة لواجهة محددة.

`ifconfig {{interface_name}}`

- عرض تفاصيل جميع الواجهات، بما في ذلك الواجهات المعطلة.

`ifconfig -a`

- تعطيل واجهة:

`ifconfig {{interface_name}} down`

- تمكين واجهة:

`ifconfig {{interface_name}} up`

تعيين عنوان IP لواجهة محددة:

`ifconfig {{interface_name}} {{ip_address}}`
