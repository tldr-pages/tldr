# stylua

> 고정된 스타일의 Lua 코드 포매터.
> 더 많은 정보: <https://github.com/JohnnyMorganz/StyLua>.

- 파일이나 전체 디렉토리를 자동으로 포맷:

`stylua {{경로/대상/파일_또는_폴더}}`

- 특정 파일이 포맷되었는지 확인:

`stylua --check {{경로/대상/파일}}`

- 특정 구성 파일로 실행:

`stylua --config-path {{경로/대상/구성_파일}} {{경로/대상/파일}}`

- `stdin`에서 코드를 포맷하고 `stdout`으로 출력:

`stylua - < {{경로/대상/파일.lua}}`

- 공백을 사용하고 단일 인용부호를 선호하여 파일이나 디렉토리 포맷:

`stylua --indent-type {{Spaces}} --quote-style {{AutoPreferSingle}} {{경로/대상/파일_또는_폴더}}`
