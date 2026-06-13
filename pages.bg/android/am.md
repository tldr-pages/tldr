# am

> Мениджър на дейности на Android.
> Повече информация: <https://developer.android.com/tools/adb#am>.

- Стартиране на дейността с конкретен компонент и име на пакет [n]ame:

`am start -n {{com.android.settings/.Settings}}`

- Стартиране на действие [a]ction и предаване на [d]ata към него:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Стартиране на дейност, съответстваща на конкретно [a]ction и [c]ategory:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Конвертиране на намерение в URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
