# input

> ارسال کد رویداد یا ورودی صفحه نمایش به یک دستگاه اندروید.
> این دستور فقط از طریق `adb shell` قابل اجراست.
> اطلاعات بیشتر: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- ارسال کد رویداد یک کاراکتر به یک دستگاه اندروید :

`input keyevent {{event_code}}`

- ارسال یک متن به یک دستگاه اندروید (`%s` نمایانگر فاصله است) :

`input text "{{متن}}"`

- ارسال یک ضربه به یک دستگاه اندروید :

`input tap {{x_position}} {{y_position}}`

- ارسال حرکت افقی عمودی به یک دستگاه اندروید :

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- ارسال یک نگهداشتن بلند مدت به یک دستگاه اندرویدی از طریق حرکت افقی عمودی :

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`
