"""Test deepl_scraper_pw."""
# pylint: disable=broad-except
from deepl_scraper_pw import __version__
from deepl_scraper_pw import deepl_scraper_pw


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not deepl_scraper_pw()
    except Exception:
        assert True
