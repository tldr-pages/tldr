# envsubst

> Înlocuiește variabilele de mediu cu valoarea lor în șiruri de format shell.
> Variabilele care trebuie înlocuite trebuie să fie în format `$ {var} `sau `$var`.
> Mai multe informaţii: <https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>

- Înlocuiți variabilele de mediu în stdin și ieșire la stdout:

`echo '{{$HOME}}' | envsubst`

- Înlocuiți variabilele de mediu într-un fișier de intrare și ieșiți la stdout:

`envsubst < {{path/to/input_file}}`

- Înlocuiți variabilele de mediu într-un fișier de intrare și ieșiți într-un fișier:

`envsubst  <{{path/to/input_file}}> {{path/to/output_file}}`

- Înlocuiți variabilele de mediu într-un fișier de intrare dintr-o listă separată de spațiu:

`envsubst '{{$USER $SHELL $HOME}}' < {{path/to/input_file}}`
