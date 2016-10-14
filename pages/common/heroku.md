# heroku

> A tool for creating and managing Heroku apps from the command line.

- Login to your heroku account:

`herolu login`

- Create a heroku app:

`heroku create`

- Show Logs for an app:

`heroku logs --app {{app_name}}`

- Run a one-off process inside a heroku dyno:

`heroku run {{process_name}} --app {{app_name}}`

- List dynos for an app:

`heroku ps --app {{app_name}}`

- Permanently destrroy an app:

`heroku destroy --app {{app_name}}`
