# input

> Wysyłanie kodów zdarzeń lub gestów na ekranie dotykowym do urządzenia Android.
> Ta komenda może być używana tylko poprzez `adb shell`.
> Więcej informacji: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Wyślij kod zdarzenia dla pojedynczego znaku do urządzenia Android:

`input keyevent {{kod_eventu}}`

- Wyślij tekst do urządzenia z systemem Android (`%s` reprezentuje spacje):

`input text "{{tekst}}"`

- Wyślij pojedyncze stuknięcie do urządzenia Android:

`input tap {{x_pos}} {{y_pos}}`

- Wyślij gest machnięcia do urządzenia Android:

`input swipe {{x_start}} {{y_start}} {{x_koniec}} {{y_koniec}} {{czas_trwania_w_ms}}`

- Wyślij długie naciśnięcie do urządzenia Android za pomocą gestu machnięcia:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{czas_trwania_w_ms}}`
