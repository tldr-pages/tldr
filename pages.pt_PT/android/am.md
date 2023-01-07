# am

> Gestor de atividades do Android (Activity Manager).
> Mais informações: <https://developer.android.com/studio/command-line/adb#am>.

- Iniciar uma atividade específica:

`am start -n {{com.android.settings/.Settings}}`

- Iniciar uma atividade e passar-lhe dados:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Iniciar uma atividade com uma ação e categoria específicas:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converter um `intent` num URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
