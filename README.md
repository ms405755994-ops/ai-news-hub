# ai-news-hub

FreshRSS -> Python -> AI中文翻译/总结 -> Telegram / 企业微信

## 1. 安装依赖

pip install -r requirements.txt

## 2. 配置环境变量

复制 .env.example 为 .env，并填入配置。

## 3. 运行

python -m app.main

## 4. 当前版本说明

- 通过 FreshRSS 暴露的 RSS 地址抓取内容
- 通过 OpenAI 兼容接口生成中文标题和摘要
- 推送到 Telegram 和企业微信
- SQLite 记录已发送链接，避免重复发送
