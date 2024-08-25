# proctl

> Manage, Switch Between templated Licenses, and set Languages
> More information: <https://github.com/HeCodes2Much/proctl>.

- Initialize a git repo for a project:

`proctl -initialize/-i @project_name`

- List available licenses:

`proctl -list-licenses/-ll`

- List available languages

`proctl -list-languages/-lL`

- Show current active project license

`proctl -current-license/-c`

- Pick a license in a FZF menu

`proctl -pick-license/-pl`

- Pick a language in a FZF menu

`proctl -pick-language/-pL`

- Preview a license template
  
`proctl -preview-license/-P @license_name`

- Remove all licenses from the current project

`proctl -remove-license/-r`

- Search for license

`proctl -search-license/-sl '<query | patten>'`

- Search for language

`proctl -search-language/-sL '<query | patten>'`

- Print help for templating

`proctl -template-help/-T`

- Create a new license template

`proctl -new-template/-t`

- Delete a license from templates

`proctl -delete-license/-R @license_name ...`

- Create a default config overwriting current one

`proctl -new-config/-C`

- Check if current licene(s) are conflicting

`proctl -check-conflict/-k`

- Show this helpful list of commands

`proctl -help/-h`

