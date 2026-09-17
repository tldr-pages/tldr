# pip list

> 설치된 Python 패키지 목록 표시.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_list/>.

- 설치된 패키지 목록 표시:

`pip list`

- 업그레이드 가능한 오래된(outdated) 패키지 목록 표시:

`pip list {{[-o|--outdated]}}`

- 최신 상태(up-to-date) 패키지 목록 표시:

`pip list {{[-u|--uptodate]}}`

- JSON 형식으로 패키지 목록 표시:

`pip list --format json`

- 다른 패키지에 의해 요구되지 않는 패키지 목록 표시:

`pip list --not-required`

- 사용자 사이트에 설치된 패키지만 표시:

`pip list --user`

- editable 패키지를 제외하고 패키지 목록 표시:

`pip list --exclude-editable`

- freeze 형식으로 패키지 목록 표시 (`pip freeze`와 달리, editable 설치 정보는 표시하지 않음):

`pip list --format freeze`
