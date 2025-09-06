# rails

> A server-side MVC framework written in Ruby.
> Some subcommands such as `generate` have their own usage documentation.
> More information: <https://guides.rubyonrails.org/command_line.html>.

- Create a new rails project:

`rails new "{{project_name}}"`

- Generate a scaffold for a model named Post, predefining the attributes title and body:

`rails generate scaffold Post title:string body:text`

- Run migrations:

`rails db:migrate`

- List all routes:

`rails routes`

- Start local server for current project on port 3000:

`rails server`

- Start local server for current project on a specified port:

`rails server {{[-p|--port]}} "{{port}}"`

- Open console to interact with application from command-line:

`rails console`

- Check current version of rails:

`rails {{[-v|--version]}}`
