import json

def load_json(file_path):
    """JSON 파일을 로드하는 함수"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def insert_scenechg_with_urls(scenechg_data, main_data):
    """
    scenechg 데이터(45개)를 기존 JSON 리스트(main_data)와 번갈아가며 삽입하는 함수.
    """
    modified_data = []
    index = 0

    for item in main_data:
        if index < len(scenechg_data):
            modified_data.append(scenechg_data[index])  # scenechg 삽입
            index += 1
        modified_data.append(item)  # 기존 데이터 삽입
    
    return modified_data

# scenechg 데이터 불러오기
scenechg_data = load_json("default_url.json")

# 첫 번째 JSON 파일 로드 및 병합
json_file_1 = "HarmWeb.json"
data1 = load_json(json_file_1)
modified_data1 = insert_scenechg_with_urls(scenechg_data, data1)

# 수정된 JSON 저장
output_file_1 = "autoHarmWeb.json"
with open(output_file_1, "w", encoding="utf-8") as f:
    json.dump(modified_data1, f, indent=4, ensure_ascii=False)

print(f"✅ '{output_file_1}' 저장 완료!")
