# pio remote

> Comanda Helper pentru PlatForMio Remote Development.
> `pio remote [command] 'ia aceleași argumente ca și omologul său executant local `pio [command]”.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>

- Lista tuturor agenților activi de la distanță:

`pio remote agent list`

- Începeți un nou agent de la distanță cu un nume specific și partajați-l cu prietenii:

`pio remote agent start --name {{agent_name}} --share {{example1@example.com}} --share {{example2@example.com}}`

- Lista dispozitivelor de la agenții specificați (omiteți `—agent` pentru a specifica toți agenții):

`pio remote --agent {{agent_name1}} --agent {{agent_name2}} device list`

- Conectați-vă la portul serial al unui dispozitiv la distanță:

`pio remote --agent {{agent_name}} device monitor`

- Rulați toate țintele pe un agent specificat:

`pio remote --agent {{agent_name}} run`

- Actualizarea pachetelor de bază instalate, platforme de dezvoltare și biblioteci globale pe un anumit Agent:

`pio remote --agent {{agent_name}} update`

- Rulați toate testele în toate mediile pe un anumit agent:

`pio remote --agent {{agent_name}} test`
