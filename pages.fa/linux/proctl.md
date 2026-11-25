# proctl

> مدیریت مجوزها و زبان‌های پروژه‌ها و تغییر میان مجوزهای قالب‌بندی‌شده.
> اطلاعات بیشتر: <https://github.com/CreativeCodeCat/proctl>.

- فهرست کردن مجوزهای موجود:

`proctl {{[-ll|-list-licenses]}}`

- فهرست کردن زبان‌های موجود:

`proctl {{[-lL|-list-languages]}}`

- انتخاب مجوز در منوی FZF:

`proctl {{[-pl|-pick-license]}}`

- انتخاب زبان در منوی FZF:

`proctl {{[-pL|-pick-language]}}`

- حذف همهٔ مجوزها از پروژهٔ فعلی:

`proctl {{[-r|-remove-license]}}`

- ایجاد قالب مجوز جدید:

`proctl {{[-t|-new-template]}}`

- حذف مجوز از قالب‌ها:

`proctl {{[-R|-delete-license]}} {{@license_name1 @license_name2 ...}}`

- نمایش راهنما:

`proctl {{[-h|-help]}}`
