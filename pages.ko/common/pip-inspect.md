# pip inspect

> Python 환경을 검사하고 JSON 형식 보고서 생성.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_inspect/>.

- 현재 환경 검사:

`pip inspect`

- 검사 결과를 파일로 저장:

`pip inspect > {{환경_검사결과.json}}`

- 로컬에 설치된 패키지만 검사 (전역 패키지 제외):

`pip inspect --local`

- 사용자 설치 패키지만 검사:

`pip inspect --user`

- 특정 경로의 패키지 검사:

`pip inspect --path {{경로/대상/환경}}`

- 자세한 출력과 함께 검사 (참고: `-v`를 여러 번 사용하면 더 상세한 출력 제공):

`pip inspect {{[-v|--verbose]}}`
