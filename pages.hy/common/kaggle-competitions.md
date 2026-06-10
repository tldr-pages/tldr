# kaggle մրցույթներ

> Կառավարեք Kaggle մրցույթները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>:.

- Թվարկեք բոլոր մրցույթները.:

`kaggle {{[c|competitions]}} list`

- Ներբեռնեք մրցույթի տվյալները.:

`kaggle {{[c|competitions]}} download {{competition_name}}`

- Ներբեռնեք հատուկ ֆայլ.:

`kaggle {{[c|competitions]}} download {{competition_name}} {{[-f|--file]}} {{file}}`

- Ներկայացրեք ֆայլերը մրցույթին.:

`kaggle {{[c|competitions]}} submit {{competition_name}} {{[-f|--file]}} {{path/to/file}} {{[-m|--message]}} "{{message}}"`

- Ցույց տալ կամ ներբեռնել առաջատարների աղյուսակը.:

`kaggle {{[c|competitions]}} leaderboard {{competition_name}} {{--show|--download}}`

- Դիտեք ներկայացումները.:

`kaggle {{[c|competitions]}} submissions {{competition_name}}`
