# arduino

> Arduino Studio - Ambiente de Desenvolvimento Integrado para a plataforma Arduino.
> Mais informações: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Compilar um sketch:

`arduino --verify {{caminho/para/arquivo.ino}}`

- Compilar e enviar sketch:

`arduino --upload {{caminho/para/arquivo.ino}}`

- Compilar e enviar sketch para um Arduino Nano com uma CPU Atmega328p, conectada na porta `/dev/ttyACM0`:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{caminho/para/arquivo.ino}}`

- Definir a preferência `nome` para um determinado `valor`:

`arduino --pref {{nome}}={{valor}}`

- Compilar um sketch, colocar o resultado da compilação no diretório de compilação, e reutilizar qualquer resultado pre-existente neste diretório:

`arduino --pref build.path={{caminho/para/diretório}} --verify {{caminho/para/arquivo.ino}}`

- Salvar todas as preferências (alteradas) para `preferences.txt`:

`arduino --save-prefs`

- Instalar a última placa SAM:

`arduino --install-boards "{{arduino:sam}}"`

- Instalar bibliotecas Bridge e Servo:

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
