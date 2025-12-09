# topydo

> Une application de liste de choses à faire qui utilise le format todo.txt.
> Plus d'informations : <https://github.com/topydo/topydo>.

- Ajouter une tâche à un projet spécifique avec un contexte donné :

`topydo add "{{todo_message}} +{{projet_nom}} @{{context_nom}}"`

- Ajouter une tâche à faire avec une date d'échéance de demain et une priorité de `A` :

`topydo add "(A) {{todo _message}} due:{{1d}}"`

- Ajouter une tâche à faire dont la date d'échéance est le vendredi :

`topydo add "{{todo_message}} due:{{fri}}"`

- Ajouter une tâche répétitive non stricte (jour + récurrence) :

`topydo add "water flowers due:{{mon}} rec:{{1w}}"`

- Ajouter une tâche répétitive stricte (prochaine échéance = date + récurrence) :

`topydo add "{{todo_message}} due:{{2020-01-01}} rec:{{+1m}}"`

- Revenir sur la dernière commande `topydo` exécutée :

`topydo revert`
