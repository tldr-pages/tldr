# mods

> 파이프라인을 위해 설계된 커맨드라인 AI.
> 더 많은 정보: <https://github.com/charmbracelet/mods>.

- 일반적인 질문하기:

`mods "{{오리너구리에 대한 시를 써 줘}}"`

- `$EDITOR`에서 설정 열기:

`mods --settings`

- 코드에 대한 의견을 마크다운 형식으로 요청하기:

`mods --format "{{이 코드를 개선하기 위한 의견은?}}" < {{경로/대상/파일}}`

- 문서화 도움을 마크다운 형식으로 요청하기:

`mods --format "{{r을 누르면 무료 토끼를 보내주는 기능에 대한 새로운 섹션을 이 README에 작성해 줘}}" < {{README.md}}`

- 비디오를 마크다운 형식으로 정리하기:

`ls {{경로/대상/비디오}} | mods --format "{{이를 시대별로 정리하고 요약해 줘}}"`

- 원시 HTML을 읽고 내용을 마크다운 형식으로 요약하기:

`curl "{{https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m}}" | mods --format "{{이 날씨 데이터를 사람을 위해 요약해 줘}}"`

- 도움말 표시:

`mods --help`
