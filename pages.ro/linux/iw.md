# iw

> Afișați și manipulați dispozitivele fără fir.

- Scanare pentru reţele wireless disponibile:

`iw dev {{wlp}} scan`

- Alăturați-vă unei rețele fără fir deschise:

`iw dev {{wlp}} connect {{SSID}}`

- Închideți conexiunea curentă:

`iw dev {{wlp}} disconnect`

- Afișați informații despre conexiunea curentă:

`iw dev {{wlp}} link`
