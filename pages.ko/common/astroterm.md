# astroterm

> 터미널 기반 별자리 지도.
> 더 많은 정보: <https://github.com/da-luce/astroterm#usage>.

- 현재 위치를 기준으로, 별과 행성의 실시간 위치 표시:

`astroterm`

- 별자리를 표시하고, 색상을 사용하며, 지정한 프레임 속도로 시뮬레이션 렌더링:

`astroterm {{[-C|--constellations]}} {{[-c|--color]}} {{[-f|--fps]}} {{60}}`

- 기본 ASCII 문자 대신 유니코드 문자를 사용하고, 지정한 등급보다 밝은 별만 렌더링:

`astroterm {{[-u|--unicode]}} {{[-t|--threshold]}} {{2.0}}`

- 지정한 위도, 경도 및 날짜/시간 사용:

`astroterm {{[-a|--latitude]}} {{90.0}} {{[-o|--longitude]}} {{-180.0}} {{[-d|--datetime]}} {{2025-08-04T12:00:00}}`

- 지정한 도시의 경도, 위도를 사용하고 시뮬레이션 속도를 지정한 배율로 설정:

`astroterm {{[-i|--city]}} {{Singapore}} {{[-s|--speed]}} {{1000.0}}`
