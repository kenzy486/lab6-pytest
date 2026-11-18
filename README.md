# Lab 6 - Coverage Testing with pytest

## Setup

```bash
pip install -r requirements.txt
```

## Run the tests

```bash
pytest
```

`pyproject.toml` already adds `--cov=src --cov-branch`, so this prints the
branch-coverage table too.

## HTML coverage report (open `htmlcov/index.html`)

```bash
pytest --cov-report=html
```

## Run one group of tests (custom markers)

```bash
pytest -m bank          # only the BankAccount tests
pytest -m text          # only the TextProcessor tests
pytest -m edge          # only the edge-case tests
pytest -m "not edge"    # everything except the edge cases
```

Run `pytest -m bank` and look at the coverage of `text_processor.py`:
the report shows what that group of tests does *not* reach.

## Project structure

```
├── src/
│   ├── bank_account.py         <- BankAccount class (has bugs!)
│   └── text_processor.py       <- TextProcessor class (has bugs!)
├── tests/
│   ├── test_bank_account.py    <- write your BankAccount tests here
│   └── test_text_processor.py  <- write your TextProcessor tests here
├── pyproject.toml              <- pytest + coverage settings, marker list
└── requirements.txt
```

## The annotations you will use

| Annotation | What it does |
|---|---|
| `@pytest.fixture` | Builds a fresh object for every test that asks for it by name |
| `@pytest.mark.parametrize` | Runs one test function once per row of inputs |
| `@pytest.mark.skip(reason=...)` | Does not run the test; the report shows `SKIPPED` |
| `@pytest.mark.xfail(reason=..., strict=True)` | Documents a known bug; the report shows `XFAIL` |
| `@pytest.mark.bank`, `text`, `edge` | Labels; run one group with `pytest -m <name>` |

(In Python these are called *decorators*.)

## Your task

1. Run `pytest`. Every test is `SKIPPED` and coverage is low.
2. Pick a test, remove its `@pytest.mark.skip` line, and replace `pass` with real code.
   The fixtures (`account`, `funded_account`, `bob`, `tp`) are already written - use them.
3. Where a `TODO` asks for it, write the `@pytest.mark.parametrize` table yourself.
4. Run `pytest --cov-report=html` and open `htmlcov/index.html`. Red and yellow lines
   show what your tests have not reached yet.
5. A failing test means you found a bug. Document it with
   `@pytest.mark.xfail(reason="BUG #N: ...", strict=True)` and keep going.
6. Finish when no test is skipped, all 9 bugs are documented, and branch coverage is 90% or more.
7. Optional: fix a bug in `src/`. The `strict=True` test will now fail with `XPASS` -
   that is pytest telling you to remove the `xfail` annotation.
