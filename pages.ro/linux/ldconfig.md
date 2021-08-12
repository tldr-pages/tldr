# ldconfig

> Configurați linkurile simbolic și memoria cache pentru dependențele bibliotecii partajate.

- Actualizați linkurile simbolice și reconstruiți memoria cache (de obicei rulați atunci când este instalată o bibliotecă nouă):

`sudo ldconfig`

- Actualizați linkurile simbolice pentru un anumit director:

`sudo ldconfig -n {{path/to/directory}}`

- Imprimați bibliotecile în memoria cache și verificați dacă o anumită bibliotecă este prezentă:

`ldconfig -p | grep {{library_name}}`
