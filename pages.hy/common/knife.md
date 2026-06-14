#դանակ

> Շփվեք շեֆ-սերվերի հետ տեղական խոհարարի պահեստից:.
> Լրացուցիչ տեղեկություններ. <https://docs.chef.io/workstation/knife/>:.

- Bootstrap նոր հանգույց.:

`knife bootstrap {{fqdn_or_ip}}`

- Նշեք բոլոր գրանցված հանգույցները.:

`knife node list`

- Ցույց տալ հանգույց.:

`knife node show {{node_name}}`

- Խմբագրել հանգույց.:

`knife node edit {{node_name}}`

- Խմբագրել դերը.:

`knife role edit {{role_name}}`

- Դիտեք տվյալների պայուսակը.:

`knife data bag show {{data_bag_name}} {{data_bag_item}}`

- Վերբեռնեք տեղական խոհարարական գիրքը խոհարարի սերվերում.:

`knife cookbook upload {{cookbook_name}}`
