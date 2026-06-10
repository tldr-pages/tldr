#կագել

> Պաշտոնական CLI Kaggle-ի համար, որն իրականացվել է Python 3-ում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>:.

- Դիտեք ընթացիկ կազմաձևման արժեքները.:

`kaggle config view`

- Ներբեռնեք կոնկրետ ֆայլ մրցույթի տվյալների բազայից.:

`kaggle {{[c|competitions]}} download {{competition}} {{[-f|--file]}} {{path/to/file}}`

- Թվարկեք մրցույթները, որոնք համապատասխանում են որոնման տերմինին.:

`kaggle {{[c|competitions]}} list {{[-s|--search]}} {{search_term}}`

- Ցուցակել ֆայլերը, որոնք հասանելի են որոշակի մրցույթի համար.:

`kaggle {{[c|competitions]}} files {{competition}}`

- Ներկայացրեք ֆայլ մրցույթին հաղորդագրությամբ.:

`kaggle {{[c|competitions]}} submit {{competition}} {{[-f|--file]}} {{path/to/submission.csv}} {{[-m|--message]}} "{{message}}"`

- Ցուցակեք որոնման տերմինին համապատասխանող տվյալների հավաքածուները.:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} {{search_term}}`

- Ներբեռնեք բոլոր ֆայլերը տվյալների բազայից.:

`kaggle {{[d|datasets]}} download {{owner}}/{{dataset_name}}`

- Ցուցակեք միջուկները (նոթատետրերը), որոնք համապատասխանում են որոնման տերմինին.:

`kaggle {{[k|kernels]}} list {{[-s|--search]}} {{search_term}}`
