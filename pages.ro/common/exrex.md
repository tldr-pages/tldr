# exrex

> Generați șiruri de potrivire aleatorie pentru o expresie regulată.
> De asemenea, poate simplifica expresii regulate.
> Mai multe informaţii: <https://github.com/asciimoo/exrex>

- Generați toate șirurile posibile care se potrivesc cu o expresie regulată:

`exrex '{{regular_expression}}'`

- Generează un șir aleatoriu care se potrivește cu o expresie regulată:

`exrex --random '{{regular_expression}}'`

- Generați cel mult 100 de șiruri care se potrivesc cu o expresie regulată:

`exrex --max-number {{100}} '{{regular_expression}}'`

- Generați toate șirurile posibile care se potrivesc cu o expresie regulată, unite împreună printr-un șir de delimitator personalizat:

`exrex --delimiter "{{, }}" '{{regular_expression}}'`

- Imprimați numărul tuturor șirurilor de caractere posibile care se potrivesc cu o expresie regulată:

`exrex --count '{{regular_expression}}'`

- Simplificați o expresie regulată:

`exrex --simplify '{{ab|ac}}'`

- Ochi de imprimare:

`exrex '{{[oO0](_)[oO0]}}'`

- Tipăreşte o barcă:

`exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'`
