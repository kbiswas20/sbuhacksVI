import requests
from bs4 import BeautifulSoup

link = "https://www.ebay.com/itm/276320394705?epid=10050031081&hash=item4055fa9dd1:g:x5IAAOSwacZlwPHF&amdata=enc%3AAQAIAAAA4D6898CrUvDXSivk2Y2mKM3Mt3mqEqQUSNy%2BUAIZ4GXeCOO4cOd0y5aegM4rr9RKZekwfIXDqY3XAhdMEWwnley83XLj718ktZ1Jgp9w%2Fx%2F2qagT%2Fh6f4VXYhhrR0BA9ALy67Xwt7%2BT36pXjBhD%2BxyTWdYTOVdcfeQlNUH70TamzpR6Gi4xBWw0nn56%2BAGLXh7rN1afhdduua8Q9hOK1VltY79iOMUwbty93vdzGtHKHrolStYBgv5t%2FoEoC018MUv19ke4Wu%2FdToZOm3HBP4rGzxD2cnYw2yRiQAXvOjP7y%7Ctkp%3ABFBM_rjPzrJj"

response = requests.get(link)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the price
price_element = soup.find("span", {"id": "prcIsum"})

# Check if the price element exists
if price_element is not None:
    
    # Extract the text containing the price
    price_text = price_element.text.strip()
    print("Price:", price_text)
else:
    print("Price element not found.")


# # Attempting to Web-Scrape Ebay (ATTEMPT 3)
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import requests

# link = "https://www.ebay.com/itm/404055090393?hash=item5e138f64d9:g:z6EAAOSwMkli9Wte&amdata=enc%3AAQAIAAAA4MpiRpGhW4lV9DUcE27VtSficp81yZmOn8LW4azKhAUZT7utu7xyFd%2BABAlY4uDKM1F7ztALVYeVy5rz6mpHGE%2B4C%2FEnrRU%2BLl81R8Zyr9dsThIh4%2BJuMZ0DDy%2B%2F6VLS7Z9rOdLYmswvB%2BXATTz6L%2Fl6fULd%2FsnT8D%2FaWBdwgdHnFOvEApfDfOGoEwSowFCySmVcc73YOYW31Xo7XyeATyuW9DwE54jFak%2FBmyhPPmP3g4OiCfjuzFOpwOyePqa5JUYt1NgnoLm43KR1vYntgG2yIgKp1S7853WdEDKhkzgL%7Ctkp%3ABk9SR6bAwM2yYw"

# req = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# print(webpage)


# # Attempting to Web-Scrape Ebay (ATTEMPT 2)
# import httpx

# session = httpx.Client(
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#     },
#     http2 = True,
#     follow_redirects = True
# )

# from parsel import Selector
# import httpx

# def parse_product(response: httpx.Response) -> dict:
#     """Parse Ebay's product listing page for core product data"""
#     sel = Selector(response.text)
#     # define helper functions that chain the extraction process
#     css_join = lambda css: "".join(sel.css(css).getall()).strip()  # join all CSS selected elements
#     css = lambda css: sel.css(css).get("").strip()  # take first CSS selected element and strip of leading/trailing spaces

#     item = {}
#     item["url"] = css('link[rel="canonical"]::attr(href)')
#     item["id"] = item["url"].split("/itm/")[1].split("?")[0]  # we can take ID from the URL
#     item["price"] = css('.x-price-primary>span::text')
#     item["name"] = css_join("h1 span::text")
#     item["seller_name"] = css_join("[data-testid=str-title] a ::text")
#     item["seller_url"] = css("[data-testid=str-title] a::attr(href)").split("?")[0]
#     item["photos"] = sel.css('.ux-image-filmstrip-carousel-item.image img::attr("src")').getall()  # carousel images
#     item["photos"].extend(sel.css('.ux-image-carousel-item.image img::attr("src")').getall())  # main image
#     # description is an iframe (independant page). We can keep it as an URL or scrape it later.
#     item["description_url"] = css("div.d-item-description iframe::attr(src)")
#     if not item["description_url"]:
#         item["description_url"] = css("div#desc_div iframe::attr(src)")
#     # feature details from the description table:
#     feature_table = sel.css("div.ux-layout-section--features")
#     features = {}
#     for ft_label in feature_table.css(".ux-labels-values__labels"):
#         # iterate through each label of the table and select first sibling for value:
#         label = "".join(ft_label.css(".ux-textspans::text").getall()).strip(":\n ")
#         ft_value = ft_label.xpath("following-sibling::div[1]")
#         value = "".join(ft_value.css(".ux-textspans::text").getall()).strip()
#         features[label] = value
#     item["features"] = features
#     return item

# # establish our HTTP2 client with browser-like headers
# session = httpx.Client(
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#     },
#     http2=True,
#     follow_redirects=True
# )
# # example use: scrape this item and parse the data
# response = session.get("https://www.ebay.com/itm/332562282948")
# item = parse_product(response)
# import json
# print(json.dumps(item, indent=2))

# # Attempt to Web-Scrape Amazon (ATTEMPT 1)

# # import requests
# url = 'https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L'

# response = requests.get(url)

# print(response.text)

# custom_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
#     'Accept-Language': 'da, en-gb, en',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     # 'Referer': 'https://www.google.com/'
# }

# response = requests.get(url, headers = 
# custom_headers)