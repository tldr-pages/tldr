#մարիմո

> Python-ի ռեակտիվ նոթատետրի միջավայր:.
> Համատեղում է Jupyter-ի, Streamlit-ի և այլ նոթատետրային գործիքների առանձնահատկությունները ռեակտիվ կատարման հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.marimo.io/cli/>:.

- Ստեղծեք կամ խմբագրեք նոթատետրեր՝ գործարկելով marimo սերվեր.:

`marimo edit`

- Սկսեք marimo սերվերը որոշակի նավահանգստում առանց բրաուզերի գործարկման.:

`marimo edit {{[-p|--port]}} {{port_number}} --headless`

- Խմբագրել կոնկրետ նոթատետր.:

`marimo edit {{path/to/notebook.py}}`

- Գործարկել marimo նոթատետրը որպես հավելված միայն կարդալու ռեժիմով.:

`marimo run {{path/to/notebook.py}}`

- Սկսեք ինտերակտիվ ձեռնարկ՝ մարիմո սովորելու համար.:

`marimo tutorial {{intro|components|dataflow|io}}`

- Դիտեք հրամանի հատուկ օգնությունը.:

`marimo {{edit|run|tutorial|config|new|...}} --help`
