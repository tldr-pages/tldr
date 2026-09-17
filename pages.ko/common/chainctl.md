# chainctl

> Chainguard 공식 CLi.
> 더 많은 정보: <https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl/>.

- Chainguard 플랫폼에 인증:

`chainctl auth login`

- Chainguard 플랫폼에서 로그아웃ㅋ:

`chainctl auth logout`

- 최신 버전으로 업데이트:

`chainctl update`

- 계정에서 사용 가능한 이미지 목록을 표시:

`chainctl images list`

- 계정에서 사용 가능한 이미지 저장소 목록을 표시:

`chainctl images repos list`

- chainctl에서 이미지 태그의 변경 이력을 확인 (예: 이미지=python 태그=3):

`chainctl images history {{이미지}}:{{태그}}`

- 계정에서 사용 가능한 저장소의 패키지 버전 정보를 표시(예: package_name=go):

`chainctl packages versions list {{패키지_이름}}`

- 버전 표시:

`chainctl version`
