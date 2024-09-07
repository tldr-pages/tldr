# proctl

> Manage, Switch Between templated Licenses, and set Languages.
> More information: <https://github.com/HeCodes2Much/proctl>.

- List available licenses:

`proctl -list-licenses/-ll`

- List available languages:
- 
`proctl -list-languages/-lL`

- Pick a license in a FZF menu:

`proctl -pick-license/-pl`

- Pick a language in a FZF menu:

`proctl -pick-language/-pL`

- Remove all licenses from the current project:

`proctl -remove-license/-r`

- Create a new license template:

`proctl -new-template/-t`

- Delete a license from templates:

`proctl -delete-license/-R @license_name ...`

- Show this helpful list of commands:

`proctl -help/-h`
