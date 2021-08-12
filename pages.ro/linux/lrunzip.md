# lrunzip

> Un program mare de decompresie a fișierelor.
> A se vedea, de asemenea, `lrztar`, `lrzuntar`.

- Decomprima un fișier:

`lrunzip {{filename.lrz}}`

- Decomprima un fișier utilizând un anumit număr de fire de procesor:

`lrunzip -p {{8}} {{filename.lrz}}`

- Decomprima un fișier și suprascrie în tăcere fișierele dacă acestea există:

`lrunzip -f {{filename.lrz}}`

- Păstrați fișierele rupte sau deteriorate în loc să le ștergeți atunci când decomprimați:

`lrunzip -K {{filename.lrz}}`

- Specificați numele fișierului de ieșire și/sau calea:

`lrunzip -o {{outfilename}} {{filename.lrz}}`
