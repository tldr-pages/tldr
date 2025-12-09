# rbt

> RBTools는 Review Board 및 RBCommons와 함께 작업하기 위한 명령줄 도구 세트입니다.
> 더 많은 정보: <https://www.reviewboard.org/docs/rbtools/dev/>.

- Review Board에 변경 사항 게시:

`rbt post {{변경_번호}}`

- Review Board에 전송될 차이점 표시:

`rbt diff`

- 로컬 브랜치 또는 검토 요청에 변경사항 적용:

`rbt land {{브랜치_이름}}`

- 검토 요청에 대한 변경사항으로 트리 패치:

`rbt patch {{검토_요청_ID}}`

- RBTool을 설정하여 저장소와 통신하도록 설정:

`rbt setup-repo`
