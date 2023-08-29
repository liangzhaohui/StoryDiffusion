from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import requests
import json

app = Flask(__name__)
CORS(app)  # 添加这一行

API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"


@app.route('/api/generate', methods=['POST'])
def generate_chat_completion():
    data = request.get_json()
    user_content = data.get('content', '')
    model = data.get('model', 'gpt-4')
    temperature = data.get('temperature', 1)
    max_tokens = data.get('max_tokens', None)
    value = data.get('value', 1)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    with open("transfer_to_more_prompt.txt", "r") as f:  # 打开文件
    #with open("sketch.txt", "r") as f:
        sd_prompt = f.read()  # 读取文件
    sd_prompt = sd_prompt.replace("PIC_NUM_NEEDED", str(value))

    messages = [
        {"role": "system", "content": sd_prompt},
        {"role": "user", "content": user_content}
    ]

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
    #print(response.content)
    if response.status_code == 200:
        return jsonify({"content": response.json()["choices"][0]["message"]["content"]})
    else:
        return jsonify({"error": f"Error {response.status_code}: {response.text}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
