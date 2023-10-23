# Deep learning environment
You need:
- Python 3.6 or above
- `pip install <packages>`: `pip` is a package manager for Python (like rpm, apt, ...). You can install python packages via rpm, apt, ... but `pip` give you more choice and most of the time is OS independant.
- `scikit-learn` is a nice python package that have all sort of Machine Learning functions, enough for beginner.

# Step 1: Python
On Window, the simpliest way is to have python inside WSL.

WSL is a Linux inside Windows. The default Linux is Ubuntu that also ship python3.x

Install WSL: https://learn.microsoft.com/en-us/windows/wsl/install

# Step 2: install python packages

`pip3 install --user notebook==6.* pandas scikit-learn matplotlib`

This will automatically install all the dependant packages (like rpm would do)

# Step 3: get this code from github
```
git clone https://github.com/mhtrinh/diabete_mlp
cd diabete_mlp
```

# Step 4: start the Jupyter notebook
Jupyter notebook allow you to run one set of code at the time. Each set are inside a "cell". You can run the cells in any  order, rather than just top to bottom. All variable stay in memory across cell run. This feel like running `gdb`'s  `watch` but in better as you can tell what line of code to re-run without re-running the entire code.

In jupyter notebook, "Shift + Enter" to execute a cell

Start a jupyter notebook with `jupyter notebook`. Follow the instruction in stdout: basically, open your web browser and go to the given local url

Then click on the file `diabete_MLP.ipynb`