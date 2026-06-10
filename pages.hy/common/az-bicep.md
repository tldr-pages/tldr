# az bicep

> Bicep CLI հրամանի խումբ:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/bicep>:.

- Տեղադրեք Bicep CLI:

`az bicep install`

- Ստեղծեք Bicep ֆայլ.:

`az bicep build {{[-f|--file]}} {{path/to/file.bicep}}`

- ARM ձևանմուշի ֆայլը Bicep ֆայլի ապակոմպիլյացիայի փորձ.:

`az bicep decompile {{[-f|--file]}} {{path/to/template_file.json}}`

- Թարմացրեք Bicep CLI-ն վերջին տարբերակին.:

`az bicep upgrade`

- Ցուցադրել Bicep CLI-ի տեղադրված տարբերակը.:

`az bicep version`

- Թվարկեք Bicep CLI-ի բոլոր հասանելի տարբերակները.:

`az bicep list-versions`

- Տեղահանել Bicep CLI:

`az bicep uninstall`
