# envsubst

> A környezeti változókat helyettesíti azok értékével shell formátumú karakterláncokban. A helyettesítendő változóknak a `${var}` vagy a `$var` formátumban kell lenniük. További információ: <https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>.

- A környezeti változók helyettesítése a `stdin` és a kimenet a `stdout`:

`echo '{{$HOME}}' | envsubst`

- Környezeti változók helyettesítése egy bemeneti fájlban és kimenet a `stdout`:

`envsubst < {{path/to/input_file}}`

- Környezeti változók cseréje egy bemeneti fájlban és kimenet egy fájlba:

`envsubst < {{path/to/input_file}} > {{path/to/output_file}}`

- Környezeti változók helyettesítése egy bemeneti fájlban egy szóközzel elválasztott listából:

`envsubst '{{$USER $SHELL $HOME}}' < {{path/to/input_file}}`
