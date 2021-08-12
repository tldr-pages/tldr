# pwsh

> PowerShell Core este un instrument/cadru de automatizare și configurare între platforme.
> Mai multe informaţii: <https://docs.microsoft.com/powershell/>

- Porniți o instanță a PowerShell:

`pwsh`

- Executați un script și apoi ieșiți:

`pwsh -File {{path/to/file.ps1}}`

- Setați politica de execuție pentru sesiunea curentă:

`pwsh -ExecutionPolicy {{AllSigned|Bypass|Default|RemoteSigned|Restricted|Undefined|Unrestricted}}`

- Executați o comandă și apoi ieșiți:

`pwsh -Command {{command}}`
