import os
import numpy as np
import cv2
#TODO: once pytesseract/#66 is merged, make this a normal import (using local custom version in meantime)
from pytesseract_custom.src import pytesseract

class SpringboardOcr():
    def __init__(self, directory_path=None):
        self.app_count = {}
        if directory_path and not os.path.isdir(directory_path):
            raise ValueError("Invalid input directory")
        self.directory_path = directory_path

    def process_all(self, directory_path=None):
        if directory_path:
            self.directory_path = directory_path

        if self.directory_path:
            for screenshot in os.listdir(self.directory_path):
                if screenshot.startswith('.'):
                    continue
                screenshot_path = os.path.join(self.directory_path, screenshot)
                self.process_image_file(screenshot_path)
        else:
            raise ValueError("No directory path set")

    def process_image_file(self, screenshot_path):
        screenshot_img = cv2.imread(screenshot_path)
        self.process_image_array(screenshot_img)

    def process_image_array(self, screenshot_img):
        if self._text_is_white(screenshot_img):
            mask = cv2.inRange(screenshot_img, (240,240,240), (255,255,255))
        else:
            mask = cv2.inRange(screenshot_img, (0,0,0), (15,15,15))
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        self.increment_app_name(pytesseract.image_to_string(mask))

    def increment_app_name(self, detected_text):
        all_apps = detected_text.split()
        for app_name in all_apps:
            if app_name not in self.app_count:
                self.app_count[app_name] = 0
            self.app_count[app_name] += 1
            
    def _text_is_white(self, screenshot):
        average_color_per_row = np.average(screenshot, axis=0)
        average_color = np.average(average_color_per_row, axis=0)
        average_total = np.average(average_color)
        return average_total > 100.0

    def get_app_stats(self):
        return self.app_count
