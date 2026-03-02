# mvn

> Apache Maven：Java ベースのプロジェクトをビルドおよび管理します。
> 詳細情報: <https://manned.org/mvn>。

- プロジェクトをコンパイルする:

`mvn compile`

- コンパイルしたコードを `jar` のような配布可能な形式でパッケージ化:

`mvn package`

- ユニットテストをスキップしてコンパイルし、パッケージ化:

`mvn package {{[-D|--define]}} skipTests`

- ビルドしたパッケージをローカルの maven リポジトリにインストール (コンパイルとパッケージのコマンドも呼び出される):

`mvn install`

- ターゲットディレクトリから、ビルドアーティファクトを削除:

`mvn clean`

- clean にしてから package フェーズを起動:

`mvn clean package`

- 指定されたビルドプロファイルを使用して、コードをクリーンアップしてパッケージ化:

`mvn clean {{[-P|--activate-profiles]}} {{プロファイル}} package`

- main メソッドを持つクラスを実行:

`mvn exec:java {{[-D|--define]}} exec.mainClass="{{com.example.Main}}" {{[-D|--define]}} exec.args="{{引数1 引数2 ...}}"`
