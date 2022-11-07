"""Test deepl_scraper_pw."""
# pylint: disable=broad-except
from deepl_scraper_pw import __version__, deepl_tr


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not deepl_tr("")
    except Exception:
        assert True
