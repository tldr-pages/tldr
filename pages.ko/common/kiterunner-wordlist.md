# kiterunner wordlist

> API 및 웹 엔드포인트 탐지에 사용되는 워드리스트 관리.
> `wordlist` 하위 명령은 `~/.cache/kiterunner`에 저장된 워드리스트의 조회 및 저장을 처리.
> 더 많은 정보: <https://github.com/assetnote/kiterunner#usage>.

- 캐시된 모든 Assetnote 워드리스트와 사용 가능한 워드리스트 목록 표시:

`kiterunner wordlist list`

- 워드리스트 목록을 JSON 형식으로 출력:

`kiterunner wordlist list {{[-o|--output]}} {{json}}`

- 자세한 디버그 출력과 함께 워드리스트 목록 표시:

`kiterunner wordlist list {{[-v|--verbose]}} {{디버그}}`

- 별칭으로 특정 Assetnote 워드리스트 저장:

`kiterunner wordlist save {{apiroutes-210328}}`

- 전체 파일 이름을 사용하여 특정 Assetnote 워드리스트 저장:

`kiterunner wordlist save {{경로/대상/httparchive_apiroutes_2024_05_28.txt}}`

- 별칭으로 여러 워드리스트를 한 번에 저장:

`kiterunner wordlist save {{apiroutes-210328,aspx-210328}}`

- 출력 없이 워드리스트 저장:

`kiterunner wordlist save {{apiroutes-210328}} {{[-q|--quiet]}}`
