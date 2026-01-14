# alembic

> Outil de migration de base de données pour SQLAlchemy.
> Plus d'informations : <https://alembic.sqlalchemy.org>.

- Initialiser Alembic dans un projet :

`alembic init {{nom_du_repertoire}}`

- Créer un script de migration avec génération automatique :

`alembic revision --autogenerate -m "{{message}}"`

- Mettre à jour la base de données vers la dernière révision :

`alembic upgrade head`

- Revenir à la révision précédente :

`alembic downgrade -1`

- Afficher l'historique des migrations :

`alembic history`
