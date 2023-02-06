# am

> Android tevékenységkezelő. További információ: <https://developer.android.com/studio/command-line/adb#am>.

- Egy adott tevékenység elindítása:

`am start -n {{com.android.settings/.Settings}}`

- Egy tevékenység elindítása és \[d\]ata átadása:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Egy adott műveletnek és \[c\]ategóriának megfelelő tevékenység indítása:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Egy szándék URI-vé alakítása:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
