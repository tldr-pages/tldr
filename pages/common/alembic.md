# alembic

> Database migration tool for SQLAlchemy.
> More information: <https://manned.org/alembic>.

- Initialize Alembic in a project:

`alembic init {{path/to/directory}}`

- Create a new migration script with autogeneration:

`alembic revision --autogenerate -m "{{message}}"`

- Upgrade the database to the latest revision:

`alembic upgrade head`

- Downgrade the database by one revision:

`alembic downgrade -1`

- Show the migration history:

`alembic history`
