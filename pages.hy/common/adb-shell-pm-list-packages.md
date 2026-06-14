# adb shell pm ցուցակի փաթեթներ

> Ցուցակեք տեղադրված, հայտնի կամ զտված փաթեթները Android սարքում:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Նշեք բոլոր տեղադրված փաթեթները.:

`adb shell pm list packages`

- Թվարկեք բոլոր փաթեթները և դրանց հետ կապված APK [f]ile ուղիները.:

`adb shell pm list packages -f`

- Նշեք միայն [d]անջատված փաթեթները.:

`adb shell pm list packages -d`

- Նշեք միայն [e]միացված փաթեթները.:

`adb shell pm list packages -e`

- Նշեք միայն [s] համակարգի փաթեթները.:

`adb shell pm list packages -s`

- Ցուցակե՛ք միայն [3]-րդ կողմի (ոչ համակարգային) փաթեթները.:

`adb shell pm list packages -3`

- Ցույց տալ [i]nstaller-ը յուրաքանչյուր փաթեթի համար.:

`adb shell pm list packages -i`
