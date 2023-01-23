# adb shell

> Android Debug Bridge Shell: Távoli shell parancsok futtatása egy Android emulátor példányon vagy csatlakoztatott Android eszközökön. További információ: <https://developer.android.com/studio/command-line/adb>.

- Távoli interaktív shell indítása az emulátoron/készüléken:

`adb shell`

- Az összes tulajdonság lekérése az emulátorból vagy az eszközről:

`adb shell getprop`

- Az összes futásidejű jogosultság visszaállítása az alapértelmezettre:

`adb shell pm reset-permissions`

- Veszélyes engedély visszavonása egy alkalmazáshoz:

`adb shell pm revoke {{package}} {{permission}}`

- Kulcsesemény kiváltása:

`adb shell input keyevent {{keycode}}`

- Egy alkalmazás adatainak törlése egy emulátoron vagy eszközön:

`adb shell pm clear {{package}}`

- Egy tevékenység elindítása emulátoron/eszközön:

`adb shell am start -n {{package}}/{{activity}}`

- Kezdő tevékenység indítása egy emulátoron vagy eszközön:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
