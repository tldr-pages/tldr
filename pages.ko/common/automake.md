# automake

> GNU 표준을 기반으로 소프트웨어 프로젝트의 Makefile을 자동으로 생성하는 도구.
> 더 많은 정보: <https://www.gnu.org/software/automake/manual/automake.html#automake-Invocation>.

- `Makefile.am` 수정 후 Makefile 재생성:

`automake`

- 비 GNU 프로젝트용 `Makefile.in` 생성 (foreign 모드):

`automake --foreign`

- 디버깅을 위한 상세 출력 활성화:

`automake {{[-v|--verbose]}}`

- 필요한 표준 파일 (INSTALL, COPYING, depcomp 등) 자동 추가:

`automake {{[-a|--add-missing]}}`

- 도움말 표시:

`automake --help`
