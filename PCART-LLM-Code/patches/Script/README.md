# dynamicMatch.diff Notes

Language / 语言: [中文](README.md) | **English**

The patch file in this directory is [dynamicMatch.diff](./dynamicMatch.diff). It describes the differences from [PCART-original/Script/dynamicMatch.py](../../PCART-original/Script/dynamicMatch.py) to [PCART-modified/Script/dynamicMatch.py](../../PCART-modified/Script/dynamicMatch.py).

## Patch Coverage

- Adds logic to extract `inspect.getdoc(eval(api))` and `inspect.getsource(eval(api))` when dynamic matching succeeds.
- Writes the resulting `docstring` and `sourceCode` into the serialized `matchDict`.

## Patch Significance

- Allows the dynamic matching stage to output both signature information and semantic auxiliary material.
- Provides stable, near-source input for the `String` and `Code` categories of LLM difference analysis implementations.
