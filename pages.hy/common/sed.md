# sed

> Խմբագրել տեքստը տեքստային եղանակով:.
> Տես նաև՝ `awk`, `ed`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sed.1posix>:.

- Բոլոր `apple` (հիմնական `regex`) դեպքերը փոխարինեք `mango`-ով (հիմնական `regex`) մուտքագրման բոլոր տողերում և արդյունքը տպեք `stdout`-ում՝:

`{{command}} | sed 's/apple/mango/g'`

- Կատարեք հատուկ սկրիպտ [f]ile և տպեք արդյունքը `stdout`-ում:

`{{command}} | sed -f {{path/to/script.sed}}`

- Տպեք ընդամենը առաջին տողը `stdout`-ում՝:

`{{command}} | sed -n '1p'`
