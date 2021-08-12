# jc

> Un utilitar pentru a converti ieșirea mai multor comenzi la JSON.
> Mai multe informaţii: <https://github.com/kellyjonbrazil/jc>

- Conversia comenzii de ieșire la JSON prin țeavă:

`{{ifconfig}} | jc {{--ifconfig}}`

- Conversia comenzii de ieșire la JSON prin intermediul sintaxei magice:

`jc {{ifconfig}}`

- Ieșire destul de JSON prin țeavă:

`{{ifconfig}} | jc {{--ifconfig}} -p`

- Ieșire destul de JSON prin intermediul sintaxei magice:

`jc -p {{ifconfig}}`
