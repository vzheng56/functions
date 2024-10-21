import random
import json

def main(req, res):
    # 词汇列表
    words = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", 
        "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", 
        "quince", "raspberry", "strawberry", "tangerine", "watermelon", "xigua"
    ]
    
    # 随机选择 5 到 10 个词汇
    selected_words = random.sample(words, random.randint(5, 10))
    
    # 构建返回结果
    result = {
        "selected_words": selected_words
    }
    
    # 返回 JSON 响应
    res.json(result)
