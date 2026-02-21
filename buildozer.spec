[app]
title = Brain Games
package.name = braingames
package.domain = org.logicpuzzles
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0

# المتطلبات الأساسية
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow

orientation = portrait

# اجعل fullscreen تساوي 0 وقم بالتعليق (#) على سطر window إذا وجد
fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True
android.enable_androidx = True

[buildozer]
log_level = 2
