# TensorVision — GPU Matrix, Neural Network & Python Automation Lab

**TensorVision** is a unified, Vercel-ready interactive engineering platform that consolidates all Python, NumPy, PyTorch ROCm, Jupyter Notebook (`.ipynb`), Flask microservice, Regex text-mining, and PyAutoGUI desktop automation scripts into one cohesive web application.

Built with a **Serverless Flask Backend (`api/index.py`)** paired with a **Zero-Dependency Resilient Frontend (`index.html`, `css/style.css`, `js/main.js`)** that includes complete client-side calculation and rendering fallbacks.

---

## ✨ 4 Interactive Workspaces

### 1. ⚡ Benchmark Lab (CPU Loop vs Vectorized SIMD & Tensor Speedup)
- **Source Modules:** `source_code/gpu_matrix_lab/numpy_vs_loop.py` & `source_code/gpu_matrix_lab/cpu_time.py`
- **Capabilities:**
  - Interactive array dimension slider ($5 \times 10^4$ to $10^7$ elements) with contiguous RAM buffer calculator.
  - Live comparison between Pure Python List Comprehension (`[x * 2 for x in data_list]`), Sequential Integer Accumulator (`for i in range(N): total += i`), Vectorized NumPy C/SIMD Array Multiplication (`data_array * 2`), and AMD ROCm / PyTorch GPU Tensor Kernel throughput.
  - Real-time latency bar charts, speedup multipliers, slice preview, and side-by-side source code inspection.

### 2. 🧮 Interactive Matrix & Array Playground
- **Source Modules:** `source_code/gpu_matrix_lab/matrix_multiplication.py`, `math_array.py`, `numpy_basic.py`
- **Capabilities:**
  - Editable $2\times 2$ and $3\times 3$ matrix grids for Matrix $A$ and Matrix $B$ with randomizer and original preset buttons.
  - Computes `C = A @ B` with an explicit **Step-by-Step Dot Product Breakdown** ($C_{i,j} = \sum_k A_{i,k} B_{k,j}$).
  - Computes element-wise addition (`A + B`), Hadamard product (`A * B`), power (`A ** 2`), square root (`np.sqrt(B)`), Determinant $\det(A)$, Trace $\text{Tr}(A)$, and tensor metadata (`.shape`, `.ndim`, `.size`).
  - Interactive 1D Boolean Mask Filter (`a[a > threshold]`) and array slicing (`a[1:4]`).

### 3. 📓 Native Jupyter Notebook & Unified Source Explorer
- **Source Modules:** Renders all **5 Jupyter Notebooks (`.ipynb`)** and **10 Python Scripts (`.py`)** natively in the browser:
  - `Lab_3_Libraries_PyTorch.ipynb` *(AMD ROCm, `rocBLAS` SGEMM, `MIOpen` Convolutions, `rocFFT`, PyTorch GPU Training)*
  - `Design_to_Code_Workbook.ipynb` *(6-part interactive HTML, CSS, Figma, and Debugging Mini-Games workbook)*
  - `From_Design_to_Deployment_Bootcamp.ipynb` *(4-hour end-to-end Figma to GitHub & Vercel deployment curriculum)*
  - `Main.ipynb` & `test_nb.ipynb`
  - Interactive Virtual Python Terminal for all `.py` scripts, including a live **Flask Route Tester** for `app.py` (`GET /`, `GET /about`, `GET /contact`).

### 4. 🤖 Regex & Macro Automation Sandbox
- **Regex Document Number Extractor (`2.py` / `regex_number_extractor.py`):**
  - Runs `re.findall('[0-9]+', line)` across arbitrary documents or preset telemetry logs, highlighting every matched numeric token inline and computing Count, Grand Total Sum, Mean, Min, and Max in real time.
- **PyAutoGUI Keystroke Macro Simulator (`spammer.py`) & CLI Stdin Runner (`Hello.py`):**
  - Browser-sandboxed execution of `spammer.py` with configurable message payload, repeat count `n`, inter-message delay, 5-second safety countdown (`5... 4... 3... 2... 1... Fire in the hole!!!`), and live dispatch telemetry.

---

## 📂 Unified Project Structure

```text
TensorVision/
├── api/
│   └── index.py                                         # Serverless Flask API (/api/files, /api/file, /api/benchmark, /api/matrix, /api/regex-extract, /api/run-script)
├── css/
│   └── style.css                                        # Obsidian dark UI stylesheet
├── js/
│   └── main.js                                          # Interactive workspace controllers + full client-side fallback engine
├── source_code/
│   ├── gpu_matrix_lab/
│   │   ├── cpu_time.py
│   │   ├── Lab_3_Libraries_PyTorch.ipynb
│   │   ├── math_array.py
│   │   ├── matrix_multiplication.py
│   │   ├── numpy_basic.py
│   │   └── numpy_vs_loop.py
│   ├── notebooks_and_flask/
│   │   ├── app.py
│   │   ├── Design_to_Code_Workbook.ipynb
│   │   ├── From_Design_to_Deployment_Bootcamp.ipynb
│   │   ├── Main.ipynb
│   │   └── test_nb.ipynb
│   └── automation_and_utilities/
│       ├── 2.py
│       ├── regex_number_extractor.py
│       ├── Hello.py
│       └── spammer.py
├── index.html                                           # Main application shell & 4 interactive workspaces
├── requirements.txt                                     # Python dependencies (Flask, Werkzeug, numpy)
├── vercel.json                                          # Vercel serverless + static routing configuration
└── README.md                                            # Project documentation
```

---

## 🚀 Running Locally & Deploying to Vercel

### Local Development (Flask)
```bash
pip install -r requirements.txt
python api/index.py
```
Then open `http://localhost:5000` in your browser.

### Deploying to Vercel
Push this directory to a GitHub repository and import it into Vercel, or run:
```bash
vercel --prod
```
