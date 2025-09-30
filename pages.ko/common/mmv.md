# mmv

> 파일을 대량으로 이동 및 이름 변경.
> 더 많은 정보: <https://manned.org/mmv.1>.

- 특정 확장자를 가진 모든 파일의 확장자 변경:

`mmv "*{{.old_extension}}" "#1{{.new_extension}}"`

- `report6part4.txt`를 `./french/rapport6partie4.txt`로 복사하고, 유사한 이름을 가진 모든 파일도 함께 복사:

`mmv -c "{{report*part*.txt}}" "{{./french/rapport#1partie#2.txt}}"`

- 모든 `.txt` 파일을 하나의 파일로 합치기:

`mmv -a "{{*.txt}}" "{{모두.txt}}"`

- 파일 이름의 날짜 형식을 "M-D-Y"에서 "D-M-Y"로 변환:

`mmv "{{[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt}}" "{{#3#4-#1#2-#5#6#7#8.txt}}"`
