"""Scrape deepl via playwright (get_pwbrowser_sync).

org deepl_tr_pp

import os
from pathlib import Path
os.environ['PYTHONPATH'] = Path(r"../get-pwbrowser-sync")
"""
import sys
from time import sleep
from typing import Union
from urllib.parse import quote

import logzero
from about_time import about_time
from get_pwbrowser_sync import get_pwbrowser_sync as get_pwbrowser, loop
from logzero import logger
from pyquery import PyQuery as pq

URL = r"https://www.deepl.com/translator"


def deepl_tr(
    text: str,
    from_lang: str = "auto",
    to_lang: str = "zh",
    page=None,
    verbose: Union[bool, int] = False,
    timeout: float = 5,
):
    """Deepl via playwright-sync.

    text = "Test it and\n\n more"
    from_lang="auto"
    page=None
    to_lang="zh"
    verbose=True
    """
    #

    # set verbose=40 to turn most things off
    if isinstance(verbose, bool):
        if verbose:
            logzero.setup_default_logger(level=10)
        else:
            logzero.setup_default_logger(level=20)
    else:  # integer: log_level
        logzero.setup_default_logger(level=verbose)

    logger.debug(" Entry ")

    # reuse page
    try:
        deepl_tr.page  # run previsously
        page = deepl_tr.page
    except AttributeError:
        if page is None:
            try:
                browser = get_pwbrowser()
            except Exception as exc:
                logger.error(exc)
                raise

            try:
                page = browser.new_page()
            except Exception as exc:
                logger.error(exc)
                raise

            url = r"https://www.deepl.com/translator"
            try:
                page.goto(url, timeout=45 * 1000)
            except Exception as exc:
                logger.error(exc)
                raise

            deelp.page = page
        else:
            deelp_tr.page = page

    page = deepl_tr.page

    url0 = f"{URL}#{from_lang}/{to_lang}/"

    url_ = f"{URL}#{from_lang}/{to_lang}/{quote(text)}"

    # selector = ".lmt__language_select--target > button > span"

    if verbose < 11 or verbose is True:
        _ = False  # silent
    else:
        _ = True

    # with CodeTimer(name="fetching", unit="s", silent=_):
    with about_time() as dur:
        try:
            content = page.content()
        except Exception as exc:
            logger.error(exc)
            raise

        doc = pq(content)
        text_old = doc("#source-dummydiv").html()
        logger.debug("Old source: %s", text_old)

        try:
            deepl_tr.first_run
        except AttributeError:
            deepl_tr.first_run = 1
            text_old = "_some unlikely random text_"

        # selector = "div.lmt__translations_as_text"
        if text.strip() == text_old.strip():
            logger.debug(" ** early result: ** ")
            logger.debug(
                "%s, %s", text, doc(".lmt__translations_as_text__text_btn").html()
            )
            doc = pq(page.content())
            # content = doc(".lmt__translations_as_text__text_btn").text()
            content = doc(".lmt__translations_as_text__text_btn").html()
        else:
            # record content
            try:
                # page.goto(url_)
                page.goto(url0)
            except Exception as exc:
                logger.error(exc)
                raise

            try:
                # page.wait_for_selector(".lmt__translations_as_text", timeout=20000)
                page.wait_for_selector(".lmt__target_textarea", timeout=20000)
            except Exception as exc:
                logger.error(exc)
                raise

            doc = pq(page.content())
            # content_old = doc(".lmt__translations_as_text__text_btn").text()
            content_old = doc(".lmt__translations_as_text__text_btn").html()

            # selector = ".lmt__translations_as_text"
            # selector = ".lmt__textarea.lmt__target_textarea.lmt__textarea_base_style"
            # selector = ".lmt__textarea.lmt__target_textarea"
            # selector = '.lmt__translations_as_text__text_btn'
            try:
                page.goto(url_)
            except Exception as exc:
                logger.error(exc)
                raise

            try:
                # page.wait_for_selector(".lmt__translations_as_text", timeout=20000)
                page.wait_for_selector(".lmt__target_textarea", timeout=20000)
            except Exception as exc:
                logger.error(exc)
                raise

            doc = pq(page.content())
            content = doc(".lmt__translations_as_text__text_btn").text()

            logger.debug("content_old: [%s], \n\t content: [%s]", content_old, content)

            # loop until content changed
            idx = 0
            # bound = 50  # 5s
            while idx < timeout / 0.1:
                idx += 1
                sleep(0.1)
                doc = pq(page.content())
                content = doc(".lmt__translations_as_text__text_btn").html()
                logger.debug(
                    "content_old: (%s), \n\tcontent: (%s)", content_old, content
                )

                if content_old != content and bool(content):
                    break

            logger.debug(" loop: %s", idx)

    deepl_tr.duration = dur.duration_human

    logger.debug(" Fini ")

    return content


def main():
    """Main."""
    text = "test this and that and more"
    res = deepl_tr(text)
    logger.info("%s, %s,", text, res)

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = "test this and that"

    res = deepl_tr(text)
    logger.info("%s, %s,", text, res)

    # stop loop, will close all browsers
    loop.stop()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        logger.error(exc)
