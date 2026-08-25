# pm

> Менеджер пакетов Android.
> Больше информации: <https://developer.android.com/tools/adb#pm>.

- Показать список установленных пакетов:

`pm list packages`

- Установить пакет приложения по указанному пути:

`pm install /{{путь/к/приложению}}.apk`

- Удалить пакет с устройства:

`pm uninstall {{пакет}}`

- Очистить все данные приложения для пакета:

`pm clear {{пакет}}`

- Включить пакет или компонент:

`pm enable {{пакет_или_класс}}`

- Отключить пакет или компонент:

`pm disable-user {{пакет_или_класс}}`

- Предоставить разрешение приложению:

`pm grant {{пакет}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Отозвать разрешение у приложения:

`pm revoke {{пакет}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
