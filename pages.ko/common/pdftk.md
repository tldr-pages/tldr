# pdftk

> PDF 도구 모음.
> 더 많은 정보: <https://www.pdflabs.com/docs/pdftk-man-page/>.

- PDF 파일에서 1-3, 5, 6-10 페이지를 추출하여 다른 파일로 저장:

`pdftk {{입력.pdf}} cat {{1-3 5 6-10}} output {{출력.pdf}}`

- PDF 파일 목록을 병합(연결)하여 결과를 다른 파일로 저장:

`pdftk {{파일1.pdf 파일2.pdf ...}} cat output {{출력.pdf}}`

- PDF 파일의 각 페이지를 별도의 파일로 분할하고, 지정된 파일 이름 출력 패턴 사용:

`pdftk {{입력.pdf}} burst output {{출력_%d.pdf}}`

- 모든 페이지를 시계 방향으로 180도 회전:

`pdftk {{입력.pdf}} cat {{1-endsouth}} output {{출력.pdf}}`

- 세 번째 페이지만 시계 방향으로 90도 회전하고 나머지는 변경 없이 유지:

`pdftk {{입력.pdf}} cat {{1-2 3east 4-end}} output {{출력.pdf}}`
