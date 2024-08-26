import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import matplotlib.pyplot as plt

#select model
model_id = "CompVis/stable-diffusion-v1-4"  
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Define prompt
prompt = "Hulk Smash"

# Generate the image
with torch.no_grad():
    image = pipe(prompt).images[0]

# Display the image
plt.imshow(image)
plt.axis("off")  
plt.show()

#save the image
image.save("generated_image_3.png")