# afplay

> 명령줄 오디오 플레이어.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- 사운드 파일 재생 (재생이 끝날 때까지 대기):

`afplay {{경로/대상/파일}}`

- 사운드 파일을 2배속으로 재생 (재생 속도):

`afplay --rate {{2}} {{경로/대상/파일}}`

- 사운드 파일을 반속도로 재생:

`afplay --rate {{0.5}} {{경로/대상/파일}}`

- 사운드 파일의 처음 N초만 재생:

`afplay --time {{초}} {{경로/대상/파일}}`
