#նմուշ

> Վերլուծության համար ընտրեք և գրանցեք պրոցեսորի պրոֆիլները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mstange/samply>:.

- Գրանցեք հրամանի պրոֆիլը և բացեք այն բրաուզերում.:

`samply record {{path/to/command arg1 arg2 ...}}`

- Կարգավորել նմուշառման արագությունը.:

`samply record --rate {{rate_in_hz}} {{path/to/command arg1 arg2 ...}}`

- Գրանցեք պրոֆիլը ֆայլում՝ առանց զննարկիչը բացելու.:

`samply record --save-only --output {{path/to/profile.json}} -- {{path/to/command arg1 arg2 ...}}`

- Բեռնել նախկինում պահպանված պրոֆիլը դիտարկիչում.:

`samply load {{path/to/profile.json}}`
