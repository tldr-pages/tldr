# cs complete-dep

> 웹에서 직접 검색하지 않고도 라이브러리를 검색할 수 있음.
> 더 많은 정보: <https://get-coursier.io/docs/cli-complete>.

- 특정 Maven 그룹 식별자로 게시된 아티팩트를 출력:

`cs complete-dep {{그룹_아이디}}`

- 특정 Maven 그룹 식별자 및 아티팩트 식별자로 게시된 라이브러리 버전을 나열:

`cs complete-dep {{그룹_아이디}}:{{아티팩트_아이디}}`

- ivy2local에서 검색하여 특정 Maven 그룹 ID 아래에 게시된 아티팩트를 출력:

`cs complete-dep {{그룹_아이디}} --repository ivy2local`

- 특정 저장소 및 자격 증명에서 검색하는 Maven 그룹 식별자 아래에 게시된 아티팩트를 나열:

`cs complete-dep {{그룹_아이디}}:{{아티팩트_아이디}} --repository {{레포지토리_주소}} --credentials {{사용자}}:{{비밀번호}}`
