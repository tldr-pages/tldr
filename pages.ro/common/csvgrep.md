# csvgrep

> Filtrați rândurile CSV cu potrivire șir și model.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>

- Găsiți rânduri care au un anumit șir în coloana 1:

`csvgrep -c {{1}} -m {{string_to_match}} {{data.csv}}`

- Găsiți rânduri în care coloanele 3 sau 4 se potrivesc cu o anumită expresie regulată:

`csvgrep -c {{3,4}} -r {{regular_expression}} {{data.csv}}`

- Găsiți rânduri în care coloana „nume” NU include șirul „John Doe”:

`csvgrep -i -c {{name}} -m "{{John Doe}}" {{data.csv}}`
