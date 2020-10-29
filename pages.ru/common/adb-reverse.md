# adb reverse

> Android Debug Bridge Reverse: обратное соединение от эмулятора Android или подключенного устройства Android.
> Больше информации: <https://developer.android.com/studio/command-line/adb>.

- Вывести список всех обратных соединений от эмуляторов и устройств:

`adb reverse --list`

- Указать TCP-порт от эмулятора или устройства до localhost:

`adb reverse tcp:{{удалённый_порт}} tcp:{{локальный_порт}}`

- Создать обратное соединение от эмулятора или устройства:

`adb reverse --remove tcp:{{удалённый_порт}}`

- Удалить все обратные соединения на всех эмуляторах и устройствах:

`adb reverse --remove-all`
