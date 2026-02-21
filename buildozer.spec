[app]
# (str) Title of your application
title = Brain Games

# (str) Package name
package.name = braingames

# (str) Package domain (needed for android packaging)
package.domain = org.logicpuzzles

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Added pillow and sdl2_ttf for stability
requirements = python3,kivy==2.3.0,kivymd==1.1.1,sdl2_ttf==2.0.15,pillow

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Skip byte compile for .py files
android.skip_byte_compile = False

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1
