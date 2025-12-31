# immich-go

> Immich-Go는 대규모 사진 컬렉션을 자체 호스팅 Immich 서버에 업로드하는 작업을 간소화하도록 설계된 오픈소스 도구.
> 참고: `immich`.
> 더 많은 정보: <https://github.com/simulot/immich-go>.

- Google 사진 테이크아웃 파일을 Immich 서버에 업로드:

`immich-go -server={{서버_주소}} -key={{서버_키}} upload {{경로/대상/테이크아웃_파일.zip}}`

- 앨범을 자동 생성하면서 2019년 6월에 촬영한 사진을 가져옴:

`immich-go -server={{서버_주소}} -key={{서버_키}} upload -create-albums -google-photos -date={{2019-06}} {{경로/대상/테이크아웃_파일.zip}}`

- 구성 파일의 서버 및 키를 사용하여 테이크아웃 파일 업로드:

`immich-go -use-configuration={{~/.immich-go/immich-go.json}} upload {{경로/대상/테이크아웃_파일.zip}}`

- Immich 서버 콘텐츠를 검사하고, 품질이 낮은 이미지를 제거하고, 엘범을 보존:

`immich-go -server={{서버_주소}} -key={{서버_키}} duplicate -yes`

- "YYYY-MM-DD" 패턴으로 생성된 모든 앨범 삭제:

`immich-go -server={{서버_주소}} -key={{서버_키}} tool album delete {{\d{4}-\d{2}-\d{2}}}`
