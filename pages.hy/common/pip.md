# pip

> Python փաթեթի կառավարիչ:.
> Որոշ ենթահրամաններ, ինչպիսիք են `install`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip/>:.

- Տեղադրեք փաթեթ (տես `pip install` տեղադրման ավելի շատ օրինակներ).:

`pip install {{package}}`

- Տեղադրեք փաթեթ օգտատիրոջ գրացուցակում` համակարգի ամբողջ լռելյայն գտնվելու վայրի փոխարեն.:

`pip install --user {{package}}`

- Թարմացրեք փաթեթը.:

`pip install {{[-U|--upgrade]}} {{package}}`

- Ապատեղադրել փաթեթը.:

`pip uninstall {{package}}`

- Պահպանեք տեղադրված փաթեթները ֆայլում.:

`pip freeze > {{requirements.txt}}`

- Տեղադրված փաթեթների ցանկ.:

`pip list`

- Ցուցադրել տեղադրված փաթեթի տվյալները.:

`pip show {{package}}`

- Տեղադրեք փաթեթներ ֆայլից.:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
