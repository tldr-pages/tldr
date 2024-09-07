# exa

> `ls`의 현대적인 대체품 (디렉토리 내용 나열).
> 더 많은 정보: <https://the.exa.website>.

- 파일을 한 줄에 하나씩 나열:

`exa --oneline`

- 숨김 파일을 포함한 모든 파일 나열:

`exa --all`

- 모든 파일의 긴 형식 목록 (권한, 소유권, 크기 및 수정 날짜):

`exa --long --all`

- 가장 큰 파일을 맨 위에 나열:

`exa --reverse --sort={{size}}`

- 파일 트리를 3단계 깊이로 표시:

`exa --long --tree --level={{3}}`

- 수정 날짜순으로 파일 나열 (오래된 것부터):

`exa --long --sort={{modified}}`

- 헤더, 아이콘 및 Git 상태와 함께 파일 나열:

`exa --long --header --icons --git`

- `.gitignore`에 언급된 파일은 나열하지 않음:

`exa --git-ignore`
