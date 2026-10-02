# topydo

> Une application de liste de choses à faire qui utilise le format todo.txt.
> Plus d'informations : <https://github.com/topydo/topydo>.

- Ajoute une tâche à un projet spécifique avec un contexte donné :

`topydo add "{{message_todo}} +{{nom_projet}} @{{nom_contexte}}"`

- Ajoute une tâche à faire avec une date d'échéance de demain et une priorité de `A` :

`topydo add "(A) {{message_todo}} due:{{1d}}"`

- Ajoute une tâche à faire dont la date d'échéance est le vendredi :

`topydo add "{{message_todo}} due:{{fri}}"`

- Ajoute une tâche répétitive non stricte (jour + récurrence) :

`topydo add "water flowers due:{{mon}} rec:{{1w}}"`

- Ajoute une tâche répétitive stricte (prochaine échéance = date + récurrence) :

`topydo add "{{message_todo}} due:{{2020-01-01}} rec:{{+1m}}"`

- Revient sur la dernière commande `topydo` exécutée :

`topydo revert`
