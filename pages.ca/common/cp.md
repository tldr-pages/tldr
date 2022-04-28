# cp

> Copia fitxers i directoris.
> Més informació: <https://www.gnu.org/software/coreutils/cp>.

- Copia un fitxer a un altre directori:

`cp {{camí/al/fitxer_origen.ext}} {{camí/al/fitxer_destí.ext}}`

- Copia un fitxer a un altre directori, mantenint el nom:

`cp {{camí/al/fitxer_origen.ext}} {{camí/al/directori}}`

- Copia recursivament els continguts d'un directori a un altre (si aquest existeix,els continguts es copien dins):

`cp -R {{camí/al/directori_origen}} {{camí/al/directori_destí}}`

- Copia un directori recursivament, de manera verbosa (mostra els fitxers a mesura que es van copiant):

`cp -vR {{camí/al/directori_origen}} {{camí/al/directori_destí}}`

- Copia els fitxers amb extensió `.txt` a una altra ubicació en mode interactiu (demana al usuari abans de sobreescriure un fitxer):

`cp -i {{*.txt}} {{camí/al/directori_destí}}`

- Copia enllaços simbòlics sense mantenir la referència al original:

`cp -L {{enllaç}} {{camí/al/directori_destí}}`
