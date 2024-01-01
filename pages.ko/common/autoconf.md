# autoconf

> 소프트웨어 소스 코드 패키지를 자동으로 구성하는 구성 스크립트 생성.
> 더 많은 정보: <https://www.gnu.org/software/autoconf>.

- `configure.ac` (있는 경우) 또는 `configure.in` 에서 구성 스크립트를 생성하고 이 스크립트를 `configure`에 저장:

`autoconf`

- 지정된 템플릿에서 구성 스크립트를 생성; `stdout`으로 출력:

`autoconf {{템플릿-파일}}`

- 지정된 템플릿에서 구성 스크립트를 생성하고(입력 파일이 변경되지 않은 경우에도) 출력을 파일에 작성:

`autoconf --force --output={{출력파일}} {{템플릿-파일}}`
