# uuidgen

> تولید شناسه‌های یکتا (UUID).
> همچنین ببینید: `uuid`.
> اطلاعات بیشتر: <https://manned.org/uuidgen>.

- ایجاد UUIDv4 تصادفی:

`uuidgen {{[-r|--random]}}`

- ایجاد UUIDv1 بر اساس زمان فعلی:

`uuidgen {{[-t|--time]}}`

- ایجاد UUIDv5 برای نام با پیشوند فضای نام مشخص:

`uuidgen {{[-s|--sha1]}} {{[-n|--namespace]}} {{@dns|@url|@oid|@x500}} {{[-N|--name]}} {{object_name}}`
