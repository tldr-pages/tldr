# terraform fmt

> Format configuration according to Terraform language style conventions.
> More information: <https://www.terraform.io/docs/commands/fmt.html>.

- Format the configuration in the current directory:

`terraform fmt`

- Format the configuration in the current directory and subdirectories:

`terraform fmt -recursive`

- Display diffs of formatting changes:

`terraform fmt -diff`

- Do not list files that were formatted to stdout:

`terraform fmt -list=false`

Android Developers


Bas Za
DOCUMENTATION

Android Developers
Android Developers
Docs
Guides
Was this helpful?

Get started with the Navigation component 


This topic shows you how to set up and work with the Navigation component. For a high level overview of the Navigation component, see the Navigation overview.


Set up your environment
Note: The Navigation component requires Android Studio 3.3 or higher and is dependent on Java 8 language features.
To include Navigation support in your project, add the following dependencies to your app's build.gradle file:

Groovy
Kotlin
dependencies {
  def nav_version = "2.3.5"

  // Java language implementation
  implementation "androidx.navigation:navigation-fragment:$nav_version"
  implementation "androidx.navigation:navigation-ui:$nav_version"

  // Kotlin
  implementation "androidx.navigation:navigation-fragment-ktx:$nav_version"
  implementation "androidx.navigation:navigation-ui-ktx:$nav_version"

  // Feature module Support
  implementation "androidx.navigation:navigation-dynamic-features-fragment:$nav_version"

  // Testing Navigation
  androidTestImplementation "androidx.navigation:navigation-testing:$nav_version"

  // Jetpack Compose Integration
  implementation "androidx.navigation:navigation-compose:"
}
For information on adding other Architecture Components to your project, see Adding components to your project.

Create a navigation graph
Navigation occurs between your app's destinations—that is, anywhere in your app to which users can navigate. These destinations are connected via actions.

A navigation graph is a resource file that contains all of your destinations and actions. The graph represents all of your app's navigation paths.

Figure 1 shows a visual representation of a navigation graph for a sample app containing six destinations connected by five actions. Each destination is represented by a preview thumbnail, and connecting actions are represented by arrows that show how users can navigate from one destination to another.


Figure 1. A navigation graph that shows previews of six different destinations that are connected via five actions.
Destinations are the different content areas in your app.
Actions are logical connections between your destinations that represent paths that users can take.
To add a navigation graph to your project, do the following:

In the Project window, right-click on the res directory and select New > Android Resource File. The New Resource File dialog appears.
Type a name in the File name field, such as "nav_graph".
Select Navigation from the Resource type drop-down list, and then click OK.
When you add your first navigation graph, Android Studio creates a navigation resource directory within the res directory. This directory contains your navigation graph resource file (nav_graph.xml, for example).

Note: When adding a navigation graph to your project, if you haven't already added navigation dependencies to your app's build.gradle file, Android Studio displays a prompt and offers to add the dependencies for you. Note, however, that Android Studio 3.4 adds the non-KTX 1.0.0 versions of the dependencies, so be sure to replace these values if you are using Kotlin or intend to use version 2.0.0 or higher.
Navigation Editor
After adding a graph, Android Studio opens the graph in the Navigation Editor. In the Navigation Editor, you can visually edit navigation graphs or directly edit the underlying XML.


Figure 2. The Navigation Editor
Destinations panel: Lists your navigation host and all destinations currently in the Graph Editor.
Graph Editor: Contains a visual representation of your navigation graph. You can switch between Design view and the underlying XML representation in the Text view.
Attributes: Shows attributes for the currently-selected item in the navigation graph.
Click the Text tab to see the corresponding XML, which should look similar to the following snippet:

<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:app="http://schemas.android.com/apk/res-auto"
            android:id="@+id/nav_graph">

</navigation>
The <navigation> element is the root element of a navigation graph. As you add destinations and connecting actions to your graph, you can see the corresponding <destination> and <action> elements here as child elements. If you have nested graphs, they appear as child <navigation> elements.

Add a NavHost to an activity
One of the core parts of the Navigation component is the navigation host. The navigation host is an empty container where destinations are swapped in and out as a user navigates through your app.

A navigation host must derive from NavHost. The Navigation component's default NavHost implementation, NavHostFragment, handles swapping fragment destinations.

Note: The Navigation component is designed for apps that have one main activity with multiple fragment destinations. The main activity is associated with a navigation graph and contains a NavHostFragment that is responsible for swapping destinations as needed. In an app with multiple activity destinations, each activity has its own navigation graph.
Add a NavHostFragment via XML
The XML example below shows a NavHostFragment as part of an app's main activity:

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <androidx.appcompat.widget.Toolbar
        .../>

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/nav_host_fragment"
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"

        app:defaultNavHost="true"
        app:navGraph="@navigation/nav_graph" />

    <com.google.android.material.bottomnavigation.BottomNavigationView
        .../>

</androidx.constraintlayout.widget.ConstraintLayout>
Note the following:

The android:name attribute contains the class name of your NavHost implementation.
The app:navGraph attribute associates the NavHostFragment with a navigation graph. The navigation graph specifies all of the destinations in this NavHostFragment to which users can navigate.
The app:defaultNavHost="true" attribute ensures that your NavHostFragment intercepts the system Back button. Note that only one NavHost can be the default. If you have multiple hosts in the same layout (two-pane layouts, for example), be sure to specify only one default NavHost.
You can also use the Layout Editor to add a NavHostFragment to an activity by doing the following:

In your list of project files, double-click on your activity's layout XML file to open it in the Layout Editor.
Within the Palette pane, choose the Containers category, or alternatively search for "NavHostFragment".
Drag the NavHostFragment view onto your activity.
Next, in the Navigation Graphs dialog that appears, choose the corresponding navigation graph to associate with this NavHostFragment, and then click OK.
Add destinations to the navigation graph
You can create a destination from an existing fragment or activity. You can also use the Navigation Editor to create a new destination or create a placeholder to later replace with a fragment or activity.

In this example, let's create a new destination. To add a new destination using the Navigation Editor, do the following:

In the Navigation Editor, click the New Destination icon , and then click Create new destination.
In the New Android Component dialog that appears, create your fragment. For more information on fragments, see the fragment documentation.
Back in the Navigation Editor, notice that Android Studio has added this destination to the graph.

Figure 3 shows an example of a destination and a placeholder destination.


Figure 3. A destination and a placeholder
For other ways to add destinations to your navigation graph, see Create destinations.

Anatomy of a destination
Click on a destination to select it, and note the following attributes in the Attributes panel:

The Type field indicates whether the destination is implemented as a fragment, activity, or other custom class in your source code.
The Label field contains the user-readable name of the destination. This might be surfaced to the UI—for example, if you connect the NavGraph to a Toolbar using setupWithNavController(). For this reason, it is recommended that you use resource strings for this value.
The ID field contains the ID of the destination which is used to refer to the destination in code.
The Class dropdown shows the name of the class that is associated with the destination. You can click this dropdown to change the associated class to another destination type.
Click the Text tab to show the XML view of your navigation graph. The XML contains the same id, name, label, and layout attributes for the destination, as shown below:


<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    xmlns:android="http://schemas.android.com/apk/res/android"
    app:startDestination="@id/blankFragment">
    <fragment
        android:id="@+id/blankFragment"
        android:name="com.example.cashdog.cashdog.BlankFragment"
        android:label="@string/label_blank"
        tools:layout="@layout/fragment_blank" />
</navigation>
Designate a screen as the start destination
The start destination is the first screen users see when opening your app, and it's the last screen users see when exiting your app. The Navigation editor uses a house icon  to indicate the start destination.

Once you have all of your destinations in place, you can choose a start destination by doing the following:

In the Design tab, click on the destination to highlight it.

Click the Assign start destination button . Alternatively, you can right-click on the destination and click Set as Start Destination.

Connect destinations
An action is a logical connection between destinations. Actions are represented in the navigation graph as arrows. Actions usually connect one destination to another, though you can also create global actions that take you to a specific destination from anywhere in your app.

With actions, you're representing the different paths that users can take through your app. Note that to actually navigate to destinations, you still need to write the code to perform the navigation. This is covered in the Navigate to a destination section later in this topic.

You can use the Navigation Editor to connect two destinations by doing the following:

In the Design tab, hover over the right side of the destination that you want users to navigate from. A circle appears over the right side of the destination, as shown in figure 4.


Figure 4. A destination with an action connection circle
Click and drag your cursor over the destination you want users to navigate to, and release. The resulting line between the two destinations represents an action, as shown in figure 5.


Figure 5. Connecting destinations with an action
Click on the arrow to highlight the action. The following attributes appear in the Attributes panel:

The Type field contains “Action”.
The ID field contains the ID for the action.
The Destination field contains the ID for the destination fragment or activity.
Click the Text tab to toggle to the XML view. An action element is now added to the source destination. The action has an ID and a destination attribute that contains the ID of the next destination, as shown in the example below:

<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    xmlns:android="http://schemas.android.com/apk/res/android"
    app:startDestination="@id/blankFragment">
    <fragment
        android:id="@+id/blankFragment"
        android:name="com.example.cashdog.cashdog.BlankFragment"
        android:label="@string/label_blank"
        tools:layout="@layout/fragment_blank" >
        <action
            android:id="@+id/action_blankFragment_to_blankFragment2"
            app:destination="@id/blankFragment2" />
    </fragment>
    <fragment
        android:id="@+id/blankFragment2"
        android:name="com.example.cashdog.cashdog.BlankFragment2"
        android:label="@string/label_blank_2"
        tools:layout="@layout/fragment_blank_fragment2" />
</navigation>
In your navigation graph, actions are represented by <action> elements. At a minimum, an action contains its own ID and the ID of the destination to which a user should be taken.

Navigate to a destination
Navigating to a destination is done using a NavController, an object that manages app navigation within a NavHost. Each NavHost has its own corresponding NavController. You can retrieve a NavController by using one of the following methods:

Kotlin:

Fragment.findNavController()
View.findNavController()
Activity.findNavController(viewId: Int)
Java:

NavHostFragment.findNavController(Fragment)
Navigation.findNavController(Activity, @IdRes int viewId)
Navigation.findNavController(View)
When creating the NavHostFragment using FragmentContainerView or if manually adding the NavHostFragment to your activity via a FragmentTransaction, attempting to retrieve the NavController in onCreate() of an Activity via Navigation.findNavController(Activity, @IdRes int) will fail. You should retrieve the NavController directly from the NavHostFragment instead.

Kotlin
Java
NavHostFragment navHostFragment =
        (NavHostFragment) supportFragmentManager.findFragmentById(R.id.nav_host_fragment);
NavController navController = navHostFragment.getNavController();
Ensure type-safety by using Safe Args
The recommended way to navigate between destinations is to use the Safe Args Gradle plugin. This plugin generates simple object and builder classes that enable type-safe navigation and argument passing between destinations.

Note: For other ways to navigate, see Navigate to a destination.
To add Safe Args to your project, include the following classpath in your top level build.gradle file:

Groovy
Kotlin
buildscript {
    repositories {
        google()
    }
    dependencies {
        def nav_version = "2.3.5"
        classpath "androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version"
    }
}
You must also apply one of two available plugins.

To generate Java language code suitable for Java or mixed Java and Kotlin modules, add this line to your app or module's build.gradle file:

Groovy
Kotlin
plugins {
  id 'androidx.navigation.safeargs'
}
Alternatively, to generate Kotlin code suitable for Kotlin-only modules add:

Groovy
Kotlin
plugins {
  id 'androidx.navigation.safeargs.kotlin'
}
You must have android.useAndroidX=true in your gradle.properties file as per Migrating to AndroidX.

After you enable Safe Args, the plugin generates code that contains classes and methods for each action you've defined. For each action, Safe Args also generates a class for each originating destination, which is the destination from which the action originates. The generated class name is a combination of the originating destination class name and the word "Directions". For example, if the destination is named SpecifyAmountFragment, the generated class is named SpecifyAmountFragmentDirections. The generated class contains a static method for each action defined in the originating destination. This method takes any defined action parameters as arguments and returns a NavDirections object that you can pass to navigate().

As an example, assume we have a navigation graph with a single action that connects the originating destination, SpecifyAmountFragment, to a receiving destination, ConfirmationFragment.

Safe Args generates a SpecifyAmountFragmentDirections class with a single method, actionSpecifyAmountFragmentToConfirmationFragment() that returns a NavDirections object. This returned NavDirections object can then be passed directly to navigate(), as shown in the following example:

Kotlin
Java
@Override
public void onClick(View view) {
    NavDirections action =
        SpecifyAmountFragmentDirections
            .actionSpecifyAmountFragmentToConfirmationFragment();
    Navigation.findNavController(view).navigate(action);
}
For more information on passing data between destinations with Safe Args, see Use Safe Args to pass data with type safety.

More information
Navigation overview
Create destinations
Navigate to a destination
Update UI components with NavigationUI
Pass data between destinations
Global actions
Conditional destinations
Custom destination types
Android Jetpack: manage UI navigation with Navigation Controller (Google I/O 2018)
Migrate an existing project to the Navigation Architecture Component
Navigation Codelab
If you encounter any issues with Navigation, please submit feedback via one of the following channels:

File a Navigation editor bug
File a Navigation library bug
Tag an issue on StackOverflow
For information on how to provide the most helpful information in bug reports, see the following links:

Reporting Bugs (Android platform)
Report a bug (Android Studio)
Was this helpful?

Content and code samples on this page are subject to the licenses described in the Content License. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2021-12-15 UTC.

TwitterTwitter
YouTubeYouTube
MORE ANDROID
Android
Android for Enterprise
Security
Source
News
Blog
Podcasts
DISCOVER
Gaming
Machine Learning
Privacy
5G
ANDROID DEVICES
Large screens
Wear OS
Android TV
Android for cars
Android Things
Chrome OS devices
RELEASES
Android 11
Android 10
Pie
Oreo
Nougat
Marshmallow
Lollipop
KitKat
DOCUMENTATION AND DOWNLOADS
Android Studio guide
Developers guides
API reference
Download Studio
Android NDK
SUPPORT
Report platform bug
Report documentation bug
Google Play support
Join research studies
Google Developers
Android
Chrome
Firebase
Google Cloud Platform
All products
Privacy
License
Brand guidelines
Get news and tips by email
Subscribe
English
