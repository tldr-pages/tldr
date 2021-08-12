# berks

> Manager de dependență carte de bucate Chef.
> Mai multe informaţii: <https://docs.chef.io/berkshelf.html>

- Instalați dependențele de cărți de bucate într-un repo local:

`berks install`

- Actualizați o anumită carte de bucate și dependențele sale:

`berks update {{cookbook}}`

- Încărcați o carte de bucate pe serverul Chef:

`berks upload {{cookbook}}`

- Vizualizați dependențele unei cărți de bucate:

`berks contingent {{cookbook}}`
