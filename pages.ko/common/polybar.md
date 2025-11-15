# polybar

> 빠르고 사용하기 쉬운 상태 표시줄.
> 더 많은 정보: <https://github.com/polybar/polybar/wiki>.

- Polybar 시작 (구성 파일에 하나의 막대만 정의되어 있는 경우 막대 이름은 선택 사항):

`polybar {{막대_이름}}`

- 지정된 구성 파일로 Polybar 시작:

`polybar --config={{경로/대상/config.ini}} {{막대_이름}}`

- 구성 파일이 수정될 때 막대를 다시 로드하며 Polybar 시작:

`polybar --reload {{막대_이름}}`
