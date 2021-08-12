# bluetoothctl

> Manipularea dispozitivelor bluetooth din carcasă.
> Mai multe informaţii: <https://www.npmjs.com/package/bluetoothctl>

- Introduceţi învelişul bluetoothctl:

`bluetoothctl`

- Lista dispozitivelor:

`bluetoothctl -- devices`

- Asocierea unui dispozitiv:

`bluetoothctl -- pair {{mac_address}}`

- Scoateți un dispozitiv:

`bluetoothctl -- remove {{mac_address}}`

- Conectați un dispozitiv asociat:

`bluetoothctl -- connect {{mac_address}}`

- Deconectați un dispozitiv asociat:

`bluetoothctl -- disconnect {{mac_address}}`
