import urllib3
from bs4 import BeautifulSoup
import time


def crawl(
    pool: urllib3.PoolManager,
    url,
    phrase=None,
    deep=1,
    sleep_time=0.5,
    n=5,
    prefix="https://en.wikipedia.org",
    verbose=False,
    how_many_times=0
):

    if verbose:
        site = url.split("/")[-1]
        print(f"{deep} Entering {site}")
        how_many_times += 1
    time.sleep(sleep_time)
    site = pool.request("GET", url)
    soup = BeautifulSoup(site.data, parser="lxml")
    links = get_links_from_wiki(soup=soup, n=n, prefix=prefix)
    is_phrase_present = any([phrase in link for link in links]) and phrase is not None
    if deep > 0 and not is_phrase_present:
        return (
            url,
            [
                crawl(
                    pool=pool,
                    url=url_,
                    phrase=phrase,
                    deep=deep - 1,
                    sleep_time=sleep_time,
                    n=n,
                    prefix=prefix,
                    verbose=verbose,
                )
                for url_ in links
            ],
        )
    return url, links, how_many_times


def get_links_from_wiki(soup, n=5, prefix="https://en.wikipedia.org"):
    arr = []
    div = soup.find("div", class_="mw-parser-output")

    for element in div.find_all("p") + div.find_all("ul"):
        for i, a in enumerate(element.find_all("a", href=True)):
            if len(arr) >= n:
                break
            if (
                a["href"].startswith("/wiki/")
                and len(a["href"].split("/")) == 3
                and ("." not in a["href"] and ("(" not in a["href"]))
            ):
                arr.append(prefix + a["href"])
    return arr


def start(start_page):
    pool_main = urllib3.PoolManager(cert_reqs='CERT_NONE')
    return crawl(pool_main,
                 start_page,
                 phrase="Philosophy",
                 deep=50,
                 n=1,
                 verbose=True)

# inspired by: https://dev.to/finloop/getting-to-philosophy-with-python-4nmc - Thanks Piotr
