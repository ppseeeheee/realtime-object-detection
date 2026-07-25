from ultralytics import YOLO
import cv2

# YOLO 모델 불러오기
model = YOLO("yolo11n.pt")

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 웹캠 정상 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO 실행
    results = model(frame)
    
    annotated_frame = results[0].plot()

    # 화면 출력
    cv2.imshow("Real-Time Detection", annotated_frame)

    # q를 누르면 종료
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()