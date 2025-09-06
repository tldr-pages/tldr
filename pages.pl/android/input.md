# input

> Wysyłaj kody zdarzeń lub gestów na ekranie dotykowym do urządzenia Android.
> Ta komenda może być używana tylko poprzez `adb shell`.
> Więcej informacji: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Wyślij kod zdarzenia dla pojedynczego znaku do urządzenia Android:

`input keyevent {{kod_zdarzenia}}`

- Wyślij tekst do urządzenia z systemem Android (`%s` reprezentuje spacje):

`input text "{{tekst}}"`

- Wyślij pojedyncze stuknięcie do urządzenia Android:

`input tap {{pozycja_x}} {{pozycja_y}}`

- Wyślij gest przesunięcia do urządzenia Android:

`input swipe {{x_start}} {{y_start}} {{x_koniec}} {{y_koniec}} {{czas_trwania_w_ms}}`

- Wyślij długie naciśnięcie do urządzenia Android za pomocą gestu przesunięcia:

`input swipe {{pozycja_x}} {{pozycja_y}} {{pozycja_x}} {{pozycja_y}} {{czas_trwania_w_ms}}`
