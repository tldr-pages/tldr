# boot

> Build tooling for Clojure.

- Generate scaffolding for a new project based on a template:

`boot -d boot/new new --template {{template_name}} --name {{project_name}}`

- Start a REPL session either with the project or standalone:

`boot repl`

- Build for development (if using the boot/new template):

`boot dev`

- Build for production (if using the boot/new template):

`boot prod`

- Build a single jar:

`boot jar`
