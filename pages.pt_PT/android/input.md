# input

> Envia códigos de eventos ou toques no ecrã para um dispositivo Android.
> Este comando só pode ser usado com a `adb shell`.
> Mais informações: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Enviar um código de evento de um caractere para um dispositivo Android:

`input keyevent {{codigo_de_evento}}`

- Enviar texto para um dispositivo Android (`%s` representa espaços):

`input text "{{texto}}"`

- Enviar um único toque para um dispositivo Android:

`input tap {{x_pos}} {{y_pos}}`

- Enviar um gesto de deslizar para um dispositivo Android:

`input swipe {{x_inicio}} {{y_inicio}} {{x_fim}} {{y_fim}} {{duração_em_ms}}`

- Enviar um toque prolongado usando um gesto de deslize para um dispositivo Android:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duração_em_ms}}`
