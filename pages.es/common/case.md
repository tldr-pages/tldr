# case

> Construcción de Bash para crear sentencias condicionales multi-elección.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- Compara una variable con literales de cadena para decidir qué comando ejecutar:

`case {{$COUNTRULE}} in {{palabras}}) {{wc -w LEAME}} ;; {{líneas}}) {{wc -l LEAME}} ;; esac`

- Combina patrones con |, usa * como patrón de reserva:

`case {{$COUNTRULE}} in {{[wW]|palabras}}) {{wc -w LEAME}} ;; {{[lL]|líneas}}) {{wc -l LEAME}} ;; *) {{echo "¿qué?"}} ;; esac`

- Permite la coincidencia de múltiples patrones:

`case {{$ANIMAL}} in {{gato}}) echo "Es un gato" ;;& {{gato|perro}}) echo "Es un gato o un perro" ;;& *) echo "Fallback" ;; esac`

- Continúa con los comandos del siguiente patrón sin comprobar el patrón:

`case {{$ANIMAL}} in {{gato}}) echo "Es un gato" ;& {{perro}}) echo "O es un perro o es un gato" ;& *) echo "Fallback" ;; esac`
