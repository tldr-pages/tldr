# am

> Gerenciador de atividades do Android (Activity Manager).
> Mais informações: <https://developer.android.com/studio/command-line/adb#am>.

- Inicia uma activity específica:

`am start -n {{com.android.settings/.Settings}}`

- Inicia uma activity e passa dados para ela:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Inicia uma activity correspondente a uma ação e categoria específicas:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converte uma intent em uma URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
