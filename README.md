# Springboard OCR
Quick preprocessing of springboard screenshots to make OCR easy. Basically, the only novelty here is checking (or more accurately, guessing) whether the text will be black or white. A mask is made to try to get rid of the background colors, and then OCRed and results tallied. 

# Usage & Example
![img_4606](https://user-images.githubusercontent.com/7699842/28741061-61c35ea2-73c3-11e7-956c-7dbca18a995a.PNG  | width=200)
```
from springboard_ocr import SpringboardOcr
import json
so = SpringboardOcr()
so.process_image_file("test.png")
print(json.dumps(so.get_app_stats()))
```
returns
```
{
  "Mobile": 1,
  "BLAST": 1,
  "V'": 1,
  "Entertainment": 1,
  "Chrome": 1,
  "Duo": 1,
  "YouTube": 1,
  "Surfline": 1,
  "been": 1,
  "Netflix": 1,
  "h": 1,
  "News": 1,
  "NPR": 1,
  "OpenTable": 1,
  "OED": 1
}
```

# Getting Started
## Requirements
- Install by doing a ```brew install tesseract```, or follow [this guide](https://github.com/tesseract-ocr/tesseract) for directions on your system.

- Install python requirements by doing a ```pip install -r requirements.txt --user``` or however you wish manage your packages.
