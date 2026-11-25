# legit

> رابط خط فرمان تکمیلی برای Git.
> اطلاعات بیشتر: <https://frostming.github.io/legit/>.

- رفتن به شاخهٔ مشخص با ذخیرهٔ موقت و بازیابی تغییرات stageنشده:

`git sw {{target_branch}}`

- همگام‌سازی شاخهٔ فعلی با ادغام یا rebase خودکار و ذخیره و بازیابی تغییرات موقت:

`git sync`

- انتشار شاخهٔ مشخص در سرور راه دور:

`git publish {{branch_name}}`

- حذف شاخه از سرور راه دور:

`git unpublish {{branch_name}}`

- فهرست کردن همهٔ شاخه‌ها و وضعیت انتشار آن‌ها:

`git branches {{glob_pattern}}`

- حذف آخرین commit از تاریخچه:

`git undo --hard`
