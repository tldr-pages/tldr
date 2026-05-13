# protontricks

> Proton을 지원하는 게임을 위해 Winetricks 명령을 실행하는 간단한 래퍼.
> 더 많은 정보: <https://github.com/Matoking/protontricks#usage>.

- protontricks GUI 실행:

`protontricks --gui`

- 특정 게임에 대해 Winetricks 실행:

`protontricks {{앱_id}} {{winetricks_인수}}`

- 게임 설치 디렉토리 내에서 명령 실행:

`protontricks -c {{명령어}} {{앱_id}}`

- 설치된 모든 게임 [l]나열:

`protontricks -l`

- 게임의 이름으로 앱 ID [s]검색:

`protontricks -s {{게임_이름}}`

- 도움말 표시:

`protontricks --help`
