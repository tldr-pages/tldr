# checkinstall

> 소프트웨어 패키지의 로컬 설치를 추적하고 시스템의 기본 패키지 관리 도구와 함께 사용할 수 있는 바이너리 패키지를 생성합니다.
> 더 많은 정보: <https://checkinstall.izto.org/docs.php>.

- 기본 설정으로 패키지를 생성하고 설치:

`sudo checkinstall --default`

- 패키지를 생성하지만 설치하지 않음:

`sudo checkinstall --install={{no}}`

- 문서 없이 패키지 생성:

`sudo checkinstall --nodoc`

- 패키지를 생성하고 이름 설정:

`sudo checkinstall --pkgname {{패키지}}`

- 패키지를 생성하고 저장할 위치 지정:

`sudo checkinstall --pakdir {{경로/대상/폴더}}`
