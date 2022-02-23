# cp

> Còpia arxius i directoris.
> Més informació: <https://www.gnu.org/software/coreutils/cp>.

- Copia un arxiu a un altre directori:

`cp {{ruta/al/arxiu_origen.ext}} {{ruta/al/archiu_destí.ext}}`

- Copia un archivo en otro directorio, conservando el nombre del archivo:

`cp {{ruta/al/arxiu_origen.ext}} {{ruta/al/directori_destinatari}}`

- Còpia de forma recursiva el contingut d'un directori a una altra ubicació (si el destí existeix, el directori és copiat en aquesta ubicació):

`cp -r {{ruta/al/directori_origen}} {{ruta/al/directori_destinatari}}`

- Còpia un directori de forma recursiva en mode verbose (mostra els arxius a mesura que es copien):

`cp -vr {{ruta/al/directori_origen}} {{ruta/al/directori_destinatari}}`

- Còpia arxius de text en una altra ubicació en mode interactiu (pregunta al usuari abans de sobreescriure):

`cp -i {{*.txt}} {{ruta/al/directori_destinatari}}`

- Segueix els enllaços simbòlics abans de copiar:

`cp -L {{link}} {{ruta/al/directori_destinatari}}`

- Utilitza la ruta completa dels arxius d'origen, creant els directoris intermitjos faltants al copiar:

`cp --parents {{ruta_de_origen/al/archiu}} {{ruta/al/archiu_destí}}`
