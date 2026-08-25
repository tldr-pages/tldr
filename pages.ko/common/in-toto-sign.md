# in-toto-sign

> in-toto 링크 또는 레이아웃 메타데이터에 서명하거나 서명을 검증하는 도구.
> 더 많은 정보: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-sign.html>.

- 두 개의 키로 'unsigned.layout'에 서명하고 'root.layout'로 저장:

`in-toto-sign {{[-f|--file]}} {{unsigned.layout}} {{[-k|--keep]}} {{개인키1}} {{개인키2}} {{[-o|--output]}} {{root.layout}}`

- 링크 파일의 서명을 교체하고 기본 파일명으로 저장:

`in-toto-sign {{[-f|--file]}} {{package.2f89b927.link}} {{[-k|--keep]}} {{개인키}}`

- 3개의 키로 서명된 레이아웃 검증:

`in-toto-sign {{[-f|--file]}} {{root.layout}} {{[-k|--keep]}} {{공개키0}} {{공개키1}} {{공개키2}} --verify`

- 기본 GPG 키를 사용하여 레이아웃 서명:

`in-toto-sign {{[-f|--file]}} {{root.layout}} {{[-g|--gpg]}}`

- 특정 keyid('...439F3C2')의 GPG 키로 레이아웃 검증:

`in-toto-sign {{[-f|--file]}} {{root.layout}} --verify {{[-g|--gpg]}} {{...439F3C2}}`
