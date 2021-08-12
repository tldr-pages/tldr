# git clone

> Clonează un depozit existent.
> Mai multe informaţii: <https://git-scm.com/docs/git-clone>

- Clonează un depozit existent:

`git clone {{remote_repository_location}}`

- Clonează un depozit existent într-un anumit director:

`git clone {{remote_repository_location}} {{path/to/directory}}`

- Clonează un depozit existent și submodulele sale:

`git clone --recursive {{remote_repository_location}}`

- Clonează un depozit local:

`git clone -l {{path/to/local/repository}}`

- Clona în liniște:

`git clone -q {{remote_repository_location}}`

- Clonează un depozit existent doar preluarea celor mai recente 10 angajări pe ramura implicită (util pentru a economisi timp):

`git clone --depth {{10}} {{remote_repository_location}}`

- Clonează un depozit existent doar aducând o anumită ramură:

`git clone --branch {{name}} --single-branch {{remote_repository_location}}`

- Clonează un depozit existent utilizând o comandă SSH specifică:

`git clone --config core.sshCommand="{{ssh -i path/to/private_ssh_key}}" {{remote_repository_location}}`
