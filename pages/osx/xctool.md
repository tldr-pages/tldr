# XCTool

> Tool for build Xcode projects

- Build a project that is part of a workspace

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} build`

- Build a single project without any workspace

`xctool.sh -project {{YourProject.xcodeproj}} -scheme {{YourScheme}} build`

- Clean, build and execute all the tests

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} clean build test`
