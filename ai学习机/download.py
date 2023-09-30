import os
import csv
import requests


def download_query_img():
    # 设置下载图片存放的目录
    download_folder = 'D:/query_imgs'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # 打开csv文件
    with open('D:/image2.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # 遍历每一行并下载图片
        for row in reader:
            try:
                print(row[0])
                response = requests.get(row[0])
                # 解析文件名并保存到本地文件夹
                filename = os.path.basename(row[0])
                with open(os.path.join(download_folder, filename), 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                print(f"Error downloading {row[0]}: {e}")


def main():
    download_query_img()


if __name__ == '__main__':
    main()