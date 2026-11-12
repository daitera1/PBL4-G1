# Run the image blending system

The two implementation folders are maintained side by side for comparison. Run commands from the repository root unless shown otherwise.

## Environment

Use Python 3 and a desktop session that supports OpenCV windows. Create a virtual environment, then install the dependencies imported by the existing source:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate` instead. Dependencies are not pinned because the team has not supplied a validated version lock.

## With gamma compensation

```bash
cd ImageBlendingWithGamma
python main.py left
# For the other projector, run in a separate terminal/display session:
python main.py right
```

## Without gamma compensation

```bash
cd ImageBlendingNoGamma
python main.py left
python main.py right
```

Each invocation opens a full-screen feed and waits for a keypress before closing. The second command can be run after the first exits, or in a separate terminal for a second display session. Physical projector/display assignment must be configured for the classroom equipment.

Each folder has its own `config.json` and `test_picture.jpg`. Configure `p_width`, `p_height`, `p_overlap`, `gamma`, `image_name` and `side` there. The command-line side overrides the JSON default. Run from the chosen implementation folder so relative image paths resolve correctly.

## Validation boundary

Repository packaging and source syntax are checked separately from hardware acceptance. This documentation does not claim a successful two-projector demonstration or measured image-quality results. The shared Drive test-results and final-files folders were empty when inspected on 12 November 2026.
