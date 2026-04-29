# ARK: Survival Ascended

> headless ARK: Survival Ascended 서버를 생성하고 실행하는 방법.
> 더 많은 정보: <https://ark.wiki.gg/wiki/Server_configuration>.

- 특정 맵으로 서버 시작:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}}`

- 세션 이름, 서버 비밀번호, 관리자 비밀번호 설정하여 시작:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}}?SessionName={{세션_이름}}?ServerPassword={{서버_비밀번호}}?ServerAdminPassword={{관리자_비밀번호}}`

- 특정 포트와 최대 플레이어 수 설정하여 시작:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}} -port={{7777}} -WinLiveMaxPlayers={{1..70}}`

- PvE 활성화 및 PvP 비활성화:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}}?ServerPVE=true`

- 야생 생물 최대 레벨에 영향을 줄 수 있는 서버 난이도 배열 설정:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}}?DifficultyOffset={{1.0}}`

- 충돌 문제 방지를 위해 생물 애니메이션 최적화 비활성화:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}} -AlwaysTickDedicatedSkeletalMeshes`

- 특정 모드 활성화 (ID를 쉼표로 구분):

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}} -mods={{mod_id1,mod_id2,...}}`

- 특정 플랫폼에서의 접속 허용:

`{{경로/대상}}/ArkAscendedServer {{TheIsland_WP}} -ServerPlatform={{PC+XSX+PS5}}`
