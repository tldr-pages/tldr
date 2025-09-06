# msfconsole

> Metasploit 프레임워크의 콘솔.
> 더 많은 정보: <https://docs.rapid7.com/metasploit/msf-overview>.

- 콘솔 시작:

`msfconsole`

- 배너 없이 조용히 콘솔 시작:

`msfconsole --quiet`

- 데이터베이스 지원을 비활성화하고 시작:

`msfconsole --no-database`

- 콘솔 명령 실행 (참고: 여러 명령을 전달하려면 `;` 사용):

`msfconsole --execute-command "{{use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run}}"`

- 버전 표시:

`msfconsole --version`
