# fastlane

> 构建和发布移动应用程序。
> 更多信息：<https://docs.fastlane.tools/actions/>.

- 在当前目录中构建并签名 iOS 应用程序：

`fastlane run build_app`

- 为当前目录中的项目运行 `pod install`：

`fastlane run cocoapods`

- 从 Xcode 中删除派生数据：

`fastlane run clear_derived_data`

- 清除 pods 的缓存：

`fastlane run clean_cocoapods_cache`