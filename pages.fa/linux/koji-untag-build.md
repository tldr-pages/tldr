# koji untag-build

> حذف برچسب از یک یا چند ساخت.
> اطلاعات بیشتر: <https://docs.pagure.org/koji/>.

- حذف برچسب از یک یا چند ساخت:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}}`

- حذف برچسب از همهٔ نسخه‌های بسته در این برچسب:

`koji untag-build {{tag}} {{pkg1 pkg2 ...}} --all`

- حذف برچسب از همهٔ نسخه‌های بسته در این برچسب به‌جز جدیدترین نسخه:

`koji untag-build {{tag}} {{pkg1 pkg2 ...}} --non-latest`

- حالت آزمایشی:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}} {{[-n|--test]}}`

- چاپ جزئیات:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}} {{[-v|--verbose]}}`

- نمایش راهنما:

`koji untag-build {{[-h|--help]}}`
