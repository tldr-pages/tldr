# պիլինտ

> Python-ի կոդերի ներդիր:.
> Լրացուցիչ տեղեկություններ. <https://pylint.pycqa.org/en/latest/>:.

- Ցույց տալ lint սխալները ֆայլում.:

`pylint {{path/to/file.py}}`

- Փաթեթ կամ մոդուլ փակցրեք (պետք է ներմուծվի, ոչ `.py` վերջածանց).:

`pylint {{package_or_module}}`

- Տեղադրեք փաթեթը գրացուցակի ուղուց (պետք է պարունակի `__init__.py` ֆայլ).:

`pylint {{path/to/directory}}`

- Տեղադրեք ֆայլը և օգտագործեք կազմաձևման ֆայլ (սովորաբար կոչվում է `pylintrc`):

`pylint --rcfile {{path/to/pylintrc}} {{path/to/file.py}}`

- Տեղադրեք ֆայլը և անջատեք հատուկ սխալի կոդը.:

`pylint --disable {{C,W,no-error,design}} {{path/to/file}}`
