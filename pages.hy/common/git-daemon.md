# git daemon

> Իսկապես պարզ սերվեր Git պահեստների համար:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-daemon>:.

- Գործարկեք Git Daemon-ը սպիտակ ցուցակում նշված դիրեկտորիաների հավաքածուով.:

`git daemon --export-all {{path/to/directory1 path/to/directory2 ...}}`

- Գործարկեք Git daemon-ը հատուկ բազային գրացուցակով և թույլ տվեք քաշել բոլոր ենթագրքերից, որոնք նման են Git պահոցներին.:

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- Գործարկեք Git Daemon-ը նշված գրացուցակի համար՝ մանրամասնորեն տպելով տեղեկամատյանների հաղորդագրությունները և թույլ տալով Git հաճախորդներին գրել դրան.:

`git daemon {{path/to/directory}} --enable=receive-pack --informative-errors --verbose`
