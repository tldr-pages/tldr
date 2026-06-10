#ընտրել

> Bash ներկառուցված կոնստրուկցիա՝ մենյու ստեղծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-select>:.

- Ստեղծեք մենյու առանձին բառերից.:

`select {{word}} in {{apple orange pear banana}}; do echo ${{word}}; done`

- Ստեղծեք մենյու մեկ այլ հրամանի ելքից.:

`select {{line}} in $({{command}}); do echo ${{line}}; done`

- Նշեք հուշման տողը `select`-ի համար և ստեղծեք ընտրացանկ՝ ընթացիկ գրացուցակից ֆայլ կամ թղթապանակ ընտրելու համար.:

`PS3="{{Select a file: }}"; select {{file}} in *; do echo ${{file}}; done`

- Ստեղծեք մենյու Bash զանգվածից.:

`{{fruits}}=({{apple orange pear banana}}); select {{word}} in ${{{fruits[@]}}}; do echo ${{word}}; done`
