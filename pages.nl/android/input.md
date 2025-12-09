# input

> Stuur gebeurteniscodes of touchscreen-gebaren naar een Android-apparaat.
> Dit commando kan alleen worden gebruikt via `adb shell`.
> Meer informatie: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Stuur een gebeurteniscode voor een enkel teken naar een Android-apparaat:

`input keyevent {{event_code}}`

- Stuur een tekst naar een Android-apparaat (`%s` vertegenwoordigt spaties):

`input text "{{text}}"`

- Stuur een enkele tik naar een Android-apparaat:

`input tap {{x_position}} {{y_position}}`

- Stuur een swipe-gebaar naar een Android-apparaat:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Stuur een lange druk naar een Android-apparaat met behulp van een swipe-gebaar:

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`
