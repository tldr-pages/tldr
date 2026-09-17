# pacgraph

> 설치된 패키지의 그래프를 PNG/SVG/GUI/콘솔로 그립니다.
> 더 많은 정보: <https://manned.org/pacgraph>.

- SVG 및 PNG 그래프 생성:

`pacgraph`

- SVG 그래프 생성:

`pacgraph {{[-s|--svg]}}`

- 콘솔에 요약 출력:

`pacgraph {{[-c|--console]}}`

- 기본 파일명/위치 재정의 (참고: 파일 확장자를 지정하지 마십시오):

`pacgraph {{[-f|--file]}} {{경로/대상/파일}}`

- 의존성이 아닌 패키지의 색상 변경:

`pacgraph {{[-t|--top]}} {{색상}}`

- 패키지 의존성의 색상 변경:

`pacgraph {{[-d|--dep]}} {{색상}}`

- 그래프 배경 색상 변경:

`pacgraph {{[-b|--background]}} {{색상}}`

- 패키지 간 연결의 색상 변경:

`pacgraph {{[-l|--link]}} {{색상}}`
