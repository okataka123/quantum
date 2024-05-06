# 読みたい・読むべき・読んだ論文まとめ、ノート
## Survey
  - [A Survey on Quantum Machine Learning: Current Trends, Challenges, Opportunities, and the Road Ahead](https://arxiv.org/abs/2310.10315)
    - T.B.D.
    - 未読

## Paper

  - [[arxiv 2312.15657]Preconditioning for a Variational Quantum Linear Solver](https://arxiv.org/abs/2312.15657)
    - Hosakaさん論文。変分量子線形ソルバー(Variational Quantum Linear Solver, VQLS)を用いて解いた話(?)
    - 未読

### Quantum kernel関連

  - [[arxiv 2101.11020]Supervised quantum machine learning models are kernel methods](https://arxiv.org/abs/2101.11020)
    - この論文では、教師あり学習のフレームワーク内での量子機械学習モデルが、実質的には特定の種類の古典的な機械学習モデル、すなわちカーネル方に対応することを示している。カーネル法はデータを高次元空間にマッピングすることで非線形のパターンを捉える能力を持つ機械学習の手法です。この論文では、量子機械学習モデルがその量子特性を利用して高次元の特徴空間にデータをマッピングするカーネル法と等価であることを示している。この結果は、量子機械学習の理解と開発に重要な洞察を提供する。特に、量子コンピュータが古典的なコンピュータに比べてどのような利点を持つか、または持たないかについての理解を深めることができる。
    - 未読

### QNN関連
  - [[arxiv 1906.07682] Parameterized quantum circuits as machine learning models](https://arxiv.org/abs/1906.07682)
    - Benedetti et al.によって2019年に発表されたもので、パラメータ化された量子回路を機械学習モデルとして使用する方法について詳しく説明している。この研究では、量子コンピュータ上で実行可能なパラメータ化された量子回路を用いて、機械学習のタスクを解く新たなフレームワークを提案している。具体的には、量子回路のパラメータを調整することで、データの複雑なパターンを学習し、分類や回帰などのタスクを解くことが可能になる。このフレームワークは、量子コンピュータの計算能力を活用して、古典的な機械学習モデルが苦手とする特定のタスクに対して高いパフォーマンスを発揮する可能性がある。また、この研究は量子機械学習の分野において新たな研究の道を開くものとなった。
    - 未読

  - [[arxiv 1905.10876] Expressibility and entangling capability of parameterized quantum circuits for hybrid quantum-classical algorithms](https://arxiv.org/abs/1905.10876)
    - Sim et al.によって2019年に発表されたもので、古典-量子ハイブリッドアルゴリズムのためのパラメータ化された量子回路の表現力とエンタングル能力について調査している。この研究では、古典-量子ハイブリッドアルゴリズム（量子コンピュータと古典コンピュータを組み合わせて使用するアルゴリズム）の一部として使用されるパラメータ化された量子回路の特性について詳しく調査している。特に、量子回路の表現力（どのような量子状態を生成できるか）とエンタングル能力（量子ビット間の相互作用の強さ）に焦点を当てている。この研究の結果は、古典-量子ハイブリッドアルゴリズムの設計を実装において、どのような量子回路を選択すべきか、また、どのようにパラメータを調整すべきかという重要な示唆を提供している。これは、量子機械学習や量子最適化など、古典-量子ハイブリッドアルゴリズムが重要な役割を果たす分野において特に重要な研究となっている。
    - 未読

  - [[arxiv 1803.00745]Quantum Circuit Learning](https://arxiv.org/abs/1803.00745)
    - hybrid QNN関連
    - 量子回路を用いた新しい学習アルゴリズムを提案している。
    - この論文では、パラメータ化された量子回路（PQC）を用いて、データをエンコードし、その後の処理を行う新しい学習アルゴリズムを提案している。PQCは学習可能なパラメータを持つ量子ゲートのシーケンスで構成され、これにより量子状態を操作する。
    - 提案されたアルゴリズムは、古典的な機械学習の手法と同様に、訓練データを用いてパラメータを最適化する。しかし、量子回路を用いることで、高次元の複雑なデータ構造を効率的に表現することが可能となる。
    - この論文では、具体的な応用例として、分類問題や回帰問題、そして生成モデルへの応用を示している。また、提案されたアルゴリズムが、古典的なニューラルネットワークと比較して、一部の問題に対して優れた性能を示すことを示している。
    - この研究は、量子機械学習の分野における重要な一歩であり、量子コンピュータを用いた新しい学習アルゴリズムの開発に対する道筋を示している。

  - [[arxiv 1806.06871]Continuous-variable quantum neural networks](https://arxiv.org/abs/1806.06871)
    - hybrid QNN関連
    - この論文では、連続変数量子システムを用いた量子ニューラルネットワークの設計と実装について述べられています。連続変数量子システムは、量子情報処理において重要な役割を果たし、量子コンピュータの物理的実装にも利用されている。
    - 著者たちは、この連続変数量子システムを用いて、量子版のニューラルネットワークを設計し、その訓練方法を提案している。具体的には、量子版のバックプロパゲーション法を用いて、量子ニューラルネットワークのパラメータを最適化する方法が示されている。
    - また、この論文では提案された量子ニューラルネットが、特定のタスク（例えば、関数近似やパターン分類）において、古典的なニューラルネットワークと比較して優れた性能を示す可能性があることも示されている。

  - [[arxiv 2404.12741 Multi-Class Quantum Convolutional Neural Networks]](https://arxiv.org/abs/2404.12741)
    - 古典データの多クラス分類のための、量子畳み込みニューラルネットワーク(QCNN)。最適化過程は、パラメトライズ量子回路を通してクロスエントロピー損失を最小化することで行われる。分類クラスが多くなると、QCNNが古典を凌駕すると判明。参考：https://twitter.com/tweetnakasho/status/1782530820437361054

  - [[arxiv 2404.15377] Fourier Series Guided Design of Quantum Convolutional Neural Networks for Enhanced Time Series Forecasting](https://arxiv.org/abs/2404.15377)
    - 時系列予測タスクに1D QCNNを適用。変分量子回路が多次元Fourier級数で表現可能として先行研究をもとに、異なるアーキテクチャ・ansatzの能力を探索。自由パラメータ数がFoueier級数自由度を超えなくとも、高次Fourier関数が生成可能とした。https://twitter.com/tweetnakasho/status/1783558653783732635

  - [[arxiv 2404.15015] A Hybrid Quantum-Classical Physics-Informed Neural Network Architecture for Solving Quantum Optimal Control Problems](https://arxiv.org/abs/2404.15015)
    - Physics-Informed Neural Network(PINN: 物理情報ニューラルネットワーク)の枠組みを用いて、Pontryaginの最小原理を基礎とした量子最適制御問題のための量子古典ハイブリッド手法を提案。https://twitter.com/tweetnakasho/status/1783235404269064456


## Reference URLs
 - [最適なパラメータ化された量子回路を発見するための考え方](https://www.investor-daiki.com/qiskit-textbook-pqc)
    - Parametrized Quantum Circuits (PQCs)の説明あり。
    - PQCsとは、量子回路に調整可能なパラメータを用いたゲートを含む量子回路のこと。

 - [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/)
    - 様々な量子アルゴリズムが網羅的に掲載されたホームページ。

 - [Quantum Native Dojo](https://dojo.qulacs.org/ja/latest/index.html)
    - 量子コンピューティングのための勉強サイト。

 - [Qiskit Ecosystem 機械学習チュートリアル](https://qiskit-community.github.io/qiskit-machine-learning/locale/ja_JP/tutorials/index.html)
    - qiskit-communityによる、Qiskitを使った量子機械学習チュートリアルのページ。PyTorchによるqGANや量子AutoEncoderなど、話題が豊富。一通り読みたい。

 - [量子アニーリングの数理](https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/189516/1/bussei_el_033203.pdf)
    - 西森先生による量子アニーリングの物理に関する解説記事。

 - [量子近似最適化アルゴリズム(QAOA)を用いた複数制約条件付き最適化問題への応用](https://www.jstage.jst.go.jp/article/pjsai/JSAI2020/0/JSAI2020_4B3GS102/_pdf/-char/ja#:~:text=Quantum%20Approximation%20Optimization%20Algorithm%20(QAOA)%E3%81%AF%20QAA%20%E3%81%A8%E5%90%8C%E6%A7%98%E3%81%AB,%E8%A1%8C%E3%81%86%E9%87%8F%E5%AD%90%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82)
     - JSAI2020での電通大の発表。QAA(Quantum Adiabatic Algorithm, 量子断熱計算)とQAOAを用いて複数の組み合わせ最適化問題を解いた結果と、他のアルゴリズムを用いてこれらの問題を解いたときの結果を比較している。更に、QAOAのハイパラや変数パラメータの最適化手法を変化させることによる計算能力の変化について調べている。QAAやQAOAの入門的、かつ数理的な内容がとても整理されているので理解しやすい。

## Youtube動画
 - [QC4U(Quantum Computing for You)](https://www.youtube.com/watch?v=i_r3jP5yL7U&list=PLsBJ3psEqyr9cl5s4A6GZZNY0EwNkzL_6)
    - 大関先生の2022年QC4U(Quantum Computing for You)の動画再生リスト。QC4U2もあるので視聴すること！

 - [Quantum Tokyo](https://www.youtube.com/@QuantumTokyoo)
    - 有志の量子コンピューター勉強会によるYoutube動画チャンネル。QAOAやqGAN、グローバーのアルゴリズムなどがとてもわかり易い。
    - コミュニティのページは、https://quantum-tokyo.github.io/introduction/intro.html
    - 上記のコミュニティでは「Qiskitテキストブック 日本語版」と呼ばれる、量子コンピューティングや量子機械学習のテキストブック（Jupyter Notebook形式）が公開されている。

 - [量子コンピュータチャンネル](https://www.youtube.com/@blueqat428)
    - Blueqat社によるYoutube動画チャンネル

 - [Google Quantum AI](https://www.youtube.com/@GoogleQuantumAI)
    - Googleのやつ。

 - [Quantum ML](https://www.youtube.com/@quantumml8791)
    - 出どころ不明だがなんかよさげ。

## Quantum Programming関連
  - [IBM Quantum](https://quantum.ibm.com/)
    - IBM Quantumのページ。ここでアカウントを作ることによりIBMの実機量子コンピュータが利用できる。

  - [[arxiv 2404.12603] Qwerty: A Basis-Oriented Quantum Programming Language](https://arxiv.org/abs/2404.12603)
    - プログラマがゲートよりも表現力豊かに量子ビットを操作できる量子プログラミング言語Qwerty。ゲート選択という泥臭いタスクはコンパイラに任せる。新しい基底型とPythonとの相互運用性により高レベルの量子古典計算フレームワークを実現した。参考：https://x.com/tweetnakasho/status/1782519232959586390


### install方法関連
  - [IBM Quantum Documentation -Install Qiskit](https://docs.quantum.ibm.com/start/install#local)
  - [Qiskit Aer import error](https://discourse.jupyter.org/t/qiskit-aer-import-error/24377)
    - T.B.D.


## Keyword
  - HHL Argorithm
  - Variational Quantum Argorithm (VQA)
    - 古典量子ハイブリッドの一つ。最近ホットな話題らしい。
  - 量子Fourier変換 (QFT)
  - Reuploading QNN
  - Quantum AutoEncoder (QAE)
  - 量子カーネル法
  - NISQ
  - FTQC