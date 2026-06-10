# mkdir

> Ստեղծեք դիրեկտորիաներ և սահմանեք դրանց թույլտվությունները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>:.

- Ստեղծեք հատուկ դիրեկտորիաներ.:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- Անհրաժեշտության դեպքում ստեղծեք հատուկ գրացուցակներ և նրանց ծնողները.:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- Ստեղծեք դիրեկտորիաներ հատուկ թույլտվություններով.:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`

- Ստեղծեք մի քանի ներդիր գրացուցակներ ռեկուրսիվ կերպով.:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`
