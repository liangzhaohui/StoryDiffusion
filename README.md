# Storyboard_Generator

A web tool called Story Diffusion, which enables collaborative storyboard creation between human and computer, through natural language input and automatic storyboard generation.

## Stable Diffusion
```
python webui.py --nowebui --xformers --no-half
```


## GPT4

in flask_gpt4/style (Running on http://127.0.0.1:5000)
```
python style.py 
```
in flask_gpt4/transfer (Running on http://127.0.0.1:5001)
```
python transfer.py
```
in flask_gpt4 (Running on http://127.0.0.1:5010)
```
python prompt_edit.py 
```

## UI
```
npm install
```

```
npm run serve
```

(Running on http://localhost:8080)

## Frp
```
cd frp
```
```
frpc.exe -c frpc.ini
```
