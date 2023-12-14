# Stable diffusion samples

## Install dependencies

```
accelerate               0.25.0
aiohttp                  3.9.1
aiosignal                1.3.1
alembic                  1.13.0
annotated-types          0.6.0
async-timeout            4.0.3
attrs                    23.1.0
certifi                  2023.11.17
charset-normalizer       3.3.2
coloredlogs              15.0.1
colorlog                 6.8.0
controlnet-aux           0.0.7
cuda-python              12.3.0
datasets                 2.15.0
diffusers                0.24.0
dill                     0.3.7
einops                   0.7.0
filelock                 3.9.0
flatbuffers              23.5.26
frozenlist               1.4.0
fsspec                   2023.10.0
greenlet                 3.0.2
huggingface-hub          0.19.4
humanfriendly            10.0
idna                     3.6
imageio                  2.33.1
importlib-metadata       7.0.0
invisible-watermark      0.2.0
Jinja2                   3.1.2
lazy_loader              0.3
lightning-utilities      0.10.0
Mako                     1.3.0
MarkupSafe               2.1.3
mpmath                   1.3.0
multidict                6.0.4
multiprocess             0.70.15
networkx                 3.0rc1
numpy                    1.26.2
nvidia-cublas-cu12       12.1.3.1
nvidia-cuda-cupti-cu12   12.1.105
nvidia-cuda-nvrtc-cu12   12.1.105
nvidia-cuda-runtime-cu12 12.1.105
nvidia-cudnn-cu12        8.9.2.26
nvidia-cufft-cu12        11.0.2.54
nvidia-curand-cu12       10.3.2.106
nvidia-cusolver-cu12     11.4.5.107
nvidia-cusparse-cu12     12.1.0.106
nvidia-nccl-cu12         2.18.1
nvidia-nvjitlink-cu12    12.1.105
nvidia-nvtx-cu12         12.1.105
nvtx                     0.2.8
olive-ai                 0.5.0
onnx                     1.14.1
onnx-graphsurgeon        0.3.27
opencv-python            4.8.0.74
optimum                  1.14.1
optuna                   3.4.0
ort-nightly-gpu          1.17.0.dev20231209002
packaging                23.2
pandas                   2.1.4
Pillow                   10.1.0
pip                      23.3.1
polygraphy               0.49.0
protobuf                 3.20.3
psutil                   5.9.6
py3nvml                  0.2.7
pyarrow                  14.0.1
pyarrow-hotfix           0.6
pydantic                 2.5.2
pydantic_core            2.14.5
python-dateutil          2.8.2
pytorch-triton           2.1.0+bcad9dabe1
pytz                     2023.3.post1
PyWavelets               1.5.0
PyYAML                   6.0.1
regex                    2023.10.3
requests                 2.31.0
safetensors              0.4.1
scikit-image             0.22.0
scipy                    1.11.4
sentencepiece            0.1.99
setuptools               68.0.0
six                      1.16.0
SQLAlchemy               2.0.23
sympy                    1.12
tensorrt                 8.6.1.post1
tensorrt-bindings        8.6.1
tensorrt-libs            8.6.1
tifffile                 2023.12.9
timm                     0.9.12
tokenizers               0.15.0
torch                    2.1.1
torchmetrics             1.2.1
torchvision              0.16.1
tqdm                     4.66.1
transformers             4.35.2
triton                   2.1.0
typing_extensions        4.8.0
tzdata                   2023.3
urllib3                  2.1.0
wheel                    0.41.2
xmltodict                0.13.0
xxhash                   3.4.1
yarl                     1.9.4
zipp                     3.17.0
```

## Run pipeline with diffusers

```bash
python run_stablediffusion_df.py
```

## Generate model with Olive

export TRANFORMERS_CACHE=`pwd`/.cache




