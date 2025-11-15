# kube-fzf

> Kubernetes Pod의 명령줄 퍼지 검색을 위한 셸 명령.
> 관련 명령은 `kubectl`을 참고하세요.
> 더 많은 정보: <https://github.com/thecasualcoder/kube-fzf>.

- Pod 세부 정보 가져오기 (현재 네임스페이스에서):

`findpod`

- Pod 세부 정보 가져오기 (모든 네임스페이스에서):

`findpod -a`

- Pod 설명:

`describepod`

- Pod 로그 실시간 보기:

`tailpod`

- Pod의 컨테이너에 접속:

`execpod {{셸_명령어}}`

- Pod 포트 포워딩:

`pfpod {{포트_번호}}`
