# ufw

> جدار حماية بسيط.
> واجهة أمامية لـ `iptables` تهدف إلى تسهيل تكوين جدار الحماية.
> لمزيد من التفاصيل: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- تفعيل ufw:

`ufw enable`

- تعطيل ufw:

`ufw disable`

- عرض قواعد ufw مع أرقامها:

`ufw status numbered`

- السماح بحركة المرور الواردة على المنفذ 5432 مع تعليق يحدد الخدمة:

`ufw allow {{5432}} comment "{{Service}}"`

- السماح بحركة مرور TCP فقط من العنوان 192.168.0.4 إلى أي عنوان على هذا الجهاز، على المنفذ 22:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- منع حركة المرور على المنفذ 80 على هذا الجهاز:

`ufw deny {{80}}`

- منع جميع حركة مرور UDP إلى المنافذ في النطاق 8412:8500:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- حذف قاعدة معينة. يمكن الحصول على رقم القاعدة من أمر `ufw status numbered`:

`ufw delete {{rule_number}}`
