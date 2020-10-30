# adb shell

> Android Debug Bridge Shell: Запуск удалённых команд оболочки на экземпляре эмулятора Андроид или на подключённом Андроид устройстве.
> Больше информации на <https://developer.android.com/studio/command-line/adb>.

- Запуск удалённой интерактивной оболочки на эмуляторе/устройстве:

`adb shell`

- Получить все свойства из эмулятора или устройства:

`adb shell getprop`

- Вернуть все разрешения времени исполнения на умолчательные:

`adb shell pm reset-permissions`

- Отменить все опасные разрешения для приложения:

`adb shell pm revoke {{пакет}} {{разрешения}}`

- Вызвать событие клавиши:

`adb shell input keyevent {{код_клавиши}}`

- Очистить данные приложения на эмуляторе или устройстве:

`adb shell pm clear {{пакет}}`

- Запуск активности на эмуляторе/устройстве:

`adb shell am start -n {{пакет}}/{{активность}}`

- Запуск домашней активности на эмуляторе/устройстве:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
