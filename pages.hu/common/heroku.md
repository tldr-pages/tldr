# heroku

> Heroku alkalmazások létrehozása és kezelése a parancssorból. További információ: <https://www.heroku.com/>.

- Jelentkezzen be a Heroku-fiókjába:

`heroku login`

- Hozzon létre egy Heroku alkalmazást:

`heroku create`

- Egy alkalmazás naplóinak megjelenítése:

`heroku logs --app {{app_name}}`

- Egyszeri folyamat futtatása egy dyno (Heroku virtuális gép) belsejében:

`heroku run {{process_name}} --app {{app_name}}`

- Dinók (Heroku virtuális gépek) listázása egy alkalmazáshoz:

`heroku ps --app {{app_name}}`

- Egy alkalmazás végleges megsemmisítése:

`heroku destroy --app {{app_name}}`
