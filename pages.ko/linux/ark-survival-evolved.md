# ARK: Survival Evolved

> headless ARK: Survival Evolved 서버를 생성하고 실행하는 방법.
> 더 많은 정보: <https://ark.wiki.gg/wiki/Server_configuration>.

- 특정 맵으로 서버 시작:

`{{경로/대상}}/ShooterGameServer {{TheIsland}}`

- 세션 이름, 서버 비밀번호, 관리자 비밀번호 설정하여 시작:

`{{경로/대상}}/ShooterGameServer {{TheIsland}}?SessionName={{세션_이름}}?ServerPassword={{서버_비밀번호}}?ServerAdminPassword={{관리자_비밀번호}}`

- 특정 포트와 최대 플레이어 수 설정하여 시작:

`{{경로/대상}}/ShooterGameServer {{TheIsland}}?Port={{7777}}?MaxPlayers={{1..70}}`

- PvE 활성화 및 PvP 비활성화:

`{{경로/대상}}/ShooterGameServer {{TheIsland}}?ServerPVE=true`

- 야생 생물 최대 레벨에 영향을 줄 수 있는 서버 난이도 배열 설정:

`{{경로/대상}}/ShooterGameServer {{TheIsland}}?DifficultyOffset={{1.0}}`

- 특정 이벤트 활성화:

`{{경로/대상}}/ShooterGameServer {{TheIsland}} -ActiveEvent={{Summer}}`

- 자동 모드 다운로드, 설치 및 업데이트 활성화 (Steam 전용):

`{{경로/대상}}/ShooterGameServer {{TheIsland}} -automanagedmods`

- Steam과 Epic Games Store 간 교차플레이 활성화:

`{{경로/대상}}/ShooterGameServer {{TheIsland}} -crossplay -PublicIPForEpic={{아이피_주소}}`
