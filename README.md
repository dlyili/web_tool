# web tool
# 1.Save web page
Simple python function that let you save a whole web page using Selenium and Pillow libraries.
Fork from https://github.com/netolyrg/save_webpage

## Description
Please download chromedriver.exe from "https://chromedriver.storage.googleapis.com/index.html", and put it to python dir,
like:C:\Python\Python37\chromedriver.exe
ʵ�ַ�ʽ:����chromedriver����chrome�������������ַ����ȡ��ҳͼƬ������Ϊpdf����ͼƬ�ļ�

Choose chromedriver version, see like this page:
http://chromedriver.storage.googleapis.com/2.40/notes.txt
https://chromedriver.storage.googleapis.com/index.html?path=2.40/

## Usage
examples:
python save_webpage https://play2048.co/
python save_webpage https://play2048.co/ -f pdf -o test_2048 --simple
python save_webpage https://play2048.co/ -f jpg -o test_2048


