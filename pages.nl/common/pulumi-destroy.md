# pulumi destroy

> Vernietig alle bestaande bronnen in een stack.
> Meer informatie: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_destroy/>.

- Vernietig alle bronnen in de huidige stack:

`pulumi destroy`

- Vernietig alle bronnen in een specifieke stack:

`pulumi destroy {{[-s|--stack]}} {{stack}}`

- Keur automatisch bronnen goed en vernietig deze na voorvertoning:

`pulumi destroy {{[-y|--yes]}}`

- Sluit beschermde bronnen uit van vernietigd worden:

`pulumi destroy --exclude-protected`

- Verwijder de stack en het bijbehorende configuratiebestand nadat alle bronnen in de stack zijn verwijderd:

`pulumi destroy --remove`

- Ga door met de bronnen vernietigen, zelfs als er een fout optreedt:

`pulumi destroy --continue-on-error`
