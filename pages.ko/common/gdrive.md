# gdrive

> Google 드라이브와 상호작용.
> 폴더/파일 ID는 구글 드라이브 폴더나 ID URL에서 얻을 수 있음.
> 더 많은 정보: <https://github.com/gdrive-org/gdrive>.

- 지정된 ID를 사용하여 상위 폴더에 대한 로컬 경로를 업로드:

`gdrive upload -p {{아이디}} {{경로/대상/파일_또는_폴더}}`

- ID 별로 파일이나 디렉터리를 현재 디렉터리로 다운로드:

`gdrive download {{아이디}}`

- 해당 ID로 지정된 로컬 경로에 다운로드:

`gdrive download --path {{경로/대상/폴더}} {{아이디}}`

- 주어진 파일이나 폴더를 사용하여 ID의 새로운 개정판을 생성:

`gdrive update {{아이디}} {{경로/대상/파일_또는_폴더}}`
