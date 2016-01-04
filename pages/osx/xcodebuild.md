# xcodebuild

> xcodebuild builds one or more targets contained in an Xcode project, or builds a scheme contained in an
     Xcode workspace or Xcode project.
     
### OS X

- The Mac OS X platform accepts an arch keyword, which can be either x86_64 or i386. x86_64 is the default.

```
xcodebuild \
  -workspace MyMacApp.xcworkspace \
  -scheme MyMacApp \
  -destination 'platform=OS X,arch=x86_64' \
  clean test
```

### iOS

- The iOS platform should be used when you want to run tests on a connected device. It supports two keys, id and name. Either one of the two must be provided, but not both.

```
xcodebuild \
  -workspace MyApp.xcworkspace \
  -scheme MyApp \
  -destination "platform=iOS,name=Gio's iPhone" \
  clean test
```

```
xcodebuild \
  -workspace MyApp.xcworkspace \
  -scheme MyApp \
  -destination 'platform=iOS,id=YOUR_PHONE_UUID' \
  clean test
```

### iOS Simulator

- iOS Simulator is the platform I use more often. It supports the same id and name mutually exclusive keys as iOS, plus an OS key. OS expects a target version number, like 9.1, or latest, which is the default.

```
xcodebuild \
  -workspace MyApp.xcworkspace \
  -scheme MyApp \
  -destination 'platform=iOS Simulator,name=iPhone 6,OS=9.1' \
  clean test
```

### watchOS and watchOS Simulator

```
xcodebuild \
  -workspace MyApp.xcworkspace \
  -scheme MyWatchKitApp
  -destination 'platform=iOS Simulator,name=iPhone 6,OS=9.1' \
  build
```
