# -*- coding: utf-8 -*-

import json

file_path = "C:/Users/IBK/Desktop/나만의-우테코/kakaomap-data-scrap/reviewdata/second-trial/output-final-호남순대국-2039472007"

with open(file_path, "r", encoding="UTF8") as file:
    data = json.load(file)
    print(type(data))
    print(data)
