from springboard_ocr import SpringboardOcr
import json

so = SpringboardOcr()
so.process_all("test/")
print(json.dumps(so.get_app_stats()))
