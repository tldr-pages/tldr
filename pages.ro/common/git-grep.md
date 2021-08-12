# git-grep

> Găsiți șiruri de caractere în interiorul fișierelor oriunde în istoricul unui depozit.
> Acceptă o mulțime de aceleași steaguri ca și regulate `grep`.
> Mai multe informaţii: <https://git-scm.com/docs/git-grep>

- Căutați un șir în fișierele urmărite:

`git grep {{search_string}}`

- Căutați un șir în fișiere care se potrivesc cu un model în fișierele urmărite:

`git grep {{search_string}} -- {{file_glob_pattern}}`

- Căutați un șir în fișierele urmărite, inclusiv submodulele:

`git grep --recurse-submodules {{search_string}}`

- Căutați un șir la un anumit punct din istorie:

`git grep {{search_string}} {{HEAD~2}}`

- Căutați un șir în toate ramurile:

`git grep {{search_string}} $(git rev-list --all)`
