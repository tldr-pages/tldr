# axel

> 가속기를 다운로드 하십시오.
> HTTP, HTTPS, FTP를 지원합니다.
> 같이 보기: `aria2c`.
> 더 많은 정보: <https://manned.org/axel>.

- 파일로 URL 다운로드:

`axel {{url}}`

- 다운로드 및 파일 이름 지정:

`axel {{url}} {{[-o|--output]}} {{경로/대상/파일}}`

- 여러 연결로 다운로드:

`axel {{[-n|--num-connections]}} {{connections_num}} {{url}}`

- mirrors 검색:

`axel {{[-S|--search=]}}{{mirrors_num}} {{url}}`

- 다운로드 속도 제한 (초당 바이트):

`axel {{[-s|--max-speed]}} {{speed}} {{url}}`
