# avrdude

> Program driver untuk memrogram mikrokontroler Atmel AVR.
> Informasi lebih lanjut: <https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>.

- Baca ([r]ead) isi penyimpanann flash ROM suatu perangkat mikrokontroler AVR dengan nomor suku cadang ([p]art):

`avrdude -p {{part_id}} -c {{programmer_id}} -U flash:r:{{file.hex}}:i`

- Tulis ([w]rite) isi memori menuju penyimpanan flash perangkat mikrokontroler AVR:

`avrdude -p {{part_id}} -c {{programmer}} -U flash:w:{{file.hex}}`

- Tampilkan daftar perangkat AVR yang didukung:

`avrdude -p \?`

- Tampilkan daftar pemrogram AVR yang didukung:

`avrdude -c \?`
