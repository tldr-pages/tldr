# input

> Отправить коды событий или жесты сенсорного экрана на устройство Android.
> Эту команду можно использовать только через `adb shell`.
> Больше информации: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Отправить код события для одного символа на устройство Android:

`input keyevent {{event_code}}`

- Отправить текст на устройство Android (`%s` означает пробел):

`input text "{{text}}"`

- Отправить одно нажатие на экран на устройство Android:

`input tap {{x_pos}} {{y_pos}}`

- Отправить жест смахивания на устройство Android:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Отправить длинное нажатие на экран на устройство Android с помощью жеста смахивания:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`
