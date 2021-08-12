# mongo

> MongoDB client shell interactiv.
> Mai multe informaţii: <https://docs.mongodb.com/manual/reference/program/mongo>

- Conectarea la o bază de date:

`mongo {{database}}`

- Conectați-vă la o bază de date care rulează pe o anumită gazdă pe un anumit port:

`mongo --host {{host}} --port {{port}} {{database}}`

- Conectarea la o bază de date cu un anumit nume de utilizator; utilizatorul va fi solicitat pentru parolă:

`mongo --username {{username}} {{database}} --password`

- Evaluați o expresie JavaScript în baza de date:

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{database}}`
