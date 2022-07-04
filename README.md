# My Python Kata

[![PyPI](https://img.shields.io/pypi/v/my-python-kata.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/my-python-kata.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/my-python-kata)][python version]
[![License](https://img.shields.io/pypi/l/my-python-kata)][license]

[![Read the documentation at https://my-python-kata.readthedocs.io/](https://img.shields.io/readthedocs/my-python-kata/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/scalasm/my-python-kata/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/scalasm/my-python-kata/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/my-python-kata/
[status]: https://pypi.org/project/my-python-kata/
[python version]: https://pypi.org/project/my-python-kata
[read the docs]: https://my-python-kata.readthedocs.io/
[tests]: https://github.com/scalasm/my-python-kata/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/scalasm/my-python-kata
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Disclaimer

This is second fresh attempt to study Computer Algorithms and Data Structures by following the
[MIT Course](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb).

In this repository I'm using Python, in order to also gain some practice, like in [Kata](https://en.wikipedia.org/wiki/Kata)! I try to make them as good as possible but I take no responsibility for any problems
or errors you may incur if you try to use them :)

## Features

### Arrays and Matrices

- [Finding peaks in arrays](./docs/algorithms/FindPeak.md), both 1-dimensional and 2-dimensional arrays.
- Merge of N arrays (lists)

### Graphs

- Graph (using adjacency lists for its implementation)
- Breadth-first Traversal (BFT)

### Heap

- MaxHeap and basic operations

## Requirements

- Python 3.10
- Poetry 1.1.13 or better
- Nox 1.0.1

As alternative, you can use the bundled remote container configuration for Visual Studio Code.

## Installation

You can install _My Python Kata_ via [pip] from [PyPI]:

```console
$ pip install my-python-kata
```

## Usage

Open this project in Visual Studio Code with remote container extenstion and have fun :)

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_My Python Kata_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/scalasm/my-python-kata/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/scalasm/my-python-kata/blob/main/LICENSE
[contributor guide]: https://github.com/scalasm/my-python-kata/blob/main/CONTRIBUTING.md
[command-line reference]: https://my-python-kata.readthedocs.io/en/latest/usage.html
