# atomupd-manager

> مدیریت به‌روزرسانی‌های SteamOS.
> اطلاعات بیشتر: <https://github.com/evlaV/atomupd-daemon>.

- بررسی به‌روزرسانی‌های موجود:

`sudo atomupd-manager check`

- به‌روزرسانی به یک تصویر مشخص:

`sudo atomupd-manager update {{version_id}}`

- چاپ کانال به‌روزرسانی فعلی که دنبال می‌شود:

`atomupd-manager tracked-branch`

- فهرست کردن کانال‌های به‌روزرسانی موجود:

`atomupd-manager list-branches`

- تغییر به یک کانال به‌روزرسانی مشخص:

`sudo atomupd-manager switch-branch {{stable|beta|preview|rc|bc|pc|main}}`
