# jpegoptim

> JPEG 이미지 최적화 도구.
> 더 많은 정보: <https://github.com/tjko/jpegoptim>.

- JPEG 이미지 세트를 최적화하고 모든 관련 데이터를 유지:

`jpegoptim {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`

- JPEG 이미지 최적화, 모든 비필수 데이터를 제거:

`jpegoptim --strip-all {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`

- 출력 이미지를 프로그레시브 형식으로 강제 변환:

`jpegoptim --all-progressive {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`

- 출력 이미지의 최대 파일 크기를 고정된 크기로 설정:

`jpegoptim --size={{250k}} {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`
