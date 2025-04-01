# fastlane

> 构建和发布移动应用。
> 更多信息：<https://docs.fastlane.tools/actions/>.

- 构建并签名当前目录中的 iOS 应用：

`fastlane run build_app`

- 为当前目录中的项目运行 `pod install`：

`fastlane run cocoapods`

- 删除 Xcode 的派生数据：

`fastlane run clear_derived_data`

- 清除 pods 的缓存：

`fastlane run clean_cocoapods_cache`
