#չխաչազարդել

> C, C++, C#, D, Java և Pawn կոդերի ձևաչափիչ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/uncrustify>:.

- Ձևաչափեք մեկ ֆայլ.:

`uncrustify -f {{path/to/file.cpp}} -o {{path/to/output.cpp}}`

- Կարդացեք ֆայլերի անունները `stdin`-ից և պահուստավորեք՝ նախքան ելքը սկզբնական ֆայլուղիներին վերադառնալը.:

`find . -name "*.cpp" | uncrustify -F - --replace`

- Մի կրկնօրինակեք (օգտակար է, եթե ֆայլերը գտնվում են տարբերակի հսկողության տակ).:

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- Օգտագործեք հատուկ կազմաձևման ֆայլ և արդյունքը գրեք `stdout`-ում:

`uncrustify -c {{path/to/uncrustify.cfg}} -f {{path/to/file.cpp}}`

- Հստակորեն սահմանեք կազմաձևման փոփոխականի արժեքը.:

`uncrustify --set {{option}}={{value}}`

- Ստեղծեք նոր կազմաձևման ֆայլ.:

`uncrustify --update-config -o {{path/to/new.cfg}}`
