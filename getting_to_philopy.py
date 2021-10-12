import urllib3
from bs4 import BeautifulSoup
import time
import ssl


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

    # Sleep to avoid getting banned
    time.sleep(sleep_time)
    site = pool.request("GET", url)
    soup = BeautifulSoup(site.data, parser="lxml")

    # Get links from wiki (I'll show it later)
    links = get_links_from_wiki(soup=soup, n=n, prefix=prefix)

    # If phrase was given check if any of the links have it
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

    # Get div with article contents
    div = soup.find("div", class_="mw-parser-output")

    for element in div.find_all("p") + div.find_all("ul"):
        # In each paragraph find all <a href="/wiki/article_name"></a> and
        # extract "/wiki/article_name"
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
    links, how_many_times = crawl(pool_main, start_page, phrase="Philosophy", deep=50, n=1, verbose=True)
    return links, how_many_times

# inspired by: https://dev.to/finloop/getting-to-philosophy-with-python-4nmc
