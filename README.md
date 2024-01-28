# Config File Parser

A Python module for parsing configuration files in INI format.

## Overview

This project provides a simple and flexible Python module for parsing configuration files in INI format. It allows you to read an INI file and convert it into a nested dictionary structure for easy access to configuration settings.

## Features

- Parse INI configuration files.
- Handle sections, keys, values, and comments.
- Support for various data types, including strings, integers, booleans, and floating-point numbers.
- Easy-to-use API for accessing configuration settings.

## Getting Started

### Installation

Using PyPI:

```bash
pip install iniutil
```

## Usage
```python
from iniutil import parse_ini
confg = parse_ini("path/to/config.ini")
```