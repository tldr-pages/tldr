# msbuild

> Instrumentul de compilare Microsoft pentru soluții de proiect Visual Studio.
> Mai multe informaţii: <https://docs.microsoft.com/visualstudio/msbuild>

- Construiți primul fișier de proiect în directorul curent:

`msbuild`

- Construiți un fișier de proiect specific:

`msbuild {{path/to/project_file}}`

- Setați unul sau mai multe obiective separate prin punct și virgulă pentru a construi:

`msbuild {{path/to/project_file}} /target:{{targets}}`

- Setați una sau mai multe proprietăți separate prin punct și virgulă:

`msbuild {{path/to/project_file}} /property:{{name=value}}`

- Setați versiunea de instrumente de compilare pentru a utiliza:

`msbuild {{path/to/project_file}} /toolsversion:{{version}}`

- Afișați informații detaliate la sfârșitul jurnalului despre modul în care proiectul a fost configurat:

`msbuild {{path/to/project_file}} /detailedsummary`

- Afișează informații detaliate de ajutor:

`msbuild /help`
