# whereis

> 명령의 바이너리, 소스 및 매뉴얼 페이지 파일을 찾습니다.
> 더 많은 정보: <https://manned.org/whereis>.

- SSH에 대한 바이너리, 소스 및 매뉴얼 페이지 찾기:

`whereis {{ssh}}`

- ls에 대한 바이너리 및 매뉴얼 페이지 찾기:

`whereis -bm {{ls}}`

- gcc의 소스와 Git의 매뉴얼 페이지 찾기:

`whereis -s {{gcc}} -m {{git}}`

- `/usr/bin/`에서만 gcc의 바이너리 찾기:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- 비정상적인 바이너리 찾기 (시스템에 하나 이상의 바이너리가 있는 경우):

`whereis -u *`

- 비정상적인 매뉴얼 항목을 가진 바이너리 찾기 (하나 이상의 매뉴얼이 설치된 경우):

`whereis -u -m *`
