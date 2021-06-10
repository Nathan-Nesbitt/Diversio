"""
Nathan Nesbitt, 2021

This program pulls from the API and outputs the response times. 

Based on observing the site, I can see that the site pulls from an API that
provides data in the following structure:

"title"
"status"
"monitor":{
    "monitorId"
    "statusClass"
    "name"
    "createdAt"
    "url"
    "type"
    "checkInterval"
    "logs"
    "responseTimes"
    "7dRatio"
    "1dRatio"
    "30dRatio"
    "90dRatio"
    "dailyRatios"
},
"days"
"timezone":
"statistics": {
    "counts": {
        "up"
        "down"
        "paused"
        "total"
    },
    "count_result"
}

Instead of parsing the page, which could change over time, I instead choose to
pull from the API https://stats.uptimerobot.com/api/getMonitor/ using the params 
from the provided URL and output the stats from there.

The one thing that does need to be done is to scrape the ID from the page if it
is not defined in the URL. This can be found in a hidden input in the page. 

If the page was to change, instead of having to figure out how to pull the data
from the graph you would just have to figure out where the `name` value is 
within the page. It seems its tagged as `pspi`. 
"""

import json
import argparse
import requests
from bs4 import BeautifulSoup


def get_data(url):

    # Splits the URL and gets the params
    split_url = url.split("/")

    # If the `name` wasn't provided we scrape for it
    if len(split_url) == 4:
        id = split_url[3]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        name = soup.find("input", {"id": "pspi"})["value"]
    else:
        name = split_url[3]
        id = split_url[4]

    # Then we request the API URL with the 2 params
    r = requests.get(
        "https://stats.uptimerobot.com/api/getMonitor/{}?m={}".format(name, id)
    )
    d = json.loads(r.text)

    sorted_values = sorted(d["monitor"]["responseTimes"], key=lambda k: k["value"])

    # Prints out the result
    print(
        "Blog received highest ping on {} with value {}ms in last 90 days".format(
            sorted_values[len(sorted_values) - 1]["datetime"],
            sorted_values[len(sorted_values) - 1]["value"],
        )
    )
    print(
        "The min ping was {}ms on {}".format(
            sorted_values[0]["value"], sorted_values[0]["datetime"]
        )
    )

    # This is a faster way to compute median as the array is already sorted.
    index = (len(sorted_values) - 1) // 2

    if len(sorted_values) % 2:
        print("The median was {}ms".format(sorted_values[index]["value"]))
    else:
        print(
            "The median was {}ms".format(
                (sorted_values[index]["value"] + sorted_values[index + 1]["value"])
                / 2.0
            )
        )


if __name__ == "__main__":
    # This is just a parser for the input, so we get a help menu and good params.
    parser = argparse.ArgumentParser(
        prog="Q2.py",
        description="Script that takes the URL as input, and outputs the date + time when the response time was the highest",
    )
    parser.add_argument(
        "--url",
        "-u",
        metavar="url",
        type=str,
        required=True,
        help="The URL that you are trying to get a summary of.",
    )
    args = parser.parse_args()

    get_data(args.url)
