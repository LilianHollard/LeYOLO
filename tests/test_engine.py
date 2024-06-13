# Ultralytics YOLO 🚀, AGPL-3.0 license

from ultralytics import YOLO
from ultralytics.cfg import get_cfg
from ultralytics.engine.exporter import Exporter
from ultralytics.models.yolo import classify, detect, segment
from ultralytics.utils import ASSETS, DEFAULT_CFG, WEIGHTS_DIR

CFG_DET = 'yolov8n.yaml'
CFG_SEG = 'yolov8n-seg.yaml'
CFG_CLS = 'yolov8n-cls.yaml'  # or 'squeezenet1_0'
CFG = get_cfg(DEFAULT_CFG)
MODEL = WEIGHTS_DIR / 'yolov8n'


def test_func(*args):  # noqa
    """Test function callback."""
    print('callback test passed')


def test_export():
    """Test model exporting functionality."""
    exporter = Exporter()
    exporter.add_callback('on_export_start', test_func)
    assert test_func in exporter.callbacks['on_export_start'], 'callback test failed'
    f = exporter(model=YOLO(CFG_DET).model)
    YOLO(f)(ASSETS)  # exported model inference


def test_detect():
    """Test object detection functionality."""
    overrides = {'data': 'coco8.yaml', 'model': CFG_DET, 'imgsz': 32, 'epochs': 1, 'save': False}
    CFG.data = 'coco8.yaml'
    CFG.imgsz = 32

    # Trainer
    trainer = detect.DetectionTrainer(overrides=overrides)
    trainer.add_callback('on_train_start', test_func)
    assert test_func in trainer.callbacks['on_train_start'], 'callback test failed'
    trainer.train()

    # Validator
    val = detect.DetectionValidator(args=CFG)
    val.add_callback('on_val_start', test_func)
    assert test_func in val.callbacks['on_val_start'], 'callback test failed'
    val(model=trainer.best)  # validate best.pt

    # Predictor
    pred = detect.DetectionPredictor(overrides={'imgsz': [64, 64]})
    pred.add_callback('on_predict_start', test_func)
    assert test_func in pred.callbacks['on_predict_start'], 'callback test failed'
    result = pred(source=ASSETS, model=f'{MODEL}.pt')
    assert len(result), 'predictor test failed'

    overrides['resume'] = trainer.last
    trainer = detect.DetectionTrainer(overrides=overrides)
    try:
        trainer.train()
    except Exception as e:
        print(f'Expected exception caught: {e}')
        return

    Exception('Resume test failed!')


def test_segment():
    """Test image segmentation functionality."""
    overrides = {'data': 'coco8-seg.yaml', 'model': CFG_SEG, 'imgsz': 32, 'epochs': 1, 'save': False}
    CFG.data = 'coco8-seg.yaml'
    CFG.imgsz = 32
    # YOLO(CFG_SEG).train(**overrides)  # works

    # Trainer
    trainer = segment.SegmentationTrainer(overrides=overrides)
    trainer.add_callback('on_train_start', test_func)
    assert test_func in trainer.callbacks['on_train_start'], 'callback test failed'
    trainer.train()

    # Validator
    val = segment.SegmentationValidator(args=CFG)
    val.add_callback('on_val_start', test_func)
    assert test_func in val.callbacks['on_val_start'], 'callback test failed'
    val(model=trainer.best)  # validate best.pt

    # Predictor
    pred = segment.SegmentationPredictor(overrides={'imgsz': [64, 64]})
    pred.add_callback('on_predict_start', test_func)
    assert test_func in pred.callbacks['on_predict_start'], 'callback test failed'
    result = pred(source=ASSETS, model=f'{MODEL}-seg.pt')
    assert len(result), 'predictor test failed'

    # Test resume
    overrides['resume'] = trainer.last
    trainer = segment.SegmentationTrainer(overrides=overrides)
    try:
        trainer.train()
    except Exception as e:
        print(f'Expected exception caught: {e}')
        return

    Exception('Resume test failed!')


def test_classify():
    """Test image classification functionality."""
    overrides = {'data': 'imagenet10', 'model': CFG_CLS, 'imgsz': 32, 'epochs': 1, 'save': False}
    CFG.data = 'imagenet10'
    CFG.imgsz = 32
    # YOLO(CFG_SEG).train(**overrides)  # works

    # Trainer
    trainer = classify.ClassificationTrainer(overrides=overrides)
    trainer.add_callback('on_train_start', test_func)
    assert test_func in trainer.callbacks['on_train_start'], 'callback test failed'
    trainer.train()

    # Validator
    val = classify.ClassificationValidator(args=CFG)
    val.add_callback('on_val_start', test_func)
    assert test_func in val.callbacks['on_val_start'], 'callback test failed'
    val(model=trainer.best)

    # Predictor
    pred = classify.ClassificationPredictor(overrides={'imgsz': [64, 64]})
    pred.add_callback('on_predict_start', test_func)
    assert test_func in pred.callbacks['on_predict_start'], 'callback test failed'
    result = pred(source=ASSETS, model=trainer.best)
    assert len(result), 'predictor test failed'
