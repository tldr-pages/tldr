# xcodebuild

> xcodebuild is build xcode project and generate ipa for command line tools

- Build Workspace (ps: CocoaPods Generate Project)

`xcodebuild -workspace {{YourWorkspace.workspace}} -scheme {{SchemeName}} -configuration {{YourConfiguration}} clean build SYMROOT={{YourSYMROOTPath}}`

- Build Project

`xcodebuild -target {{targetname}} -configuration {{YourConfiguration}} clean build SYMROOT={{YourSYMROOTPath}}`

- View Sdks

`xcodebuild -showsdks`

- xcrun Generate ipa file 

`xcrun -sdk iphoneos PackageApplication -v {{projectName.app}} -o {{ipaName.ipa}}`
