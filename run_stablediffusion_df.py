from diffusers import DiffusionPipeline
import torch

print("Loading pipeline...")
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)

print("Sending to CUDA ")
pipeline.to("cuda")

print("Running pipeline...")
image = pipeline("An image of a squirrel in Picasso style").images[0]

print("Saving image...")
image.save("image_of_squirrel_painting.png")