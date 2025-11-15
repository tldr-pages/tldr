# zathura

> vim과 유사한 모달 문서 뷰어로, 통합 명령줄을 제공합니다.
> 백엔드(poppler, PostScript, 또는 DjVu)가 설치되었는지 확인하세요.
> 더 많은 정보: <https://pwmt.org/projects/zathura/>.

- 파일 열기:

`zathura {{경로/대상/파일}}`

- 왼쪽/위/아래/오른쪽으로 이동:

`{{<h>|<j>|<k>|<l>|<ArrowKeys>}}`

- 회전:

`<r>`

- 색상 반전:

`<Ctrl r>`

- 주어진 문자열로 텍스트 검색:

`</>{{문자열}}`

- 북마크 생성/삭제:

`<:>{{bmark|bdelete}} {{북마크_이름}}<Enter>`

- 북마크 목록 나열:

`<:>blist<Enter>`
