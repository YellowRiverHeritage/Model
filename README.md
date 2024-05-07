# ChatGLM-6B

这个仓库包含一个基于chatglm-6b模型的后端API，使用FastAPI框架构建。该API旨在提供自然语言处理服务，支持基于大型语言模型的自然语言理解和生成。

## 项目介绍

ChatGLM-6B API使用最新的大型语言模型chatglm-6b，配备了NVIDIA CUDA加速，以提供高效的文本生成服务。这个API支持多种用例，包括聊天机器人、文本摘要、问答系统等。

## 安装指南

要运行此API，您需要确保已安装Python、CUDA和必要的依赖。

请按照原仓库说明进行配置 [THUDM/ChatGLM-6B: ChatGLM-6B: An Open Bilingual Dialogue Language Model | 开源双语对话语言模型 (github.com)](https://github.com/THUDM/ChatGLM-6B)

## 使用说明

在完成安装后，先从huggingface上下载模型文件，链接在此 [THUDM/chatglm3-6b · Hugging Face](https://huggingface.co/THUDM/chatglm3-6b)，在根目录新建文件夹 chatglm，放入所有的模型文件，接着运行以下命令启动API服务器：

```bash
python api.py
```

服务器将在端口8888上运行。

## API接口

- **POST /**
  
  - **功能**: 接受一个文本提示并返回生成的文本。
  - **请求体**:
    ```json
    {
      "prompt": "输入的提示文本",
      "history": [],
      "max_length": 2048,
      "top_p": 0.7,
      "temperature": 0.95
    }
    ```
  - **响应**: 
    ```json
    {
      "response": "生成的文本",
      "history": [],
      "status": 200,
      "time": "响应时间"
    }
    ```



