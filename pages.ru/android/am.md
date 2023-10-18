# am

> Менеджер активностей Android.
> Больше информации: <https://developer.android.com/studio/command-line/adb#am>.

- Начать определённую активность:

`am start -n {{com.android.settings/.Settings}}`

- Начать активность и передать в неё данные:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Начать активность соответствующую определенному действию и категории:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Преобразовать намерение в URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
