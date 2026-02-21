[app]
title = Brain Games Elite
package.name = braingameselite
package.domain = org.braingames
source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow

fullscreen = 1
orientation = portrait

android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

p4a.branch = master

[buildozer]
log_level = 2
