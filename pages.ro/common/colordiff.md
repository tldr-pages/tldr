# colordiff

> Un instrument pentru colorarea ieșirii diff.
> Scriptul Perl colordiff este un wrapper pentru `diff` și produce aceeași ieșire, dar cu evidențierea destul de sintaxă. Schemele de culori pot fi personalizate.
> Mai multe informaţii: <https://github.com/kimmel/colordiff>

- Comparaţi fişierele:

`colordiff {{file1}} {{file2}}`

- Ieșire în două coloane:

`colordiff -y {{file1}} {{file2}}`

- Ignorați diferențele de caz în conținutul fișierului:

`colordiff -i {{file1}} {{file2}}`

- Raportați când două fișiere sunt aceleași:

`colordiff -s {{file1}} {{file2}}`

- Ignoră spațiile albe:

`colordiff -w {{file1}} {{file2}}`
