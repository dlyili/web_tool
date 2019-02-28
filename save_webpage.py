#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import time
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from PIL import Image

DEFAULT_IMAGE_FORMAT = "PDF"
#DEFAULT_IMAGE_FORMAT = "JPEG"
DEFAULT_IMAGE_QUALITY = 80
TIME_TO_WAIT = 6


def save_webpage(url, file_name, simple, scroll_sleep_time=1.0, options=None, cookies=None, **image_options):
    """

    :param url: valid url
    :param file_name:
    :scroll_sleep_time scrool window sleep time
    :param options: browser options
    :param cookies: list of additional cookies
    :param image_options: keywords parameters to pillow save function
    :type url: str
    :type file_name: str
    :type scroll_sleep_time: float
    :type cookies: list
    :type image_options: dict
    :return: name of file
    """

    # necessary javascript
    device_pixel_ratio_js = "return window.devicePixelRatio"
    scroll_height_js = "return document.body.scrollHeight"
    inner_height_js = "return window.innerHeight"
    scroll_to_js = "window.scrollTo(0, {})"

    # define necessary image properties
    image_options["format"] = image_options.get("format") or DEFAULT_IMAGE_FORMAT
    image_options["quality"] = image_options.get("quality") or DEFAULT_IMAGE_QUALITY

    # if have browser options - just add it
    chrome_options = Options()
    if options:
        for option in options:
            chrome_options.add_argument(option)

    driver = webdriver.Chrome(
        options=chrome_options
    )

    driver.get(url)

    # set cookies
    if cookies:
        for cookie in cookies:
            driver.add_cookie(cookie)
        # we need to 'activate' cookies
        driver.refresh()
    
    driver.implicitly_wait(TIME_TO_WAIT)
     # hide scrollbar coz it's lame
    driver.execute_script("document.documentElement.style.overflow = 'hidden'")
    device_pixel_ratio = driver.execute_script(device_pixel_ratio_js)
    inner_height = driver.execute_script(inner_height_js)
    scroll_height = driver.execute_script(scroll_height_js)
    actual_page_size = scroll_height*device_pixel_ratio

    slices = []

    for offset in range(0, scroll_height+1, inner_height):
        driver.execute_script(scroll_to_js.format(offset))
        # sleep a while, maybe browswer is download image and render it
        time.sleep(scroll_sleep_time)
        img = Image.open(BytesIO(driver.get_screenshot_as_png()))
        slices.append(img)

    # create image
    screenshot = Image.new('RGB', (slices[0].size[0], int(actual_page_size)))

    if simple or len(slices) == 1 or scroll_height % inner_height == 0:
        for i, img in enumerate(slices):
            screenshot.paste(img, (0, int(i * inner_height * device_pixel_ratio)))
    else:
        for i, img in enumerate(slices[:-1]):
            screenshot.paste(img, (0, int(i * inner_height * device_pixel_ratio)))
        else:
            screenshot.paste(slices[-1], (0, int((scroll_height - inner_height) * device_pixel_ratio)))
        
    screenshot.save(file_name, **image_options)
    driver.quit()

    return file_name

def main():
    kwargs = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help = "save output to file", default="output")
    parser.add_argument('-f', '--format', help = "output file format", default="jpeg")
    parser.add_argument('--simple', action = 'store_true', help = "simple save")
    parser.add_argument("url", help = "the website to store")
    args = parser.parse_args()
    file_path = args.output + "." + args.format
    image_options = {"format": args.format}

    save_webpage(args.url, file_path, args.simple, **image_options)

if __name__ == '__main__':
    main()