from icrawler.builtin import GoogleImageCrawler

categories = {
    "phone": "手機 phone",
    "wallet": "錢包 wallet",
    "key": "鑰匙 key",
    "powerbank": "行動電源 powerbank",
    "bag": "帆布袋 bag",
    "bottle": "水壺 bottle",
    "glasses": "眼鏡 glasses"
}

def crawl_images():
    for label, keyword in categories.items():
        crawler = GoogleImageCrawler(storage={"root_dir": f"dataset/{label}"})
        crawler.crawl(keyword=keyword, max_num=300)

if __name__ == "__main__":
    crawl_images()
