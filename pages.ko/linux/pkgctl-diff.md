# pkgctl diff

> 패키지 파일을 다양한 모드로 비교.
> 같이 보기: `pkgctl`.
> 더 많은 정보: <https://manned.org/pkgctl-diff>.

- tar 콘텐츠 [l]리스트 비교 모드(기본값)로 패키지 파일 비교:

`pkgctl diff {{[-l|--list]}} {{경로/대상/파일|패키지명}}`

- [d]iffoscope 비교 모드로 패키지 파일 비교:

`pkgctl diff {{[-d|--diffoscope]}} {{경로/대상/파일|패키지명}}`

- `.PKGINFO` 비교 모드로 패키지 파일 비교:

`pkgctl diff {{[-p|--pkginfo]}} {{경로/대상/파일|패키지명}}`

- `.BUILDINFO` 비교 모드로 패키지 파일 비교:

`pkgctl diff {{[-b|--buildinfo]}} {{경로/대상/파일|패키지명}}`
