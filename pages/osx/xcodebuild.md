# xcodebuild

> xcodebuild is build xcode project and generate ipa for command line tools

- Build Workspace (ps: CocoaPods Generate Project)

`xcodebuild -workspace workspacename -scheme schemename -configuration [-configuration configurationname] clean build SYMROOT=(SYMROOT)`

- Build Project

`xcodebuild -target targetname -configuration [-configuration configurationname] clean build SYMROOT=(SYMROOT)`

- View Sdks

`xcodebuild -showsdks`

- xcrun Generate ipa file 

`xcrun -sdk iphoneos PackageApplication -v projectName.app -o ipaName.ipa`
