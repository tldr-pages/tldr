# proctl

> Manage projects licenses and languages, switch between templated licenses.
> More information: <https://github.com/HeCodes2Much/proctl>.

- List available licenses:

`proctl {{-ll|-list-licenses}}`

- List available languages:

`proctl {{-lL|-list-languages}}`

- Pick a license in a FZF menu:

`proctl {{-pl|-pick-license}}`

- Pick a language in a FZF menu:

`proctl {{-pL|-pick-language}}`

- Remove all licenses from the current project:

`proctl {{-r|-remove-license}}`

- Create a new license template:

`proctl {{-t|-new-template}}`

- Delete a license from templates:

`proctl {{-R|-delete-license}} {{@license_name1 @license_name2 ...}}`

- Show this helpful list of commands:

`proctl {{-h|-help}}`
