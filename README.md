# deepl-scraper-playwright
[![pytest](https://github.com/ffreemt/deepl-scraper-playwright/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/deepl-scraper-playwright/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/deepl_scraper_pw.svg)](https://badge.fury.io/py/deepl_scraper_pw)

Scrape deepl using playwright

## Install it

```shell
pip install deepl-scraper-pw

# pip install git+https://github.com/ffreemt/deepl-scraper-playwright
# poetry add git+https://github.com/ffreemt/deepl-scraper-playwright
# git clone https://github.com/ffreemt/deepl-scraper-playwright && cd deepl-scraper-playwright
```

## Use it
```python
from pprint import pprint
from deepl_scraper_pw import deepl_tr

pprint(deepl_tr("Test me\n\nTest him"))
# '测试我\n\n测试他'

pprint(deepl_tr("Test me\n\nTest him", from_lang="en", to_lang="de"))
# 'Teste mich\n\nTesten Sie ihn'
```
## Debug
Should something go wrong, you can turn on HEADFUL (a firefox browser will show up). Place .env in the current work directory, with the following content:
```bash
PWBROWSER_HEADFUL=1
```

You can also set DEBUG env variable to turn on detailed debug messages, in Windows:
```
set DEBUG=1
```
In Linux and friends
```
export DEBUG=1
```