# flask-unsign

> Գործիք, որը թույլ է տալիս կոպիտ ուժ կիրառել, վերծանել և ստեղծել `Flask` սեսիայի թխուկներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Paradoxis/Flask-Unsign>:.

- Վերծանել Flask նիստի թխուկը՝:

`flask-unsign {{[-d|--decode]}} {{[-c|--cookie]}} {{cookie}}`

- Վերծանեք սեսիայի թխուկը, որը բերվել է URL-ից, որը վերադարձնում է `Set-Cookie` վերնագիր.:

`flask-unsign {{[-d|--decode]}} --server {{url}}`

- Գաղտնի բանալի կոպիտ ուժով պարտադրել լռելյայն flask-unsign-wordlist (պահանջում է `flask-unsign-wordlist`):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}}`

- Բացահայտեք գաղտնի բանալի հատուկ բառացանկով (օգտագործեք `--no-literal-eval` չակերտավոր գրառումների համար).:

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}}`

- Ստորագրեք նոր նստաշրջանի թխուկը գաղտնի բանալիով.:

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} "{{{'logged_in': False}}}" {{[-S|--secret]}} {{secret}}`

- Ստորագրեք նստաշրջանի թխուկը՝ օգտագործելով ժառանգական ժամանակի դրոշմը (օգտակար հին տարբերակների համար).:

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} "{{{'logged_in': False}}}" {{[-S|--secret]}} {{secret}} {{[-l|--legacy]}}`

- Դաժանորեն պարտադրել նստաշրջանի թխուկը հատուկ թելերով և առանց բառացի գնահատման.:

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-t|--threads]}} {{threads}} {{[-nE|--no-literal-eval]}}`
