import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models

# Load a pretrained ResNet model
model = models.resnet18(pretrained=True)
model.eval()

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted_class = output.max(1)
    return f"Predicted class: {predicted_class.item()}"
