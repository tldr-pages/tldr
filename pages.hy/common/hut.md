#խրճիթ

> CLI գործիք sourcehut-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/hut>:.

- Նախաձեռնեք `hut`-ի կազմաձևման ֆայլը (սա կպահանջի OAuth2 մուտքի նշան, որը պահանջվում է `hut` օգտագործելու համար):

`hut init`

- Ցուցակեք Git/Mercurial պահեստները.:

`hut {{git|hg}} list`

- Ստեղծեք հանրային Git/Mercurial պահոց.:

`hut {{git|hg}} create {{name}}`

- Ցուցակեք աշխատանքները <https://builds.sr.ht>-ում:

`hut builds list`

- Ցույց տալ աշխատանքի կարգավիճակը.:

`hut builds show {{job_id}}`

- SSH-ը աշխատանքի կոնտեյների մեջ.:

`hut ssh {{job_id}}`
