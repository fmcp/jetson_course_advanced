from torchvision import models
import torch
import argparse

if __name__ == '__main__':
    # Input arguments
    parser = argparse.ArgumentParser(description='Course pth model')
    parser.add_argument('--onnx_path', type=str, default='/home/nano/resnet50_onnx.onnx', required=False, help="Path to save model")
    parser.add_argument('--dynamic_batch', default=False, action='store_true')
    parser.add_argument('--onnx_path_dynamic_batch', type=str, default='/home/nano/resnet50_onnx_dynamic_batch.onnx', required=False, help="Path to save model with dynamic batch")

    args = parser.parse_args()

    onnx_path = args.onnx_path
    dynamic_batch = args.dynamic_batch
    onnx_path_dynamic_batch = args.onnx_path_dynamic_batch

    #ResNet50 pretrained model
    model = models.resnet50(pretrained=True)

    input = torch.randn(1, 3, 224, 224)

    if dynamic_batch:
        torch.onnx.export(model, input, onnx_path_dynamic_batch,
                          input_names=['input'],  # the model's input names
                          output_names=['output'],  # the model's output names
                          dynamic_axes={'input': {0: 'batch_size'},  # variable length axes
                                        'output': {0: 'batch_size'}})
    else:
        torch.onnx.export(model, input, onnx_path, input_names=['input'],
                          output_names=['output'], export_params=True)
