# arduino

> Arduino Studio - Ambiente de Desenvolvimento Integrado para a plataforma Arduino.
> Mais informações: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Compila um sketch:

`arduino --verify {{caminho/para/arquivo.ino}}`

- Compila e envia sketch:

`arduino --upload {{caminho/para/arquivo.ino}}`

- Compila e envia sketch para um Arduino Nano com uma CPU Atmega328p, conectada na porta `/dev/ttyACM0`:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{caminho/para/arquivo.ino}}`

- Define a preferência `nome` para um determinado `valor`:

`arduino --pref {{nome}}={{valor}}`

- Compila um sketch, coloca o resultado da compilação no diretório de compilação, e reutiliza qualquer resultado pre-existente neste diretório:

`arduino --pref build.path={{caminho/para/diretório}} --verify {{caminho/para/arquivo.ino}}`

- Salva todas as preferências (alteradas) para `preferences.txt`:

`arduino --save-prefs`

- Instala a última placa SAM:

`arduino --install-boards "{{arduino:sam}}"`

- Instala bibliotecas Bridge e Servo:

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
