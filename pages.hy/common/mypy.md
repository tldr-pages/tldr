# mypy

> Մուտքագրեք ստուգման Python կոդը:.
> Լրացուցիչ տեղեկություններ. <https://mypy.readthedocs.io/en/stable/running_mypy.html>:.

- Մուտքագրեք ստուգեք որոշակի ֆայլ.:

`mypy {{path/to/file.py}}`

- Մուտքագրեք ստուգեք որոշակի մոդուլ.:

`mypy {{[-m|--module]}} {{module_name}}`

- Մուտքագրեք ստուգեք որոշակի փաթեթ.:

`mypy {{[-p|--package]}} {{package_name}}`

- Մուտքագրեք ստուգեք կոդի տողը.:

`mypy {{[-c|--command]}} "{{code}}"`

- Անտեսեք բացակայող ներմուծումները.:

`mypy --ignore-missing-imports {{path/to/file_or_directory}}`

- Ցույց տալ մանրամասն սխալի հաղորդագրությունները.:

`mypy {{[--tb|--show-traceback]}} {{path/to/file_or_directory}}`

- Նշեք հատուկ կազմաձևման ֆայլ.:

`mypy --config-file {{path/to/config_file}}`

- Ցուցադրել օգնությունը.:

`mypy {{[-h|--help]}}`
