# am

> Менеджер активностей Android.
> Больше информации: <https://developer.android.com/tools/adb#am>.

- Запустить активность с указанным компонентом и именем ([n]ame) пакета:

`am start -n {{com.android.settings/.Settings}}`

- Запустить намерение с указанным действием ([a]ction) и передать в него данные ([d]ata):

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Запустить активность, соответствующую указанному действию ([a]ction) и категории ([c]ategory):

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Преобразовать намерение в URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Запустить домашнюю активность на эмуляторе или устройстве:

`am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
