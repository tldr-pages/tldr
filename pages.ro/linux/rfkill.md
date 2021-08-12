# rfkill

> Activați și dezactivați dispozitivele fără fir.

- Lista dispozitivelor:

`rfkill`

- Filtrare după coloane:

`rfkill -o {{ID,TYPE,DEVICE}}`

- Blocați dispozitivele după tip (de exemplu bluetooth, wlan):

`rfkill block {{bluetooth}}`

- Deblocați dispozitivele după tip (de exemplu bluetooth, wlan):

`rfkill unblock {{wlan}}`

- Ieșire în format JSON:

`rfkill -J`
