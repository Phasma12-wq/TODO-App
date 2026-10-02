# Tools - Utility Modules for TODO App

This folder contains utility modules and helper functions used in the TODO App project. These tools provide reusable functionality for date/time operations, input validation, and other common tasks that support the core application logic.

## Table of Contents

- [Overview](#overview)
- [Purpose](#purpose)
- [Module Structure](#module-structure)
- [Available Tools](#available-tools)
- [Tool Details](#tool-details)
- [Usage Examples](#usage-examples)
- [Dependencies](#dependencies)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [Related Documentation](#related-documentation)

## Overview

The `tools` folder is part of the LLM Workflow project and serves as a centralized location for reusable utility functions and helper modules. While the current TODO App implementation uses only the Python standard library, this folder is designed to be extensible for future enhancements.

### Design Philosophy

- **Reusability**: Functions designed to be used across multiple projects
- **Single Responsibility**: Each tool module focuses on one specific task
- **Testing**: Every tool is thoroughly tested with edge cases
- **Documentation**: Clear usage examples and type hints

## Purpose

The tools folder serves three main purposes:

### 1. **Centralized Utilities**

Instead of scattering utility functions across multiple files, they are organized in a dedicated folder:

| Utility | Location | Purpose |
|---------|----------|---------|
| Date/Time Operations | `date.py` | Timestamp handling, formatting |
| Input Validation | `validation.py` (future) | General input sanitization |
| Error Handling | `errors.py` (future) | Custom exception classes |
| File Operations | `files.py` (future) | Safe file reading/writing |

### 2. **Testing Ground for New Features**

New utility functions can be developed and tested here before being integrated into the main application:

```python
# Development workflow
1. Create new tool in tools/
2. Write comprehensive tests
3. Add documentation
4. Move to main application if needed
```

### 3. **Future-Proof Architecture**

The folder structure anticipates future project requirements:

```
llm workflow/tools/
├── date.py              # Date/time utilities
├── validation.py        # Input validation helpers
├── errors.py            # Custom exception classes
├── files.py             # File operations
├── logging.py           # Logging utilities
└── ReadMe.md           # This file
```

## Module Structure

### Current Modules

| Module | Status | Description | Files |
|--------|--------|-------------|-------|
| `date.py` | ✅ Active | Date and time utilities | 1 file |
| `ReadMe.md` | ✅ Active | Module documentation | 1 file |

### Planned Modules

| Module | Status | Description | Priority |
|--------|--------|-------------|----------|
| `validation.py` | 📋 Planned | General input validation helpers | High |
| `errors.py` | 📋 Planned | Custom exception classes | Medium |
| `files.py` | 📋 Planned | Safe file operations | Medium |
| `logging.py` | 📋 Planned | Logging utilities | Low |

## Available Tools

### 1. Date Utilities (`date.py`)

**Status**: ✅ Active and tested

**Purpose**: Provides date and time manipulation functions for the TODO App

**Functions:**

| Function | Signature | Description |
|----------|-----------|-------------|
| `format_timestamp()` | `format_timestamp(dt: datetime) -> str` | Format datetime as readable string |
| `parse_timestamp()` | `parse_timestamp(s: str) -> datetime` | Parse string to datetime object |
| `get_current_timestamp()` | `get_current_timestamp() -> str` | Get current timestamp in standard format |
| `add_days()` | `add_days(dt: datetime, days: int) -> datetime` | Add/subtract days from datetime |
| `is_expired()` | `is_expired(dt: datetime, expires_in: int) -> bool` | Check if datetime is within expiration |

**Dependencies:**
- `datetime` (standard library)

**Testing:**
- ✅ 8 test cases covering all functions
- ✅ Edge cases: invalid dates, timezone handling
- ✅ 100% code coverage

### 2. Input Validation (Planned)

**Status**: 📋 Not yet implemented

**Purpose**: General input validation utilities

**Planned Functions:**

| Function | Description |
|----------|-------------|
| `validate_string_length()` | Check if string is within length limits |
| `validate_non_empty()` | Ensure string is not empty or whitespace-only |
| `validate_numeric_range()` | Check if number is within acceptable range |
| `validate_special_chars()` | Filter or validate special characters |

**Dependencies:**
- None (uses only standard library)

**Planned Testing:**
- 20+ test cases
- Edge cases: Unicode, very long strings, special characters

### 3. Error Handling (Planned)

**Status**: 📋 Not yet implemented

**Purpose**: Custom exception classes for TODO App

**Planned Classes:**

| Class | Purpose | Inherits |
|-------|---------|----------|
| `TodoError` | Base class for all TODO App errors | `Exception` |
| `InvalidInputError` | Raised for invalid user input | `TodoError` |
| `ListNotFoundError` | Raised when list doesn't exist | `TodoError` |
| `IndexOutOfBoundsError` | Raised for invalid list index | `TodoError` |

**Dependencies:**
- None (uses only standard library)

## Tool Details

### date.py - Date and Time Utilities

#### Function Signatures

```python
from datetime import datetime

def format_timestamp(dt: datetime) -> str:
    """Format a datetime object as a human-readable string.
    
    Args:
        dt: datetime object to format
        
    Returns:
        Formatted string in 'YYYY-MM-DD HH:MM:SS' format
    """


def parse_timestamp(s: str) -> datetime:
    """Parse a string into a datetime object.
    
    Args:
        s: String in 'YYYY-MM-DD HH:MM:SS' format
        
    Returns:
        datetime object
        
    Raises:
        ValueError: If string is not in correct format
    """


def get_current_timestamp() -> str:
    """Get the current timestamp in standard format.
    
    Returns:
        Formatted string of current time
    """


def add_days(dt: datetime, days: int) -> datetime:
    """Add or subtract days from a datetime object.
    
    Args:
        dt: Starting datetime
        days: Number of days to add (positive) or subtract (negative)
        
    Returns:
        New datetime with days added/subtracted
    """


def is_expired(dt: datetime, expires_in: int) -> bool:
    """Check if a datetime is within its expiration period.
    
    Args:
        dt: datetime to check
        expires_in: Number of days until expiration
        
    Returns:
        True if datetime is expired, False otherwise
    """
```

#### Usage Examples

```python
from date import format_timestamp, parse_timestamp, get_current_timestamp
from datetime import datetime, timedelta

# Get current timestamp
current = get_current_timestamp()
print(current)  # Output: 2024-10-02 15:30:45

# Parse a timestamp
parsed = parse_timestamp("2024-10-02 15:30:45")
print(parsed)   # Output: 2024-10-02 15:30:45

# Format a datetime
dt = datetime(2024, 10, 2, 15, 30, 45)
formatted = format_timestamp(dt)
print(formatted)  # Output: 2024-10-02 15:30:45

# Add days
days_later = add_days(dt, 7)
print(days_later)  # Output: 2024-10-09 15:30:45

# Check expiration
days_left = 5
expired = is_expired(dt, days_left)
print(expired)  # Output: False (if today is within 5 days)
```

#### Real-World Application

```python
# Scenario: Task expiration reminder
from date import is_expired, get_current_timestamp
from datetime import datetime, timedelta

def check_expired_tasks(tasks: list) -> list:
    """Find tasks that have expired.
    
    Args:
        tasks: List of task objects with 'created' datetime
        
    Returns:
        List of expired tasks
    """
    current = get_current_timestamp()
    expired = []
    
    for task in tasks:
        created = parse_timestamp(task.created)
        if is_expired(created, 30):  # Expire after 30 days
            expired.append(task)
    
    return expired
```

## Dependencies

### Required Dependencies

The tools folder currently has **zero external dependencies**:

| Module | Purpose | Version |
|--------|---------|--------|
| `datetime` | Date and time operations | Python 3.10+ |
| `os` (future) | File system operations | Python 3.10+ |
| `re` (future) | Regular expressions | Python 3.10+ |

### Optional Dependencies (Planned)

| Module | Purpose | Priority |
|--------|---------|----------|
| `pathlib` | Modern file paths | Medium |
| `logging` | Logging utilities | Low |
| `yaml` | Configuration files | Low |

### Installation

No installation required. All dependencies are part of the Python standard library.

```bash
# Verify Python installation
python --version
# Expected: Python 3.10.x or higher
```

## Best Practices

### When to Use Tools

| Use Tool | Don't Use Tool |
|----------|---------------|
| Reused across multiple files | One-time use |
| Complex logic that would clutter main code | Simple, inline operations |
| Needs unit testing | Ad-hoc calculations |
| Part of public API | Private helper |

### When NOT to Use Tools

| Don't Add Tool | Instead |
|----------------|----------|
| For a single use | Write inline |
| For very simple operations | Use built-in functions |
| For performance-critical paths | Benchmark first |
| For experimental code | Use a separate branch |

### Code Quality Standards

1. **Type Hints**: All functions must have type annotations
2. **Docstrings**: Every public function needs documentation
3. **Testing**: 100% test coverage required
4. **Error Handling**: Graceful degradation on failures
5. **Documentation**: Usage examples in ReadMe.md

### Example of Good Tool Design

```python
# ✅ Good: Reusable, documented, tested
def validate_email(email: str) -> bool:
    """Validate email format using basic regex.
    
    Args:
        email: Email address string
        
    Returns:
        True if email appears valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Test coverage:
# ✓ Valid emails
# ✓ Invalid emails
# ✓ Edge cases
# ✓ Performance benchmark
```

## Contributing

### Adding a New Tool

1. **Create Module**
   ```bash
   # In tools/ folder
   touch new_tool.py
   ```

2. **Write Implementation**
   ```python
   # new_tool.py
   from typing import Optional
   
   def my_tool_function(param: str) -> bool:
       """Docstring explaining what the tool does."""
       # Implementation
   ```

3. **Add Tests**
   ```bash
   # In unit tests/ folder
   touch test_new_tool.py
   ```

4. **Update ReadMe.md**
   - Add module to "Available Tools" table
   - Include function signatures
   - Add usage examples

5. **Submit for Review**
   - Run all tests
   - Check code style
   - Update documentation

### Code Review Checklist

- [ ] Function has clear name and docstring
- [ ] Type hints are complete and accurate
- [ ] All edge cases are tested
- [ ] No side effects (pure function)
- [ ] Error handling is appropriate
- [ ] Documentation is comprehensive
- [ ] Performance is acceptable
- [ ] No external dependencies added

## Related Documentation

### Main Project

- [TODO App ReadMe](../../ReadMe.md) - Main application documentation
- [LLM Workflow ReadMe](../ReadMe.md) - Workflow overview

### Generated Reports

- [Code Review](../documentation/document_code_review.txt) - Quality improvements
- [Output Analysis](../documentation/document_output.txt) - Bug reports

### Testing Resources

- [Unit Tests](../unit tests/test_todo_app.py) - Core functionality tests
- [Menu Tests](../unit tests/test_main_menu.py) - Edge case tests
- [Debug Script](../../test_debug.py) - Manual testing tool

### Code Files

- [date.py](date.py) - Date/time utilities
- [todo_tasks.py](../../todo_tasks.py) - Main business logic
- [todo_app.py](../../todo_app.py) - Application controller

## Quick Reference

| Task | Action | File |
|------|--------|------|
| Add new tool | See Contributing section | tools/
| Use date utilities | Import from `date.py` | date.py |
| Test a tool | Run unit tests | unit tests/
| Review code quality | See Code Review report | documentation/document_code_review.txt |
| Plan new tools | See Planned Modules | ReadMe.md |

## Support

For questions about the tools:

1. **Read this ReadMe.md** - Most answers are here
2. **Check unit tests** - Tests often include examples
3. **Review related code** - See how tools are used in main app
4. **Contact project lead** - For clarification on design decisions

## Appendix

### A. Module Statistics

| Metric | Value | Target |
|--------|-------|--------|
| Total Lines of Code | ~50 | < 100 per module |
| Functions | 5 | 1-10 per module |
| Test Cases | 8 | 100% coverage |
| Documentation | Complete | 100% docstrings |
| External Dependencies | 0 | 0 (standard library only) |

### B. Tool Naming Convention

```python
# Naming pattern
{noun}_function

# Examples
- validate_email
- format_timestamp
- parse_timestamp
- add_days
- is_expired
```

### C. Future Roadmap

```python
# Q4 2024
- Implement validation.py
- Add custom error classes
- Improve date.py performance

# Q1 2025
- Add logging utilities
- Implement file operations
- Create configuration parser

# Q2 2025
- Add database utilities
- Implement API helpers
- Create template engine
```

---

**Tools** - Reusable utility modules for the TODO App project
**Status**: ✅ Active (1 module), 📋 Planned (3 modules)
**Dependencies**: None (standard library only)
**Test Coverage**: 100% (8 test cases)
**Last Updated**: October 2, 2024

## Quick Start

```bash
# List available tools
ls tools/

# View date utilities
less tools/date.py

# Run tool tests
python ../unit tests/test_date.py

# Import and use a tool
python -c "from tools.date import format_timestamp; print(format_timestamp)"
```

## Related Links

- [Python Standard Library](https://docs.python.org/3/library/
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [datetime Module](https://docs.python.org/3/library/datetime.html)

---

*This module is part of the LLM Workflow project for the TODO App.*
*For questions about the tools, see the related documentation.*
*New tools are added quarterly based on project needs.*
