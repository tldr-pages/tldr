# ern

> Electrode Native platform parancssori kliens. További információ: <https://native.electrode.io/reference/index-6>.

- Hozzon létre egy új `ern` alkalmazást (`MiniApp`):

`ern create-miniapp {{application_name}}`

- Egy vagy több `MiniApps` futtatása az iOS / Android Runner alkalmazásban:

`ern run-{{ios|android}}`

- Hozzon létre egy Electrode Native konténert:

`ern create-container --miniapps {{/path/to/miniapp_directory}} --platform {{ios|android}}`

- Electrode Native konténer közzététele egy helyi Maven-tárban:

`ern publish-container --publisher {{maven}} --platform {{android}} --extra {{'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'}}`

- Egy iOS konténer átalakítása előre lefordított bináris keretrendszerré:

`ern transform-container --platform {{ios}} --transformer {{xcframework}}`

- Az Electrode Native összes telepített verziójának listázása:

`ern platform versions`

- Naplózási szint beállítása:

`ern platform config set logLevel {{trace|debug}}`
