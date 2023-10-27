# input

> Відправляє коди подій чи жести на сенсорному екрані на Android девайс.
> Ця команда може бути виконана тільки за допомогою `adb shell`.
> Більше інформації: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Відправити код події для одного знаку на Android девайс:

`input keyevent {{event_code}}`

- Відправити текст на Android девайс (`%s` визначає пробіли):

`input text "{{text}}"`

- Відправити один дотик на Android девайс:

`input tap {{x_position}} {{y_position}}`

- Відправити жест проведення(свайп) на Android девайс:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Відправити довге натискання на Android девайс, використовуючи жест проведення(свайп):

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`
