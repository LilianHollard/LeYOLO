from ultralytics import YOLO

model = YOLO("weights/LeYOLOSmall.pt")

model.train(data="ultralytics/cfg/datasets/wgisd.yaml", epochs=300, batch=64, device=0)

model.val()


