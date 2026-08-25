# msgattrib

> `.po` 번역 파일의 메시지 속성을 필터링하고 조작.
> 더 많은 정보: <https://www.gnu.org/software/gettext/manual/gettext.html#msgattrib-Invocation>.

- 번역된 메시지만 유지:

`msgattrib --translated {{입력_파일.po}} > {{translated.po}}`

- 번역되지 않은 메시지만 유지:

`msgattrib --untranslated {{입력_파일.po}} > {{untranslated.po}}`

- 퍼지(fuzzy) 메시지 제거:

`msgattrib --no-fuzzy {{입력_파일.po}} > {{제거된_파일.po}}`

- 퍼지(fuzzy) 메시지만 제거:

`msgattrib --only-fuzzy {{입력_파일.po}} > {{fuzzy.po}}`

- 모든 메시지를 퍼지(fuzzy) 상태로 표시:

`msgattrib --set-fuzzy {{입력_파일.po}} > {{fuzzy.po}}`

- 퍼지(fuzzy) 표시 제거:

`msgattrib --clear-fuzzy {{입력_파일.po}} > {{제거된_파일.po}}`

- 파일 위치 기준으로 정렬하여 출력:

`msgattrib {{[-F|--sort-by-file]}} {{입력_파일.po}} > {{정렬된_파일.po}}`

- 도움말 표시:

`msgattrib {{[-h|--help]}}`
