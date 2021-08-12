# swig

> Generați legături între codul C/C++ și diferite limbi de nivel înalt, cum ar fi JavaScript, Python, C# și multe altele.
> Utilizeaza fisiere speciale .i sau .swg pentru a genera legaturi (C/C++ cu directivele SWAG, apoi scoate un fisier C/C++ care contine tot codul de ambalaj necesar pentru a construi un modul de extensie.

- Generează o legătură între C++ și Python:

`swig -c++ -python -o {{path/to/output_wrapper.cpp}} {{path/to/swig_file.i}}`

- Generează o legare între C++ și Go:

`swig -go -cgo -intgosize 64 -c++ {{path/to/swig_file.i}}`

- Generează o legătură între C și Java:

`swig -java {{path/to/swig_file.i}}`

- Generează o legătură între C și Ruby și prefixează modulul Ruby cu {{foo። bar።}}:

`swig -ruby -prefix "{{foo::bar::}}" {{path/to/swig_file.i}}`
