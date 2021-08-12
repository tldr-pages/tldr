# case

> Ramură bazată pe valoarea unei expresii.
> Mai multe informaţii: <https://manned.org/case>

- Potriviți o variabilă cu literalele de șir pentru a decide ce comandă să rulați:

`case {{$tocount}} in {{words}}) {{wc -w README}}; ;; {{lines}}) {{wc -l README}}; ;; esac`

- Combinați modele cu |, utilizați* ca model de rezervă:

`case {{$tocount}} in {{[wW]|words}}) {{wc -w README}}; ;; {{[lL]|lines}}) {{wc -l README}}; ;; *) {{echo "what?"}}; ;; esac`
