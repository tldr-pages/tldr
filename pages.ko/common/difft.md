# difft

> 프로그래밍 언어의 구문을 기반으로 파일이나 디렉터리를 비교.
> 참고: `delta`, `diff`.
> 더 많은 정보: <https://difftastic.wilfred.me.uk/introduction.html>.

- 두 개의 파일 또는 디렉터리를 비교:

`difft {{경로/대상/파일_또는_디렉터리1}} {{경로/대상/파일_또는_디렉터리2}}`

- 파일 간의 차이점만 보고:

`difft --check-only {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 디스플레이 모드를 지정 (기본값은 `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 비교할 때 설명을 무시:

`difft --ignore-comments {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 소스코드 구문 강조 활성화/비활성화 (기본값은 `on`):

`difft --syntax-highlight {{on|off}} {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 파일 간에 차이가 없으면 아무것도 출력하지 않음:

`difft --skip-unchanged {{경로/대상/파일_또는_디렉터리1}} {{경로/대상/파일_또는_디렉터리2}}`

- 확장명과 함께, 도구에서 지원하는 모든 프로그래밍 언어를 출력:

`difft --list-languages`
