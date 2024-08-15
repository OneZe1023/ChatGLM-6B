from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from collections import Counter
import time


# 设置 Selenium 的 Chrome 浏览器
def setup_browser():
    options = Options()
    options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
    options.add_argument('--disable-gpu')  # 禁用 GPU 加速
    options.add_argument('--no-sandbox')  # 禁用沙盒模式
    options.add_argument('--disable-dev-shm-usage')  # 解决资源限制问题

    # 确保已经安装了 chromedriver，并指定路径
    service = Service('C:/Users/hp/.wdm/drivers/chromedriver')  # 修改为实际的 chromedriver 路径
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def fetch_hot_topics(url):
    driver = setup_browser()
    try:
        # 打开页面
        driver.get(url)
        time.sleep(5)  # 等待页面加载

        # 查找热门话题元素（根据实际页面结构调整）
        topics_elements = driver.find_elements(By.CSS_SELECTOR, '.hot-topic-class')  # 替换为实际选择器
        topics = [element.text.strip() for element in topics_elements]
        return topics
    except Exception as e:
        print(f"Error fetching hot topics: {e}")
        return []
    finally:
        driver.quit()


def analyze_topics(topics):
    # 统计话题频率
    counter = Counter(topics)

    # 将话题和频率转为 DataFrame 以便于分析
    df = pd.DataFrame(counter.items(), columns=['Topic', 'Frequency'])

    # 按频率排序
    df = df.sort_values(by='Frequency', ascending=False)
    return df


def main():
    # 小红书热门话题页面 URL
    url = 'https://www.xiaohongshu.com/explore'  # 替换为实际热门话题页面 URL

    # 抓取热门话题
    hot_topics = fetch_hot_topics(url)

    if hot_topics:
        # 分析话题
        df = analyze_topics(hot_topics)

        # 打印分析结果
        print("热门话题分析结果:")
        print(df)
    else:
        print("未能获取热门话题。")


if __name__ == "__main__":
    main()
