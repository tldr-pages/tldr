# cppcheck

> Un instrument de analiză statică pentru codul C/C++.
> În loc de erori de sintaxă, se concentrează pe tipurile de bug-uri pe care compilatoarele în mod normal nu le detectează.
> Mai multe informaţii: <http://cppcheck.sourceforge.net>

- Verificați recursiv directorul curent, arătând progresul pe ecran și înregistrarea mesajelor de eroare într-un fișier:

`cppcheck . 2> cppcheck.log`

- Verificați recursiv un director dat și nu imprimați mesaje de progres:

`cppcheck --quiet {{path/to/directory}}`

- Verificați un fișier dat, specificând ce teste să efectuați (în mod implicit sunt afișate numai erori):

`cppcheck --enable={{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- Lista testelor disponibile:

`cppcheck --errorlist`

- Verificați un anumit fișier, ignorând teste specifice:

`cppcheck --suppress={{test_id1}} --suppress={{test_id2}} {{path/to/file.cpp}}`

- Verificați directorul curent, oferind căi pentru a include fișiere situate în afara acestuia (de exemplu, biblioteci externe):

`cppcheck -I {{include/directory_1}} -I {{include/directory_2}} .`

- Verificați un proiect Microsoft Visual Studio (`*.vcxproj`) sau o soluție (`*.sln`):

`cppcheck --project={{path/to/project.sln}}`
