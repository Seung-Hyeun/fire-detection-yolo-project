from ultralytics import YOLO


# =========================
# 기본 설정
# =========================

# 사전 학습된 YOLOv8 모델 사용
# 정확도 우선이면 yolov8s.pt도 가능하지만, 우선은 빠른 학습을 위해 yolov8n.pt 사용
model = YOLO("yolov8n.pt")


# =========================
# 모델 학습
# =========================

model.train(
    data="/content/fire-detection-yolo-project/data/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    device=0,

    # 학습 결과 저장 위치
    project="/content/drive/MyDrive/fire_results",
    name="fire_smoke_detection_model"
)