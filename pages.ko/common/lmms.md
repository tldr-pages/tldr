# lmms

> 무료, 오픈 소스, 크로스 플랫폼 디지털 오디오 워크스테이션.
> `.mmp` 또는 `.mmpz` 프로젝트 파일을 렌더링하거나, `.mmpz`를 XML로 덤프하거나, GUI를 시작할 수 있습니다.
> 같이 보기: `mixxx`.
> 더 많은 정보: <https://lmms.io>.

- GUI 시작:

`lmms`

- GUI 시작 및 외부 구성 파일 로드:

`lmms --config {{경로/대상/config.xml}}`

- GUI 시작 및 MIDI 또는 Hydrogen 파일 가져오기:

`lmms --import {{경로/대상/midi/또는/hydrogen/파일}}`

- 지정된 창 크기로 GUI 시작:

`lmms --geometry {{x_크기}}x{{y_크기}}+{{x_오프셋}}+{{y_오프셋}}`

- `.mmpz` 파일 덤프:

`lmms dump {{경로/대상/mmpz/파일.mmpz}}`

- 프로젝트 파일 렌더링:

`lmms render {{경로/대상/mmpz_또는_mmp/파일}}`

- 프로젝트 파일의 개별 트랙 렌더링:

`lmms rendertracks {{경로/대상/mmpz_또는_mmp/파일}} {{경로/대상/덤프/폴더}}`

- 사용자 지정 샘플레이트, 포맷으로 루프 렌더링:

`lmms render --samplerate {{88200}} --format {{ogg}} --loop --output {{경로/대상/출력/파일.ogg}}`
