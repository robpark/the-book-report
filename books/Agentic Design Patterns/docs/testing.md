# Testing Strategy

## Overview

This test suite is designed to protect against regressions when upgrading packages or Python versions.

**Note**: All commands in this document should be run from the `code-examples/1-prompt-chaining/` directory.

## Test Types

### 1. **Structural Tests** (Fast, No API calls)
- `test_chain_structure()` - Verifies the chain object is created correctly
- `test_chain_invoke_signature()` - Ensures the chain has the expected interface

**Protection Level**: ⭐⭐⭐ High
- Catches breaking API changes in langchain (e.g., if `invoke()` method is renamed)
- Verifies the chain composition still works after upgrades

### 2. **Unit Tests with Mocks** (Fast, No API calls)
- `test_chain_execution_flow()` - Tests the full chain execution with mocked LLM
- `test_extraction_step()` - Tests individual chain components
- `test_chain_handles_empty_input()` - Tests edge cases

**Protection Level**: ⭐⭐ Medium
- Verifies your code logic works correctly
- Tests chain composition and data flow
- **Does NOT protect against**: Breaking changes in langchain's internal API

### 3. **Integration Tests** (Slow, Requires API key, Costs money)
- `test_chain_with_real_api()` - Tests with actual OpenAI API calls

**Protection Level**: ⭐⭐⭐⭐⭐ Very High
- Catches ALL breaking changes (API, Python version, dependencies)
- Verifies end-to-end functionality
- **Use sparingly**: Run before major upgrades or in CI

## Running Tests

### Fast unit tests (default):
```bash
uv run pytest
```

### Include integration tests:
```bash
uv run pytest --run-integration
```

### Skip integration tests explicitly:
```bash
uv run pytest -m "not integration"
```

## Upgrade Protection Strategy

### Before Upgrading Packages:

1. **Run all unit tests** (fast, free):
   ```bash
   uv run pytest
   ```

2. **Run integration test** (slow, costs money):
   ```bash
   uv run pytest --run-integration
   ```

3. **Upgrade packages**:
   ```bash
   uv sync --upgrade
   ```

4. **Re-run tests** to verify nothing broke:
   ```bash
   uv run pytest --run-integration
   ```

### Before Upgrading Python:

1. **Test with new Python version**:
   ```bash
   uv venv --python 3.14
   uv sync
   uv run pytest --run-integration
   ```

2. **Update `.python-version` and `pyproject.toml`** if tests pass

## What Tests Protect Against

✅ **Protected:**
- Breaking changes in langchain API (structural tests)
- Your code logic errors (unit tests)
- End-to-end functionality (integration tests)
- Python version incompatibilities (integration tests)

❌ **Not Protected:**
- Subtle behavior changes in LLM responses (non-deterministic)
- Performance regressions
- New deprecation warnings (use `ruff check` for this)

## Recommendations

1. **Always run unit tests** before committing
2. **Run integration tests** before major upgrades
3. **Pin dependency versions** in production (use `uv.lock`)
4. **Test Python upgrades** in a separate branch first
5. **Monitor langchain changelog** for breaking changes

## Future Improvements

Consider adding:
- **Snapshot testing** for LLM outputs (with tolerance for non-determinism)
- **Performance benchmarks** to catch regressions
- **CI/CD integration** to run tests on every PR
- **Multi-version testing** with tox or GitHub Actions matrix

