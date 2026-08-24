# farge

> 화면의 특정 픽셀 색상을 16진수 또는 RGB 형식으로 표시합니다.
> 더 많은 정보: <https://github.com/sdushantha/farge#usage>.

- 픽셀의 색상을 작은 미리보기 창에 16진수 값으로 표시하고, 이 값을 클립보드에 복사:

`farge`

- 미리보기 창 없이 픽셀의 16진수 값을 클립보드에 복사:

`farge --no-preview`

- 픽셀의 16진수 값을 `stdout`에 출력하고, 이 값을 클립보드에 복사:

`farge --stdout`

- 픽셀의 RGB 값을 `stdout`에 출력하고, 이 값을 클립보드에 복사:

`farge --rgb --stdout`

- 픽셀의 16진수 값을 5000밀리초 동안 알림으로 표시하고, 이 값을 클립보드에 복사:

`farge --notify --expire-time 5000`
