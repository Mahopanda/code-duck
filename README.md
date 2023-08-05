# Code Duck

A Python code analysis tool using OpenAI.

## Prerequisites

Before using Code Duck, ensure you have an active account with OpenAI. You will need to generate an OpenAI API Key to utilize this tool. If you haven't already, [sign up for OpenAI](https://www.openai.com/signup/) and follow their documentation to obtain your API key.


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

## Analysis Output
After running Code Duck, an analysis file will be generated alongside each .py file in the specified directory. These files provide detailed feedback and suggestions for improving the code quality. Developers can refer to this analysis while editing the original code. Once the necessary changes are made, the analysis files can be deleted.

Remember, Code Duck provides insights based on OpenAI models, so while the feedback is often valuable, use your own judgment when considering the suggestions.


