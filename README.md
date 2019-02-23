# web tool
# 1.Save web page
Simple python function that let you save a whole web page using Selenium and Pillow libraries.
fork from https://github.com/netolyrg/save_webpage

## Description

This functions save pages to files (more than 30 formats available) and support cookies and browser options such as `--headless` and others.

I need this function for testing purposes, but I think it can be useful in another tasks.

It perfectly works in headless mode on macOS High Sierra 10.13 with Google Chrome 64.
And works with headless mode on Windows 10 with Google Chrome 64.

Please download chromedriver.exe from "https://chromedriver.storage.googleapis.com/index.html", and put it to python dir,
like:C:\Python\Python37\chromedriver.exe

Choose chromedriver version, see like this page:
http://chromedriver.storage.googleapis.com/2.40/notes.txt
https://chromedriver.storage.googleapis.com/index.html?path=2.40/

## Usage
examples:
$ webpage2html -s http://gabrielecirulli.github.io/2048/ > 2048.html

