# docker inspect

> Mostra informazioni a basso livello di oggetti Docker.
> Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Mostra aiuto:

`docker inspect`

- Mostra informazioni su un container, immagine o volume usando un nome o un identificativo (ID):

`docker inspect {{nome_container|nome_immagine|ID}}`

- Mostra l'indirizzo IP di un container:

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{nome_container}}`

- Mostra il percorso dei file di log di un container:

`docker inspect --format='\{\{.LogPath\}\}' {{nome_container}}`

- Mostra il nome dell'immagine di un container:

`docker inspect --format='\{\{.Config.Image\}\}' {{nome_container}}`

- Mostra le informazioni di configurazione in formato JSON:

`docker inspect --format='\{\{json .Config\}\}' {{nome_container}}`

- Mostra il binding di tutte le porte:

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{nome_container}}`
