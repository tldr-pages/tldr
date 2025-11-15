# psexec

> 원격 컴퓨터에서 명령줄 프로세스 실행.
> 이 명령은 고급 명령이며 잠재적으로 위험할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/sysinternals/downloads/psexec>.

- 원격 쉘에서 `cmd`를 사용하여 명령 실행:

`psexec \\{{원격_호스트}} cmd`

- 원격 호스트에서 명령 실행 (사전 인증됨):

`psexec \\{{원격_호스트}} -u {{사용자명}} -p {{암호}}`

- 원격으로 명령 실행하고 결과를 파일로 출력:

`psexec \\{{원격_호스트}} cmd /c {{명령}} -an ^>{{경로\대상\파일.txt}}`

- 사용자와 상호 작용하는 프로그램 실행:

`psexec \\{{원격_호스트}} -d -i {{프로그램명}}`

- 원격 호스트의 IP 구성 표시:

`psexec \\{{원격_호스트}} ipconfig /all`
