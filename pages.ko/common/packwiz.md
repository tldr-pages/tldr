# packwiz

> Minecraft 모드팩을 생성, 편집 및 관리.
> 더 많은 정보: <https://packwiz.infra.link/reference/commands/packwiz/>.

- 현재 디렉토리에서 대화식으로 새로운 모드팩 생성:

`packwiz init`

- Modrinth 또는 Curseforge에서 모드 추가:

`packwiz {{modrinth|curseforge}} add {{url|slug|검색_용어}}`

- 모드팩의 모든 모드 나열:

`packwiz list`

- 파일을 수동으로 편집한 후 `index.toml` 업데이트:

`packwiz refresh`

- Modrinth (`.mrpack`) 또는 Curseforge (Zip) 파일로 내보내기:

`packwiz {{modrinth|curseforge}} export`
