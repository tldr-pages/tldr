# adb առաջ

> Փոխանցել վարդակից միացումները միացված Android սարքին կամ էմուլյատորին:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Փոխանցեք TCP պորտը միակ միացված էմուլյատորին կամ սարքին.:

`adb forward tcp:{{local_port}} tcp:{{remote_port}}`

- Փոխանցեք TCP պորտը հատուկ էմուլյատորին կամ սարքին (սարքի ID-ով / [սերիական համարով).:

`adb -s {{device_id}} forward tcp:{{local_port}} tcp:{{remote_port}}`

- Թվարկեք բոլոր վերահասցեավորումները.:

`adb forward --list`

- Հեռացրեք փոխանցման կանոնը.:

`adb forward --remove tcp:{{local_port}}`

- Հեռացրեք փոխանցման բոլոր կանոնները.:

`adb forward --remove-all`
