#լպշարժիր

> Տեղափոխեք աշխատանքը կամ բոլոր աշխատանքները մեկ այլ տպիչ:.
> Տես նաև՝ `cancel`, `lp`, `lpr`, `lprm`:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-lpmove.html>:.

- Տեղափոխեք կոնկրետ աշխատանք `new_printer`:

`lpmove {{job_id}} {{new_printer}}`

- Տեղափոխեք աշխատանքը `old_printer`-ից `new_printer`:

`lpmove {{old_printer}}-{{job_id}} {{new_printer}}`

- Տեղափոխեք բոլոր աշխատանքները `old_printer`-ից `new_printer`:

`lpmove {{old_printer}} {{new_printer}}`

- Տեղափոխեք որոշակի աշխատանք `new_printer` որոշակի սերվերի վրա.:

`lpmove -h {{server}} {{job_id}} {{new_printer}}`
