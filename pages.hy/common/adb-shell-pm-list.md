# adb shell pm ցուցակ

> Ցուցակե՛ք օգտվողներին, փաթեթները, թույլտվությունները, գործիքավորումը, թույլտվությունների խմբերը, հնարավորությունները և փաթեթների կառավարչի կողմից կառավարվող գրադարանները:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Նշեք բոլոր տեղադրված փաթեթները.:

`adb shell pm list packages`

- Տպել համակարգի բոլոր օգտվողներին.:

`adb shell pm list users`

- Տպել բոլոր հայտնի թույլտվությունների խմբերը.:

`adb shell pm list permission-groups`

- Տպել բոլոր հայտնի թույլտվությունները.:

`adb shell pm list permissions`

- Թվարկեք բոլոր թեստային փաթեթները.:

`adb shell pm list instrumentation`

- Տպել համակարգի բոլոր հնարավորությունները.:

`adb shell pm list features`

- Տպեք ընթացիկ սարքի կողմից աջակցվող բոլոր գրադարանները.:

`adb shell pm list libraries`
