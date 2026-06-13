# pio org

> PlatformIO 조직 및 소유자를 관리.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- 새 조직 생성:

`pio org create {{조직_이름}}`

- 조직 삭제:

`pio org destroy {{조직_이름}}`

- 사용자 조직에 추가:

`pio org add {{조직_이름}} {{사용자_이름}}`

- 사용자 조직에서 제거:

`pio org remove {{조직_이름}} {{사용자_이름}}`

- 현재 사용자가 멤버로 있는 모든 조직 및 소유자 나열:

`pio org list`

- 조직의 이름, 이메일 또는 표시 이름 업데이트:

`pio org update --orgname {{새_조직_이름}} --email {{새_이메일}} --displayname {{새_표시_이름}} {{조직_이름}}`
