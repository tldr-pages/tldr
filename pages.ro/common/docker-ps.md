# docker ps

> Lista containerelor Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/ps/>

- Lista containerelor de andocare rulează în prezent:

`docker ps`

- Listează toate containerele de andocare (rulează și oprit):

`docker ps --all`

- Arată cel mai recent container creat (include toate stările):

`docker ps --latest`

- Containerele de filtrare care conțin un substring în numele lor:

`docker ps --filter="name={{name}}"`

- Filtrarea containerelor care partajează o anumită imagine ca strămoș:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Filtrați containerele după codul de stare de ieșire:

`docker ps --all --filter="exited={{code}}"`

- Filtrați containerele după stare (create, rulate, înlăturate, întrerupte, ieșite și moarte):

`docker ps --filter="status={{status}}"`

- Containere de filtrare care montează un anumit volum sau au un volum montat într-o anumită cale:

`docker ps --filter="volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
