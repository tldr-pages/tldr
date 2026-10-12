# slmgr.vbs

> Installeer, activeer en beheer Windows-licenties.
> Gebruik `cscript` om dit programma als CLI uit te voeren, of `wscript` voor een GUI.
> Opmerking: dit commando kan uw huidige Windows-licentie overschrijven, deactiveren en/of verwijderen, ga dus met voorzichtigheid verder.
> Meer informatie: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- Toon ([d]) de huidige Windows-[l]icentie-[i]nformatie:

`cscript slmgr.vbs /dli`

- Toon ([d]) de ins[t]allatie-[i]D voor het huidige apparaat. Nuttig voor offline licentieactivatie:

`cscript slmgr.vbs /dti`

- Toon de verloopdatum ([xpr]) en -tijd van de huidige licentie:

`cscript slmgr.vbs /xpr`

- [i]nstalleer een nieuwe [p]roductsleutel ([k]) voor een Windows-licentie. Vereist beheerdersrechten en zal de bestaande licentie overschrijven:

`cscript slmgr.vbs /ipk {{product_sleutel}}`

- [a]c[t]iveer de Windows-productlicentie [o]nline. Vereist beheerdersrechten:

`cscript slmgr.vbs /ato`

- [a]c[t]iveer de Windows-[p]roductlicentie offline. Vereist beheerdersrechten en een bevestigings-ID verstrekt door Microsoft Product Activation Center:

`cscript slmgr.vbs /atp {{bevestigings_id}}`

- Wis ([c]) de [p]roductsleutel ([ky]) van de huidige licentie uit het Windows-register. Dit zal de huidige licentie niet deactiveren of verwijderen, maar voorkomt dat de sleutel in de toekomst wordt gestolen door kwaadaardige programma's:

`cscript slmgr.vbs /cpky`

- Deïnstalleer ([u]) de huidige licentie (door zijn [p]roductsleutel ([k])):

`cscript slmgr.vbs /upk`
