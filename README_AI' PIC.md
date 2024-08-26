# AI Image Generator using Stable Diffusion

This project demonstrates how to generate an AI-generated image from a text prompt using the Stable Diffusion model. The model takes a text input and generates a corresponding image. In this example, the prompt used is "Hulk Smash," but it can be modified to generate different images based on various prompts.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Explanation of the Code](#explanation-of-the-code)
- [Output](#output)
- [References](#references)

## Overview

Stable Diffusion is a state-of-the-art AI model that generates high-quality images from text descriptions. This script uses the `StableDiffusionPipeline` from the `diffusers` library to generate an image based on a given prompt.

## Requirements

Before running the code, make sure you have the following installed:

- Python 3.7+
- PyTorch
- diffusers library
- PIL (Pillow) library
- matplotlib library

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/ai-image-generator.git
   cd ai-image-generator
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Libraries:**

   ```bash
   pip install torch torchvision torchaudio
   pip install diffusers[torch]
   pip install pillow matplotlib
   ```

   Alternatively, you can install all dependencies using the `requirements.txt` file if provided:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate an image using the Stable Diffusion model, follow these steps:

1. **Run the Script:**

   ```bash
   python generate_image.py
   ```

2. **Modify the Text Prompt:**

   The script is set to generate an image from the prompt "Hulk Smash." You can change the `prompt` variable in the script to generate different images.

3. **View the Generated Image:**

   The generated image will be displayed using `matplotlib` and saved as `generated_image_3.png` in the working directory.

## Explanation of the Code

Here's a breakdown of what each part of the code does:

### 1. Importing Necessary Libraries

```python
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import matplotlib.pyplot as plt
```

- `torch`: PyTorch library used to load and run the model on the CPU or GPU.
- `StableDiffusionPipeline`: This is the main component from the `diffusers` library that handles the text-to-image generation.
- `PIL.Image`: Used to manipulate and save images.
- `matplotlib.pyplot`: Used to display images in a window.

### 2. Selecting and Loading the Model

```python
model_id = "CompVis/stable-diffusion-v1-4"  
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
```

- `model_id`: Specifies the version of the Stable Diffusion model to use.
- `from_pretrained`: Downloads and loads the pre-trained model.
- `to("cuda" if torch.cuda.is_available() else "cpu")`: Moves the model to the GPU if available for faster processing, otherwise uses the CPU.

### 3. Defining the Text Prompt

```python
prompt = "Hulk Smash"
```

- The `prompt` variable is set to the text description that will guide the image generation. You can change this to any descriptive text.

### 4. Generating the Image

```python
with torch.no_grad():
    image = pipe(prompt).images[0]
```

- `torch.no_grad()`: Disables gradient calculation, which is not needed for inference and reduces memory consumption.
- `pipe(prompt)`: Passes the text prompt through the model to generate the image.
- `image = pipe(prompt).images[0]`: The generated image is the first (and only) element in the list of images produced by the model.

### 5. Displaying and Saving the Image

```python
plt.imshow(image)
plt.axis("off")  
plt.show()

image.save("generated_image_3.png")
```

- `plt.imshow(image)`: Displays the generated image using matplotlib.
- `plt.axis("off")`: Hides the axes in the image display.
- `image.save("generated_image_3.png")`: Saves the generated image as a PNG file in the working directory.

## Output

After running the script, you should see the generated image displayed in a window. Additionally, the image will be saved as `generated_image_3.png` in the same directory as the script.

![generated_image_3](https://github.com/user-attachments/assets/e0fa010f-c92f-4e06-856d-588194ccdfd6)

![Screenshot 2024-08-25 180351](https://github.com/user-attachments/assets/6c55cb62-2588-41d9-a94c-314a740a1030)

![Screenshot 2024-08-25 185259](https://github.com/user-attachments/assets/3e7dfde7-96bc-4b2c-831e-1127f295cd91)


## References

- [Stable Diffusion GitHub Repository](https://github.com/CompVis/stable-diffusion)
- [diffusers Library Documentation](https://huggingface.co/docs/diffusers/index)

---

Feel free to modify the text prompt or explore different models to see how the generated images change.
