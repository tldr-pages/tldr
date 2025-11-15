# abrt-action-analyze-backtrace

> C/C++ 백트레이스를 분석합니다.
> 중복 해시, 백트레이스 등급을 생성하고 충돌 함수를 식별합니다.
> 문제 디렉터리에 `duphash`, `rating`, `crash_function`이라는 새 요소로 데이터를 저장합니다.
> 더 많은 정보: <https://manned.org/abrt-action-analyze-backtrace>.

- 현재 작업 디렉터리의 백트레이스를 분석:

`abrt-action-analyze-backtrace`

- 특정 디렉터리의 백트레이스를 분석:

`abrt-action-analyze-backtrace -d {{경로/대상/폴더}}`

- 자세히 백트레이스를 분석:

`abrt-action-analyze-backtrace -v`
