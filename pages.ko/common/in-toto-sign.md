# in-toto-sign

> toto 링크 또는 레이아웃 메타데이터에 로그인하거나 서명을 확인.
> 더 많은 정보: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-sign.html>.

- 두 개의 키로 'unsigned.layout'에 서명하고 'root.layout'에 작성:

`in-toto-sign -f {{unsigned.layout}} -k {{개인_키1}} {{개인_키2}} -o {{root.layout}}`

- 링크 파일의 서명을 바꾸고 기본 파일 이름에 작성:

`in-toto-sign -f {{package.2f89b927.link}} -k {{개인_키}}`

- 3개의 키로 서명된 레이아웃을 확인:

`in-toto-sign -f {{root.layout}} -k {{pub_key0}} {{pub_key1}} {{pub_key2}} --verify`

- 기본 GPG 키링에서 기본 GPG 키를 사용하여 레이아웃에 서명:

`in-toto-sign -f {{root.layout}} --gpg`

- 키 아이디 '...439F3C2'로 식별되는 GPG 키를 사용하여 레이아웃을 확인:

`in-toto-sign -f {{root.layout}} --verify --gpg {{...439F3C2}}`
