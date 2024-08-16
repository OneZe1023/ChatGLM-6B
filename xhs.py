from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from collections import Counter
import time


def setup_browser():
    options = Options()
    options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
    options.add_argument('--disable-gpu')  # 禁用 GPU 加速
    options.add_argument('--no-sandbox')  # 禁用沙盒模式
    options.add_argument('--disable-dev-shm-usage')  # 解决资源限制问题

    # 更新为新的 Chromedriver 路径
    service = Service('D:\\work\\Python项目\\ChatGLM-6B\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def login_to_xiaohongshu(driver, username, password):
    try:
        driver.get('https://www.xiaohongshu.com/user/login')  # 登录页的 URL
        time.sleep(5)  # 等待页面加载

        # 输入用户名
        username_input = driver.find_element(By.NAME, 'username')  # 根据实际情况调整
        username_input.send_keys(username)

        # 输入密码
        password_input = driver.find_element(By.NAME, 'password')  # 根据实际情况调整
        password_input.send_keys(password)

        # 提交表单
        password_input.send_keys(Keys.RETURN)
        time.sleep(10)  # 等待登录完成

        print("登录成功")
    except Exception as e:
        print(f"登录失败: {e}")


def fetch_hot_topics(driver, url):
    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载

        # 查找热门话题元素（根据实际页面结构调整）
        topics_elements = driver.find_elements(By.CSS_SELECTOR, '.hot-topic-class')  # 替换为实际选择器
        topics = [element.text.strip() for element in topics_elements]
        return topics
    except Exception as e:
        print(f"Error fetching hot topics: {e}")
        return []


def analyze_topics(topics):
    # 统计话题频率
    counter = Counter(topics)

    # 将话题和频率转为 DataFrame 以便于分析
    df = pd.DataFrame(counter.items(), columns=['Topic', 'Frequency'])

    # 按频率排序
    df = df.sort_values(by='Frequency', ascending=False)
    return df


def main():
    # 小红书登录信息
    username = 'your_username'  # 替换为实际用户名
    password = 'your_password'  # 替换为实际密码

    # 小红书热门话题页面 URL
    url = 'https://www.xiaohongshu.com/explore'  # 替换为实际热门话题页面 URL

    # 设置浏览器
    driver = setup_browser()

    # 登录
    login_to_xiaohongshu(driver, username, password)

    # 抓取热门话题
    hot_topics = fetch_hot_topics(driver, url)

    if hot_topics:
        # 分析话题
        df = analyze_topics(hot_topics)

        # 打印分析结果
        print("热门话题分析结果:")
        print(df)
    else:
        print("未能获取热门话题。")

    # 关闭浏览器
    driver.quit()


if __name__ == "__main__":
    main()
