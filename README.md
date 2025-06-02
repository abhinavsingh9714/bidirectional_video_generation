# Bidirectional Video Generation from a Single Image and Text Prompt

**Generate temporally coherent video clips from a single image and optional text prompt** by recursively expanding frames in both forward and backward directions.

> Built on a latent diffusion framework with recursive bidirectional generation and optional CLIP-guided conditioning.

---

## Project Overview

This project explores a novel generative approach that:

- Starts with a **single RGB frame** and an optional **text prompt**
- Predicts the next and previous frames jointly
- Iteratively expands the sequence in both temporal directions
- Uses **latent diffusion** + **bidirectional transformers** for efficiency and scalability

---

## Example Use Case

Given:

- `F0`: a single frame (e.g., 256×256 RGB)
- `T`: prompt like *"a dog playing fetch on a beach"*

The model produces:

```

F-4, F-3, F-2, F-1, F0, F+1, F+2, F+3, F+4

```

Each frame is visually coherent and semantically guided by the prompt.

---

## Architecture

- **Latent Diffusion Backbone** for efficient generation
- **Temporal Transformer** with shared weights for bidirectional prediction
- **Cross-attention** for text conditioning
- **Optical flow regularization** to ensure motion realism
- **Recursive Expansion** strategy for arbitrary-length video

---

## Project Structure

```

video\_bidi\_gen/
├── configs/         # YAML configs for training, inference
├── data/            # Dataset preparation scripts
├── models/          # Diffusion and transformer architectures
├── training/        # Training loop and logging
├── inference/       # Sampling and evaluation scripts
├── scripts/         # Utility scripts and CLI tools
├── outputs/         # Logs, checkpoints, visual outputs
├── docs/            # Documentation and diagrams
├── notebooks/       # Exploratory notebooks
setup.py
requirements.txt
README.md

````

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/abhinavsingh9714/bidirectional_video_generation.git
cd bidirectional_video_generation
````

### 2. Set up the environment

```bash
conda create -n video-bidi-gen python=3.10 -y
conda activate video-bidi-gen
pip install -e .
```

### 3. Prepare the Dataset

We use the [WebVid-10M](https://m-bain.github.io/webvid-dataset/) dataset.

* Store raw videos on S3
* Extract frames using `scripts/extract_frames.py`
* Convert to [WebDataset](https://github.com/webdataset/webdataset) shards

### 4. Start Training

```bash
python training/train_loop.py --config configs/train.yaml
```

### 5. Generate a Video

```bash
python inference/generate.py --image input.jpg --text "a serene lake at sunset"
```

---

## TODOs and Roadmap

* [x] Project scaffolding + modular packaging
* [x] Recursive bidirectional architecture
* [ ] Optical flow regularization
* [ ] Prompt-aware generation with CLIP/BLIP2
* [ ] Interactive inference GUI (streamlit/gradio)
* [ ] Training on WebVid subset
* [ ] Evaluation on FVD, LPIPS, Flow metrics

---

## License

MIT License. See [LICENSE](./LICENSE).

---

## 💬 Citation

Coming soon. Research in progress.

```

---