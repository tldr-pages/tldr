# alex

> 민감하지 않고, 사려깊지 않은 글을 잡는 도구.
> 이것은 당신이 선호 성별, 양극화, 인종 관련, 종교에 대한 고려가 불분명하거나 다른 문구가 아닌 문구를 찾는데 도움이 됩니다.
> 더 많은 정보: <https://github.com/get-alex/alex>.

- `stdin`으로부터 텍스트 분석:

`echo {{His network looks good}} | alex --stdin`

- 현재 디렉토리의 모든 파일 분석:

`alex`

- 특정 파일 분석:

`alex {{textfile.md}}`

- `example.md`를 제외한 모든 Markdown 파일 분석:

`alex *.md !{{example.md}}`
