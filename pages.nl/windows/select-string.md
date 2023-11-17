# Select-String

> Vindt tekst in string en bestanden in PowerShell.
> Dit commando kan alleen gebruikt worden via PowerShell.
> Je kan `Select-String` gebruiken zoals `grep` in UNIX of `findstr.exe` in Windows.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- Zoek naar een patroon binnen een bestand:

`Select-String -Path "{{pad\naar\bestand}}" -Pattern '{{zoek_patroon}}'`

- Zoek naar een exacte string (schakelt reguliere expressies uit):

`Select-String -SimpleMatch "{{exacte_string}}" {{pad\naar\bestand}}`

- Zoek naar een patroon in alle `.ext` bestanden in de huidige map:

`Select-String -Path "{{*.ext}}" -Pattern '{{zoek_patroon}}'`

- Toon het opgegeven aantal regels voor en na de regel die overeenkomt met de patroon:

`Select-String --Context {{2,3}} "{{zoek_patroon}}" {{pad\naar\bestand}}`

- Zoek in `stdin` voor regels die niet overeenkomen met een patroon:

`Get-Content {{pad\naar\bestand}} | Select-String --NotMatch "{{zoek_patroon}}"`
