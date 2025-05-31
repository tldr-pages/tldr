# tlmgr install

> TeX Live 패키지 설치.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#install-option...-pkg>.

- 패키지 및 의존성 설치:

`sudo tlmgr install {{패키지}}`

- 패키지 재설치:

`sudo tlmgr install --reinstall {{패키지}}`

- 패키지를 설치하는 시뮬레이션을 실행하되 실제 변경은 하지 않음:

`tlmgr install --dry-run {{패키지}}`

- 패키지를 의존성 없이 설치:

`sudo tlmgr install --no-depends {{패키지}}`

- 특정 파일에서 패키지 설치:

`sudo tlmgr install --file {{경로/대상/패키지}}`
