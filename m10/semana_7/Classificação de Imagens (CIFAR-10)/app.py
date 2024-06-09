from flask import Flask, request, jsonify
from PIL import Image
import io
import torch
import torchvision.transforms as transforms
from torch import nn
from torchvision.models.resnet import ResNet, BasicBlock

app = Flask(__name__)

# Custom ResNet model definition if required
class CustomResNet(ResNet):
    def __init__(self, block, layers, num_classes=10, num_input_channels=3):
        super().__init__(block, layers)
        self.conv1 = nn.Conv2d(num_input_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.fc = nn.Linear(512 * block.expansion, num_classes)

# Instantiate your model (adjust parameters as per your original model architecture)
model = CustomResNet(BasicBlock, [2, 2, 2, 2], num_classes=10)  # This matches ResNet18
model_path = 'trained_model.pth'

# Load the model weights
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')), strict=False)
model.eval()

# Image transformations
transform = transforms.Compose([
    transforms.Resize(40),
    transforms.CenterCrop(32),
    transforms.ToTensor(),
    transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])
])

# Class labels
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Process the image
    img = Image.open(io.BytesIO(file.read())).convert('RGB')
    img = transform(img).unsqueeze(0)

    # Perform the inference
    with torch.no_grad():
        outputs = model(img)
        _, predicted = outputs.max(1)
        predicted_class = classes[predicted.item()]

    return jsonify({'category': predicted_class})

# Run the API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
