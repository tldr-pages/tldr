# numfmt

> Convierte números a y desde cadenas legibles por humanos.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- Convierte 1.5K (Unidades SI) a 1500:

`numfmt --from si 1.5K`

- Convierte el 5º campo (1-indexado) a Unidades IEC sin convertir la cabecera:

`ls -l | numfmt --header=1 --field 5 --to iec`

- Convierte a unidades IEC, los rellena con 5 caracteres, alineado a la izquierda:

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
