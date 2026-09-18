# skills

> AI 코딩 에이전트에서 재사용 가능한 스킬을 관리.
> 더 많은 정보: <https://github.com/vercel-labs/skills>.

- 스킬을 대화형으로 또는 키워드로 검색:

`skills {{[f|find]}} {{키워드}}`

- 설치된 모든 스킬 목록 표시:

`skills {{[ls|list]}}`

- 저장소의 모든 스킬 설치:

`skills {{[a|add]}} {{소유자}}/{{저장소}}`

- 특정 스킬을 지정한 에이전트에 설치:

`skills {{[a|add]}} {{소유자}}/{{저장소}} {{[-s|--skill]}} {{스킬_이름}} {{[-a|--agent]}} {{에이전트_이름}}`

- 설치된 스킬 제거:

`skills {{[rm|remove]}} {{스킬_이름}}`

- 설치된 모든 스킬 업데이트:

`skills update`

- 새로운 `SKILL.md` 템플릿 생성:

`skills init {{스킬_이름}}`
