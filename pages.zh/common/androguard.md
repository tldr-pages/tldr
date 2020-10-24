# androguard

> 使用python编写的一款针对安卓应用的逆向工程工具.
> 详见: <https://github.com/androguard/androguard>.

- 展示Android manifest清单文件:

`androguard axml {{path/to/app.apk}}`

- 展示app元数据 (版本和app ID):

`androguard apkid {{path/to/app.apk}}`

- 反编译Java代码:

`androguard decompile {{path/to/app.apk}} --output {{path/to/directory}}`
