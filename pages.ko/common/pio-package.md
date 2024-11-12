# pio package

> 레지스트리에서 패키지를 관리.
> 패키지는 게시된 날짜로부터 72시간(3일) 이내에만 제거할 수 있습니다.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- 현재 디렉토리에서 패키지 tarball 생성:

`pio package pack --output {{경로/대상/package.tar.gz}}`

- 현재 디렉토리에서 패키지 tarball 생성 및 게시:

`pio package publish`

- 현재 디렉토리를 게시하고 공개 접근 제한:

`pio package publish --private`

- 패키지 게시:

`pio package publish {{경로/대상/package.tar.gz}}`

- 사용자 지정 릴리스 날짜(UTC)로 패키지 게시:

`pio package publish {{경로/대상/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- 게시된 패키지의 모든 버전을 레지스트리에서 제거:

`pio package unpublish {{패키지}}`

- 게시된 패키지의 특정 버전을 레지스트리에서 제거:

`pio package unpublish {{패키지}}@{{버전}}`

- 제거를 취소하고 패키지의 모든 버전 또는 특정 버전을 레지스트리에 복원:

`pio package unpublish --undo {{패키지}}@{{버전}}`
