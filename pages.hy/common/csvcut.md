# csvcut

> Զտել և կրճատել CSV ֆայլերը: Ինչպես Unix-ի `cut` հրամանը, բայց աղյուսակային տվյալների համար:.
> Ներառված է csvkit-ում:.
> Լրացուցիչ տեղեկություններ. <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>:.

- Տպել բոլոր սյունակների ինդեքսները և անունները.:

`csvcut {{[-n|--names]}} {{data.csv}}`

- Քաղեք առաջին և երրորդ սյունակները.:

`csvcut {{[-c|--columns]}} {{1,3}} {{data.csv}}`

- Քաղեք բոլոր սյունակները, բացի չորրորդից.:

`csvcut {{[-C|--not-columns]}} {{4}} {{data.csv}}`

- Քաղեք «id» և «first name» անուններով սյունակները (այդ հերթականությամբ).:

`csvcut {{[-c|--columns]}} {{id,"first name"}} {{data.csv}}`
