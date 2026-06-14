# feroxbuster

> Պարզ, արագ, ռեկուրսիվ բովանդակության հայտնաբերման գործիք՝ գրված Rust-ով:.
> Օգտագործվում է վեբ սերվերների վրա թաքնված ուղիների կոպիտ ուժով և ավելին:.
> Լրացուցիչ տեղեկություններ. <https://epi052.github.io/feroxbuster-docs/configuration/command-line>:.

- Բացահայտեք հատուկ դիրեկտորիաներ և ֆայլեր, որոնք համընկնում են բառացանկում ընդարձակման և 100 թելերի և պատահական օգտագործողի գործակալի հետ.:

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --threads {{100}} --extensions "{{php,txt}}" --random-agent`

- Թվարկեք դիրեկտորիաները առանց ռեկուրսիի հատուկ վստահված անձի միջոցով.:

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --no-recursion --proxy "{{http://127.0.0.1:8080}}"`

- Գտեք հղումներ վեբ էջերում.:

`feroxbuster --url "{{https://example.com}}" --extract-links`

- Զտեք որոշակի կարգավիճակի կոդով և մի շարք նիշերով.:

`feroxbuster --url "{{https://example.com}}" --filter-status {{301}} --filter-size {{4092}}`
