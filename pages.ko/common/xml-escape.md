# xml escape

> 특수 XML 문자를 이스케이프합니다. 예: `<a1>` → `&lt;a1&gt;`.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960>.

- 문자열에서 특수 XML 문자 이스케이프:

`xml {{[esc|escape]}} "{{<a1>}}"`

- `stdin`에서 특수 XML 문자 이스케이프:

`echo "{{<a1>}}" | xml {{[esc|escape]}}`

- 도움말 표시:

`xml {{[esc|escape]}} --help`
