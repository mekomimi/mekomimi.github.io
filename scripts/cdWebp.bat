@echo off
setlocal enabledelayedexpansion

:: 定义要处理的目录
set "directory=C:\Users\MI\Desktop\mekomimi.github.io"

:: 遍历目录下所有 .md 文件
for %%f in ("%directory%\*.md") do (
    :: 读取文件内容
    for /f "delims=" %%l in ('type "%%f"') do (
        set "line=%%l"
        set "line=!line:.jpg=.webp!"
        set "line=!line:.png=.webp!"
        echo !line! >> "%%f.temp"
    )
    :: 替换原文件
    move /y "%%f.temp" "%%f" >nul
)

echo 所有 .md 文件中的图片引用已替换为 .webp 格式！
pause
