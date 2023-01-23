# gnatmake

> Alacsony szintű építőeszköz Ada programokhoz (a GNAT toolchain része). További információ: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Building-with-gnatmake.html>.

- Végrehajtható program fordítása:

`gnatmake {{source_file1.adb source_file2.adb ...}}`

- Egyéni futtatható név beállítása:

`gnatmake -o {{executable_name}} {{source_file.adb}}`

- \[f\]orce recompilation:

`gnatmake -f {{source_file.adb}}`
