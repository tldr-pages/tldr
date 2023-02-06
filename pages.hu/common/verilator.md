# verilator

> A Verilog és SystemVerilog hardverleíró nyelvi (HDL) terveket C++ vagy SystemC modellé konvertálja, amelyet a fordítás után végre lehet hajtani. További információ: <https://veripool.org/guide/latest/>.

- Egy adott C projekt összeállítása az aktuális könyvtárban:

`verilator --binary --build-jobs 0 -Wall {{path/to/source.v}}`

- C++ futtatható állomány létrehozása egy adott mappában:

`verilator --cc --exe --build --build-jobs 0 -Wall {{path/to/source.cpp}} {{path/to/output.v}}`

- Végezzen lintinget egy kódon az aktuális könyvtárban:

`verilator --lint-only -Wall`

- XML-kimenet létrehozása a tervről (fájlok, modulok, példányhierarchia, logika és adattípusok), hogy más eszközökbe táplálhassa:

`verilator --xml-output -Wall {{path/to/output.xml}}`
