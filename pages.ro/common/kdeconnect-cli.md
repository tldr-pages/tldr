# kdeconnect-cli

> KDE Connect CLI.
> Mai multe informaţii: <https://kdeconnect.kde.org>

- Listează toate dispozitivele:

`kdeconnect-cli --list-devices`

- Lista dispozitivelor disponibile (asociate și accesibile):

`kdeconnect-cli --list-available`

- Solicitați asocierea cu un anumit dispozitiv, specificând ID-ul acestuia:

`kdeconnect-cli --pair --device {{device_id}}`

- Inel un dispozitiv, specificând numele său:

`kdeconnect-cli --ring --name {{device_name}}`

- Partajați un URL sau un fișier cu un dispozitiv asociat, specificând ID-ul său:

`kdeconnect-cli --share {{URL|path/to/file}} --device {{device_id}}`

- Trimiteți un SMS cu un atașament opțional la un anumit număr:

`kdeconnect-cli --name {{device_name}} --send-sms {{message}} --destination {{phone_number}} --attachment {{path/to/file}}`

- Deblochează un anumit dispozitiv:

`kdeconnect-cli --name {{device_name}} --unlock`

- Simulați o apăsare de tastă pe un anumit dispozitiv:

`kdeconnect-cli --name {{device_name}} --send-keys {{key}}`
