# avrdude

> Վարորդի ծրագիր Atmel AVR միկրոկոնտրոլերների ծրագրավորման համար:.
> Լրացուցիչ տեղեկություններ. <https://www.nongnu.org/avrdude/user-manual/avrdude_3.html#Option-Descriptions>:.

- [r]կարդացեք AVR միկրոկառավարիչի ֆլեշ ROM-ը հատուկ [p]art ID-ով.:

`avrdude -p {{part_id}} -c {{programmer_id}} -U flash:r:{{file.hex}}:i`

- [w]գրել ֆլեշ ROM AVR միկրովերահսկիչին.:

`avrdude -p {{part_id}} -c {{programmer}} -U flash:w:{{file.hex}}`

- Ցուցակեք մատչելի AVR սարքերը.:

`avrdude -p \?`

- Ցուցակեք մատչելի AVR ծրագրավորողները.:

`avrdude -c \?`
