# tsort

> 위상 정렬 수행.
> 일반적으로 유향 비순환 그래프에서 노드의 의존성 순서를 보여주는 데 사용됨.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/tsort-invocation.html>.

- 공백으로 구분된 입력의 각 줄에 대해 부분 정렬과 일치하는 위상 정렬 수행:

`tsort {{경로/대상/파일}}`

- 문자열에 대해 일관된 위상 정렬 수행:

`echo -e "{{UI Backend\nBackend Database\nDocs UI}}" | tsort`
