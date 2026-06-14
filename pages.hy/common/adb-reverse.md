# adb հակադարձ

> Հակադարձ վարդակից միացումներ միացված Android սարքից կամ էմուլյատորից:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Թվարկեք բոլոր հակադարձ վարդակների միացումները էմուլյատորներից և սարքերից.:

`adb reverse --list`

- Փոխեք TCP պորտը միակ միացված էմուլյատորից կամ սարքից դեպի localhost.:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Հետադարձեք TCP պորտը կոնկրետ էմուլյատորից կամ սարքից (ըստ սարքի ID-ի / [ս]սերիական համարի) դեպի localhost.:

`adb -s {{device_id}} reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Հեռացրեք հակադարձ վարդակից միացումը էմուլյատորից կամ սարքից.:

`adb reverse --remove tcp:{{remote_port}}`

- Հեռացրեք բոլոր հակադարձ վարդակների միացումները բոլոր էմուլյատորներից և սարքերից.:

`adb reverse --remove-all`
