from ultralytics import YOLO

# YOLO 모델 로드
model = YOLO("yolo11n.pt")

# 이미지 객체 탐지
results = model("images/test.jpg", show=True)

# 결과 저장
results[0].save(filename="results.jpg")