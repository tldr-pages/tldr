# axel

> 가속기를 다운로드 하십시오. HTTP, HTTPS, FTP를 지원합니다.
> 더 많은 정보: <https://github.com/axel-download-accelerator/axel>.

- 파일로 URL 다운로드:

`axel {{url}}`

- 다운로드 및 파일 이름 지정:

`axel {{url}} -o {{filename}}`

- 여러 연결로 다운로드:

`axel -n {{connections_num}} {{url}}`

- mirrors 검색:

`axel -S {{mirrors_num}} {{url}}`

- 다운로드 속도 제한 (초당 바이트):

`axel -s {{speed}} {{url}}`
