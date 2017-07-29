from springboard_ocr import SpringboardOcr
import json

so = SpringboardOcr("test/")
so.process_all()
print(json.dumps(so.get_app_stats()))
