# am

> Administrador de actividades de Android.
> Más información: <https://developer.android.com/tools/adb#am>.

- Inicia una actividad específica:

`am start -n {{com.android.settings/.Settings}}`

- Inicia una actividad y le suministra datos:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Inicia una actividad que coincide con una acción y categoría específicas:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Convierte una intención en una URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
