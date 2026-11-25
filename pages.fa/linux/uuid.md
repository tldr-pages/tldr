# uuid

> تولید و رمزگشایی شناسه‌های یکتای جهانی (UUID).
> همچنین : `uuidgen`.
> اطلاعات بیشتر: <https://manned.org/uuid>.

- تولید UUIDv1 (بر اساس زمان و آدرس سخت‌افزاری سیستم در صورت وجود):

`uuid`

- تولید UUIDv4 (بر اساس داده‌های تصادفی):

`uuid -v 4`

- تولید چند شناسهٔ UUIDv4 هم‌زمان:

`uuid -v 4 -n {{number_of_uuids}}`

- تولید UUIDv4 و تعیین قالب خروجی:

`uuid -v 4 -F {{BIN|STR|SIV}}`

- تولید UUIDv4 و نوشتن خروجی در فایل:

`uuid -v 4 -o {{path/to/file}}`

- تولید UUIDv5 (بر اساس نام شیء ارائه‌شده) با پیشوند فضای نام مشخص:

`uuid -v 5 ns:{{DNS|URL|OID|X500}} {{object_name}}`

- رمزگشایی UUID مشخص:

`uuid -d {{uuid}}`
