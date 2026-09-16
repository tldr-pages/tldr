# slmgr.vbs

> Installeer, activeer en beheer Windows licenties.
> Gebruik `cscript` om dit programma te gebruiken via de CLI, of `wscript` voor een GUI.
> Opmerking: dit commando kan uw huidige Windows licentie overschrijven, deactiveren en/of verwijderen, ga dus met voorzichtigheid verder.
> Meer informatie: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- Toon de huidige Windows [l]icentie [i]nformatie:

`cscript slmgr.vbs /dli`

- Toon de installatie [i]D voor het huidige apparaat. Nuttig voor offline licentie activatie:

`cscript slmgr.vbs /dti`

- Toon de verloopdatum en -tijd van de huidige licentie:

`cscript slmgr.vbs /xpr`

- [i]nstalleer een nieuwe Windows licentie [p]roduct sleutel. Vereist beheerdersrechten en zal de bestaande licentie overschrijven:

`cscript slmgr.vbs /ipk {{product_sleutel}}`

- [a]c[t]iveer de Windows product licentie [o]nline. Vereist beheerdersrechten:

`cscript slmgr.vbs /ato`

- [a]c[t]iveer de Windows [p]roduct licentie offline. Vereist beheerdersrechten een bevestigings ID verstrekt door Microsoft Product Activation Center:

`cscript slmgr.vbs /atp {{bevestigings_id}}`

- Wis de huidige licentie [p]roduct sleutel van het Windows register. Dit zal de huidige licentie niet deactiveren of verwijderen, maar voorkomt dat de sleutel in de toekomst wordt gestolen door kwaadaardige programma's:

`cscript slmgr.vbs /cpky`

- Deinstalleer de huidigie licentie (door zijn [p]roduct sleutel):

`cscript slmgr.vbs /upk`
