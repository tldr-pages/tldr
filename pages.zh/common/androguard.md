# androguard

> 使用python编写的一款针对安卓应用的逆向工程工具.
> 更多信息: <https://github.com/androguard/androguard>.

- 展示Android manifest清单文件:

`androguard axml {{路径/至/应用.apk}}`

- 展示app元数据 (版本和app ID):

`androguard apkid {{路径/至/应用.apk}}`

- 反编译Java代码:

`androguard decompile {{路径/至/应用.apk}} --output {{路径/至/目录}}`
