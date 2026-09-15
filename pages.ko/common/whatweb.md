# whatweb

> 차세대 웹 스캐너.
> 더 많은 정보: <https://github.com/urbanadventurer/WhatWeb#usage>.

- 웹 사이트 또는 대상을 스캔하여 사용 중인 웹 기술을 탐지:

`whatweb {{웹사이트1 웹사이트2 ...}}`

- 파일에서 스캔 대상 또는 웹사이트 목록 읽기:

`whatweb {{[-i|--input-file]}} {{대상_파일}}`

- 상세모드로 웹사이트 또는 대상 스캔:

`whatweb {{[-v|--verbose]}} {{example.com}}`

- 웹사이트를 공격적(agressive) 모드로 스캔:

`whatweb {{[-a|--aggression]}} 3 {{example.com}}`

- 오류 출력을 줄이고 네트워크 스캔:

`whatweb --no-errors {{192.168.0.0/24}}`

- 플러그인 목록 표시:

`whatweb {{[-l|--list-plugins]}}`

- 지정한 플러그인의 상세 정보 표시:

`whatweb {{[-I|--info-plugins]}} {{플러그인_이름}}`
