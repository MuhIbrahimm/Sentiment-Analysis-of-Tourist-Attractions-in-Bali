from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from pymongo import MongoClient

client = MongoClient('YOUR_MONGODB_CONNECTION_STRING')
db = client['YOUR_DATABASE']
collection = db['YOUR_COLLECTION']

places = [
    ('https://www.google.com/maps/place/Ulun+Danu+Beratan+Temple/@-8.3138852,115.1026287,12z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd1896c9fac0857:0x18246568e4db1b53!8m2!3d-8.2751807!4d115.1668234!16s%2Fm%2F05zyg1h?authuser=0&entry=ttu', 
    'Ulun Danu Beratan Temple'),

    ('https://www.google.com/maps/place/Garuda+Wisnu+Kencana+Cultural+Park/@-8.8419017,115.1225363,12z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd244cf54e1dec7:0x1988663e064f5a51!8m2!3d-8.8104228!4d115.1675986!16zL20vMGRyenpx?authuser=0&entry=ttu',
    'Garuda Wisnu Kencana Cultural Park'),

    ('https://www.google.com/maps/place/Kuta+Beach/@-8.7049395,115.1638943,12.83z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd246bc2ab70d43:0x82feaae12f4ab48e!8m2!3d-8.7184926!4d115.1686322!16s%2Fg%2F11c1p6r11n?authuser=0&entry=ttu',
    'Kuta Beach'),

    ('https://www.google.com/maps/place/Bali+Zoo/@-8.6027349,115.1935485,12.83z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd23e3e4361eea5:0x3bf4eb36bfd7c6be!8m2!3d-8.5915391!4d115.2658642!16s%2Fg%2F1tk_rlbg?authuser=0&entry=ttu',
    'Bali Zoo'),

    ('https://www.google.com/maps/place/Tegenungan+Waterfall/@-8.5734557,115.2561048,12z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd2161beebd0c61:0xc1ae79ddb8410c5e!8m2!3d-8.5753621!4d115.2889599!16s%2Fg%2F11bvx3j8m8?authuser=0&entry=ttu',
    'Tegunungan Waterfall'),

    ('https://www.google.com/maps/place/Jatiluwih+Rice+Terraces/@-8.3857108,115.1316325,12z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd227ab020cd7fb:0x2f0f875ff3e6839a!8m2!3d-8.37031!4d115.131372!16s%2Fg%2F11b6dfvgqz?authuser=0&entry=ttu',
    'Jatiluwih Rice Terrace'),

    ('https://www.google.com/maps/place/Pandawa+Beach/@-8.7869434,115.1318189,12z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd25b7cd8ba1f31:0x41b8785dd055b2a4!8m2!3d-8.8452802!4d115.1870679!16s%2Fg%2F1ygbcghrt?authuser=0&entry=ttu',
    'Pandawa Beach'),

    ('https://www.google.com/maps/place/Uluwatu+Temple/@-8.7869434,115.1318189,12z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd24ffc20cb8191:0xcb98d1ba7db0495!8m2!3d-8.8291432!4d115.0849069!16zL20vMGRuNWp4?authuser=0&entry=ttu',
    'Uluwatu Temple'),

    ('https://www.google.com/maps/place/Padang+Padang+Beach/@-8.8104997,115.1285907,12.81z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd245505d4ce257:0x64783bec584c4015!8m2!3d-8.8111377!4d115.1037658!16s%2Fg%2F11b6syl4fp?authuser=0&entry=ttu',
    'Padang Padang Beach'),

    ('https://www.google.com/maps/place/Pura+Tirta+Empul/@-8.4413313,115.3068067,13.08z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd218f4e06131b5:0x53a25a017714ecc1!8m2!3d-8.4156589!4d115.3153284!16s%2Fm%2F0b6jfq9?authuser=0&entry=ttu',
    'Pura Tirta Empul'),

    ('https://www.google.com/maps/place/Sacred+Monkey+Forest+Sanctuary/@-8.5434988,115.2662501,13.08z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd23d43f6189b67:0xb6ec43164befc356!8m2!3d-8.5193727!4d115.2606299!16s%2Fm%2F03wc0td?authuser=0&entry=ttu',
    'Sacred Monkey Forest Sanctuary'),

    ('https://www.google.com/maps/place/Bali+Safari+and+Marine+Park/@-8.5555079,115.2867869,13.08z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd21446b81f7d39:0x34b39c786c2e54ec!8m2!3d-8.5805621!4d115.3454147!16s%2Fm%2F0lkqtcl?authuser=0&entry=ttu',
    'Bali Safari and Marine Park'),

    ('https://www.google.com/maps/place/Taman+Ujung/@-8.4878875,115.5329055,13.08z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd20876e3e79815:0xfc9ab3edaa5d11f2!8m2!3d-8.4630811!4d115.6306692!16s%2Fm%2F011l7bd6?authuser=0&entry=ttu',
    'Taman Ujung'),

    ('https://www.google.com/maps/place/Temple+Of+Penataran+Agung+Lempuyang/@-8.4221766,115.5957336,13z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd2071753222893:0x40a0fd58fe779263!8m2!3d-8.3918426!4d115.6314767!16s%2Fg%2F11gdkpxymn?authuser=0&entry=ttu',
    'Temple of Penataran Agung Lempuyang'),

    ('https://www.google.com/maps/place/Tirta+Gangga/@-8.4221766,115.5957336,13z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd24736f4379ad1:0x65af03b0d108a7d1!8m2!3d-8.4123473!4d115.5872919!16s%2Fm%2F09rv951?authuser=0&entry=ttu',
    'Tirta Gangga'),

    ('https://www.google.com/maps/place/Besakih+Great+Temple/@-8.3728392,115.4599559,13.54z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd21cbe3748b2b7:0xbfc39798cd1bb4a!8m2!3d-8.3739976!4d115.4525567!16zL20vMDc3ZDM4?authuser=0&entry=ttu',
    'Besakih Great Temple'),

    ('https://www.google.com/maps/place/Penglipuran+Village/@-8.4696312,115.3155887,13z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd2196eace4f4a9:0x3319169adf0c3419!8m2!3d-8.4225039!4d115.3597531!16s%2Fg%2F11g6htx9w5?authuser=0&entry=ttu',
    'Penglipuran Village'),

    ('https://www.google.com/maps/place/Petitenget+Beach/@-8.7095164,115.138203,12.56z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd2470fba33f4eb:0x77f7f6be668440c7!8m2!3d-8.6823579!4d115.150964!16s%2Fg%2F11cjj07gjc?authuser=0&entry=ttu',
    'Petitenget Beach'),

    ('https://www.google.com/maps/place/Sukawati+Art+Market/@-8.5821233,115.3055013,13.81z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd23e28616c410d:0x960eaffe9f543e3c!8m2!3d-8.5965307!4d115.2826055!16s%2Fg%2F11gzm8537?authuser=0&entry=ttu',
    'Sukawati Art Market'),

    ('https://www.google.com/maps/place/Water+Sport+Adventure+Bali+Dolphin+Shop/@-8.7544605,115.2192426,17z/data=!4m14!1m7!3m6!1s0x2dd237824f71deab:0xcaabe270f7e34d69!2sTanah+Lot!8m2!3d-8.621213!4d115.086807!16zL20vMGJ2NGRo!3m5!1s0x2dd243b8e6c58b87:0xe958bb6d54a9d706!8m2!3d-8.7530772!4d115.2202874!16s%2Fg%2F11cmr0sdq1?authuser=0&entry=ttu',
    'Water Sport Adventure Bali Dolphin Shop')
]

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 60)

for url, place_name in places:
    driver.get(url)

    # Click review button
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]'))).click()
    
    time.sleep(5)
    
    # Find scroll layout
    scrollable_div = driver.find_element(By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf')

    review_summary = []

    print('\n===================================================')
    print(f'Scraping Data {place_name}')
    print('===================================================')

    j = 1
    while len(review_summary) < 800:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        time.sleep(5)

        wait_review = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div[' + str(j) + ']/div/div/div[2]/div[2]/div[1]/button/div[1]')))

        for _ in range(10):
            username = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div[' + str(j) + ']/div/div/div[2]/div[2]/div[1]/button/div[1]').text
            review_text = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div[' + str(j) + ']/div/div/div[4]/div[2]/div/span').text
            review_rate = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div[' + str(j) + ']/div/div/div[4]/div[1]/span[1]').get_attribute("aria-label")
            review_time = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div[' + str(j) + ']/div/div/div[4]/div[1]/span[2]').text

            review_summary.append([place_name, username, review_text, review_rate, review_time])
            
            j += 3

        print(f'{len(review_summary)} Data Review {place_name} Diperoleh')

    # Convert to DataFrame and save to MongoDB
    df = pd.DataFrame(review_summary, columns=['Place Name', 'Username', 'Review Text', 'Review Rating', 'Review Time'])
    print(df)
    collection.insert_many(df.to_dict('records'))

    print('================================================================')
    print(f'{len(review_summary)} Data Review {place_name} Berhasil Disimpan pada MongoDB')
    print('================================================================\n')

driver.quit()