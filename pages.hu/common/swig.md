# swig

> C/C++ kód és különböző magas szintű nyelvek, például JavaScript, Python, C# stb. közötti kötések generálása. Speciális .i vagy .swg fájlokat használ a kötések generálásához (C/C++ SWIG direktívákkal, majd egy C/C++ fájlt ad ki, amely tartalmazza a bővítőmodul létrehozásához szükséges összes csomagoló kódot. További információ: <http://www.swig.org>.

- C++ és Python közötti kötés generálása:

`swig -c++ -python -o {{path/to/output_wrapper.cpp}} {{path/to/swig_file.i}}`

- C++ és Go közötti kötés generálása:

`swig -go -cgo -intgosize 64 -c++ {{path/to/swig_file.i}}`

- C és Java közötti kötés generálása:

`swig -java {{path/to/swig_file.i}}`

- C és Ruby közötti kötés generálása és a Ruby modul előtagja {{foo::bar::}}:

`swig -ruby -prefix "{{foo::bar::}}" {{path/to/swig_file.i}}`
