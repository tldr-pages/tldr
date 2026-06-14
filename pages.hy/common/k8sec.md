# k8 վրկ

> Կառավարեք Kubernetes-ի գաղտնիքները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dtan4/k8sec>:.

- Թվարկեք բոլոր գաղտնիքները.:

`k8sec list`

- Նշեք որոշակի գաղտնիք որպես base64 կոդավորված տող.:

`k8sec list {{secret_name}} --base64`

- Սահմանեք գաղտնիքի արժեքը.:

`k8sec set {{secret_name}} {{key=value}}`

- Սահմանեք base64 կոդավորված արժեք.:

`k8sec set --base64 {{secret_name}} {{key=encoded_value}}`

- Բացահայտեք գաղտնիք.:

`k8sec unset {{secret_name}}`

- Բեռնել գաղտնիքները ֆայլից.:

`k8sec load {{[-f|--filename]}} {{path/to/file}} {{secret_name}}`

- Թափել գաղտնիքները ֆայլի մեջ.:

`k8sec dump {{[-f|--filename]}} {{path/to/file}} {{secret_name}}`
