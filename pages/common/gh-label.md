# gh label

> Work with GitHub labels on the command-line.
> More information: <https://cli.github.com/manual/gh_label>.

- List labels for the repository in the current directory:

`gh label list`

- View labels for the repository in the current directory in the default web browser:

`gh label list --web`

- Create a label with a specific name, description and color in hexadecimal format for the repository in the current directory:

`gh label create {{name}} --description "{{description}}" --color {{color_hex}}`

- Delete a label for the repository in the current directory, prompting for confirmation:

`gh label delete {{name}}`

- Update the name and description for a specific label for the repository in the current directory:

`gh label edit {{name}} --name {{new_name}} --description "{{description}}"`

- Clone labels from a specific repository into the repository in the current directory:

`gh label clone {{owner}}/{{repository}}`

- Display help for a subcommand:

`gh label {{subcommand}} --help`
