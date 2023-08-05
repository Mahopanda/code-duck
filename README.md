# Code Duck

A Python code analysis tool using OpenAI.

## Installation

Before the package is available on PyPI, you can build and install it directly from the source code.

### Build from Source
1. Clone the repository:

```bash
git clone https://github.com/Mahopanda/code-duck.git
cd code-duck
```

2. Build the package:

```bash
python3 setup.py bdist_wheel
```

3. Install the package from the built wheel:
```bash
pip install dist/code_duck-<version>-py3-none-any.whl

```

Replace <version> with the version number of the package. For example, if the version is 0.1.0, then the filename would be code_duck-0.1.0-py3-none-any.whl.


## Usage
code-duck -d /path/to/your/directory -k your_openai_key -m model_name -p

- -d: Directory to analyze.
- -k: OpenAI API Key.
- -m: OpenAI Model to use.
- -p: Show progress.

