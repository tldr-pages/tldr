# sg

> Ast-grep은 코드 구조 검색, 린트 및 재작성 도구입니다.
> 더 많은 정보: <https://ast-grep.github.io/guide/introduction.html>.

- 대화형 모드를 사용하여 가능한 쿼리 스캔:

`sg scan --interactive`

- 패턴을 사용하여 현재 디렉토리의 코드 재작성:

`sg run --pattern '{{foo}}' --rewrite '{{bar}}' --lang {{python}}`

- 변경 사항을 적용하지 않고 시각화:

`sg run --pattern '{{useState<number>($A)}}' --rewrite '{{useState($A)}}' --lang {{typescript}}`

- 결과를 JSON으로 출력하고, `jq`를 사용하여 정보 추출 후 `jless`를 통해 대화형으로 보기:

`sg run --pattern '{{Some($A)}}' --rewrite '{{None}}' --json | jq '{{.[].replacement}}' | jless`
