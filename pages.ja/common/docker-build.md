# docker build

> Dockerfileからイメージを構築します。
> もっと詳しく: <https://docs.docker.com/reference/cli/docker/buildx/build/>。

- カレントディレクトリ内のDockerfileを使ってDockerイメージを構築する:

`docker build .`

- 指定URLにあるDockerfileからDockerイメージを構築する:

`docker build {{github.com/creack/docker-firefox}}`

- Dockerイメージを構築しそれにタグを付ける:

`docker build {{[-t|--tag]}} {{名前:タグ}} .`

- ビルドコンテキスト無しでDockerイメージを構築する:

`docker build {{[-t|--tag]}} {{名前:タグ}} - < {{Dockerfile}}`

- Dockerイメージ構築時にキャッシュを使わないようにする:

`docker build --no-cache {{[-t|--tag]}} {{名前:タグ}} .`

- 指定のDockerfileを用いてDockerイメージを構築する:

`docker build {{[-f|--file]}} {{Dockerfile}} .`

- ビルド時のカスタム変数を指定してイメージを構築する:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
