import cv2

# 기본 웹캠 열기
cap = cv2.VideoCapture(0)

print("isOpened:", cap.isOpened())

# 웹캠이 열리지 않으면 종료
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    cv2.imshow("My Camera", frame)

    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()