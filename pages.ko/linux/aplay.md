# aplay

> ALSA 사운드카드 드라이버를 위한 사운드 플레이어.
> 더 많은 정보: <https://manned.org/aplay>.

- 특정 파일 재생 (파일 형식에 따라 샘플링 속도, 비트 깊이 등이 자동으로 결정됨):

`aplay {{경로/대상/파일}}`

- 특정 파일의 처음 10초를 2500 Hz에서 재생:

`aplay --duration={{10}} --rate={{2500}} {{경로/대상/파일}}`

- 22050 Hz, 모노, 8비트, Mu-Law `.au` 파일로 원시 파일 재생:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{경로/대상/파일}}`
