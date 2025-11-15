# tod

> Rust로 작성된 간단한 Todoist 클라이언트.
> 간단한 입력을 받아 인박스 또는 다른 프로젝트에 저장합니다. 자연어 처리를 활용하여 기한, 태그 등을 할당합니다.
> 더 많은 정보: <https://github.com/alanvardy/tod>.

- 프로젝트 가져오기(프로젝트 프롬프트를 활성화하려면 필요):

`tod project import`

- 기한과 함께 빠르게 작업 생성:

`tod --quickadd {{오늘 우유 더 사기}}`

- 새 작업 생성(내용 및 프로젝트를 입력하라는 메시지가 표시됨):

`tod task create`

- 특정 프로젝트에 작업 생성:

`tod task create --content "{{Rust 더 작성하기}}" --project {{코드}}`

- 특정 프로젝트의 다음 작업 가져오기:

`tod task next`

- 작업 일정 가져오기:

`tod task list --scheduled --project {{작업}}`

- 작업에 대한 모든 작업 가져오기:

`tod task list --project {{작업}}`
