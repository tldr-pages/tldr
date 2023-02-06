# case

> Elágazás egy kifejezés értéke alapján. További információ: <https://manned.org/case>.

- Egy változó és egy karakterlánc literálok közötti megfeleltetése annak eldöntéséhez, hogy melyik parancsot futtassa:

`case {{$tocount}} in {{words}}) {{wc -w README}}; ;; {{lines}}) {{wc -l README}}; ;; esac`

- Kombinálja a mintákat |-vel, használja a \*-ot tartalék mintaként:

`case {{$tocount}} in {{[wW]|words}}) {{wc -w README}}; ;; {{[lL]|lines}}) {{wc -l README}}; ;; *) {{echo "what?"}}; ;; esac`
