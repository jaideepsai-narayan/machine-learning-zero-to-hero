# Machine Learning Zero to Hero 🚀

[![Course Modules](https.img.shields.io/badge/Modules-9-indigo.svg)](COURSE-MAP.md)
[![Lessons](https://img.shields.io/badge/Lessons-19%20Complete-emerald.svg)](index.html)
[![Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20JS%20%7C%20PyTorch-orange.svg)](#tech-stack)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An interactive, visual, and math-rigorous web-based course taking learners from **absolute zero** to **state-of-the-art Deep Learning** (Transformers, Diffusion Models, GANs, and PyTorch).

Every concept is presented through a structured 4-part framework:
1. **WHY**: Real-world motivation and industrial applications.
2. **WHAT IS IT**: Intuitive conceptual analogies and core definitions.
3. **HOW DOES IT WORK**: Mathematical formulas, proofs, and step-by-step mechanics.
4. **INTERACTIVE VISUALIZER**: Live HTML5 Canvas visualizers with 2D/3D parameter controls.

---

## 🗺️ Master Curriculum Outline

| Module | Lesson | Core Concepts | Interactive Visualizer |
| :--- | :--- | :--- | :--- |
| **Module 1: Foundations** | **[0001: What is Machine Learning?](lessons/0001-what-is-machine-learning.html)** | Supervised vs Unsupervised, $y = mx + b$ | Interactive Pizza Price Predictor |
| | **[0002: Linear Regression & Loss](lessons/0002-linear-regression-loss.html)** | Mean Squared Error (MSE), Residuals | 3D Loss Surface Explorer |
| | **[0003: Gradient Descent](lessons/0003-gradient-descent.html)** | Learning Rate ($\alpha$), Partial Derivatives | 3D Loss Mountain Skiing Simulator |
| **Module 2: Linear & Kernels** | **[0004: Logistic Regression](lessons/0004-logistic-regression.html)** | Sigmoid Function, Binary Cross-Entropy Loss | 2D Logistic Decision Boundary |
| | **[0005: Support Vector Machines](lessons/0005-support-vector-machines.html)** | Max Margin Hyperplane, RBF Kernel Trick | 3D Circular Point Elevation & Separating Plane |
| **Module 3: Ensembles** | **[0006: Decision Trees](lessons/0006-decision-trees.html)** | Information Gain, Entropy, Gini Impurity | Interactive Split Threshold Boundary |
| | **[0007: Bagging & Random Forests](lessons/0007-bagging-random-forests.html)** | Bootstrapping, Variance Reduction | Ensemble Heatmap Probability Surface |
| | **[0008: Boosting (AdaBoost & XGBoost)](lessons/0008-boosting-adaboost-xgboost.html)** | Sample Weights, Sequential Residual Fitting | Interactive Weak Learner Adder |
| **Module 4: Unsupervised** | **[0009: Dimensionality Reduction](lessons/0009-dimensionality-reduction-pca.html)** | PCA Covariance Matrix, Eigenvectors, t-SNE | 3D Point Projection Drop Lines |
| | **[0010: Unsupervised Clustering](lessons/0010-unsupervised-clustering.html)** | K-Means Centroid Iteration, Voronoi Cells, DBSCAN | Live Centroid Shift & Voronoi Shading |
| **Module 5: Deep Learning** | **[0011: Neural Networks & Backprop](lessons/0011-backpropagation.html)** | Chain Rule, Activation Functions, Vanishing Gradients | Dynamic Computation Graph & Weight Updates |
| **Module 6: Vision** | **[0012: CNNs & Image Classification](lessons/0012-cnn-image-classification.html)** | Convolutions, Kernels, Feature Maps, ResNet | Live 2D Kernel Filter & 3D Feature Stacks |
| | **[0013: Object Detection](lessons/0013-object-detection.html)** | Bounding Boxes, Anchor Boxes, IoU, YOLO | Live Drag Bounding Box & IoU Calculator |
| | **[0014: Image Segmentation](lessons/0014-image-segmentation.html)** | Semantic vs Instance Segmentation, U-Net | Split-Screen U-Net Pixel Masking |
| **Module 7: Evaluation** | **[0015: Model Evaluation & Regularization](lessons/0015-model-evaluation-regularization.html)** | Precision, Recall, F1-Score, $L_1$ Lasso vs $L_2$ Ridge | Geometric Loss Contour & Constraint Boundaries |
| **Module 8: NLP & Sequences** | **[0016: Text Embeddings & NLP](lessons/0016-text-embeddings-nlp.html)** | Tokenization, TF-IDF, Word2Vec Vector Math | 3D Semantic Vector Math ($\text{King} - \text{Man} + \text{Woman}$) |
| | **[0017: RNNs & LSTMs](lessons/0017-rnn-lstm-sequences.html)** | Recurrent Hidden States, LSTM Memory Highway | Interactive Time-Step Slider & Memory Cells |
| | **[0018: Transformers & Attention](lessons/0018-transformers-attention.html)** | Self-Attention, $Q, K, V$ Matrices, Softmax Heatmap | Dynamic Curved Attention Beams & Matrix Grid |
| **Module 9: Generative AI** | **[0019: Generative AI (GANs & Diffusion)](lessons/0019-generative-ai-gans-diffusion.html)** | GAN Minimax Game, VAE Latent Space, Diffusion Denoising | 2D Denoising Steps & 3D Latent Manifold |

---

## 🌟 Key Features

- 🎨 **100% Zero-Dependency Web App**: Runs directly in any modern browser without needing Node.js, Webpack, or heavy build tools.
- 🧮 **MathJax Integration**: Crisp LaTeX mathematical equations rendered seamlessly alongside intuition visualizers.
- 🔥 **PyTorch Code Cheat Sheet**: Includes a dedicated [PyTorch Cheat Sheet](reference/pytorch-implementations-cheatsheet.html) containing ready-to-run PyTorch code snippets for all 19 algorithms.
- 📐 **Grand Evolution Cheat Sheet**: Includes the [Classification & Ensemble Cheat Sheet](reference/classification-ensemble-cheatsheet.html) summarizing decision boundaries, pros/cons, and time complexities.
- 🌐 **Responsive & Accessible Design**: Built with clean CSS tokens, modern typography, glassmorphism UI components, and keyboard/touch navigation.

---

## ⚡ Quick Start & Local Development

### Option 1: Open in Browser Directly
Simply double-click [`index.html`](index.html) or open it in any browser.

### Option 2: Run a Local Dev Server
```bash
# Clone the repository
git clone https://github.com/somsekhar799/ml-zero-to-hero.git
cd ml-zero-to-hero

# Start a simple HTTP server using Python
python3 -m http.server 8080
```
Then navigate to `http://localhost:8080` in your web browser.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript (ES6+)
- **Styling**: Vanilla CSS3 with Custom Properties / CSS Variables & Responsive Flex/Grid Layouts
- **Graphics & Animation**: HTML5 2D Canvas & Custom 3D Projection Math Engine
- **Math Rendering**: MathJax 3 (TeX / LaTeX)

---

## 📚 Curriculum References & Docs

- [Master Course Hub (`index.html`)](index.html)
- [Course Map (`COURSE-MAP.md`)](COURSE-MAP.md)
- [PyTorch Code Implementations (`reference/pytorch-implementations-cheatsheet.html`)](reference/pytorch-implementations-cheatsheet.html)
- [Classification & Ensemble Cheat Sheet (`reference/classification-ensemble-cheatsheet.html`)](reference/classification-ensemble-cheatsheet.html)
- [Glossary of Terms (`GLOSSARY.md`)](GLOSSARY.md)

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
