import fasttext
import jieba
import numpy as np


# 分词
def chinese_tokenizer(text):
    return [token for token in jieba.cut(text)]


# 获取文本向量
def get_text_vector(text, model):
    tokens = chinese_tokenizer(text)
    vec = np.zeros(model.get_dimension()).astype('float32')
    for token in tokens:
        vec += model.get_word_vector(token)
    vec /= len(tokens)
    return vec.reshape(1, -1)


def main():
    model = fasttext.load_model(r'D:\python\ai学习机\cc.zh.300.bin')
    text = '如果你还不了解 JSON，可以先阅读我们的 JSON 教程。'
    print(chinese_tokenizer(text))
    vec = get_text_vector(text, model)
    print(vec.shape)


if __name__ == '__main__':
    main()

