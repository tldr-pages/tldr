# immich

> Immich에는 커멘드라인에서 특정 작업을 수행할 수 있는 커멘드라인 인터페이스 (CLI)가 있음.
> 참고: `immich-go`.
> 더 많은 정보: <https://immich.app/docs/features/command-line-interface/>.

- Immich 서버에 인증:

`immich login {{서버_주소/api}} {{서버_키}}`

- 일부 이미지 파일 업로드:

`immich upload {{파일1.jpg 파일2.jpg}}`

- 하위 디렉터리를 포함한 디렉터리 업로드:

`immich upload --recursive {{경로/대상/디렉터리}}`

- 디렉터리를 기반으로 앨범 만들기:

`immich upload --album-name "{{My summer holiday}}" --recursive {{경로/대상/디렉터리}}`

- glob 패턴과 일치하는 리소스 건너뛰기:

`immich upload --ignore {{**/Raw/** **/*.tif}} --recursive {{경로/대상/디렉터리}}`

- 숨겨진 파일 포함:

`immich upload --include-hidden --recursive {{경로/대상/디렉터리}}`
