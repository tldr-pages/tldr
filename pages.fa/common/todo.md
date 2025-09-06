# todo

> ابزاری ساده و استاندارد برای مدیریت یادداشت و فهرست وظایف.
> اطلاعات بیشتر: <https://todoman.readthedocs.io>.

- لیست کارهای آغاز نشده:

`todo list --startable`

- اضافه کردن یک وظیفه به فهرست کارها :

`todo new {{thing_to_do}} --list {{work}}`

- اضافه کردن مکان به یک وظیفه با آیدی:

`todo edit --location {{location_name}} {{task_id}}`

- نمایش جزییات یک وظیفه:

`todo show {{task_id}}`

- علامت زدن وظیفه ها با آیدی مشخص شده به عنوان تکمیل شده:

`todo done {{task_id1 task_id2 ...}}`

- حذف یک وظیفه:

`todo delete {{task_id}}`

- حذف وظایف انجام شده و بازشماری آیدی وظایف باقی مانده:

`todo flush`
