# am

> Менеджер активностей Android.
> Больше информации: <https://developer.android.com/tools/adb#am>.

- Начать активность с указанным компонентом и именем пакета:

`am start -n {{com.android.settings/.Settings}}`

- Начать намерение с указанным действием и передать в него данные:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Начать активность, соответствующую указанному действию и категории:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Преобразовать намерение в URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Запустить домашнюю активность на эмуляторе или устройстве:

`am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
