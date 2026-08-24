# tlmgr platform

> TeX Live 플랫폼 관리.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

- 패키지 저장소에서 사용 가능한 모든 플랫폼 나열:

`tlmgr {{[arch|platform]}} list`

- 특정 플랫폼에 대한 실행 파일 추가:

`sudo tlmgr {{[arch|platform]}} add {{플랫폼}}`

- 특정 플랫폼에 대한 실행 파일 제거:

`sudo tlmgr {{[arch|platform]}} remove {{플랫폼}}`

- 현재 플랫폼을 자동으로 감지하여 전환:

`sudo tlmgr {{[arch|platform]}} set auto`

- 특정 플랫폼으로 전환:

`sudo tlmgr {{[arch|platform]}} set {{플랫폼}}`
