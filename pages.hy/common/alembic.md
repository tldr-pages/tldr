# alembic

> Տվյալների բազայի միգրացիոն գործիք SQLAlchemy-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/alembic>:.

- Նախաձեռնել Alembic-ը նախագծում.:

`alembic init {{path/to/directory}}`

- Ստեղծեք նոր միգրացիոն սցենար ավտոգեներացիայի միջոցով.:

`alembic revision --autogenerate -m "{{message}}"`

- Թարմացրեք տվյալների բազան վերջին վերանայման.:

`alembic upgrade head`

- Նվազեցնել տվյալների բազան մեկ վերանայմամբ.:

`alembic downgrade -1`

- Ցույց տալ միգրացիայի պատմությունը.:

`alembic history`
