# brctl

> مدیریت پل اترنت.
> اطلاعات بیشتر: <https://manned.org/brctl>.

- نمایش فهرستی از اطلاعات پل‌های اترنت موجود:

`sudo brctl show`

- ایجاد یک رابط پل اترنت جدید:

`sudo brctl add {{bridge_name}}`

- حذف یک رابط پل اترنت موجود:

`sudo brctl del {{bridge_name}}`

- افزودن یک رابط به پل موجود:

`sudo brctl addif {{bridge_name}} {{interface_name}}`

- حذف یک رابط از پل موجود:

`sudo brctl delif {{bridge_name}} {{interface_name}}`
