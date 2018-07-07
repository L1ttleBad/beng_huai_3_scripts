newproject beng_huai_3_scripts added by my git api

包安装
PIL直接通过anaconda安装即可
pytesseract需先安装orc模块(https://github.com/UB-Mannheim/tesseract/wiki)，然后pip install pytesseract
即可。import时如出现valueerror，Python27\Lib\site-packages\pytesseract\pytesseract.py文件，将
try:
    import Image
改为：
try:
    from PIL import Image
即可