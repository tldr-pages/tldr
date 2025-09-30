# pio team

> PlatformIO 팀 관리.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/team/>.

- 지정된 설명으로 새 팀 생성:

`pio team create --description {{설명}} {{조직_이름}}:{{팀_이름}}`

- 팀 삭제:

`pio team destroy {{조직_이름}}:{{팀_이름}}`

- 팀에 새 사용자 추가:

`pio team add {{조직_이름}}:{{팀_이름}} {{사용자_이름}}`

- 팀에서 사용자 제거:

`pio team remove {{조직_이름}}:{{팀_이름}} {{사용자_이름}}`

- 사용자가 속한 모든 팀과 그 멤버 목록:

`pio team list`

- 조직 내 모든 팀 목록:

`pio team list {{조직_이름}}`

- 팀 이름 변경:

`pio team update --name {{새_팀_이름}} {{조직_이름}}:{{팀_이름}}`

- 팀 설명 변경:

`pio team update --description {{새_설명}} {{조직_이름}}:{{팀_이름}}`
