# fastapi

> Գործարկեք FastAPI հավելվածները, որոնք օգտագործում են Uvicorn-ը գլխարկի տակ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/fastapi>:.

- Գործարկեք FastAPI հավելվածը ավտոմատ վերաբեռնմամբ (մշակման համար).:

`fastapi run {{path/to/file.py}} --reload`

- Ծառայեք ձեր հավելվածը երկու զարգացման ռեժիմով.:

`fastapi dev {{path/to/file.py}}`

- Նշեք հյուրընկալողը և նավահանգիստը, որի վրա պետք է գործարկվի.:

`fastapi run {{path/to/file.py}} --host {{host_address}} --port {{port}}`

- Սահմանեք հավելվածի փոփոխականի անունը (եթե ոչ `app`) կամ նշեք հատուկ հավելվածի գրացուցակ.:

`fastapi run {{path/to/file.py}} --app-dir {{path/to/app}} --app {{custom_app_name}}`

- Ցուցադրել օգնությունը.:

`fastapi --help`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`fastapi {{subcommand}} --help`
