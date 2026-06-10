# վիրտուալ

> Ստեղծեք վիրտուալ մեկուսացված Python միջավայրեր:.
> Լրացուցիչ տեղեկություններ. <https://virtualenv.pypa.io/en/latest/cli_interface.html>:.

- Ստեղծել նոր միջավայր.:

`virtualenv {{path/to/venv}}`

- Անհատականացրեք հուշման նախածանցը.:

`virtualenv --prompt {{prompt_prefix}} {{path/to/venv}}`

- Օգտագործեք Python-ի այլ տարբերակ virtualenv-ով.:

`virtualenv {{[-p|--python]}} {{path/to/pythonbin}} {{path/to/venv}}`

- Սկսեք (ընտրեք) միջավայրը.:

`source {{path/to/venv}}/bin/activate`

- Դադարեցրեք շրջակա միջավայրը.:

`deactivate`
