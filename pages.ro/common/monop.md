# monop

> Găseşte şi afişează semnături de tipuri şi metode în cadrul ansamblurilor NET.

- Arată structura unui tip încorporat din NET Framework:

`monop {{System.String}}`

- Listați tipurile într-un ansamblu:

`monop -r:{{path/to/assembly.exe}}`

- Afișați structura unui tip într-un ansamblu specific:

`monop -r:{{path/to/assembly.dll}} {{Namespace.Path.To.Type}}`

- Afișează numai membrii definiți în tipul specificat:

`monop -r:{{path/to/assembly.dll}} --only-declared {{Namespace.Path.To.Type}}`

- Arată membrii privaţi:

`monop -r:{{path/to/assembly.dll}} --private {{Namespace.Path.To.Type}}`

- Ascunde membrii învechiți:

`monop -r:{{path/to/assembly.dll}} --filter-obsolete {{Namespace.Path.To.Type}}`

- Listați celelalte ansambluri la care se referă un ansamblu specificat:

`monop -r:{{path/to/assembly.dll}} --refs`
