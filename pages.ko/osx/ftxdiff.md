# ftxdiff

> 두 폰트 간의 차이점을 비교합니다.
> 더 많은 정보: <https://developer.apple.com/fonts>.

- 특정 텍스트 [f]파일에 차이점 출력:

`ftxdiff --output {{경로/대상/폰트_차이_파일.txt}} {{경로/대상/폰트_파일1.ttc}} {{경로/대상/폰트_파일2.ttc}}`

- 출력에 글리프 이름 포함:

`ftxdiff --include-glyph-names`

- 출력에 유니코드 이름 포함:

`ftxdiff --include-unicode-names`
