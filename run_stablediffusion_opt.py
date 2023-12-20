from optimum.onnxruntime import ORTStableDiffusionXLPipeline

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
pipeline = ORTStableDiffusionXLPipeline.from_pretrained(model_id, export=True)

pipeline.save_pretrained("models")

prompt = "A majestic lion jumping from a big stone at night"
image = pipeline(prompt).images[0]