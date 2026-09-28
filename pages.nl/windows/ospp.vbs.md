# ospp.vbs

> Installeer, activeer en beheer volumelicentieversies van Microsoft Office-producten.
> Gebruik `cscript` om dit programma via de CLI uit te voeren, of `wscript` voor de GUI.
> Opmerking: dit commando kan je huidige volume aan gelicentieerde Office-productversies overschrijven, deactiveren en/of verwijderen, ga dus voorzichtig te werk.
> Zie ook: `gethelpcmd-officeactivationscenario`.
> Meer informatie: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- Installeer een productcode (Opmerking: dit vervangt de bestaande code):

`cscript ospp.vbs /inpkey:{{productcode}}`

- Verwijder een geïnstalleerde productcode met de laatste vijf cijfers van de productcode:

`cscript ospp.vbs /unpkey:{{productcode_cijfers}}`

- Stel een KMS-hostnaam in:

`cscript ospp.vbs /sethst:{{ip|hostnaam}}`

- Stel een KMS-poort in:

`cscript ospp.vbs /setprt:{{poort}}`

- Activeer geïnstalleerde Office-productcodes:

`cscript ospp.vbs /act`

- Toon licentie-informatie voor geïnstalleerde productcodes:

`cscript ospp.vbs /dstatus`
