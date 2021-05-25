# lambo new

> A super-powered `laravel new` for Laravel and Valet.
> More information: <https://github.com/tighten/lambo>.

- Create a new Laravel application:

`lambo new {{app_name}}`

- Install the application in a specific path:

`lambo new --path={{path/to/directory}} {{app_name}}`

- Include authentication scaffolding:

`lambo new --auth {{app_name}}`

- Include a specific frontend:

`lambo new --{{vue|bootstrap|react}} {{app_name}}`

- Install npm dependencies after the project has been created:

`lambo new --node {{app_name}}`

- Create a Valet site after the project has been created:

`lambo new --link {{app_name}}`

- Create a new MySQL database with the same name as the project:

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{app_name}}`

- Open a specific editor after the project has been created:

`lambo new --editor="{{editor}}" {{app_name}}`
