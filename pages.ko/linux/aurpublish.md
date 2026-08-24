# aurpublish

> Arch User Repository (AUR) 패키지를 배포하는 도구.
> 더 많은 정보: <https://github.com/eli-schwartz/aurpublish/blob/master/doc/aurpublish.1.asciidoc>.

- `PKGBUILD` 무결성 검사, `.SRCINFO` 생성, 커밋 메시지 템플릿 생성 후 AUR에 패키지 배포:

`aurpublish {{패키지_이름}}`

- 현재 저장소에 githooks 추가:

`aurpublish setup`

- 도움말 표시:

`aurpublish {{[-h|--help]}}`
