# topydo

> O aplicație listă Todo care utilizează formatul todo.txt.
> Mai multe informaţii: <https://github.com/topydo/topydo>

- Adaugă un todo la un anumit proiect cu un anumit context:

`topydo add "{{todo_message}} +{{project_name}} @{{context_name}}"`

- Adăugați un todo cu o dată scadentă de mâine cu o prioritate de „A”:

`topydo add "(A) {{todo _message}} due:{{1d}}"`

- Adăugați un todo cu o dată scadentă de vineri:

`topydo add "{{todo_message}} due:{{fri}}"`

- Adăugați un todo repetitiv non-strict (următorul datorită = acum + rec):

`topydo add "water flowers due:{{mon}} rec:{{1w}}"`

- Adăugați un todo repetitiv strict (următoarea datorată = currentdue + rec):

`topydo add "{{todo_message}} due:{{2020-01-01}} rec:{{+1m}}"`

- Reveniți la ultima comandă `topydo 'executată:

`topydo revert`
