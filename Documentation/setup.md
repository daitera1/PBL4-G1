# Run the image blending system

The two implementation folders are maintained side by side for comparison. Start from the repository root, then enter `Development` before running the commands below.

## 1. Prepare the environment

Extract the full ZIP. Open a terminal **in the extracted project folder** — the folder containing `Development`, `Documentation`, `Management` and `Presentation`.

Use Python 3 and a desktop that supports OpenCV windows. Create the environment:

```bash
cd Development
python3 -m venv .venv
```

Activate it using the command for your system:

| System / terminal | Command |
| --- | --- |
| macOS or Linux | `source .venv/bin/activate` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |

If Windows uses `python` rather than `python3`, use `python -m venv .venv` in the creation step. Then install the packages while still in `Development`:

```bash
python -m pip install -r requirements.txt
```

## 2. Choose one version

Both examples below start from the **Development folder** with the environment activated. Choose one example; do not run the blocks consecutively from different folders.

### Version A — with gamma correction

```bash
cd ImageBlendingWithGamma
python main.py left
```

For the right projector, use `python main.py right` from this same folder. To switch to the baseline version, first run `cd ..` to return to `Development`.

### Version B — baseline, without gamma correction

```bash
cd ImageBlendingNoGamma
python main.py left
```

For the right projector, use `python main.py right` from this same folder. To switch to the gamma version, first run `cd ..` to return to `Development`.

## 3. Display and configuration

Each invocation opens a full-screen feed and waits for a keypress before closing. Run the right-projector command after the left exits, or in a second terminal with the same environment activated and the same working folder. Physical projector/display assignment must be configured for the classroom equipment.

Each folder has its own `config.json` and `test_picture.jpg`. Configure `p_width`, `p_height`, `p_overlap`, `gamma`, `image_name` and `side` there. The command-line side overrides the JSON default. Run from the chosen implementation folder so relative image paths resolve correctly.

## What has been checked

Files and Python syntax have been checked. Package versions are not pinned because the team has not supplied a validated dependency lock. These checks are separate from hardware acceptance. This documentation does not claim a successful two-projector demonstration or measured image-quality results. The initial collection found empty test-results folders; the subsequently supplied final documentation and presentation include team-provided photographs.

The [presentation](../Presentation/README.md) includes team-reported projector photographs and describes a `main_alpha_blender.py` demonstration revision. That revision has not been matched to the delivered `main.py` implementations. Follow the commands above for the delivered code.
