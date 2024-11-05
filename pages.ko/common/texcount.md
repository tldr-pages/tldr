# texcount

> TeX 문서에서 매크로를 제외하고 단어 수를 세기.
> 참고: TeX 문서가 `\include` 또는 `\input`을 사용하고 포함된 파일을 세려면, `texcount`를 루트 TeX 파일이 있는 디렉토리에서 실행해야 합니다.
> 더 많은 정보: <https://app.uio.no/ifi/texcount/howto.html>.

- TeX 파일의 단어 수 세기:

`texcount {{경로/대상/파일.tex}}`

- `\input` 또는 `\include`로 구성된 문서 및 하위 문서의 단어 수 세기:

`texcount -merge {{파일.tex}}`

- 문서 및 하위 문서의 단어 수를 세고 각 파일을 별도로 나열 (총 단어 수 포함):

`texcount -inc {{파일.tex}}`

- 문서 및 하위 문서의 단어 수를 세고 각 챕터별로 세부 카운트 제공 (하위 섹션 대신):

`texcount -merge -sub=chapter {{파일.tex}}`

- 자세한 출력과 함께 단어 수 세기:

`texcount -v {{경로/대상/파일.tex}}`
