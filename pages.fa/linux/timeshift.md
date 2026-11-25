# timeshift

> ابزار بازیابی سیستم.
> اطلاعات بیشتر: <https://manned.org/timeshift>.

- فهرست کردن snapshotها:

`sudo timeshift --list`

- ایجاد snapshot جدید (در صورت زمان‌بندی شدن):

`sudo timeshift --check`

- ایجاد snapshot جدید (حتی بدون زمان‌بندی):

`sudo timeshift --create`

- بازیابی snapshot (انتخاب تعاملی snapshot برای بازیابی):

`sudo timeshift --restore`

- بازیابی snapshot مشخص:

`sudo timeshift --restore --snapshot '{{snapshot}}'`

- حذف snapshot مشخص:

`sudo timeshift --delete --snapshot '{{snapshot}}'`
