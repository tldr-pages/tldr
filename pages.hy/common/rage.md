#զայրույթ

> Պարզ, անվտանգ և ժամանակակից ֆայլերի գաղտնագրման գործիք (և Rust գրադարան) փոքր հստակ ստեղներով, առանց կազմաձևման ընտրանքների և UNIX-ի ոճի կոմպոզիցիայի հնարավորությամբ:.
> `age`-ի Rust իրականացումը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/str4d/rage>:.

- Գաղտնագրեք ֆայլը `user`-ի համար և պահեք այն `message.age`-ում:

`echo "{{Your secret message}}" | rage --encrypt --recipient {{user}} --output {{path/to/message.age}}`

- Ապակոդավորեք ֆայլը `identity_file`-ով և պահեք այն `message`-ում:

`rage --decrypt --identity {{path/to/identity_file}} --output {{message}}`
