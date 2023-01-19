from torchvision import models
import torch

#ResNet50 pretrained model
model = models.resnet50(pretrained=True)

input = torch.randn(1, 3, 224, 224)

onnx_path = 'resnet50.onnx'

torch.onnx.export(model, input, onnx_path, input_names=['input'],
                  output_names=['output'], export_params=True)
