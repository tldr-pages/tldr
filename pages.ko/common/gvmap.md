# gvmap

> 클러스터를 찾고, 해당하는 클러스터를 강조한 지리적 스타일의 맵을 생성.
> 더 많은 정보: <https://graphviz.org/pdf/gvmap.1.pdf>.

- DOT 형식 그래프로부터 클러스터 맵 레이아웃 생성:

`gvmap {{그래프.gv}} -o {{output.xdot}}`

- 입력에 존재하는 클러스터 서브그래프를 사용하여 맵 생성:

`gvmap -D {{그래프.gv}}`

- 출력([o]utput) 맵에 그래프 엣지 포함:

`gvmap -e {{그래프.gv}} -o {{output.xdot}}`

- 색상([c]olor) 스킴 지정 (1: 파스텔, 2: 파랑-노랑, 3: 흰색-빨강 등):

`gvmap -c {{1|2|3|...}} {{그래프.gv}} -o {{output.xdot}}`

- 최대 클러스터([C]lusters) 개수 설정 (기본값 0, 제한 없음 의미):

`gvmap -C {{10}} {{그래프.gv}} -o {{output.xdot}}`

- 클러스터 2만 그리기 (기본적으로는, 모든 클러스터가 그려짐):

`gvmap -highlight={{2}} {{그래프.gv}} -o {{output.xdot}}`
