# մինիպրո

> Կառավարեք Xgecu չիպային ծրագրավորողները (TL866A/CS, TL866II+, T48, T56):.
> Աջակցում է տարբեր չիպերի, ներառյալ AVR-ները, PIC-ները, միկրոկոնտրոլերները և հիշողության չիպերը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/minipro>:.

- Նշեք բոլոր աջակցվող սարքերը.:

`minipro {{[-l|--list]}}`

- Որոնել կոնկրետ սարք.:

`minipro {{[-L|--search]}} {{device_name}}`

- Կարդացեք չիպի ID.:

`minipro {{[-p|--device]}} {{chip_name}} {{[-D|--read_id]}}`

- Կարդացեք չիպի բովանդակությունը ֆայլում.:

`minipro {{[-p|--device]}} {{chip_name}} {{[-r|--read]}} {{path/to/output_file.bin}}`

- Գրեք ֆայլ չիպի համար.:

`minipro {{[-p|--device]}} {{chip_name}} {{[-w|--write]}} {{path/to/input_file.bin}}`

- Ստուգեք չիպի բովանդակությունը ֆայլի նկատմամբ.:

`minipro {{[-p|--device]}} {{chip_name}} {{[-m|--verify]}} {{path/to/file.bin}}`

- Ջնջել չիպը.:

`minipro {{[-p|--device]}} {{chip_name}} {{[-E|--erase]}}`

- Ցուցադրել օգնությունը.:

`minipro {{[-h|--help]}}`
