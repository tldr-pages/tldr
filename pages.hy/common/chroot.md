# chroot

> Գործարկել հրամանը կամ ինտերակտիվ վահանակը հատուկ արմատային գրացուցակով:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>:.

- Գործարկեք `$SHELL`-ը նոր արմատային գրացուցակում.:

`sudo chroot {{path/to/new_root}}`

- Գործարկել հրամանը որպես նոր արմատային գրացուցակ.:

`sudo chroot {{path/to/new_root}} {{command}}`

- Օգտագործեք հատուկ օգտվող և խումբ.:

`sudo chroot --userspec {{username_or_id}}:{{group_name_or_id}} {{path/to/new_root}}`
