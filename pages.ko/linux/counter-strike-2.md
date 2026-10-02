# Counter Strike 2

> 헤드리스 Counter Strike 2 전용 서버를 실행.
> 더 많은 정보: <https://developer.valvesoftware.com/wiki/Counter-Strike_2/Dedicated_Servers>.

- 하나의 맵으로 게임 서버 실행:

`{{경로/대상}}/cs2 -dedicated +map {{de_dust2}}`

- 최대 플레이어 수를 지정하여 게임 서버 실행:

`{{경로/대상}}/cs2 -dedicated +map {{de_dust2}} -maxplayers {{64}}`

- 서버 IP 주소와 포트를 지정하여 게임 서버 실행:

`{{경로/대상}}/cs2 -dedicated +map {{de_dust2}} -ip {{1.2.3.4}} -port {{27015}}`

- [대화형] 서버 종료:

`quit`
