# install-tl

> TeX Live 크로스 플랫폼 설치 도구.
> 더 많은 정보: <https://tug.org/texlive/>.

- 텍스트 기반 설치 프로그램 실행 (Unix 시스템 기본):

`install-tl -no-gui`

- GUI 설치 프로그램 실행 (macOS/Windows 기본, Tcl/Tk 필요):

`install-tl -gui`

- 특정 프로파일 파일에 정의된 설정으로 TeX Live 설치:

`install-tl -profile {{경로/대상/texlive.profile}}`

- 특정 프로파일 파일의 설정을 불러와 설치 시작:

`install-tl -init-from-file {{경로/대상/texlive.profile}}`

- USB 등 휴대용 장치에 설치:

`install-tl -portable`

- 도움말 표시:

`install-tl -help`
