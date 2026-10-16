# planmaker

> SoftMaker Office의 스프레드시트 애플리케이션.
> 더 많은 정보: <https://help.softmaker.com/planmaker2026/en/index.html>.

- 스프레드시트 애플리케이션 실행(파일 경로를 생략하면 새로운 빈 문서 생성):

`planmaker {{경로\대상\파일.pmdx}}`

- 문서를 열지 않고([N]o) PlanMaker 실행:

`planmaker -N`

- 열 파일([F]ile to [O]pen)을 선택할 수 있는 대화 상자와 함께 PlanMaker 실행:

`planmaker -FO`

- 새([N]ew) 문서를 생성할 템플릿 파일([F]ile)을 선택할 수 있는 대화 상자와 함께 PlanMaker 실행:

`planmaker -FN`

- 문서를 기본 프린터로 바로 인쇄([P]rint):

`planmaker -P"{{경로\대상\파일.pmdx}}"`

- 문서를 지정한 프린터로 바로 인쇄:

`planmaker -Q"{{프린터}}","{{경로\대상\파일.pmdx}}"`
