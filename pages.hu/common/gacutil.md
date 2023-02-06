# gacutil

> Global Assembly Cache (CAG) menedzsment segédprogram. További információ: <https://manned.org/gacutil>.

- Telepítse a megadott összeszerelést a GAC-be:

`gacutil -i {{path/to/assembly.dll}}`

- A megadott összeállítás eltávolítása a GAC-ból:

`gacutil -i {{assembly_display_name}}`

- A GAC tartalmának kinyomtatása:

`gacutil -l`
