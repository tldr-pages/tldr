# Minecraft

> Esegui un server di Minecraft senza interfaccia grafica.
> Maggiori informazioni: <https://minecraft.wiki/w/Tutorial:Setting_up_a_Java_Edition_server>.

- Avvia un server Minecraft e genera un mondo se non esiste:

`java -jar {{percorso/del/server.jar}} --nogui`

- Imposta il quantitativo minimo e massimo di memoria che il server può avere (Nota: Impostare gli stessi valori previene lag causati da heap scaling):

`java -Xms{{1024M}} -Xmx{{2048M}} -jar {{percorso/del/server.jar}} --nogui`

- Avvia un server con una GUI:

`java -jar {{percorso/del/server.jar}}`

- Spegne il server:

`stop`
