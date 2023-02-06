# pod

> Függőségkezelő Swift és Objective-C Cocoa projektekhez. További információ: <https://guides.cocoapods.org/terminal/commands.html>.

- Hozzon létre egy Podfile-t az aktuális projekthez az alapértelmezett tartalommal:

`pod init`

- Töltse le és telepítse a Podfile-ban definiált összes podot (amelyek még nem lettek telepítve):

`pod install`

- Listázza ki az összes elérhető podot:

`pod list`

- Az elavult podok megjelenítése (a jelenleg telepítettek közül):

`pod outdated`

- Az összes jelenleg telepített pod frissítése a legújabb verzióra:

`pod update`

- Egy adott (korábban telepített) pod frissítése a legújabb verzióra:

`pod update {{pod_name}}`

- CocoaPodok eltávolítása egy Xcode projektből:

`pod deintegrate {{xcode_project}}`
