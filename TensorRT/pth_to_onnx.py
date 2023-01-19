from torchvision import models
import torch
import argparse

if __name__ == '__main__':
    # Input arguments
    parser = argparse.ArgumentParser(description='Course pth model')
    parser.add_argument('--onnx_path', type=str, default='', required=True, help="Path to save model")

    args = parser.parse_args()

    onnx_path = args.onnx_path

    #ResNet50 pretrained model
    model = models.resnet50(pretrained=True)

    input = torch.randn(1, 3, 224, 224)

    torch.onnx.export(model, input, onnx_path, input_names=['input'],
                      output_names=['output'], export_params=True)
