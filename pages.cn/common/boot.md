# boot

> Build tooling for the Clojure programming language.

- Start a REPL session either with the project or standalone:

`boot repl`

- Build a single "uberjar":

`boot jar`

- Learn about a command:

`boot cljs --help`

- Generate scaffolding for a new project based on a template:

`boot --dependencies boot/new new --template {{template_name}} --name {{project_name}}`

- Build for development (if using the boot/new template):

`boot dev`

- Build for production (if using the boot/new template):

`boot prod`
