[app]
title = Brain Games
package.name = braingames
package.domain = org.logicpuzzles
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# تحديث الإصدارات لتدعم NDK 25b
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
