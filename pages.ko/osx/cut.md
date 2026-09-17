# cut

> `stdin` 또는 파일에서 특정 필드를 잘라내는 명령어.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- 각 줄으 다섯번째 문자([c]haracter) 출력:

`{{명령어}} | cut -c 5`

- 지정한 파일의 각 줄에서 5~10번째 문자([c]haracter)를 출력:

`cut -c 5-10 {{경로/대상/파일}}`

- 파일의 각 줄을 구분자로 나누어 2번째와 6번째 필드([f]ields) 출력 (기본 구분자: `TAB`):

`cut -f 2,6 {{경로/대상/파일}}`

- 지정한 구분자([d]elimiter)로 나누고 두 번째 필드([f]ield)부터 끝까지 출력:

`{{명령어}} | cut -d "{{구분자}}" -f 2-`

- 공백을 구분자([d]elimiter)로 사용하여 처음 3개의 필드([f]ields)만 출력:

`{{명령어}} | cut -d " " -f -3`
