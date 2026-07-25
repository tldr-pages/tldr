# Counter Strike 2

> Ospita un server headless di Counter Strike 2.
> Maggiori informazioni: <https://developer.valvesoftware.com/wiki/Counter-Strike_2/Dedicated_Servers>.

- Esegue una partita con una mappa:

`{{path/to}}/cs2 -dedicated +map {{de_dust2}}`

- Esegue una partita con un numero massimo specificato di giocatori:

`{{path/to}}/cs2 -dedicated +map {{de_dust2}} -maxplayers {{64}}`

- Esegue una partita con IP e porta del server specificati:

`{{path/to}}/cs2 -dedicated +map {{de_dust2}} -ip {{1.2.3.4}} -port {{27015}}`

- [Interattivo] Spegne il server:

`quit`
