# filen

> Filen(종단간 암호화된 클라우드 스토리지 서비스)과 상호작용하는 도구.
> 더 많은 정보: <https://github.com/FilenCloudDienste/filen-cli>.

- 대화형 모드로 진입:

`filen`

- 원격 폴더에 로컬 파일 업로드:

`filen upload {{경로/대상/로컬_파일}} {{원격_폴더_아이디}}`

- 원격 ID를 사용하여 파일 또는 폴더 다운로드:

`filen download {{원격_아이디}} {{경로/대상/로컬_목적지}}`

- 원격 폴더 내 파일 및 폴더 목록 출력:

`filen ls {{원격_폴더}}`

- 원격 파일 및 폴더 삭제 (휴지통으로 이동):

`filen rm {{원격_아이디}}`

- 휴지통 항목 복원:

`filen trash restore {{원격_아이디}}`

- 로컬과 원격 폴더 간 양방향 동기화:

`filen sync {{경로/대상/로컬_폴더}}:/{{원격_폴더}} --continuous`

- 클라우드에서 로컬로 단방향 동기화:

`filen sync {{경로/대상/로컬_폴더}}:ctl:/{{원격_폴더}}`
