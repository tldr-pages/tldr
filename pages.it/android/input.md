# input

> Invia codici evento o gesture touchscreen a un dispositivo Android.
> Questo comando può essere usato solo attraverso `abd shell`.
> Maggiori informazioni: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Invia un codice evento per un singolo carattere a un dispositivo Android:

`input keyevent {{codice_evento}}`

- Invia un testo a un dispositivo Android (`%s` rappresenta lo spazio):

`input text "{{testo}}"`

- Invia un singolo tap a un dispositivo Android:

`input tap {{pos_x}} {{pos_y}}`

- Invia una gesture di scorrimento a un dispositivo Android:

`input swipe {{inizio_x}} {{inizio_y}} {{fine_x}} {{fine_y}} {{durata_in_ms}}`

- Invia un tap lungo a un dispositivo Android usando una gesture di scorrimento:

`input swipe {{pos_x}} {{pos_y}} {{pos_x}} {{pos_y}} {{durata_in_ms}}`
