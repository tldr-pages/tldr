# koji tag-build

> اعمال برچسب به یک یا چند ساخت.
> اطلاعات بیشتر: <https://docs.pagure.org/koji/>.

- اعمال برچسب به یک یا چند ساخت:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}}`

- منتظر نماندن برای کار:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}} --nowait`

- اجرای اجباری عملیات:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}} --force`

- نمایش راهنما:

`koji tag-build {{[-h|--help]}}`
