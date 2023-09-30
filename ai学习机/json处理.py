
import os
import json
from bs4 import BeautifulSoup
def remove_html_tags(text):
    """去除html"""
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text(separator=' ')
    clean_text = clean_text.replace(u'\xa0', ' ')  # 替代其他库
    return clean_text


# 读取json
with open('D:/qst.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 创建文件夹
os.makedirs('texts', exist_ok=True)

# 遍历
for entry in data:
    entry_id = entry['id']
    content = entry['content']
    clean_content = remove_html_tags(content)

    # 读取保存
    file_path = os.path.join('texts', f'{entry_id}.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(clean_content)

    print(f'Saved {file_path}')

print('All files saved successfully.')
