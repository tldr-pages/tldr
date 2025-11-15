# am

> Androids Aktivitäten-Manager.
> Weitere Informationen: <https://developer.android.com/tools/adb#am>.

- Starte eine bestimmte Aktivität:

`am start -n {{com.android.settings/.Settings}}`

- Starte eine Aktivität und übergib ihr Daten:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Starte eine Aktivität, auf die eine bestimmte Aktion und Kategorie zutrifft:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Konvertiere ein bestimmtes Ziel in einen URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
