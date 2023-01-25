# -*- coding: utf-8 -*-

import json
import numpy as np
import os

path_prefix = (
    "C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\second-trial\\"
)


arr = os.listdir(
    "C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\second-trial"
)

for i in arr:
    path = path_prefix + i
    with open(path, "r", encoding="UTF8") as file:
        data = json.load(file)
        print(type(data))
        print(data)

    print(i, type(i))
