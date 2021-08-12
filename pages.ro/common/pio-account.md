# pio account

> Gestionați contul PlatForMio în linia de comandă.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/account/>

- Înregistrați un nou cont PlatForMio:

`pio account register --username {{username}} --email {{email}} --password {{password}} --firstname {{firstname}} --lastname {{lastname}}`

- Ștergeți definitiv contul PlatForMio și datele aferente:

`pio account destroy`

- Autentifică-te în contul tău PlatForMio:

`pio account login --username {{username}} --password {{password}}`

- Deconectați-vă din contul dvs. PlatForMio:

`pio account logout`

- Actualizați-vă profilul PlatForMio:

`pio account update --username {{username}} --email {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}`

- Afișați informații detaliate despre contul dvs. PlatForMio:

`pio account show`

- Resetați parola folosind numele de utilizator sau adresa de e-mail:

`pio account forgot --username {{username_or_email}}`
