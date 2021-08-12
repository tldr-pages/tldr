# gist

> Încărcați codul la https://gist.github.com.
> Mai multe informaţii: <https://github.com/defunkt/gist>

- Conectați-vă în gist pe acest computer:

`gist --login`

- Creați o idee din orice număr de fișiere text:

`gist {{file.txt}} {{file2.txt}}`

- Creați un gist privat cu o descriere:

`gist --private --description "{{A meaningful description}}" {{file.txt}} `

- Citiți conținutul din stdin și creați un gist din acesta:

`{{echo "hello world"}} | gist`

- Listați gisturile publice și private:

`gist --list`

- Listează toate gist-urile publice pentru orice utilizator:

`gist --list {{username}}`

- Actualizați un gist folosind id-ul din URL:

`gist --update {{GIST_ID}} {{file.txt}}`
