# duc

> 디스크 사용량을 색인화, 검사 및 시각화하는 도구 모음.
> Duc는 파일 시스템의 폴더 누적 크기를 데이터베이스로 유지하여 이를 쿼리하거나 데이터의 위치를 나타내는 멋진 그래프를 생성할 수 있게 합니다.
> 더 많은 정보: <http://duc.zevv.nl>.

- `/usr` 폴더를 색인하고 기본 데이터베이스 위치 `~/.duc.db`에 기록:

`duc index {{/usr}}`

- `/usr/local` 아래의 모든 파일과 폴더를 나열하고 상대적 파일 크기를 [g]그래프로 표시:

`duc ls --classify --graph {{/usr/local}}`

- `/usr/local` 아래의 모든 파일과 폴더를 트리뷰로 재귀적으로 나열:

`duc ls --classify --graph --recursive {{/usr/local}}`

- 선버스트 그래프를 사용하여 파일 시스템을 탐색하는 그래픽 인터페이스 시작:

`duc gui {{/usr}}`

- 파일 시스템을 탐색하기 위한 ncurses 콘솔 인터페이스 실행:

`duc ui {{/usr}}`

- 데이터베이스 정보 덤프:

`duc info`
