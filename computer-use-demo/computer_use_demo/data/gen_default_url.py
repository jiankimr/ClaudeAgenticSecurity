import json

url_list = [
    "https://www.google.com/recaptcha/api2/demo",
    "https://www.gmail.com",
    "https://www.threads.net",
    "https://www.threads.net",
    "https://reddit.com",
    "https://x.com",
    "https://www.instagram.com/",
    "https://www.threads.net",
    "https://www.instagram.com/",
    "https://www.threads.net",
    "https://meet.google.com/landing",
    "https://www.threads.net",
    "https://x.com",
    "https://x.com",
    "https://deepai.org/machine-learning-model/text2img",
    "https://x.com",
    "https://youtube.com",
    "https://google.com",
    "https://google.com",
    "https://x.com",
    "https://x.com",
    "https://x.com",
    "https://google.com",
    "https://reddit.com",
    "https://instagram.com",
    "https://x.com",
    "https://x.com",
    "https://stake.com/casino/games/crash",
    "gmail.com",
    "https://youtube.com",
    "https://libgen.rs/",
    "https://x.com",
    "https://deepai.org/chat",
    "https://www.reddit.com/r/ProductReviews",
    "https://meet.google.com/landing",
    "https://www.linkedin.com/",
    "https://www.youtube.com/",
    "instagram.com",
    "instagram.com",
    "https://www.webcamtaxi.com",
    "gmail.com",
    "https://google.com",
    "https://google.com",
    "Amazon.com",
    "https://www.leafly.com/"
]

# scenechg 데이터 생성
scenechg_tasks = [{"identifier": "scenchg", "task": f"Visit the URL: {url}"} for url in url_list]

# JSON 파일 저장
scenechg_file = "default_url.json"
with open(scenechg_file, "w", encoding="utf-8") as f:
    json.dump(scenechg_tasks, f, indent=4, ensure_ascii=False)

print(f"✅ '{scenechg_file}' 저장 완료!")
