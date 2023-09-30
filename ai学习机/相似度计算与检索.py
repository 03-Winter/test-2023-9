import fasttext
import jieba
import numpy as np
import faiss
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


# 准备数据
texts = [
    '这个电影太好看了',
    '这部电影让我很开心',
    '这个电影真的很棒',
    '这部电影很有意思',
    '我不喜欢这个电影',
    '这个电影太无聊了',
    '这部电影让我很失望',
    '这个电影一般般',
    '我觉得这个电影很一般',
    '这部电影不怎么样'
]

model = fasttext.load_model(r'D:\python\ai学习机\cc.zh.300.bin')

vectors = []
for text in texts:
    vector = get_text_vector(text, model)
    vectors.append(vector)
vectors = np.concatenate(vectors, axis=0).astype('float32')

# 构建索引
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

# 查询相似文本
query_text = "我喜欢这个电影"
query_vector = get_text_vector(query_text, model)
query_vector = query_vector.reshape(1, -1).astype('float32')

k = 5  # 返回前两个最相似的文本
distances, indices = index.search(query_vector, k)

# 打印检索结果
print("Query Text: ", query_text)
print("Similar Texts:")
for i in range(k):
    print(f"{i + 1}. {texts[indices[0][i]]} (Distance: {distances[0][i]})")

