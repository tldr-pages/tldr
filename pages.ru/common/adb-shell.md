# adb shell

> Android Debug Bridge Shell: Запуск удалённой командной оболочки на эмуляторе Android или подключенном устройстве Android.
> Больше информации: <https://developer.android.com/tools/adb>.

- Запустить удалённую интерактивную оболочку на эмуляторе или устройстве:

`adb shell`

- Получить все свойства от эмулятора или устройства:

`adb shell getprop`

- Вернуть всем разрешениям значение по умолчанию:

`adb shell pm reset-permissions`

- Отозвать опасные разрешения для приложения:

`adb shell pm revoke {{пакет}} {{разрешения}}`

- Вызвать событие клавиши:

`adb shell input keyevent {{код_клавиши}}`

- Очистить данные приложения на эмуляторе или устройстве:

`adb shell pm clear {{пакет}}`

- Запустить activity на эмуляторе или устройстве:

`adb shell am start -n {{пакет}}/{{активность}}`

- Запустить базовый activity на эмуляторе или устройстве:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
