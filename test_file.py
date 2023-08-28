
from trends_levif_scraper_mongo import fun_sum


def test_fn():

    assert fun_sum(2, 3) == 5
    assert fun_sum(-1, 1) == 0


if __name__ == "__main__":
    import pytest
    pytest.main()
