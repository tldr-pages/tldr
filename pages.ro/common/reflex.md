# reflex

> Instrument pentru a viziona un director și a rula din nou o comandă atunci când anumite fișiere se modifică.
> Mai multe informaţii: <https://github.com/cespare/reflex>

- Reconstruiți cu `make` dacă orice fișier se schimbă:

`reflex make`

- Compilați și executați aplicația Go dacă orice fișier `.go` se modifică:

`reflex --regex='{{\.go$}}' {{go run .}}`

- Ignorați un director atunci când vizionați modificările:

`reflex --inverse-regex='{{^dir/}}' {{command}}`

- Executați comanda atunci când reflexul pornește și repornește modificările fișierelor:

`reflex --start-service=true {{command}}`

- Înlocuiți numele fișierului care s-a schimbat în:

`reflex -- echo {}`
