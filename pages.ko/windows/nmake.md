# nmake

> makefile의 명령을 기반으로 프로젝트를 빌드하기 위한 Microsoft 프로그램 유지 관리 유틸리티.
> 더 많은 정보: <https://learn.microsoft.com/cpp/build/reference/nmake-reference>.

- 현재 디렉터리의 기본 makefile을 사용하여 대상 빌드:

`nmake`

- 특정 makefile를 사용하여 대상 빌드:

`nmake /F {{경로\대상\makefile}}`

- 특정 대상만 빌드:

`nmake {{타겟}}`

- 명령을 실행하지 않고 표시만 수행:

`nmake /N`

- 모든 매크로 정의 및 대상 설명 표시:

`nmake /P`

- 오류 발생 관련없는 대상으로 빌드를 계속 진행:

`nmake /K`

- 타임스탬프 확인 무시하고 빌드 (강제 재빌드):

`nmake /A`

- 저작권 메시지 숨김:

`nmake /NOLOGO`
