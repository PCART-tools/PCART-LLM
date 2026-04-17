# LLM/findDiffer Notes

Language / 语言: [中文](README.md) | **English**

This directory stores patch files for the newly added LLM-based `findDiffer` implementation family. These patches show the added content relative to the baseline where the original implementation did not contain these files. Because these files did not exist in the original implementation, the corresponding `.diff` patch headers show them as added from `/dev/null`.

## Naming Rules

- `Rule`: implementation based on a "natural-language rule description strategy". The core idea is to describe the original rule logic as a prompt and let the model directly output parameter change results.
- `Hybrid`: implementation based on a "hybrid strategy". The core idea is to first perform a hard-rule preprocessing pass, then leave the remaining difficult cases to the LLM.
- `Null`: no additional semantic information is provided to the LLM; only the parameter list is given.
- `String`: provides `docstring` as semantic information.
- `Code`: provides `source code` as semantic information.
- `V4`: uses `response_format` from the OpenAI Python SDK to accept `json_schema`.
- `V5`: places the stringified `json_schema` directly into the user prompt and asks the model to follow the textual constraints.
- `Split`: splits the original one-shot LLM request into multiple chained requests, completing the difference analysis through smaller focused stages.

## Special File

- [findDifferRuleNullSplitV5.diff](./findDifferRuleNullSplitV5.diff): the added patch corresponding to `findDifferRuleNullSpilitV5.py`. Based on `findDifferRuleNullV5.py`, it splits the original one-shot prompt and `json_schema` into multiple chained requests, reducing the complexity of a single request and dividing the analysis into clearer stages.
- [findDifferRuleStringSplitV5.diff](./findDifferRuleStringSplitV5.diff): the added patch corresponding to `findDifferRuleStringSplitV5.py`. Based on `findDifferRuleStringV5.py`, it adds a multi-step chained request flow while continuing to provide `docstring` as semantic information, allowing each step to judge parameter changes in a more focused context.

## File Characteristics

- [findDifferHybridNullV4.diff](./findDifferHybridNullV4.diff): hybrid strategy, no semantic information, using `response_format + json_schema`.
- [findDifferHybridNullV5.diff](./findDifferHybridNullV5.diff): hybrid strategy, no semantic information, using schema embedded in the prompt.
- [findDifferHybridStringV4.diff](./findDifferHybridStringV4.diff): hybrid strategy, provides `docstring`, using `response_format + json_schema`.
- [findDifferHybridStringV5.diff](./findDifferHybridStringV5.diff): hybrid strategy, provides `docstring`, using schema embedded in the prompt.
- [findDifferHybridCodeV4.diff](./findDifferHybridCodeV4.diff): hybrid strategy, provides `source code`, using `response_format + json_schema`.
- [findDifferHybridCodeV5.diff](./findDifferHybridCodeV5.diff): hybrid strategy, provides `source code`, using schema embedded in the prompt.
- [findDifferRuleNullV4.diff](./findDifferRuleNullV4.diff): rule strategy, no semantic information, using `response_format + json_schema`.
- [findDifferRuleNullV5.diff](./findDifferRuleNullV5.diff): rule strategy, no semantic information, using schema embedded in the prompt.
- [findDifferRuleStringV4.diff](./findDifferRuleStringV4.diff): rule strategy, provides `docstring`, using `response_format + json_schema`.
- [findDifferRuleStringV5.diff](./findDifferRuleStringV5.diff): rule strategy, provides `docstring`, using schema embedded in the prompt.
