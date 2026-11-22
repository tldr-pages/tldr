# pm list packages

> Показывать установленные, известные или отфильтрованные пакеты на устройстве Android.
> Больше информации: <https://developer.android.com/tools/adb#pm>.

- Показать все установленные пакеты:

`pm list packages`

- Показать все пакеты и пути к их [f]айлам APK:

`pm list packages -f`

- Показать только отключённые ([d]isabled) пакеты:

`pm list packages -d`

- Показать только включённые ([e]nabled) пакеты:

`pm list packages -e`

- Показать только [s]истемные пакеты:

`pm list packages -s`

- Показать только сторонние (не системные, [3]) пакеты:

`pm list packages -3`

- Показать [i]нсталлятор для каждого пакета:

`pm list packages -i`
