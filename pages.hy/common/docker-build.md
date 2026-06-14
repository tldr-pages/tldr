# docker build

> Կառուցեք պատկեր Dockerfile-ից:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/buildx/build/>:.

- Ստեղծեք Docker պատկեր՝ օգտագործելով Dockerfile-ը ընթացիկ գրացուցակում.:

`docker build .`

- Ստեղծեք Docker պատկեր Dockerfile-ից՝ նշված URL-ով.:

`docker build {{github.com/creack/docker-firefox}}`

- Կառուցեք Docker պատկեր և նշեք այն.:

`docker build {{[-t|--tag]}} {{name:tag}} .`

- Կառուցեք Docker պատկեր առանց կառուցման համատեքստի.:

`docker < {{Dockerfile}} build {{[-t|--tag]}} {{name:tag}} -`

- Պատկերը կառուցելիս մի օգտագործեք քեշը.:

`docker build --no-cache {{[-t|--tag]}} {{name:tag}} .`

- Կառուցեք Docker պատկեր՝ օգտագործելով հատուկ Dockerfile.:

`docker build {{[-f|--file]}} {{Dockerfile}} .`

- Կառուցեք հատուկ կառուցման ժամանակի փոփոխականներով.:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
