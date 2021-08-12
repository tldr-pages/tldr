# runuser

> Rulați comenzi ca un anumit utilizator și grup fără a solicita parola (necesită privilegii de root).

- Rulați comanda ca utilizator diferit:

`runuser {{user}} -c '{{command}}'`

- Rulați comanda ca un alt utilizator și grup:

`runuser {{user}} -g {{group}} -c '{{command}}'`

- Porniți o coajă de conectare ca utilizator specific:

`runuser {{user}} -l`

- Specificați o coajă pentru a rula în loc de shell-ul implicit (funcționează și pentru conectare):

`runuser {{user}} -s {{/bin/sh}}`

- Păstrați întregul mediu de rădăcină (numai dacă `—login` nu este specificat):

`runuser {{user}} --preserve-environment -c '{{command}}'`
