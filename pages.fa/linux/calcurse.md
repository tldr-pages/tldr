# calcurse

> برنامهٔ تقویم و زمان‌بندی مبتنی بر متن.
> اطلاعات بیشتر: <https://github.com/lfos/calcurse/blob/pu/doc/calcurse.1.txt>.

- شروع `calcurse` در حالت تعاملی:

`calcurse`

- چاپ قرارها و رویدادهای روز فعلی و خروج:

`calcurse {{[-a|--appointment]}}`

- حذف همهٔ موارد محلی calcurse و وارد کردن موارد راه دور:

`calcurse-caldav --init=keep-remote`

- حذف همهٔ موارد راه دور و ارسال موارد محلی calcurse:

`calcurse-caldav --init=keep-local`

- کپی کردن موارد محلی به سرور CalDAV و برعکس:

`calcurse-caldav --init=two-way`
