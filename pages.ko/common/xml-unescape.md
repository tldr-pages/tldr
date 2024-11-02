# xml unescape

> 특수 XML 문자를 원래대로 변환, 예: `&lt;a1&gt;` → `<a1>`.
> 더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- 문자열에서 특수 XML 문자를 원래대로 변환:

`xml unescape "{{&lt;a1&gt;}}"`

- `stdin`에서 특수 XML 문자를 원래대로 변환:

`echo "{{&lt;a1&gt;}}" | xml unescape`

- 도움말 표시:

`xml escape --help`
