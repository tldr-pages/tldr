# docker build

> 도커파일로부터 이미지 빌드.
> 더 많은 정보: <https://docs.docker.com/engine/reference/commandline/build/>.

- 현재 디렉토리 안의 도커파일을 이용해 도커 이미지 빌드:

`docker build .`

- 명시된 URL의 도커파일로부터 도커 이미지 빌드:

`docker build {{github.com/creack/docker-firefox}}`

- 도커 이미지 빌드 및 태그 추가:

`docker build --tag {{이름:태그}} .`

- 빌드 컨텍스트 없이 도커 이미지 빌드:

`docker build --tag {{이름:태그}} - < {{도커파일}}`

- 캐시를 사용하지 않고 도커 이미지 빌드:

`docker build --no-cache --tag {{이름:태그}} .`

- 특정 도커파일을 이용하여 도커 이미지 빌드:

`docker build --file {{도커파일}} .`

- 빌드 시 커스텀 변수 추가:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
