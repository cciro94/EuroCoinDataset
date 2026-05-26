---
license: cc-by-nc-4.0
task_categories:
  - image-classification
language:
  - en
tags:
  - euro
  - coins
  - currency
  - numismatics
  - image-classification
  - computer-vision
  - web-crawled
pretty_name: EURO-Coin Dataset
size_categories:
  - 10K<n<100K
---

# EURO-Coin Dataset

## Dataset Summary

The EURO-Coin Dataset is a collection of **12,878 images** of euro coins from **23 issuing countries**, spanning all **8 denominations** (1 cent to 2 euro). Images were gathered via an automated web crawler that extracted publicly available pictures from Google, Bing, and Baidu image search engines.

The dataset is intended exclusively for **non-commercial research** purposes (e.g., computer vision, deep learning, currency recognition). The original repository is available at [https://github.com/cciro94/EuroCoinDataset](https://github.com/cciro94/EuroCoinDataset).

---

## Supported Tasks

| Task | Description |
|---|---|
| **Country classification** | Predict the issuing country of a coin from its image (23 classes). |
| **Value classification** | Predict the denomination of a coin from its image (8 classes). |
| **Joint classification** | Predict both country and denomination simultaneously. |

---

## Dataset Structure

The repository includes two parallel directory trees, each containing the same 12,878 images organised from a different perspective:

```
EuroCoinDataset/
├── country_dataset/          # Organised by issuing country (23 sub-folders)
│   ├── Andorra/
│   ├── Austria/
│   ├── Belgium/
│   ├── ...
│   └── Vatican-City/
│
└── denomination_dataset/     # Organised by denomination (8 sub-folders)
    ├── 1-cent/
    ├── 2-cent/
    ├── 5-cent/
    ├── 10-cent/
    ├── 20-cent/
    ├── 50-cent/
    ├── 1-euro/
    └── 2-euro/
```

### File naming convention

- `country_dataset`: `<Country>_<index>.<ext>` (e.g., `Germany_42.jpg`)
- `denomination_dataset`: `<denomination>-<Country>_<index>.<ext>` (e.g., `2-euro-Germany_42.jpg`)

Images are provided in `.jpg` and `.jpeg` format at their original resolution as retrieved from the web.

---

## Data Statistics

| Country       | 1c  | 2c  | 5c | 10c | 20c | 50c | 1€  | 2€  | Total |
|:-------------:|:---:|:---:|:--:|:---:|:---:|:---:|:---:|:---:|:-----:|
| Andorra       |  42 |  46 | 71 |  43 |  49 |  57 |  60 | 220 |  588  |
| Austria       |  83 |  64 | 76 |  72 |  49 |  57 |  73 |  94 |  568  |
| Belgium       |  86 |  29 | 99 |  98 | 112 |  61 |  78 | 144 |  707  |
| Cyprus        |  13 |  23 | 38 |  40 |  25 |  28 |  84 | 107 |  358  |
| Estonia       |  58 |  44 | 45 |  41 |  44 |  30 |  61 | 102 |  425  |
| Finland       |  49 |  38 | 61 |  36 |  72 |  58 |  99 | 201 |  614  |
| France        |  34 |  57 | 67 |  52 |  59 |  73 |  57 | 128 |  527  |
| Germany       | 163 | 131 | 60 | 163 |  80 |  62 |  90 | 178 |  927  |
| Greece        | 121 |  52 | 58 |  63 |  69 |  59 | 117 | 169 |  708  |
| Ireland       |  56 |  65 | 50 |  83 |  76 |  45 |  66 | 124 |  565  |
| Italy         | 121 |  36 | 67 |  59 |  72 |  79 |  70 | 119 |  623  |
| Latvia        |  71 |  30 | 45 |  17 |  21 |  45 |  91 | 232 |  552  |
| Lithuania     |  94 |  15 | 25 |  28 |  35 |  31 |  90 | 181 |  499  |
| Luxembourg    |  43 |  29 | 35 |  31 |  52 |  35 |  90 | 173 |  488  |
| Malta         |  74 |  52 | 64 |  76 |  83 |  79 |  76 | 154 |  658  |
| Monaco        |  14 |   3 | 33 |  48 |  57 |  47 | 110 | 107 |  419  |
| Netherlands   |  35 |  32 | 64 |  76 |  72 |  69 |  62 | 166 |  576  |
| Portugal      |  55 |  57 | 69 |  80 |  40 |  37 | 101 | 132 |  571  |
| San Marino    |  47 |  56 | 57 |  60 |  62 |  77 | 109 | 114 |  582  |
| Slovakia      |  34 |  26 | 21 |  20 |  19 |  32 |  39 | 156 |  347  |
| Slovenia      |  56 |  45 | 42 |  50 |  52 |  45 |  65 | 136 |  491  |
| Spain         |  23 |  41 | 46 |  48 |  52 |  55 |  97 | 174 |  536  |
| Vatican City  |  52 |  30 | 34 |  58 |  50 |  91 |  62 | 172 |  549  |
| **Total**     | **1424** | **1001** | **1227** | **1342** | **1302** | **1252** | **1847** | **3483** | **12878** |

**Key figures:**
- Total images: **12,878**
- Countries: **23**
- Denominations: **8** (1c, 2c, 5c, 10c, 20c, 50c, 1€, 2€)
- Image formats: JPEG
- Class balance: Germany has the most images (927); Slovakia the fewest (347)

---

## Dataset Creation

### Collection Method

Images were collected using a custom web crawler that submitted country + denomination queries (e.g., "Germany 2 euro coin") to Google Images, Bing Images, and Baidu Images, then downloaded all publicly accessible results. No manual annotation was required: the country and denomination labels are implicit in the search query used to retrieve each image.

### Preprocessing

Images are stored at their original resolution and aspect ratio as retrieved from the web. No cropping, resizing, or colour normalisation was applied. Some images may contain multiple coins, backgrounds, watermarks, or text overlays, reflecting the natural variability of web-scraped data.

### Curation

Duplicate and clearly corrupt images were removed manually. The dataset covers **all euro-area member states** that issue coins, plus **Monaco**, **San Marino**, **Andorra**, and **Vatican City**, which mint euro coins under special agreement with the EU.

---

## Experiments and Baselines

The dataset was used in the following peer-reviewed study to benchmark deep learning models for simultaneous country and value classification:

> Cirillo, S., Solimando, G., & Virgili, L. (2023). *A deep learning approach to classify country and value of modern coins*. **Neural Computing and Applications**, 1–17. Springer. [https://doi.org/10.1007/s00521-023-08615-9](https://doi.org/10.1007/s00521-023-08615-9)

**Key experimental results reported in the paper:**
- Several CNN architectures were evaluated (custom CNNs and pre-trained models via transfer learning).
- Best models achieved high top-1 accuracy on both country and denomination classification tasks.
- The dataset was split into training, validation, and test sets with stratified sampling.
- The dual-folder structure (`country_dataset` / `denomination_dataset`) allows straightforward use for either single-label or multi-label classification scenarios.

---

## Considerations for Using the Data

### License and Permitted Use

This dataset is released under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. Use for commercial purposes is **not permitted**. Any publication or derivative work must include the citation below.

### Limitations

- Images are web-scraped and may contain noise, watermarks, or irrelevant content.
- Class sizes are unbalanced (e.g., Germany: 927 vs. Slovakia: 347).
- The dataset does not cover commemorative or special-edition coin designs exhaustively.
- No bounding-box or segmentation annotations are provided.

### Personal and Sensitive Information

The dataset contains only images of physical coins. No personally identifiable information (PII) is present.

---

## Additional Information

### Original Repository

[https://github.com/cciro94/EuroCoinDataset](https://github.com/cciro94/EuroCoinDataset)

### Dataset Curators

- Stefano Cirillo
- Giandomenico Solimando
- Luca Virgili

### Citation

If you use this dataset, please cite:

```bibtex
@article{cirillo2023deep,
  title={A deep learning approach to classify country and value of modern coins},
  author={Cirillo, Stefano and Solimando, Giandomenico and Virgili, Luca},
  journal={Neural Computing and Applications},
  pages={1--17},
  year={2023},
  publisher={Springer}
}
```
