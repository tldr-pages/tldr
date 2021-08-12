# singularity

> Gestionați containerele și imaginile singularitate.

- Descărcați o imagine la distanță din Sylabs Cloud:

`singularity pull --name {{image.sif}} {{library://godlovedc/funny/lolcow:latest}}`

- Reconstruiți o imagine la distanță utilizând cel mai recent format de imagine Singularity:

`singularity build {{image.sif}} {{docker://godlovedc/lolcow}}`

- Porniți un container dintr-o imagine și obțineți o coajă în interiorul acestuia:

`singularity shell {{image.sif}}`

- Porniți un container dintr-o imagine și executați o comandă:

`singularity exec {{image.sif}} {{command}}`

- Porniți un container dintr-o imagine și executați execuția internă:

`singularity run {{image.sif}}`

- Construiți o imagine singularitate dintr-un fișier rețetă:

`sudo singularity build {{image.sif}} {{recipe}}`
