# input

> Envia códigos de evento ou gestos de toque para um dispositivo Android.
> Esse comando só pode ser usado através de `adb shell`.
> Mais informações: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Envia um código de evento de um caractere para um dispositivo Android:

`input keyevent {{event_code}}`

- Envia texto para um dispositivo Android (`%s` representa espaços):

`input text "{{text}}"`

- Envia um único toque para um dispositivo Android:

`input tap {{x_pos}} {{y_pos}}`

- Envia um gesto de deslizar para um dispositivo Android:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Envia um pressionamento longo usando gesto de deslizar para um dispositivo Android:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`
