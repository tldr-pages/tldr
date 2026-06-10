# տբ

> Կառավարեք առաջադրանքները և նշումները մի քանի տախտակների վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/klaudiosinani/taskbook#usage>:.

- Ավելացնել նոր առաջադրանք տախտակին.:

`tb {{[-t|--task]}} {{task_description}} @{{board_name}}`

- Ավելացնել նոր նշում գրատախտակին.:

`tb {{[-n|--note]}} {{note_description}} @{{board_name}}`

- Խմբագրել նյութի առաջնահերթությունը.:

`tb {{[-p|--priority]}} @{{item_id}} {{priority}}`

- Ստուգեք/հանեք կետը.:

`tb {{[-c|--check]}} {{item_id}}`

- Արխիվացրեք բոլոր ստուգված տարրերը.:

`tb --clear`

- Տարրը տեղափոխեք տախտակ.:

`tb {{[-m|--move]}} @{{item_id}} {{board_name}}`
