# choco new

> Chocolatey로 새 패키지 사양 파일 생성.
> 더 많은 정보: <https://chocolatey.org/docs/commands-new>.

- 새 패키지 스켈레톤 생성:

`choco new {{패키지}}`

- 특정 버전으로 새 패키지 생성:

`choco new {{패키지}} --version {{버전}}`

- 특정 관리자 이름으로 새 패키지 생성:

`choco new {{패키지}} --maintainer {{관리자_이름}}`

- 사용자 지정 출력 디렉터리에 새 패키지 생성:

`choco new {{패키지}} --output-directory {{경로/대상/폴더}}`

- 특정 32비트 및 64비트 설치 프로그램 URL로 새 패키지 생성:

`choco new {{패키지}} url="{{url}}" url64="{{url}}"`
