# indent

> Wijzig het uiterlijk van een C/C++-programma door spaties in te voegen of te verwijderen.
> Meer informatie: <https://keith.github.io/xcode-man-pages/indent.1.html>.

- Formatteer C/C++-broncode volgens de Berkeley-stijl:

`indent {{pad/naar/bronbestand.c}} {{pad/naar/ingesprongen_bestand.c}} -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Formatteer C/C++-broncode volgens de stijl van Kernighan & Ritchie (K&R):

`indent {{pad/naar/bronbestand.c}} {{pad/naar/ingesprongen_bestand.c}} -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
