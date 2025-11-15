# am

> Менеджер активності Android.
> Більше інформації: <https://developer.android.com/tools/adb#am>.

- Почати специфічну активність:

`am start -n {{com.android.settings/.Settings}}`

- Почати активність та передайте дані у неї:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Почати активність яка є специфічною дією та категорією:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Перетворити значення в посилання:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
