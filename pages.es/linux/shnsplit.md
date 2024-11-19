# shnsplit

> Divide archivos de audio según un archivo `.cue`.
> Más información: <http://shnutils.freeshell.org/shntool/>.

- Divide un archivo `.wav` + `.cue` en múltiples archivos:

`shnsplit -f {{ruta/al/archivo.cue}} {{ruta/al/archivo.wav}}`

- Muestra formatos compatibles:

`shnsplit -a`

- Divide un archivo `.flac` en varios archivos:

`shnsplit -f {{ruta/al/archivo.cue}} -o flac {{ruta/al/archivo.flac}}`

- Divide un archivo `.wav` en archivos de la forma "número-de-pista - álbum - título":

`shnsplit -f {{ruta/al/archivo.cue}} {{ruta/al/archivo.wav}} -t "%n - %a - %t"`
