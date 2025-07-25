from icrawler.builtin import BingImageCrawler

# 定義要抓的物品與數量
objects = {
    "手機 phone": 50,
    "錢包 wallet": 50,
    "鑰匙 keys": 50,
    "行動電源 power bank": 50,
    "水壺 bottle": 50,
    "帆布袋 bag": 50,
    "眼鏡 glasses": 50
}

# 下載圖片
for name, num in objects.items():
    keyword = name
    folder = name.split()[-1]  # 英文當作資料夾名
    crawler = BingImageCrawler(storage={'root_dir': f'images_raw/{folder}'})
    crawler.crawl(keyword=keyword, max_num=num)
