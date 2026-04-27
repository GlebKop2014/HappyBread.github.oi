@echo off
set /p myVar="Enter commit comment: "
echo Hello, %myVar%!

git remote set-url origin https://github.com/GlebKop2014/HappyBread.github.oi.git

:: Основное добавление (убедитесь, что .gitignore уже лежит в корне)
git add .
git commit -m "%myVar%"

git push