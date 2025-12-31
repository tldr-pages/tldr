# flameshot

> GUI가 있는 스크린샷 도구.
> 텍스트, 도형, 색상, imgur 같은 기본 이미지 편집을 지원합니다.
> 더 많은 정보: <https://flameshot.org/docs/advanced/commandline-options/>.

- 전체 화면 스크린샷 생성:

`flameshot full`

- 상호작용 방식으로 스크린샷 생성:

`flameshot gui`

- 특정 경로에 스크린샷 저장:

`flameshot gui --path {{경로/대상/폴더}}`

- 간소화된 모드로 상호작용 방식의 스크린샷 생성:

`flameshot launcher`

- 특정 모니터에서 스크린샷 생성:

`flameshot screen --number {{2}}`

- 스크린샷을 생성하고 `stdout`에 출력:

`flameshot gui --raw`

- 스크린샷을 생성하고 클립보드에 복사:

`flameshot gui --clipboard`

- 특정 밀리초 지연 후 스크린샷 생성:

`flameshot full --delay {{5000}}`
