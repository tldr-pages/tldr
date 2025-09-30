# nala

> 더 나은 형식의 패키지 관리 도구.
> `python-apt` API의 프론트엔드.
> 더 많은 정보: <https://gitlab.com/volian/nala>.

- 패키지를 설치하거나 최신 버전으로 업데이트:

`sudo nala install {{패키지}}`

- 패키지 제거:

`sudo nala remove {{패키지}}`

- 패키지 및 설정 파일 제거:

`nala purge {{패키지}}`

- 단어, 정규식(기본값) 또는 glob을 사용하여 패키지 이름 및 설명 검색:

`nala search "{{패턴}}"`

- 사용 가능한 패키지 목록을 업데이트하고 시스템 업그레이드:

`sudo nala upgrade`

- 시스템에서 사용하지 않는 모든 패키지 및 의존성 제거:

`sudo nala autoremove`

- 다운로드 속도를 개선하기 위해 빠른 미러 가져오기:

`sudo nala fetch`

- 모든 거래 내역 표시:

`nala history`
