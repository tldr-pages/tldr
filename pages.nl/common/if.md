# if

> Voert voorwaardelijke verwerking uit in shell-scripts.
> Zie ook: `test`, `[`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- Voer de opgegeven commando's uit als de exitstatus van het voorwaardelijke commando nul is:

`if {{voorwaarde_commando}}; then {{echo "Voorwaarde is waar"}}; fi`

- Voer de opgegeven commando's uit als de exitstatus van het voorwaardelijke commando niet nul is:

`if ! {{voorwaarde_commando}}; then {{echo "Voorwaarde is waar"}}; fi`

- Voer de eerste opgegeven commando's uit als de exitstatus van het voorwaardelijke commando nul is, anders voer de tweede opgegeven commando's uit:

`if {{voorwaarde_commando}}; then {{echo "Voorwaarde is waar"}}; else {{echo "Voorwaarde is onwaar"}}; fi`

- Controleer of een bestand ([f]) bestaat:

`if [[ -f {{pad/naar/bestand}} ]]; then {{echo "Voorwaarde is waar"}}; fi`

- Controleer of een map ([d]) bestaat:

`if [[ -d {{pad/naar/map}} ]]; then {{echo "Voorwaarde is waar"}}; fi`

- Controleer of een bestand of map b[e]staat:

`if [[ -e {{pad/naar/bestand_of_map}} ]]; then {{echo "Voorwaarde is waar"}}; fi`

- Controleer of een variabele is gedefinieerd:

`if [[ -n "${{variabele}}" ]]; then {{echo "Voorwaarde is waar"}}; fi`

- Toon alle mogelijke voorwaarden (`test` is een alias voor `[`; beide worden vaak gebruikt met `if`):

`man test`
