import json
import os

# JSON 파일이 저장된 디렉토리 경로 설정
json_dir = r"C:\Users\goodh\Downloads\datasample\labels_j"  ## 디렉토리 변경 위치
output_dir = r"C:\Users\goodh\Downloads\datasample\labels"  ## txt 저장 디렉토리 변경

# YOLO 라벨을 저장할 디렉토리 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# JSON 디렉토리 내의 모든 파일 처리
for json_filename in os.listdir(json_dir):
    if json_filename.endswith(".json"):
        json_file_path = os.path.join(json_dir, json_filename)

        # JSON 파일 로드 (UTF-8 인코딩 사용)
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 이미지 정보와 주석 정보 추출
        images = {img["id"]: img for img in data["images"]}
        annotations = data["annotations"]
        categories = {cat["id"]: cat for cat in data["categories"]}

        # YOLO 형식으로 변환
        for ann in annotations:
            image_id = ann["image_id"]
            image_info = images[image_id]
            category_id = ann["category_id"]
            bbox = ann["bbox"]

            # 바운딩 박스 변환
            x_center = (bbox[0] + bbox[2] / 2) / image_info["width"]
            y_center = (bbox[1] + bbox[3] / 2) / image_info["height"]
            width = bbox[2] / image_info["width"]
            height = bbox[3] / image_info["height"]

            # YOLO 라벨 파일 경로
            yolo_label_file = os.path.join(
                output_dir, f"{os.path.splitext(image_info['file_name'])[0]}.txt"
            )

            # YOLO 라벨 파일에 저장
            with open(yolo_label_file, "a") as f:
                f.write(f"{category_id - 1} {x_center} {y_center} {width} {height}\n")
