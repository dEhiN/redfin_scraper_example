from redfin_scraper import RedfinScraper

# scraper=RedfinScraper()
# scraper.setup('./zip_code_sample.csv',multiprocessing=True)

scraper = RedfinScraper()
scraper.setup('./zip_code_sample.csv')

# scraper.scrape(city_states=None,zip_codes=['JUNK'])
# scraper.scrape(city_states=None,zip_codes='JUNK')
# scraper.scrape(city_states=['Omaha, NE'],zip_codes='JUNK')
scraper.scrape(city_states=None, zip_codes=['77002', '77003'])
scraper.scrape(city_states=['Omaha,NE'], zip_codes=None)
# scraper.scrape(city_states=[('Newark', 'NJ'),('Georgia', 'AL')],zip_codes=None)
# scraper.scrape(city_states=['junk, junky'],zip_codes=['77002'])
# scraper.scrape() # From Config
# scraper.scrape(city_states=['Omaha,NE'],zip_codes=None,sold=True,sale_period='3mo')

for i in range(1, 3):
    try:
        print(scraper.get_data(id=f"D00{i}"))
        print("Success!")
    except:
        print("Failed")
