# apptainer capability

> مدیریت قابلیت‌های لینوکس برای کاربران و گروه‌ها.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_capability.html>.

- نمایش همهٔ قابلیت‌های موجود لینوکس:

`apptainer capability avail`

- نمایش توضیحات قابلیت‌های مشخص:

`apptainer capability avail {{cap_chown,cap_net_raw,...}}`

- فهرست کردن قابلیت‌ها برای همهٔ کاربران و گروه‌ها:

`apptainer capability list`

- فهرست کردن قابلیت‌ها برای یک کاربر یا گروه مشخص:

`apptainer capability list {{username|groupname}}`

- افزودن قابلیت‌ها به یک کاربر:

`sudo apptainer capability add {{[-u|--user]}} {{username}} {{cap_net_raw,cap_chown,...}}`

- افزودن قابلیت‌ها به یک گروه:

`sudo apptainer capability add {{[-g|--group]}} {{groupname}} {{cap_net_raw,cap_chown,...}}`

- حذف قابلیت‌ها از یک کاربر:

`sudo apptainer capability drop {{[-u|--user]}} {{username}} {{cap_net_raw,cap_chown,...}}`

- حذف همهٔ قابلیت‌ها از یک کاربر:

`sudo apptainer capability drop {{[-u|--user]}} {{username}} all`
