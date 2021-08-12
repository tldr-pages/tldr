# cf

> instrument de linie de comandă pentru gestionarea aplicațiilor și serviciilor în Cloud Foundry.
> Mai multe informaţii: <https://docs.cloudfoundry.org>

- Apăsați o aplicație utilizând setările implicite:

`cf push {{app_name}}`

- Vizualizaţi serviciile disponibile de la organizaţia dumneavoastră:

`cf marketplace`

- Creați o instanță de serviciu:

`cf create-service {{service}} {{plan}} {{service_name}}`

- Conectați o aplicație la un serviciu:

`cf bind-service {{app_name}} {{service_name}}`

- Rulați un script al cărui cod este inclus în aplicație, dar rulează independent:

`cf run-task {{app_name}} "{{script_command}}" --name {{task_name}}`

- Începeți o sesiune SSH interactivă cu un VM care găzduiește o aplicație:

`cf ssh {{app_name}}`

- Vizualizați un dump de jurnale recente de aplicații:

`cf logs {{app_name}} --recent`
