# ddev

> PHP միջավայրերի համար կոնտեյների վրա հիմնված տեղական զարգացման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://docs.ddev.com/en/stable/users/usage/cli/>:.

- Նախագիծ սկսել.:

`ddev start`

- Կազմաձևեք նախագծի տեսակը և հաստատումը.:

`ddev config`

- Հետևեք գրանցամատյանին.:

`ddev logs {{[-f|--follow]}}`

- Գործարկել կոմպոզիտորը կոնտեյներով.:

`ddev composer`

- Տեղադրեք հատուկ Node.js տարբերակ.:

`ddev nvm install {{version}}`

- Արտահանել տվյալների բազա.:

`ddev export-db {{[-f|--file]}} {{/tmp/db.sql.gz}}`

- Գործարկեք հատուկ հրաման կոնտեյների մեջ.:

`ddev exec {{echo 1}}`
