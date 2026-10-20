# EaaS Builder Python Test

Test extension for CloudBlue Connect EaaS that logs the Python version it runs on. Each tag
declares a different `python` constraint in `pyproject.toml`; nothing else changes. It is meant
to check how an extension with each constraint is built and run on runner images with
Python 3.10 and Python 3.12.

| Tag | `python` | Scenario |
| --- | --- | --- |
| `1.0.0` | `>=3.10,<3.13` | 3.10 and 3.12 |
| `1.10.0` | `>=3.10,<3.11` | 3.10 only |
| `1.11.0` | `>=3.11,<3.12` | neither (3.11), no `poetry.lock` |
| `1.12.0` | `>=3.12,<3.13` | 3.12 only |

## Expected results

| Tag | Runner with Python 3.12 | Runner with Python 3.10 |
| --- | --- | --- |
| `1.0.0` | runs on 3.12 | runs on 3.10 |
| `1.10.0` | image build fails at `pip install` (Requires-Python) | runs on 3.10 |
| `1.11.0` | build fails in Poetry: no compatible Python | same |
| `1.12.0` | runs on 3.12 | image build fails at `pip install` (Requires-Python) |

## Checking the Python version

The events application has one schedulable method, **Python check**. Create a schedule for it
in the DevOps module and run it: it logs, at level ERROR, a line like

```
PYTHON-CHECK version=1.10.0 python=3.10.19 executable=/usr/local/bin/python sys.version='...'
```
