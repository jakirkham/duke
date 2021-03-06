# duke -- Dataset Understanding via Knowledge-base Embeddings

1. First, you should download wiki2vec model (English Wikipedia) using a torrent as described on this link: https://github.com/idio/wiki2vec -- untar it at a preferred location and note it. 

2. Clone this repository, open main.py and modify embedding_path variable to the aforementioned wiki2vec model location.

3. Using python3.5+, pip3 install required libraries in requirements.txt.

4. Identify a dataset of interest, and specify its path in main.py (via dataset_path variable).

5. Finally, run it as follows, and enjoy the magic:

```bash
python3 main.py
```

Note: experimental and continuously improving pip installable version of the program Duke can be obtained as
```bash
pip3 install git+https://github.com/NewKnowledge/duke@pa/pip
```
