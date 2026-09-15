# powerpnt

> Microsoft Office의 프레젠테이션 애플리케이션.
> 더 많은 정보: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=powerpoint%2C_powerpoint_viewer>.

- 프레젠테이션 애플리케이션 실행:

`powerpnt`

- 새로운 빈([b]lank) 프레젠테이션 생성:

`powerpnt /b`

- 템플릿으로 새로운([n]ew) 프레젠테이션 생성:

`powerpnt /n {{경로\대상\파일.potm}}`

- 하나 이상의 프레젠테이션 파일 열기([o]pen):

`powerpnt /o {{경로\대상\파일1.pptx 경로\대상\파일2.pptx ...}}`

- 슬라이드 쇼([s]lideshow) 모드로 프레젠테이션 열기:

`powerpnt /s {{경로\대상\파일.pptx}}`

- 프레젠테이션을 열고, 지정한 매크로([m]acro) 실행:

`powerpnt /m {{경로\대상\파일.pptm}} "{{매크로_이름}}"`

- 출력 대화상자를 통해 프레젠테이션 출력:

`powerpnt /pwo {{경로\대상\파일.pptx}}`

- 지정한 프린터로([t]o) 프레젠테이션 직접 출력([p]rint):

`powerpnt /pt {{프린터_이름}} {{경로\대상\파일.pptx}}`
