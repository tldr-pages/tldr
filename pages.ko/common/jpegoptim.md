# jpegoptim

> JPEG 이미지 최적화 도구.
> 더 많은 정보: <https://manned.org/jpegoptim>.

- 모든 관련 데이터를 유지하며 JPEG 이미지 집합 최적화:

`jpegoptim {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`

- 모든 비필수 데이터를 제거하며 JPEG 이미지 최적화:

`jpegoptim --strip-all {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`

- 출력 이미지를 프로그레시브 형식으로 강제 변환:

`jpegoptim --all-progressive {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`

- 출력 이미지의 최대 파일 크기를 고정:

`jpegoptim --size={{250k}} {{이미지1.jpeg}} {{이미지2.jpeg}} {{이미지N.jpeg}}`
