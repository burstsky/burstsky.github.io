@echo off
setlocal enabledelayedexpansion

:: 创建备份目录
if not exist backup mkdir backup

:: 复制所有文件到备份目录
copy IMG_*.jpg backup\

:: 设置计数器
set count=1

:: 按名称排序并重命名文件
for /f "tokens=*" %%a in ('dir /b /on IMG_*.jpg') do (
    echo 重命名 %%a 为 !count!.jpg
    ren "%%a" "!count!.jpg"
    set /a count+=1
)

echo 重命名完成！共处理了 %count% 个文件。 