from redfin_scraper import RedfinScraper

scraper = RedfinScraper()
scraper.setup('./zip_code_sample.csv')

scraper.scrape(city_states=None, zip_codes=['77002', '77003'])
scraper.scrape(city_states=['Omaha,NE'], zip_codes=None)
scraper.scrape(city_states=['Omaha,NE'],
               zip_codes=None, sold=True, sale_period='3mo')

for i in range(1, 4):
    try:
        data = scraper.get_data(id=f"D00{i}")
        print(f"Scrape {i}: Success!")
        print(type(data))
        print(data)
    except:
        print("Failed")
    print()
