# xinput

> Listați dispozitivele de intrare disponibile, interogați informații despre un dispozitiv și modificați setările dispozitivului de intrare.

- Listează toate dispozitivele de intrare:

`xinput list`

- Dezactivează o intrare:

`xinput disable {{id}}`

- Activează o intrare:

`xinput enable {{id}}`

- Deconectați o intrare de la comandantul său:

`xinput float {{id}}`

- Reatașați o intrare ca sclav unui maestru:

`xinput reattach {{id}} {{master_id}}`

- Lista setărilor unui dispozitiv de intrare:

`xinput list-props {{id}}`

- Modificați o setare a unui dispozitiv de intrare:

`xinput set-prop {{id}} {{setting_id}} {{value}}`
