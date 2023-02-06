# iverilog

> Előfeldolgozza és lefordítja a Verilog HDL (IEEE-1364) kódot futtatható programokká a szimulációhoz. További információ: <https://github.com/steveicarus/iverilog>.

- Forrásfájlok fordítása végrehajtható programmá:

`iverilog {{path/to/source.v}} -o {{path/to/executable}}`

- Egy forrásfájlt fordít le végrehajtható programmá, miközben megjeleníti az összes figyelmeztetést:

`iverilog {{path/to/source.v}} -Wall -o {{path/to/executable}}`

- Kifejezetten a VVP futtatóprogrammal történő fordítás és futtatás:

`iverilog -o {{path/to/executable}} -tvvp {{path/to/source.v}}`

- Kompilálás Verilog könyvtárfájlok felhasználásával egy másik elérési útvonalról:

`iverilog {{path/to/source.v}} -o {{path/to/executable}} -I{{path/to/library_directory}}`

- Verilog kód előfeldolgozása fordítás nélkül:

`iverilog -E {{path/to/source.v}}`
