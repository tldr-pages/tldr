# parallel

> Rulați comenzi pe mai multe nuclee CPU.
> Mai multe informaţii: <https://www.gnu.org/software/parallel>

- Gzip mai multe fișiere simultan, folosind toate nucleele:

`parallel gzip ::: {{file1}} {{file2}} {{file3}}`

- Citiți argumentele de la stdin, executați 4 locuri de muncă simultan:

`ls *.txt | parallel -j4 gzip`

- Conversia imaginilor JPG în PNG folosind șiruri de înlocuire:

`parallel convert {} {.}.png ::: *.jpg`

- Xargs paralel, ghiftui cât mai multe args posibil pe o singură comandă:

`{{args}} | parallel -X {{command}}`

- Break stdin în ~ 1M blocuri, hrana pentru animale fiecare bloc la stdin de comandă nouă:

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- Rulați pe mai multe mașini prin SSH:

`parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`
