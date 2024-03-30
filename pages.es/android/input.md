# input

> Envía códigos de eventos o gestos de pantalla táctil a un dispositivo Android.
> Este comando solo se puede usar a través de `adb shell`.
> Más información: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Envía un código de evento para un solo carácter a un dispositivo Android:

`input keyevent {{codigo_evento}}`

- Envía un texto a un dispositivo Android (`%s` representa espacios):

`input text "{{texto}}"`

- Envía una pulsación a un dispositivo Android:

`input tap {{x_pos}} {{y_pos}}`

- Envía un gesto de deslizamiento a un dispositivo Android:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duracion_en_ms}}`

- Envía una pulsación larga a un dispositivo Android mediante un gesto de deslizamiento:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duracion_en_ms}}`
