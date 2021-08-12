# pio access

> Setați nivelul de acces la resursele publicate (pachetele) din registry.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/access/>

- Acordarea accesului utilizatorului la o resursă:

`pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}`

- Eliminarea accesului unui utilizator la o resursă:

`pio access revoke {{username}} {{resource_urn}}`

- Afișați toate resursele la care un utilizator sau o echipă are acces și nivelul de acces:

`pio access list {{username}}`

- Restricționarea accesului la o resursă pentru anumiți utilizatori sau membri ai echipei:

`pio access private {{resource_urn}}`

- Permite accesul tuturor utilizatorilor la o resursă:

`pio access public {{resource_urn}}`
