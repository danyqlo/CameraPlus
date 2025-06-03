[app]
title = CameraPlus
package.name = cameraplus
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1
requirements = python3,kivy,opencv-python
orientation = portrait
fullscreen = 1
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 24

[buildozer]
log_level = 2
warn_on_root = 1
