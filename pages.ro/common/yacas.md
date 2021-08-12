# yacas

> Cu toate acestea, un alt sistem de algebră calculator.
> Mai multe informaţii: <http://www.yacas.org>

- Începeți o sesiune interactivă `yacas`:

`yacas`

- În timpul unei sesiuni `yacas`, executați o declarație:

`{{Integrate(x)Cos(x)}};`

- În timpul sesiunii `yacas`, afisati un exemplu:

`{{Example()}};`

- Renunţă la o sesiune `yacas`:

`{{quit}}`

- Execută unul sau mai multe scripturi `yacas` (fără terminale sau solicitări), apoi ieșiți:

`yacas -p -c {{path/to/script1}} {{path/to/script2}}`

- Executați și imprimați rezultatul unei declarații, apoi ieșiți:

`echo "{{Echo( Deriv(x)Cos(1/x) );}}" | yacas -p -c /dev/stdin`
