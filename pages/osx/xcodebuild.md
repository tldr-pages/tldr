# xcodebuild

> Build Xcode projects.

- Build workspace (CocoaPods Generate Project):

`xcodebuild -workspace {{YourWorkspace.workspace}} -scheme {{SchemeName}} -configuration {{YourConfiguration}} clean build SYMROOT={{YourSYMROOTPath}}`

- Build project:

`xcodebuild -target {{targetname}} -configuration {{YourConfiguration}} clean build SYMROOT={{YourSYMROOTPath}}`

- Show SDKs:

`xcodebuild -showsdks`
