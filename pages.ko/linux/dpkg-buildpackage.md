# dpkg-buildpackage

> 소스 코드로부터 Debian 바이너리 및/또는 소스 패키지를 빌드.
> 일반적으로 `debian/` 디렉터리를 포함한 소스 트리에서 실행됨.
> 빌드 의존성 처리, `.buildinfo` 및 `.changes` 파일 생성, 필요한 경우 결과물 서명도 수행.
> 더 많은 정보: <https://manned.org/dpkg-buildpackage>.

- 소스 및 바이너리 패키지 생성:

`dpkg-buildpackage`

- 바이너리 패키지만 생성 (소스 패키지는 생성하지 않음):

`dpkg-buildpackage {{[-b|--build=binary]}}`

- 소스 패키지만 생성 (바이너리 컴파일 없이):

`dpkg-buildpackage {{[-S|--build=source]}}`

- `.dsc` 및 `.changes` 파일에 서명하지 않음:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- 컴파일 전에 `clean` 대상 실행 생략:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- 빌드 중 루트 권한 획득을 위해 `fakeroot` 사용:

`dpkg-buildpackage {{[-r|--root-command=]}}fakeroot`

- 지정한 `debian/rules` 대상 실행:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`
