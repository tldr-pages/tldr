# adb reverse

> Android Debug Bridge Reverse: Android emulátor példányból vagy csatlakoztatott Android eszközökből származó socket kapcsolatok visszafordítása. További információ: <https://developer.android.com/studio/command-line/adb>.

- Az összes fordított socket-kapcsolat listázása emulátorokból és eszközökről:

`adb reverse --list`

- Egy emulátorból vagy eszközből származó TCP-port visszafordítása a localhosthoz:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Egy emulátorból vagy eszközből származó fordított aljzatkapcsolat eltávolítása:

`adb reverse --remove tcp:{{remote_port}}`

- Az összes fordított aljzatkapcsolat eltávolítása az összes emulátorról és eszközről:

`adb reverse --remove-all`
