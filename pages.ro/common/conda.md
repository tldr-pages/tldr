# conda

> Gestionarea pachetelor, dependenței și mediului pentru orice limbaj de programare.
> Mai multe informaţii: <https://github.com/conda/conda>

- Creați un mediu nou, instalând pachete denumite în el:

`conda create --name {{environment_name}} {{python=3.9 matplotlib}}`

- Listează toate mediile:

`conda info --envs`

- Încărcați un mediu:

`conda {{activate environment_name}}`

- Descărcaţi un mediu:

`conda {{deactivate}}`

- Ștergeți un mediu (eliminați toate pachetele):

`conda remove --name {{environment_name}} --all`

- Instalați pachetele în mediul curent:

`conda install {{python=3.4 numpy}}`

- Lista pachetelor instalate în prezent în mediul curent:

`conda list`

- Ștergeți pachetele și cache-urile neutilizate:

`conda clean --all`
