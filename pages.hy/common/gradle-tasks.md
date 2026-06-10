# gradle առաջադրանքներ

> Թվարկե՛ք Gradle նախագծում առկա առաջադրանքները:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_tasks>:.

- Թվարկեք հիմնական խնդիրները.:

`gradle tasks`

- Թվարկեք բոլոր առաջադրանքները, ներառյալ ենթաառաջադրանքները.:

`gradle tasks --all`

- Նշեք առաջադրանքները կոնկրետ խմբում.:

`gradle tasks --group {{group_name}}`

- Նշեք առաջադրանքները կոնկրետ ենթածրագրի համար.:

`gradle :{{subproject}}:tasks`
