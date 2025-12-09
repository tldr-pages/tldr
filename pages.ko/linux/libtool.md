# libtool

> 공유 라이브러리를 사용하는 복잡성을 일관되고 이식 가능한 인터페이스 뒤로 숨기는 제네릭 라이브러리 지원 스크립트.
> 더 많은 정보: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- 소스 파일을 `libtool` 객체로 컴파일:

`libtool --mode=compile gcc {{[-c|--compile]}} {{경로/대상/원본.c}} {{[-o|--output]}} {{경로/대상/원본.lo}}`

- 라이브러리 또는 실행 파일 생성:

`libtool --mode=link gcc {{[-o|--output]}} {{경로/대상/라이브러리.lo}} {{경로/대상/원본.lo}}`

- 라이브러리 경로를 자동으로 설정하여 다른 프로그램이 설치되지 않은 `libtool` 생성 프로그램 또는 라이브러리를 사용할 수 있도록 합니다:

`libtool --mode=execute gdb {{경로/대상/프로그램}}`

- 공유 라이브러리 설치:

`libtool --mode=install cp {{경로/대상/라이브러리.la}} {{경로/대상/설치_디렉토리}}`

- 시스템에서 `libtool` 라이브러리 설치 완료:

`libtool --mode=finish {{경로/대상/설치_디렉토리}}`

- 설치된 라이브러리 또는 실행 파일 삭제:

`libtool --mode=uninstall {{경로/대상/설치된_라이브러리.la}}`

- 설치되지 않은 라이브러리 또는 실행 파일 삭제:

`libtool --mode=clean rm {{경로/대상/원본.lo}} {{경로/대상/라이브러리.la}}`
