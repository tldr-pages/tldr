# cppcheck

> Strumento di analisi statica per codice C/C++.
> Piuttosto che sugli errori di sintassi, si concentra su tipi di bug che normalmente non vengono rilevati dai compilatori.
> Maggiori informazioni: <http://cppcheck.sourceforge.net>.

- Controlla la directory corrente ricorsivamente, mostrando il progresso a schermo e loggando i messaggi di errore in un file:

`cppcheck . 2> cppcheck.log`

- Controlla una determinata directory ricorsivamente, senza stampare informazioni sul progresso:

`cppcheck --quiet {{percorso/della/directory}}`

- Controlla un determinato file, specificando quali test eseguire (di default, solo gli errori sono mostrati):

`cppcheck --enable={{error|warning|style|performance|portability|information|all}} {{percorso/del/file.cpp}}`

- Elenca i test disponibili:

`cppcheck --errorlist`

- Controlla un determinato file, ignorando specifici test:

`cppcheck --suppress={{id_test1}} --suppress={{it_test2}} {{percorso/del/file.cpp}}`

- Controlla la directory corrente, fornendo percorsi da includere per file esterni (e.g. librerie esterne):

`cppcheck -I {{include/directory_1}} -I {{include/directory_2}} .`

- Controlla un progetto Microsoft Visual Studio (`*.vcxproj`) o file solution (`*.sln`):

`cppcheck --project={{percorso/del/progetto.sln}}`
