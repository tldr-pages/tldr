# slackcat

> Segédprogram fájlok és parancsok kimenetének átadására a Slacknek. További információ: <https://github.com/bcicen/slackcat>.

- Fájl küldése a Slackre:

`slackcat --channel {{channel_name}} {{path/to/file}}`

- Fájl küldése a Slackre egyéni fájlnévvel:

`slackcat --channel {{channel_name}} --filename={{filename}} {{path/to/file}}`

- A parancsok kimeneteinek átvezetése a Slackre szöveges részletként:

`{{command}} | slackcat --channel {{channel_name}} --filename={{snippet_name}}`

- Folyamatos parancskimenet streamelése a Slackre:

`{{command}} | slackcat --channel {{channel_name}} --stream`
