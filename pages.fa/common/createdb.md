# createdb

> ساخت یک دیتابیس پستگرس.
> اطلاعات بیشتر: <https://www.postgresql.org/docs/current/app-createdb.html>.

- ساخت یک دیتابیس که صاحب آن کاربر فعلی باشد:

`createdb {{database_name}}`

- ساخت یک دیتابیس که صاحب آن یک کاربر خاص باشد و توضیحاتی درمورد آن نیز ارائه شده باشد:

`createdb --owner {{username}} {{database_name}} '{{description}}'`

- ساخت یک دیتابیس از روی یک قالب:

`createdb --template {{template_name}} {{database_name}}`
