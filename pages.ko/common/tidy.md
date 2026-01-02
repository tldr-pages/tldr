# tidy

> HTML, XHTML 및 XML 파일을 정리하고 보기 좋게 출력.
> 참고: `tidy`는 원래 들여쓰기를 보존할 수 없습니다.
> 더 많은 정보: <https://api.html-tidy.org/tidy/tidylib_api_next/group__options__cli.html#gad7a9fcaf7b2a712a82e625e84c042b28>.

- HTML 파일을 보기 좋게 출력:

`tidy {{경로/대상/파일.html}}`

- [i]ndentation을 활성화하고, 줄을 100으로 [w]rapping하여 `output.html`에 저장:

`tidy --indent y --wrap 100 -output {{경로/대상/output.html}} {{경로/대상/파일.html}}`

- 설정 파일을 사용하여 HTML 파일을 직접 수정:

`tidy -config {{경로/대상/설정}} -modify {{경로/대상/파일.html}}`
