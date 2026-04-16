# map.diff Notes

Language / 语言: [中文](README.md) | **English**

The patch file in this directory is [map.diff](./map.diff). It describes the differences from [PCART-original/Map/map.py](../../PCART-original/Map/map.py) to [PCART-modified/Map/map.py](../../PCART-modified/Map/map.py).

## Patch Coverage

- After dynamic matching succeeds, writes the `docstring` and `sourceCode` produced by `dynamicMatch.py` back into the matching result dictionary.
- Adjusts the data source for the LLM path with semantic information so that it preferentially uses semantic fields from the current matching result instead of reading from `_dynamicMatch.json` again.

## Patch Significance

- Ensures that the `docstring` and `sourceCode` of the old and new versions do not overwrite each other.
- Ensures that the semantic material seen by subsequent LLM analysis strictly corresponds to the current version.
