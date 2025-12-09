# mvn

> Apache Maven：Java ベースのプロジェクトをビルドおよび管理します。
> もっと詳しく: <https://manned.org/mvn>。

- プロジェクトをコンパイルする:

`mvn compile`

- コンパイルしたコードを `jar` のような配布可能な形式でパッケージ化:

`mvn package`

- ユニットテストをスキップしてコンパイルし、パッケージ化:

`mvn package -DskipTests`

- ビルドしたパッケージをローカルの maven リポジトリにインストール (コンパイルとパッケージのコマンドも呼び出される):

`mvn install`

- ターゲットディレクトリから、ビルドアーティファクトを削除:

`mvn clean`

- clean にしてから package フェーズを起動:

`mvn clean package`

- 指定されたビルドプロファイルを使用して、コードをクリーンアップしてパッケージ化:

`mvn clean -P {{プロファイル}} package`

- main メソッドを持つクラスを実行:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{引数1 引数2 ...}}"`
