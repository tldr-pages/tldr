# aspell

> 대화형 맞춤법 검사기.
> 더 많은 정보: <http://aspell.net/man-html/index.html>.

- 단일 파일의 철자 검사:

`aspell check {{경로/대상/파일}}`

- `stdin`에서 철자가 틀린 단어를 나열:

`cat {{경로/대상/파일}} | aspell list`

- 사용 가능한 사전적 언어 표시:

`aspell dicts`

- 다른 언어로 `aspell`을 실행 (두 글자 ISO 639 언어 코드 사용):

`aspell --lang={{cs}}`

- `stdin`에서 철자가 틀린 단어를 나열하고, 개인 단어 목록에서 단어를 무시:

`cat {{경로/대상/파일}} | aspell --personal={{personal-word-list.pws}} list`
