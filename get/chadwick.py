import pandas as pd


def get_register_urls():
    BASE_URL = "https://raw.githubusercontent.com/chadwickbureau/register/master/data/"
    REGISTER_URL_SUFFIXES = [hex(i)[-1] for i in range(16)]
    REGISTER_URLS = [f"{BASE_URL}/people-{suffix}.csv"
                     for suffix in REGISTER_URL_SUFFIXES]

    return REGISTER_URLS


def get_register_df():
    REGISTER_URLS = get_register_urls()
    REGISTER_DF = pd.concat([pd.read_csv(url, low_memory=False)
                            for url in REGISTER_URLS])

    return REGISTER_DF
