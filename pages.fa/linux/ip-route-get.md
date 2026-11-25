# ip route get

> دریافت یک مسیر به مقصد و چاپ محتویات آن دقیقاً به‌شکلی که هسته می‌بیند.
> اطلاعات بیشتر: <https://manned.org/ip-route>.

- چاپ مسیر به یک مقصد:

`ip {{[r|route]}} {{[g|get]}} {{1.1.1.1}}`

- چاپ مسیر به مقصد از آدرس مبدأ مشخص:

`ip {{[r|route]}} {{[g|get]}} {{destination}} from {{source}}`

- چاپ مسیر به مقصد برای بسته‌های رسیده به واسط مشخص:

`ip {{[r|route]}} {{[g|get]}} {{destination}} iif {{ethX}}`

- چاپ مسیر به مقصد با اجبار خروج از واسط مشخص:

`ip {{[r|route]}} {{[g|get]}} {{destination}} oif {{ethX}}`

- چاپ مسیر به مقصد با نوع سرویس (ToS) مشخص:

`ip {{[r|route]}} {{[g|get]}} {{destination}} tos {{0x10}}`

- چاپ مسیر به مقصد با نمونهٔ مشخص VRF (مسیریابی و ارسال مجازی):

`ip {{[r|route]}} {{[g|get]}} {{destination}} vrf {{myvrf}}`
