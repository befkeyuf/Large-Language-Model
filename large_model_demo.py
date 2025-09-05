# 大语言模型调用示例（安全版）
from transformers import pipeline

def generate_text(prompt, max_length=100):
    """
    使用Hugging Face的text-generation管道进行安全文本生成
    模型使用本地缓存路径，避免网络请求
    """
    # 初始化文本生成管道（使用本地模型）
    generator = pipeline(
        'text-generation', 
        model='gpt2',
        device=0 if torch.cuda.is_available() else -1,
        cache_dir='./model_cache'
    )
    
    # 生成文本
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text']

if __name__ == "__main__":
    import torch
    print("大语言模型安全调用示例
")
    
    # 用户输入
    user_prompt = input("请输入生成提示: ") or "解释基因预测中的GC含量意义"
    
    # 执行模型调用
    try:
        output = generate_text(user_prompt)
        print("
生成结果:
" + "-"*40 + "
" + output)
    except Exception as e:
        print(f"生成失败: {str(e)}")
    
    # 保存结果到文件
    with open("model_output.txt", "w", encoding="utf-8") as f:
        f.write(f"提示: {user_prompt}
结果:
{output}")
    
    print("
结果已保存至 model_output.txt")
