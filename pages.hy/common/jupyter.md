# jupyter

> Վեբ հավելված՝ կոդ, պատկերացումներ և նշումներ պարունակող փաստաթղթեր ստեղծելու և համօգտագործելու համար:.
> Հիմնականում օգտագործվում է տվյալների վերլուծության, գիտական ​​հաշվարկների և մեքենայական ուսուցման համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.jupyter.org/en/latest/use/jupyter-command.html>:.

- Գործարկեք Jupyter նոութբուքի սերվերը ընթացիկ գրացուցակում.:

`jupyter notebook`

- Բացեք կոնկրետ Jupyter նոթատետր.:

`jupyter notebook {{path/to/file}}.ipynb`

- Արտահանել կոնկրետ Jupyter նոթատետր այլ ձևաչափով.:

`jupyter nbconvert --to {{html|markdown|pdf|script|...}} {{path/to/file}}.ipynb`

- Գործարկեք սերվեր որոշակի նավահանգստում.:

`jupyter notebook --port {{port}}`

- Ցուցակեք ներկայումս գործող նոութբուքերի սերվերները.:

`jupyter notebook list`

- Դադարեցրեք ներկայումս գործող սերվերը.:

`jupyter notebook stop`

- Սկսեք JupyterLab-ը, եթե տեղադրված է, ընթացիկ գրացուցակում.:

`jupyter lab`
