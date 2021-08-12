# docker inspect

> Returnați informații de nivel scăzut despre obiectele Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/inspect/>

- Arată ajutor:

`docker inspect`

- Afișați informații despre un container, imagine sau volum utilizând un nume sau un ID:

`docker inspect {{container|image|ID}}`

- Afișează adresa IP a containerului:

`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {{container}}`

- Afișează calea către fișierul jurnal al containerului:

`docker inspect --format='{{.LogPath}}' {{container}}`

- Afișează numele imaginii containerului:

`docker inspect --format='{{.Config.Image}}' {{container}}`

- Afișează informațiile de configurare ca JSON:

`docker inspect --format='{{json .Config}}' {{container}}`

- Afișează toate legăturile de port:

`docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{container}}`
