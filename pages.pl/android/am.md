# am

> Menedżer aktywności Android.
> Więcej informacji: <https://developer.android.com/tools/adb#am>.

- Rozpocznij aktywność z określoną [n]azwą komponentu i pakietu:

`am start -n {{com.android.settings/.Settings}}`

- Rozpocznij [a]kcję intencji i przekaż do niej [d]ane:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Rozpocznij aktywność dopasowaną do konkretnej akcji i kategorii ([c]ategory):

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Konwertuj intencję na URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
