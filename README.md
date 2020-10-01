# web tool
# 1.Save web page
Simple python function that let you save a whole web page using Selenium and Pillow libraries.
Fork from https://github.com/netolyrg/save_webpage

## Description
Please download chromedriver.exe from "https://chromedriver.storage.googleapis.com/index.html", and put it to python dir,
like:C:\Python\Python37\chromedriver.exe
实现方式:利用chromedriver，打开chrome浏览器，访问网址并截取网页图片，保存为pdf或者图片文件

Choose chromedriver version, see like this page:
http://chromedriver.storage.googleapis.com/2.40/notes.txt
https://chromedriver.storage.googleapis.com/index.html?path=2.40/

## Usage
examples:
python save_webpage https://play2048.co/
python save_webpage https://play2048.co/ -f pdf -o test_2048 --simple
python save_webpage https://play2048.co/ -f jpg -o test_2048


