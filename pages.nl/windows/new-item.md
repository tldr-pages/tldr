# New-Item

> Maak een nieuw bestand, directory, symbolische link of een registerinvoer.
> Dit commando kan alleen worden uitgevoerd onder PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- Maak een nieuw leeg bestand (gelijk aan `touch`):

`New-Item {{pad\naar\bestand}}`

- Maak een nieuwe map:

`New-Item -ItemType Directory {{pad\naar\map}}`

- Schrijf een nieuw tekstbestand met opgegeven inhoud:

`New-Item {{pad\naar\bestand}} -Value {{content}}`

- Schrijf hetzelfde tekstbestand op meerdere locaties:

`New-Item {{pad\naar\bestand1 , pad\naar\bestand2 , ...}} -Value {{content}}`

- Maak een symbolische link\harde link\junction naar een bestand of map:

`New-Item -ItemType {{SymbolicLink|HardLink|Junction}} -Path {{pad\naar\link_file}} -Target {{pad\naar\bronbestand_of_map}}`

- Maak een nieuw lege registerinvoer (in REG_SZ, gebruik `New-ItemProperty` of `Set-ItemProperty` om het waardetype te verfijnen):

`New-Item {{pad\naar\registersleutel}}`

- Maak een nieuw lege registerinvoer met gespecificeerde waarde:

`New-Item {{pad\naar\registersleutel}} -Value {{value}}`
