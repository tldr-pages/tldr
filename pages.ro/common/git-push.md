# git push

> Push se angajează într-un depozit la distanță.
> Mai multe informaţii: <https://git-scm.com/docs/git-push>

- Trimiteți modificările locale din sucursala curentă către omologul său de la distanță:

`git push`

- Trimiteți modificările locale într-o anumită sucursală la omologul său de la distanță:

`git push {{remote_name}} {{local_branch}}`

- Publicați sucursala curentă într-un depozit la distanță, setând numele ramurii la distanță:

`git push {{remote_name}} -u {{remote_branch}}`

- Trimiteți modificări la toate sucursalele locale omologilor lor într-un depozit de la distanță dat:

`git push --all {{remote_name}}`

- Ștergeți o ramură într-un depozit la distanță:

`git push {{remote_name}} --delete {{remote_branch}}`

- Eliminați ramurile la distanță care nu au un partener local:

`git push --prune {{remote_name}}`

- Publicați etichete care nu sunt încă în depozitul de la distanță:

`git push --tags`
