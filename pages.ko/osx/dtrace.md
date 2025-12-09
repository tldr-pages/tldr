# dtrace

> D 언어 컴파일러를 호출하고, 버퍼된 추적을 검색하며, DTrace 커널 기능에서 추적된 데이터를 출력하는 간단한 인터페이스.
> DTrace 기능을 위한 일반적인 프론트엔드로, 루트 권한이 필요합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/dtrace.1.html>.

- 특정 아키텍처에 대한 대상 데이터 모델 설정:

`dtrace -arch {{아키텍처_이름}}`

- [a]익명 추적 상태를 확보하고 추적된 데이터 표시:

`dtrace -a`

- 주요 추적 버퍼 크기 설정. 지원되는 단위는 `k`, `m`, `g`, 또는 `t`입니다:

`dtrace -b {{2g}}`

- 지정된 D 프로그램 [s]소스 파일 컴파일:

`dtrace -s {{D_스크립트}}`

- 지정된 [c]명령어를 실행하고 완료 시 종료:

`dtrace -c {{명령어}}`

- 추적 또는 목록(-l 옵션)할 [f]함수 이름 지정. 해당 인자는 `provider:module:function`, `module:function` 또는 `function`과 같은 프로브 설명 형식을 포함할 수 있습니다:

`dtrace -f {{함수}}`

- 지정된 [p]프로세스 ID를 가져와 심볼 테이블을 캐시하고 완료 시 종료:

`dtrace -p {{프로세스_ID}}`

- 프로세스에서 함수 추적을 위한 다양한 옵션 결합:

`dtrace -a -b {{버퍼_크기}} -f {{함수}} -p {{프로세스_ID}}`
