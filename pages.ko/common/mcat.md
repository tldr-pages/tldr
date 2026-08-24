# mcat

> 파일(Markdown 포함), 디렉터리, 이미지, 비디오를 파싱, 변환 및 미리보기하는 도구.
> 더 많은 정보: <https://github.com/Skardyy/mcat#example-usage>.

- 파일 내용 표시:

`mcat {{경로/대상/파일}}`

- 특정 테마를 사용하여 Markdown 파일 표시:

`mcat {{[-t|--theme]}} {{테마_이름}} {{경로/대상/파일.md}}`

- Display an image or video inline:

`mcat {{[-i|--output inline]}} {{경로/대상/파일}}`

- 파일을 특정 형식(예. `html`, `md`, `image`)으로 변환:

`mcat {{[-o|--output]}} {{포맷}} {{경로/대상/파일}}`

- 디렉터리 내용 표시:

`mcat {{경로/대상/디렉터리}}`

- 숨김 파일 포함해 디렉터리 내용 표시:

`mcat {{[-a|--hidden]}} {{경로/대상/디렉터리}}`

- 페이징 없이 내용 출력:

`mcat {{[-P|--paging never]}} {{경로/대상/파일}}`
