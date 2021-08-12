# git stash

> Stash modificări locale Git într-o zonă temporară.
> Mai multe informaţii: <https://git-scm.com/docs/git-stash>

- Ascundere modificările curente, cu excepția fișierelor noi (neurmărite):

`git stash [push -m {{optional_stash_message}}]`

- Ascunderea modificărilor curente, inclusiv fișiere noi (neurmărite):

`git stash -u`

- Selectați interactiv părți ale fișierelor modificate pentru ascundere:

`git stash -p`

- Listează toate stash-urile (afișează numele stash, filiala asociată și mesajul):

`git stash list`

- Aplicați o stash (implicit este cea mai recentă, numită stash@ {0}):

`git stash apply {{optional_stash_name_or_commit}}`

- Aplicați o stash (implicit este stash@ {0}) și eliminați-o din lista stash dacă aplicarea nu provoacă conflicte:

`git stash pop {{optional_stash_name}}`

- Arunca o stash (implicit este stash@ {0}):

`git stash drop {{optional_stash_name}}`

- Arunca toate stashes:

`git stash clear`
