"""Test simple.

Switched to get_pwbrowser_sync. dev branch, can be deleted.
start fresh from deepl-scraper-playwright
"""
from deepl_scraper_pw import deepl_tr


def test_simple():
    """Test simple.

    @pytest.fixture(scope="function")
    async def
        ...
    @pytest.mark.asyncio
        ...

    wont work, always runtime errors: loop already closed
    """
    text = "test this and more"
    res = deepl_tr(text)

    assert "试" in res


def test_para_info():
    """Test para_info."""
    text = "test this \n\nand more"
    res = deepl_tr(text)

    assert res.split("\n\n").__len__() == 2
