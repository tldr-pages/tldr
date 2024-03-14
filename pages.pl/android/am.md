# am

> Menedżer aktywności Android.
> Więcej informacji: <https://developer.android.com/tools/adb#am>.

- Rozpocznij konkretną aktywność:

`am start -n {{com.android.settings/.Settings}}`

- Rozpocznij aktywność i przekaż do niej dane:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Rozpocznij aktywność dopasowaną do konkretnej akcji i kategorii:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Konwertuj zamiar w URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
