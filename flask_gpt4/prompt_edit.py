from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

STYLE_PATH = "style/style.txt"
TRANSFER_PATH = "transfer/transfer.txt"


@app.route('/api/save-log', methods=['POST'])
def save_log():
    log_content = request.json.get('log')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 请注意，我们已经移除了额外的 datetime
    formatted_log = f"{timestamp}: {log_content}\n"

    with open('logs.txt', 'a') as f:
        f.write(formatted_log)

    return jsonify({"message": "Log saved successfully!"})


@app.route('/api/resetTempFiles', methods=['GET'])
def reset_temp_files():
    try:
        # Reset style_temp.txt
        with open(STYLE_PATH, 'r') as original, open(STYLE_PATH.replace(".txt", "_temp.txt"), 'w') as temp:
            temp.write(original.read())

        # Reset transfer_temp.txt
        with open(TRANSFER_PATH, 'r', encoding='utf-8') as original, open(TRANSFER_PATH.replace(".txt", "_temp.txt"),
                                                                          'w') as temp:
            temp.write(original.read())

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/api/fetchStyle', methods=['GET'])
def fetch_style():
    with open(STYLE_PATH, 'r') as file:
        content = file.read()
    return jsonify({"content": content})


@app.route('/api/saveStyle', methods=['POST'])
def save_style():
    data = request.get_json()
    with open(STYLE_PATH.replace(".txt", "_temp.txt"), 'w') as file:
        file.write(data["content"])
    return jsonify({"status": "success"})


@app.route('/api/fetchTransfer', methods=['GET'])
def fetch_transfer():
    with open(TRANSFER_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
    return jsonify({"content": content})


@app.route('/api/saveTransfer', methods=['POST'])
def save_transfer():
    data = request.get_json()
    with open(TRANSFER_PATH.replace(".txt", "_temp.txt"), 'w') as file:
        file.write(data["content"])
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
