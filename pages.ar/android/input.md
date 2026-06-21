# input

> ارسال (event codes) او (touchscreen gestures) الى اجهزة اندرويد
> يمكنك استخدام هذا الامر من خلال `adb shell`.
> لمزيد من التفاصيل: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- ارسال (event code) او حرف واحد لأجهزة الاندرويد:

`input keyevent {{event_code}}`

- ارسال نص لجهاز اندرويد (`%s` تمثل مسافة (space)):

`input text "{{text}}"`

- ارسال نقرة واحدة لجهاز اندرويد:

`input tap {{x_position}} {{y_position}}`

- ارسال سحبة لجهاز انرويد:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- ارسال سحبة طويلة لجهاز اندرويد من خلال سحبة:

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`
