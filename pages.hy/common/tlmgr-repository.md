# tlmgr պահոց

> Կառավարեք TeX Live տեղադրման պահեստները:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#repository>:.

- Թվարկեք բոլոր կազմաձևված պահեստները և դրանց պիտակները (եթե սահմանված է).:

`tlmgr repository list`

- Թվարկեք բոլոր փաթեթները, որոնք հասանելի են հատուկ պահոցում.:

`tlmgr repository list {{path|url|tag}}`

- Ավելացնել նոր պահոց հատուկ պիտակով (պիտակը պարտադիր չէ).:

`sudo tlmgr repository add {{path|url}} {{tag}}`

- Հեռացրեք հատուկ պահոց.:

`sudo tlmgr repository remove {{path|url|tag}}`

- Սահմանեք պահեստների նոր ցուցակ՝ վերագրելով նախորդ ցուցակը.:

`sudo tlmgr repository set {{path|url|tag}}#{{tag}} {{path|url|tag}}#{{tag}} {{...}}`

- Ցույց տալ բոլոր կազմաձևված պահոցների ստուգման կարգավիճակը.:

`tlmgr repository status`
