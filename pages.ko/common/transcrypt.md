# transcrypt

> Git 저장소 내에서 파일을 투명하게 암호화.
> 더 많은 정보: <https://github.com/elasticdog/transcrypt#command-line-options>.

- 구성되지 않은 저장소 초기화:

`transcrypt`

- 현재 암호화된 파일 나열:

`git ls-crypt`

- 구성된 저장소의 자격 증명 표시:

`transcrypt --display`

- 구성된 저장소의 새 클론을 초기화하고 복호화:

`transcrypt --cipher={{암호화_알고리즘}}`

- 암호화 알고리즘이나 암호를 변경하기 위한 키 재설정:

`transcrypt --rekey`
