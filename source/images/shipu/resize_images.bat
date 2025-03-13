@echo off
title 图片大小调整工具 - 2544x3464
color 0A

echo ======================================
echo    图片大小调整工具 - 2544x3464
echo ======================================
echo.
echo 正在调整图片大小为 2544x3464...
echo 请稍候，这可能需要几分钟时间...
echo.

:: 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo 错误: 未检测到Python安装。
    echo 请安装Python并确保它已添加到PATH环境变量中。
    echo.
    echo 按任意键退出...
    pause >nul
    exit /b 1
)

:: 检查Pillow库是否安装
python -c "from PIL import Image" >nul 2>&1
if %errorlevel% neq 0 (
    color 0E
    echo 警告: 未检测到Pillow库。
    echo 正在尝试安装Pillow库...
    pip install pillow
    if %errorlevel% neq 0 (
        color 0C
        echo 错误: 安装Pillow库失败。
        echo 请手动运行: pip install pillow
        echo.
        echo 按任意键退出...
        pause >nul
        exit /b 1
    )
    echo Pillow库安装成功！
    echo.
)

:: 运行Python脚本
python "%~dp0resize_images_replace.py"
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo 错误: 脚本执行失败。
    echo.
    echo 按任意键退出...
    pause >nul
    exit /b 1
)

color 0A
echo.
echo ======================================
echo    处理完成！
echo ======================================
echo.
echo 按任意键退出...
pause >nul 