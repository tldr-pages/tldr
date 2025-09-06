# exiftool

> 파일의 메타 정보를 읽고 쓰기.
> 더 많은 정보: <https://exiftool.org>.

- 특정 파일에 대한 EXIF 메타데이터를 출력 :

`exiftool {{경로/대상/파일}}`

- 지정된 파일에서 모든 EXIF 메타데이터를 제거 :

`exiftool -All= {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 지정된 이미지 파일에서 GPS EXIF 메타데이터를 제거:

`exiftool "-gps*=" {{경로/대상/이미지1 경로/대상/이미지2 ...}}`

- 지정된 이미지 파일에서 모든 EXIF 메타데이터를 제거한 다음, 색상 및 방향에 대한 메타데이터를 다시 추가:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{경로/대상/이미지1 경로/대상/이미지2 ...}}`

- 디렉터리의 모든 사진을 찍은 날짜를 1시간 앞으로 이동:

`exiftool "-AllDates+=0:0:0 1:0:0" {{경로/대상/디렉토리}}`

- 현재 디렉토리의 모든 JPEG 사진을 촬영한 날짜를 1일 2시간 뒤로 이동:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- 백업을 유지하지 않고, `DateTimeOriginal` 필드에서 1.5 시간을 뺀 값만 변경:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- `DateTimeOriginal` 필드를 기반으로 디렉토리에 있는 모든 JPEG 사진의 이름을 반복적으로 변경:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{경로/대상/디렉토리}} -r -ext jpg`
