# heroku

> Creați și gestionați aplicații Heroku din linia de comandă.
> Mai multe informaţii: <https://www.heroku.com/>

- Conectați-vă la contul dvs. heroku:

`heroku login`

- Creați o aplicație heroku:

`heroku create`

- Afișează jurnalele pentru o aplicație:

`heroku logs --app {{app_name}}`

- Rulați un proces unic în interiorul unui dyno (mașină virtuală Heroku):

`heroku run {{process_name}} --app {{app_name}}`

- Lista dynos (Heroku mașini virtuale) pentru o aplicație:

`heroku ps --app {{app_name}}`

- Distruge permanent o aplicație:

`heroku destroy --app {{app_name}}`
