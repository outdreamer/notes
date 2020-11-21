Config Guide

File extensions

  No extension - an executable with its extension hidden, or a binary
  .sh - this is a Unix shell executable meant to be run from the command line
  .bat - this is a Windows shell executable
  .json - JSON is a data structure where you can specify multiple levels & groups of key -> value pairs; JSON files are used to store small amounts of data, such as lists of states, lists of packages to install, or other configuration settings

Continuous Integration

  Travis is a tool that executes the build steps specified in the .travis.yml config whenever someone pushes changes to the repo. This can include setting variables, installing software, running scripts, and other deployment metadata

  .travis.yml
  https://docs.travis-ci.com/user/customizing-the-build

  Circle is a tool similar to Travis that can run deployment steps according to your circle.yml config:

  circle.yml
  https://circleci.com/docs/config-sample/

  Jenkins is a service that does this, but you can also use .jervis.yml config to execute jobs in Jenkins like Travis & Circle do in a yml config file.
  https://github.com/samrocketman/jervis/wiki/Build-overview

  Comparison between Jenkins, Travis CI, and Circle CI:
  https://stackshare.io/stackups/travis-ci-vs-circleci-vs-jenkins

Grunt/Gulp

  Grunt and Gulp are tools that run tasks for you. Those tasks may remind you of Travis/Jenkins jobs, although T & J are used to tune your OS environment so it's ready to deliver a web site, and Grunt/Gulp are usually used for lower-order development tasks within a project (tasks such as compiling CSS files into a single file, or minimizing a file to remove unnecessary characters so it's smaller, or reloading the browser when a file is saved, or using a preprocessor like Compass to compile to CSS).

  The T/J continuous integration tools may involve running a Grunt or Gulp task such as compiling CSS.

  Any files that begin with grunt.* involve grunt specifications:
  http://gruntjs.com/api/grunt.config

  Gruntfile.js is where you'll find any runnable tasks registered as well as the path to the Grunt config.

  Same for gulp.* -
  https://github.com/gulpjs/gulp/blob/master/docs/API.md

Bower

  .bowerrc

    Bower is a tool to manage packages of front-end assets - so it's known as a web package manager.
    You add the packages you need in bower.json after installing the npm bower module, and then run the command 'bower install' to install new resources, or 'bower update' to update with changes.

    Configuration Docs
    https://bower.io/docs/config/

NPM

  package.json

    This is used to store lists of npm modules to install as well as options related to those modules, plus any related scripts & metadata of the npm environment.

    Docs for installing npm packages:
    https://docs.npmjs.com/cli/install

  .npmignore
    Similar to .gitignore to specify unnecessary packages but specific to npm

Version Control config (git-specific)

  .gitattributes

    This specifies file conventions to follow for files added to the git repository.

    Samples
    https://github.com/alexkaratarakis/gitattributes

  .gitignore

    Used to prevent certain files, directories, or filesystem patterns from being added to the git repository. This is helpful when you have large, local-specific, or otherwise unnecessary files (such as dependency libraries or sql code) that you don't want added to your repository because either your build script already installs these packages on your remote environments, or you maintain your remote environments so that this software is already installed independently of your project, so you don't have to store those large files in your repository.

    Samples here:
    https://github.com/github/gitignore

  ~/.gitconfig

    This is a global version of the repository configuration in your <project_root>/.git/config used to store the same settings.
    https://git-scm.com/docs/git-config

Web site config

  Apache

    .htaccess
      provides project-specific directions for Apache on how to serve the website. There are so many options for this that .htaccess may as well be its own language or dialect. You might only modify .htaccess beyond the defaults to tune performance by implementing custom php settings in .htaccess. Otherwise its configuration options can be set in the original Apache configuration files rather than .htaccess, which usually goes in your project root, unless you implement folder-specific settings in a descendant directory of your project root.

    Here's a good overview if you need to search for options quickly though it's important to check that this is up-to-date by referencing the official docs:
    http://www.askapache.com/htaccess/

    Docs
    http://httpd.apache.org/docs/2.0/howto/htaccess.html

  robots.txt

    This file tells bots what it can do on your site, so it goes in your project root.
    http://www.robotstxt.org/robotstxt.html

  IIS

    web.config
      specifies project-specific directions for IIS. Instructions include imperatives like access rules & default endpoints (such as index.php for a PHP application) that should be followed for requests to the site.

Coding Standards & Testing

  .babelrc

    Babel is a tool to compile javascript - people use it frequently to make sure any fancy new ES6 code (thats javascript version 6) gets converted to ES5 code so that any browser can run your code, even if that browser version doesnt support ES6 yet.

    To implement Babel, you would include the Babel libraries & environment settings in your .babelrc or package.json file, and run 'npm install' when developing (and put that command in your Travis or Jenkins build script)

    Babel RC configuration:
    http://babeljs.io/docs/usage/babelrc/

    Sample environment settings:
    http://babeljs.io/docs/plugins/preset-env/

  .csslintrc

    .csslintrc is for specifying which css standards you want to use, example config here:
    https://github.com/ebednarz/csslintrc/blob/master/.csslintrc

    IDE's that have csslint plugins:
    https://github.com/CSSLint/csslint/wiki/IDE-integration

    If you don't want to use an IDE, you can check your css by running the csslint command, once the csslint npm module is installed.

    Commands
    https://github.com/CSSLint/csslint/wiki/Command-line-interface

  .editorconfig
    This will tell your IDE (Sublime, JetBeans, PHPStorm, etc) what your format preferences are.
    http://docs.editorconfig.org/en/master/editorconfig-format.html#format

  .eslintrc (new version of .jshintrc)

    Similar to .csslintrc, this is a file for storing your javascript standards preferences. You can use a .eslintrc file or store your javascript coding standards in your package.json, with the eslintConfig key, once you've installed the eslint npm module.

    Full guide
    http://eslint.org/docs/user-guide/configuring

    Commands
    http://eslint.org/docs/user-guide/command-line-interface

    You can also use .eslintignore to specify certain files & directories or file system patterns to ignore when checking the javascript by command line or IDE.

  Type Checking

    .flowconfig

      Flow is a npm module that lets you type-check your javascript:
      https://flowtype.org/docs/getting-started.html#_

      You can store your Flow settings in a package.json element or .flowconfig and then include the following at the top of your javascript file, and integrates with babel -
      // @flow

      So once you have the npm Flow module installed, you can run the flow command and it'll notify you of any type errors in your annotation js code:
      https://flowtype.org/docs/cli.html#_

  Javascript Testing

    jest-preset.json

    Jest is a tool for testing your javascript, created by Facebook:
    https://facebook.github.io/jest/docs/configuration.html

SASS

  config.rb
    This is where you tell your preprocessor (we usually use Compass) where to find the SASS files to compile and where to put the outputted CSS file
    https://gist.github.com/nathansmith/1179395

  With Ruby, packages are called gems (other terms you might be more familiar with are packages, modules, plugins, tools, libraries, or dependencies). The Ruby dependency management gem, called bundler, lets you store a list of gems needed for your application in the configuration file called Gemfile; when you've installed the packages, bundler stores the list of installed Gem packages in Gemfile.lock

    Gemfile
    Gemfile.lock

  Bundler (Ruby dependency management tool)
  http://bundler.io/

  After the bundler gem is installed, you can use it to generate your Gemfile.lock file with the command 'bundle install'.

PHP Projects

  Dependency Management

    You can tell the Composer tool what PHP packages to install in composer.json, and when it installs those packages, it creates a log of what it installed in composer.lock. You need to have composer installed on your system in order to use composer to manage your PHP packages.

    Quick reference for Composer:
    http://composer.json.jolicode.com/

    composer.json
    composer.lock

Legal & Notes

  LICENSE - legal status of project, whether it can be re-used by other people without asking permission or is intended for educational purposes only or some similar stipulation.
  PATENTS - patents related to project.
  README.md - introductory notes that help developers understand the project purpose, installation, and usage.
  Releases.md - changes included with each new release of the project.
  AUTHORS - lists authors of application

OS User Config:

  http://www.joshstaiger.org/archives/2005/07/bash_profile_vs.html

  .bashrc and .bash_profile are both used to set variables & run commands - .bash_profile is only used when you login to the shell, except on a Mac, which uses the .bash_profile config on opening the Terminal app.

  .bashrc
  .bash_profile

iOS app

  *.podspec (relevant to iOS apps)

    specifies metadata about a Cocoa pod being used in your iOS app project, normally built with XCode
    https://guides.cocoapods.org/syntax/podspec.html

  *.plist

    List of properties for iOS apps
    https://www.icanlocalize.com/site/tutorials/how-to-translate-plist-files/

  Cartfile

    Carthage is a dependency manager for iOS:
    https://github.com/Carthage/Carthage

    And if you use it you can specify frameworks to include in your project in a Cartfile:
    https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile

Android app

  Gradle

    You use Gradle to build C++/Java projects

    Intro to build.gradle:
    https://developer.android.com/studio/build/dependencies.html

    Sample app with Gradle configuration:
    https://github.com/codepath/intro_android_demo

    Files with *.gradle or gradlew.* (gradle wrapper) are relevant to this tool's configuration:
      gradlew - gradle wrapper
      gradlew.bat
      build.gradle
      react.gradle
      settings.gradle

  Building Executables

    Make and Buck are examples of build automation tools that developers use to build their executables from source. They might remind you of Travis CI or Circle CI continuous integration tools, or Grunt/Gulp task-running tools, in that they allow configuration of a series of steps, and simplify the process of running those steps. What's different about Make and Buck is that they're used to build executables written in C/C++ or Java.

    Make Intro
    https://robots.thoughtbot.com/the-magic-behind-configure-make-make-install

    Make Samples
    https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html

    Buck Docs
    https://buckbuild.com/concept/buckconfig.html

  Properties

    *.properties

      This is a file used primarily in Java apps to store lists of properties:
      https://en.wikipedia.org/wiki/.properties

      Sample
      http://crunchify.com/java-properties-file-how-to-read-config-properties-values-in-java/

      Docs
      https://docs.oracle.com/javase/tutorial/essential/environment/properties.html

Glossary

  Acronyms

    CLI (also referred to as the terminal or shell) - a program that allows you to run commands and view output in a limited range of display options (unstyled text), as opposed to an application or browser that responds to user application/browser events and allows you to view output in a variety of user-friendly highly functional styled options (images, videos, editable styled documents, etc). We use the terminal to edit configuration or variables, check processes that are running, find things quickly, test web requests, run commands (like for importing a database) or scripts, and install/uninstall software.
