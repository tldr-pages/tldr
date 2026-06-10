# adb

> Android Debug Bridge. հաղորդակցվել Android emulator օրինակի կամ միացված Android սարքերի հետ:.
> Որոշ ենթահրամաններ, ինչպիսիք են `shell`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Ստուգեք, արդյոք adb սերվերի գործընթացը աշխատում է և սկսեք այն.:

`adb start-server`

- Դադարեցրեք adb սերվերի գործընթացը.:

`adb kill-server`

- Սկսեք հեռակառավարման վահանակ թիրախային էմուլյատորի/սարքի օրինակում.:

`adb shell`

- Android հավելվածը մղեք էմուլյատորին/սարքին.:

`adb install -r {{path/to/file}}.apk`

- Պատճենեք ֆայլ/տեղեկատու թիրախային սարքից.:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Պատճենեք ֆայլը/տեղեկատուը թիրախային սարքին.:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Նշեք բոլոր միացված սարքերը.:

`adb devices`

- Նշեք, թե որ սարքին պետք է հրամաններ ուղարկել, եթե կան մի քանի սարքեր.:

`adb -s {{device_id}} {{shell}}`
