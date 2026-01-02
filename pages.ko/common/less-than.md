# <

> 데이터를 `stdin`으로 리다이렉트.
> 더 많은 정보: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- 파일을 `stdin`으로 리다이렉트 (`cat file.txt |`와 동일한 효과를 가짐):

`{{명령어}} < {{경로/대상/파일.txt}}`

- 히어 문서를 생성하여 `stdin`으로 전달 (여러 줄 명령 필요):

`{{명령어}} << {{EOF}} <Enter> {{여러_줄_데이터}} <Enter> {{EOF}}`

- 히어 문자열을 생성하여 `stdin`으로 전달 (`echo string |`와 동일한 효과를 가짐):

`{{명령어}} <<< {{문자열}}`
