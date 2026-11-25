# ttyplot

> ابزار رسم بلادرنگ برای خط فرمان با ورودی داده از `stdin`.
> اطلاعات بیشتر: <https://github.com/tenox7/ttyplot>.

- رسم مقادیر `1`، `2` و `3` (توجه: `cat` مانع خروج `ttyplot` می‌شود):

`{ echo 1 2 3; cat; } | ttyplot`

- تنظیم عنوان و واحد مشخص:

`{ echo {{1 2 3}}; cat; } | ttyplot -t {{title}} -u {{unit}}`

- استفاده از حلقهٔ while برای رسم پیوستهٔ مقادیر تصادفی:

`{ while true; do echo $RANDOM; sleep {{1}}; done } | ttyplot`

- تجزیهٔ خروجی `ping` و نمایش بصری آن:

`ping {{8.8.8.8}} | sed -u '{{s/^.*time=//g; s/ ms//g}}' | ttyplot -t "{{ping to 8.8.8.8}}" -u {{ms}}`
