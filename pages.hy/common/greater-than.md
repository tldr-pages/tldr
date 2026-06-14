# >

> Վերահղման ելքը:.
> Լրացուցիչ տեղեկություններ. <https://gnu.org/software/bash/manual/bash.html#Redirecting-Output>:.

- Վերահղեք `stdout` ֆայլ՝:

`{{command}} > {{path/to/file}}`

- Ավելացրեք ֆայլին.:

`{{command}} >> {{path/to/file}}`

- Վերահղեք և՛ `stdout`, և՛ `stderr` ֆայլին՝:

`{{command}} &> {{path/to/file}}`

- Վերահղեք `stderr` դեպի `/dev/null`՝ տերմինալի ելքը մաքուր պահելու համար.:

`{{command}} 2> /dev/null`

- Մաքրել ֆայլի բովանդակությունը կամ ստեղծել նոր դատարկ ֆայլ.:

`> {{path/to/file}}`

- Վերահղեք `stderr` դեպի `stdout`՝ դրանք իրար միացնելու համար:

`{{command1}} 2>&1 | {{command2}}`

- Բացեք մշտական ֆայլի նկարագրիչ.:

`exec {{3}}>{{path/to/file}}`

- Գրեք հատուկ ֆայլի նկարագրիչ.:

`{{echo text}} >&{{3}}`
