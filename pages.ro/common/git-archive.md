# git archive

> Creați o arhivă de fișiere dintr-un arbore denumit.
> Mai multe informaţii: <https://git-scm.com/docs/git-archive>

- Creați o arhivă de gudron din conținutul HEAD curent și imprimați-l la ieșire standard:

`git archive --verbose HEAD`

- Creați o arhivă zip din HEAD curent și imprimați-o la ieșire standard:

`git archive --verbose --format=zip HEAD`

- La fel ca mai sus, dar scrieți arhiva zip la fișier:

`git archive --verbose --output={{path/to/file.zip}} HEAD`

- Creați o arhivă de gudron din conținutul celei mai recente comite pe o anumită ramură:

`git archive --output={{path/to/file.tar}} {{branch_name}}`

- Creați o arhivă de gudron din conținutul unui anumit director:

`git archive --output={{path/to/file.tar}} HEAD:{{path/to/directory}}`

- Pregăteşte o cale către fiecare fişier pentru a-l arhiva în interiorul unui anumit director:

`git archive --output={{path/to/file.tar}} --prefix={{path/to/prepend}}/ HEAD`
