# jello

> Un procesor JSON de linie de comandă utilizând sintaxa Python.
> Mai multe informaţii: <https://github.com/kellyjonbrazil/jello>

- Pretty-print JSON sau JSON linii de date de la stdin la stdout:

`cat {{file.json}} | jello`

- Ieșiți o schemă de date JSON sau JSON Lines de la stdin la stdout (util pentru grep):

`cat {{file.json}} | jello -s`

- Ieșiți toate elementele din matrice (sau toate valorile din obiecte) în datele JSON sau JSON de la stdin la stdout:

`cat {{file.json}} | jello -l`

- Ieșiți primul element din datele JSON sau JSON de la stdin la stdout:

`cat {{file.json}} | jello _[0]`

- Ieșiți valoarea unei chei date a fiecărui element în datele JSON sau JSON de la stdin la stdout:

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- Ieșiți valoarea mai multor chei ca obiect JSON nou (presupunând că intrarea JSON are cheile `key_name` și `other_key_name`):

`cat {{file.json}} | jello '{"{{my_new_key}}": _.{{key_name}}, "{{my_other_key}}": _.{{other_key_name}}}'`

- Ieșiți valoarea unei chei date la un șir (și dezactivați ieșirea JSON):

`cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'`
