# gdbus

> تعامل با اشیای D-Bus.
> بخشی از GLib است.
> اطلاعات بیشتر: <https://manned.org/gdbus>.

- بازرسی یک شیء برای مشاهدهٔ رابط‌ها و متدهای آن:

`gdbus introspect --session --dest {{destination_bus_name}} --object-path /{{path/to/object}}`

- فراخوانی متد یک شیء با آرگومان‌ها:

`gdbus call --session --dest {{destination_bus_name}} --object-path /{{path/to/object}} --method {{interface.method_name}} {{argument1 argument2 ...}}`

- ارسال سیگنال از یک شیء با آرگومان‌ها:

`gdbus emit --session --object-path /{{path/to/object}} --signal {{interface.signal_name}} {{argument1 argument2 ...}}`

- پایش همهٔ پیام‌ها در گذرگاه نشست:

`gdbus monitor --session`
