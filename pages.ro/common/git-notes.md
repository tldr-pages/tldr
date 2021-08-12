# git notes

> Adăugarea sau inspectarea notelor obiectului.
> Mai multe informaţii: <https://git-scm.com/docs/git-notes>

- Listează toate notele și obiectele la care sunt atașate:

`git notes list`

- Listează toate notele atașate la un anumit obiect (valorile implicite la HEAD):

`git notes list [{{object}}]`

- Afișează notele atașate la un anumit obiect (valorile implicite la HEAD):

`git notes show [{{object}}]`

- Adăugați o notă la un obiect specificat (deschide editorul de text implicit):

`git notes append {{object}}`

- Adăugați o notă la un obiect specificat, specificând mesajul:

`git notes append --message="{{message_text}}"`

- Editați o notă existentă (implicită la HEAD):

`git notes edit [{{object}}]`

- Copiați o notă de la un obiect la altul:

`git notes copy {{source_object}} {{target_object}}`

- Eliminați toate notele adăugate la un obiect specificat:

`git notes remove {{object}}`
