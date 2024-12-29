import torch


def load_yolov5_model(model_path, model_weights,device='cuda', img_size=640, half=False, iou=0.45, conf=0.25):
    """
    加载YOLOv5模型的函数，可传入iou、conf等参数来设置模型检测相关阈值。

    参数:
    - model_path: 训练好的模型权重文件的路径，字符串类型，例如'model.pt'
    - device: 运行模型的设备，可选 'cpu' 或者 'cuda'（如果有可用的GPU），默认 'cpu'
    - img_size: 模型输入图像的尺寸，默认640，通常可以是320、416、640等YOLOv5支持的尺寸
    - half: 是否使用半精度（FP16），在GPU上可以加速运算，默认False
    - iou: 交并比阈值，用于非极大值抑制，去除重叠度高的冗余检测框，默认0.45
    - conf: 置信度阈值，可根据实际需求调整，只有置信度高于此值的检测结果才会被保留，默认0.25

    返回:
    - 加载好的YOLOv5模型对象
    """
    # 根据指定的设备来加载模型
    if device == 'cuda' and torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    # 加载自定义的YOLOv5模型，这里使用torch.hub.load
    model = torch.hub.load(repo_or_dir=model_path, model='custom', path=model_weights, source='local')

    # 设置模型的一些参数
    model.conf = conf
    model.iou = iou
    model.max_det = 1000  # 每张图像最多检测的目标数量
    model.agnostic = False  # 是否进行类别无关的NMS（非极大值抑制），一般设为False

    # 设置模型输入图像尺寸
    model.img_size = img_size

    # 将模型移动到指定的设备上
    model.to(device)

    # 如果使用半精度（并且设备是GPU），转换模型为半精度
    if half and device.type == 'cuda':
        model.half()

    return model