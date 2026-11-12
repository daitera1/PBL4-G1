# Development — code and how to run it

[Professor guide](../PROFESSOR_START_HERE.md) · [Step-by-step setup](../Documentation/setup.md)

This folder contains two versions of the image-blending program. Both use Python to prepare images for two projectors.

| Version | What it does | Open the code |
| --- | --- | --- |
| With gamma correction | Adjusts brightness in the area where the two projected images overlap | [ImageBlendingWithGamma](ImageBlendingWithGamma/) |
| Baseline, without gamma correction | Provides a version to compare against | [ImageBlendingNoGamma](ImageBlendingNoGamma/) |

## To review the work

1. Read the [setup and run guide](../Documentation/setup.md).
2. Open either version's folder to inspect its Python files and `config.json` settings.
3. Use the [sample images and data guide](data/README.md) to find inputs and settings.
4. See the [presentation](../Presentation/README.md) for the team's reported experiments and photographs.

## To run the program

Install the [required packages](requirements.txt), then follow **one** version in the [setup guide](../Documentation/setup.md). Run commands from the stated folder so the program can find its settings and sample image.

The delivered programs start with `main.py`. The final documentation's `code/` directory contains class skeletons, not a separate runnable application. Packaging checks confirm file integrity and Python syntax; hardware testing is recorded separately.
