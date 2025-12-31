# libtoolize

> `autotools` 도구로, `libtool`을 사용하기 위해 패키지를 준비합니다.
> 여러 작업을 수행하며, 필요한 파일 및 디렉토리를 생성하여 `libtool`을 프로젝트에 원활하게 통합합니다.
> 더 많은 정보: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- `libtool`을 필요한 파일을 복사하여(심볼릭 링크는 피함) 프로젝트를 초기화하고 필요한 경우 기존 파일을 덮어씀:

`libtoolize {{[-cf|--copy --force]}}`
