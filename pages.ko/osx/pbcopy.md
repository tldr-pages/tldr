# pbcopy

> `stdin`에서 데이터를 클립보드로 복사합니다.
> 키보드에서 `<Cmd c>`를 누르는 것과 비슷합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- 특정 [f]파일의 내용을 클립보드에 복사:

`pbcopy < {{경로/대상/파일}}`

- 특정 명령의 결과를 클립보드에 복사:

`find . -type t -name "*.png" | pbcopy`
