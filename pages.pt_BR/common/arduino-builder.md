# arduino-builder

> Uma ferramenta de linha de comando para compilar sketches do arduino.
> AVIDO DE OBSOLESCÊNCIA: Esta ferramenta está sendo descontinuada e substituida pelo `arduino`.
> Mais informações: <https://github.com/arduino/arduino-builder>.

- Compilar um sketch:

`arduino-builder -compile {{caminho/para/sketch.ino}}`

- Definir o nível de debug (1 a 10, o padrão é 5):

`arduino-builder -debug-level {{nivel}}`

- Definir um diretório de compilação customizado:

`arduino-builder -build-path {{caminho/para/diretorio}}`

- Usar um arquivo com as opções de compilação, em vez de especificar `--hardware`, `--tools`, etc. manualmente toda hora:

`arduino-builder -build-options-file {{caminho/para/build.options.json}}`

- Habilitar o modo verboso:

`arduino-builder -verbose {{true}}`
