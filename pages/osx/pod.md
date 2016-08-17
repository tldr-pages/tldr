# pod

> Dependency manager for Swift and Objective-C Cocoa projects.

- Create a Podfile for the current project with the default contents:

`pod init`

- Download all pod defined in Podfile and create an Xcode Pods library project in `./Pods`:

`pod install`

- Download a new pod for the current project and add it to the Podfile:

`pod install {{pod_name}}`

- Show the outdated pods in the current `Podfile.lock`:

`pod outdated`

- Update all pods in the current project to their newest version:

`pod update`

- Update a specific pod in the current project to their newest version:

`pod update {{pod_name}}`

- Remove CocoaPods from a Xcode project:

`pod deintegrate {{xcode_project}}`
