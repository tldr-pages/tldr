# iverilog

> Preprocesează și compilează codul Verilog HDL (IEEE-1364), în programe executabile pentru simulare.
> Mai multe informaţii: <http://iverilog.icarus.com/>

- Compilarea unui fișier sursă într-un executabil:

`iverilog {{source.v}} -o {{executable}}`

- Afișează și toate avertismentele:

`iverilog {{source.v}} -Wall -o {{executable}}`

- Compilați și executați în mod explicit folosind runtime VVP:

`iverilog -o {{executable}} -tvvp {{source.v}}`

- Compilați utilizând fișiere de bibliotecă Verilog dintr-o altă cale:

`iverilog {{source.v}} -o {{executable}} -I{{path/to/library_directory}}`

- Preprocesează codul Verilog fără compilare:

`iverilog -E {{source.v}}`
