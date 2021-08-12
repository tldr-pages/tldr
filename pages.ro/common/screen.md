# screen

> Țineți deschisă o sesiune pe un server la distanță. Gestionați mai multe ferestre cu o singură conexiune SSH.

- Începeți o nouă sesiune de ecran:

`screen`

- Începeți o nouă sesiune de ecran denumită:

`screen -S {{session_name}}`

- Porniți un nou daemon și conectați ieșirea la `screenlog.x`:

`screen -dmLS {{session_name}} {{command}}`

- Afișează sesiuni pe ecran deschis:

`screen -ls`

- Reatașați la un ecran deschis:

`screen -r {{session_name}}`

- Detașați din interiorul unui ecran:

`Ctrl + A, D`

- Omoară sesiunea curentă de ecran:

`Ctrl + A, K`

- Omoară un ecran detașat:

`screen -X -S {{session_name}} quit`
