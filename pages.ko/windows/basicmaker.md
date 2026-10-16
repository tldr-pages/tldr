# basicmaker

> SoftMaker Office의 BASIC 매크로 편집기 애플리케이션.
> 더 많은 정보: <https://help.softmaker.com/basicmaker2026/en/index.html>.

- 매크로 편집기 실행(파일 경로를 생략하면 새로운 빈 파일 생성):

`basicmaker {{경로\대상\파일.bas}}`

- 스크립트를 열고 지정한 줄로 이동:

`basicmaker -Line={{줄_번호}} "{{경로\대상\파일.bas}}"`

- 지정한 매크로 스크립트를 백그라운드에서 조용히([S]ilently) 실행:

`basicmaker -S "{{경로\대상\파일.bas}}"`

- 매크로 스크립트를 열지 않고([N]o) BasicMaker 실행:

`basicmaker -N`

- 열 파일([F]ile to [O]pen)을 선택할 수 있는 대화 상자와 함께 BasicMaker 실행:

`basicmaker -FO`

- 매크로 스크립트를 기본 프린터로 바로 인쇄([P]rint):

`basicmaker -P"{{경로\대상\파일.bas}}"`

- 매크로 스크립트를 지정한 프린터로 바로 인쇄:

`basicmaker -Q"{{프린터}}","{{경로\대상\파일.bas}}"`
