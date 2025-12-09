# input

> Send event codes or touchscreen gestures to an Android device.
> This command can only be used through `adb shell`.
> More information: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Send an event code for a single character to an Android device:

`input keyevent {{event_code}}`

- Send a text to an Android device (`%s` represents spaces):

`input text "{{text}}"`

- Send a single tap to an Android device:

`input tap {{x_position}} {{y_position}}`

- Send a swipe gesture to an Android device:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Send a long press to an Android device using a swipe gesture:

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`
