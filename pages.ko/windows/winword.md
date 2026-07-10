# winword

> Microsoft Office 워드 프로세스 애플리케이션.
> 더 많은 정보: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=word>.

- Microsoft Word 실행:

`winword`

- 문서를 열지 않고([n]o) Microsoft Word 실행:

`winword /n`

- 새 빈 문서 작성([w]rite):

`winword /w`

-  기존 파일을 기반으로([f]rom) 새 문서 생성:

`winword /f {{경로\대상\파일.docx}}`

- 하나 이상의 문서를 편집용(edi[t]ing)으로 열기:

`winword /t {{경로\대상\파일1.docx 경로\대상\파일2.docx ...}}`

- 모든 AutoExec 매크로([m]acros)를 비활성화한 상태로 문서 열기:

`winword /m {{경로\대상\파일.docm}}`

- 모든 AutoExec 매크로([m]acros)를 비활성화한 상태로 문서를 연 후, 지정한 매크로 실행:

`winword /m{{매크로_이름}} {{경로\대상\파일.docm}}`

- 안전 모드(Safe Mode)로 Microsoft Word 실행:

`winword /safe`
