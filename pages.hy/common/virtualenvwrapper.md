# virtualenvrapper

> Python-ի `virtualenv` գործիքի պարզ փաթաթման հրամանների խումբ:.
> Լրացուցիչ տեղեկություններ. <https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html>:.

- Ստեղծեք նոր Python `virtualenv` `$WORKON_HOME`-ում:

`mkvirtualenv {{virtualenv_name}}`

- Ստեղծեք `virtualenv` Python-ի կոնկրետ տարբերակի համար.:

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- Ակտիվացրեք կամ օգտագործեք այլ `virtualenv`՝:

`workon {{virtualenv_name}}`

- Դադարեցրեք `virtualenv`-ը.:

`deactivate`

- Թվարկեք բոլոր վիրտուալ միջավայրերը.:

`lsvirtualenv`

- Հեռացնել `virtualenv`:

`rmvirtualenv {{virtualenv_name}}`

- Ստացեք բոլոր virtualenvwrapper հրամանների ամփոփագիրը.:

`virtualenvwrapper`
