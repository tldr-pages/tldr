# lambo

> A super-powered `laravel new` for Laravel and Valet.
> More information: <https://github.com/tighten/lambo>.

- Create a new Laravel application:

`lambo new {{name}}`

- Install the application in a specific path:

`lambo new --path={{path/to/directory}} {{name}}`

- Include authentication scaffolding:

`lambo new --auth {{name}}`

- Include a specific frontend:

`lambo new --{{vue|bootstrap|react}} {{name}}`

- Install npm dependencies after the project has been created:

`lambo new --node {{name}}`

- Create a Valet site after the project has been created:

`lambo new --link {{name}}`

- Create a new MySQL database with the same name as the project:

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{name}}`

- Open a specific editor after the project has been created:

`lambo new --editor="{{editor}}" {{name}}`
