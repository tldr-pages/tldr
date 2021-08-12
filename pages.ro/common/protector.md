# protector

> Protejați sau deprotejați ramurile din depozitele GitHub.
> Mai multe informaţii: <https://github.com/jcgay/protector>

- Protejați ramurile unui depozit GitHub (creați reguli de protecție a ramurilor):

`protector {{branches_regex}} -repos {{organization/repository}}`

- Folosiți rularea uscată pentru a vedea ce ar fi protejat (poate fi folosit și pentru eliberare):

`protector -dry-run {{branches_regex}} -repos {{organization/repository}}`

- Sucursalele libere ale unui depozit GitHub (ștergeți regulile de protecție a ramurilor):

`protector -free {{branches_regex}} -repos {{organization/repository}}`
