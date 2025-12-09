# makepkg

> `pacman`과 함께 사용할 수 있는 패키지를 생성합니다.
> 기본적으로 현재 작업 디렉토리의 `PKGBUILD` 파일을 사용합니다.
> 더 많은 정보: <https://manned.org/makepkg.8>.

- 패키지 생성:

`makepkg`

- 패키지를 생성하고 의존성을 설치:

`makepkg {{[-s|--syncdeps]}}`

- 패키지를 생성하고 의존성을 설치한 다음 시스템에 설치:

`makepkg {{[-s|--syncdeps]}} {{[-i|--install]}}`

- 패키지를 생성하되 소스의 해시 검사를 건너뜀:

`makepkg --skipchecksums`

- 빌드가 성공한 후 작업 디렉토리 정리:

`makepkg {{[-c|--clean]}}`

- 소스의 해시 검증:

`makepkg --verifysource`

- 소스 정보를 `.SRCINFO`에 생성하고 저장:

`makepkg --printsrcinfo > .SRCINFO`
