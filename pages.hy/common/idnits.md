# idnits

> Ստուգեք ինտերնետ-սևագրերը ներկայացման կետերի համար:.
> Փնտրում է <https://www.ietf.org/id-info/checklist>-ում թվարկված պահանջների 2.1 և 2.2 բաժինների խախտումները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ietf-tools/idnits>:.

- Ստուգեք ֆայլը nits-ի համար.:

`idnits {{path/to/file.txt}}`

- Հաշվեք բիտերը՝ առանց դրանք ցուցադրելու.:

`idnits --nitcount {{path/to/file.txt}}`

- Ցույց տալ լրացուցիչ տեղեկություններ վիրավորական գծերի մասին.:

`idnits --verbose {{path/to/file.txt}}`

- ակնկալեք նշված տարին կաթսայի մեջ ընթացիկ տարվա փոխարեն.:

`idnits --year {{2021}} {{path/to/file.txt}}`

- Ենթադրենք, որ փաստաթուղթը նշված կարգավիճակի է.:

`idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{path/to/file.txt}}`
