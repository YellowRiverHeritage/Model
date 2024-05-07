import torch
print(torch.cuda.is_available())

from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("chatglm", trust_remote_code=True)
model = AutoModel.from_pretrained("chatglm", trust_remote_code=True).quantize(bits=4, device="cuda").half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
response, history = model.chat(tokenizer, "讲一个关于大学生的笑话", history=history)
print(response)
response, history = model.chat(tokenizer, "从这个笑话你能得到什么启示", history=history)
print(response)
