# zerotier-idtool

> ZeroTier 아이덴티티를 생성하고 관리.
> 관련 항목: `zerotier-cli`, `zerotier-one`.
> 더 많은 정보: <https://github.com/zerotier/ZeroTierOne/blob/dev/doc/zerotier-idtool.1.md>.

- 새로운 ZeroTier 아이덴티티를 생성하고 비밀 키 부분을 `stdout`으로 출력:

`zerotier-idtool generate`

- 새로운 ZeroTier 아이덴티티를 생성하고 비밀 키와 공개 키 부분을 각각 파일에 저장:

`zerotier-idtool generate {{경로/대상/아이덴티티.secret}} {{경로/대상/아이덴티티.public}}`

- 지정한 16진수 vanity 접두사를 사용하여 새로운 ZeroTier 아이덴티티를 생성 (오래 걸릴 수 있음):

`zerotier-idtool generate {{경로/대상/아이덴티티.secret}} {{경로/대상/아이덴티티.public}} {{vanity_접두사}}`

- 비밀 아이덴티티에서 공개 키 부분 추출:

`zerotier-idtool getpublic {{경로/대상/아이덴티티.secret}}`

- 비밀 아이덴티티를 사용해 파일에 서명:

`zerotier-idtool sign {{경로/대상/아이덴티티.secret}} {{경로/대상/파일}}`

- 공개 아이덴티티와 16진수 서명을 사용해 서명된 파일을 검증:

`zerotier-idtool verify {{경로/대상/아이덴티티.public}} {{경로/대상/파일}} {{16진수_서명}}`

- 아이덴티티의 키와 작업 증명을 로컬에서 검증:

`zerotier-idtool validate {{경로/대상/아이덴티티.public}}`

- 도움말 표시:

`zerotier-idtool help`
