import re
import requests

html_contents = "cotb7*** abc**abc 12*** %***"#이런 내용
id_results = re.findall("([A-Za-z0-9]+\*\*\*)", html_contents)
#[] 해당내용 하나 이상
#\* = *

for result in id_results:
    print(result)