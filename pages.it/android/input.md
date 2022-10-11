# input

> Invia codici evento o gesture touchscreen a un dispositivo Android.
> Questo comando può essere usato solo attraverso `abd shell`.
> Maggiori informazioni: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Invia un codice evento per un singolo carattere a un dispositivo Android:

`input keyevent {{event_code}}`

- Invia un testo a un dispositivo Android (`%s` rappresenta lo spazio):

`input text "{{text}}"`

- Invia un singolo tap a un dispositivo Android:

`input tap {{x_pos}} {{y_pos}}`

- Invia una gesture di scorrimento a un dispositivo Android:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Invia un tap lungo a un dispositivo Android usando una gesture di scorrimento:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`
