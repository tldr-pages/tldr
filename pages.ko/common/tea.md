# tea

> Gitea 서버와 상호 작용.
> 더 많은 정보: <https://gitea.com/gitea/tea>.

- Gitea 서버에 로그인:

`tea login add --name "{{이름}}" --url "{{URL}}" --token "{{토큰}}"`

- 모든 저장소 표시:

`tea repos ls`

- 이슈 목록 표시:

`tea issues ls`

- 특정 저장소의 이슈 목록 표시:

`tea issues ls --repo "{{저장소}}"`

- 새 이슈 생성:

`tea issues create --title "{{제목}}" --body "{{본문}}"`

- 열려 있는 풀 리퀘스트 목록 표시:

`tea pulls ls`

- 현재 저장소를 브라우저에서 열기:

`tea open`
