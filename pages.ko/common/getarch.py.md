# getArch.py

> 원격 Windows 시스템의 OS 아키텍처(x86 또는 x64) 확인.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 단일 대상 시스템의 아키텍처 확인:

`getArch.py -target {{대상}}`

- 파일에 정의된 여러 대상 시스템의 아키텍처 확인 (한 줄에 하나씩):

`getArch.py -targets {{경로/대상/대상_파일}}`

- 사용자 지정 소켓 타임아웃 설정 (기본 2초):

`getArch.py -target {{대상}} -timeout {{초}}`

- 자세한 출력을 위한 디버그 모드 활성화:

`getArch.py -target {{대상}} -debug`
