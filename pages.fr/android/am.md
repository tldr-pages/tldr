# am

> Manager d'activité Android.
> Plus d'informations : <https://developer.android.com/tools/adb#am>.

- Commence une activité spécifique :

`am start -n {{com.android.settings/.Settings}}`

- Commence une activité et insère de la donnée :

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Commence une activité qui correspond à une action et une catégorie spécifique :

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Convertis une intention en URI :

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
