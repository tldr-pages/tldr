# flutter

> Google's free, open source, and cross-platform mobile app SDK.
> More information: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Initialize a new Flutter project in a directory of the same name:

`flutter create {{project_name}}`

- Check if all external tools are correctly installed:

`flutter doctor`

- List or change Flutter channel:

`flutter channel {{stable|beta|dev|master}}`

- Run Flutter on all started emulators and connected devices:

`flutter run -d all`

- Download all packages specified in `pubspec.yaml`:

`flutter pub get`

- Run tests in a terminal from the root of the project:

`flutter test {{test/example_test.dart}}`

- Build a release APK targeting most modern smartphones:

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`

- Display help about a specific command:

`flutter help {{command}}`
