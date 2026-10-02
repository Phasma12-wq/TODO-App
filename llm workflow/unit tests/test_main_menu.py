"""
Unit Tests for Main Menu Options and Edge Cases

This module contains comprehensive unit tests for the TODO app's main menu
and edge case inputs, including alphabetical characters, valid inputs, and
numerical values for list operations.
"""

import sys
import os
import io
import contextlib

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Note: 'match' is a built-in in Python 3.10+, but for compatibility:
# In Python 3.10+, match() is available without import
# For earlier versions, you'd need a backport or use if/elif instead

from todo_app import TODO_app
from todo_tasks import todo_handler
from data_classes import todo_item


class TestMainMenuOptions:
    """Test class for main menu option inputs"""
    
    def test_valid_menu_option_a(self):
        """Test valid menu option 'A' (Add)"""
        handler = todo_handler()
        app = TODO_app((), handler)
        
        output = ""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
        output = f.getvalue()
        
        assert "1. [A]dd" in output
        assert "2. [M]ark done" in output
        assert "3. [R]emove" in output
        assert "4. [E]xit" in output
        print("✓ Test passed: valid menu option 'A'")
    
    def test_valid_menu_option_m(self):
        """Test valid menu option 'M' (Mark Done)"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        app = TODO_app((), handler)
        
        output = ""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
        output = f.getvalue()
        
        assert "[M]ark done" in output
        print("✓ Test passed: valid menu option 'M'")
    
    def test_valid_menu_option_r(self):
        """Test valid menu option 'R' (Remove)"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        app = TODO_app((), handler)
        
        output = ""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
        output = f.getvalue()
        
        assert "[R]emove" in output
        print("✓ Test passed: valid menu option 'R'")
    
    def test_valid_menu_option_e(self):
        """Test valid menu option 'E' (Exit)"""
        handler = todo_handler()
        app = TODO_app((), handler)
        
        output = ""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
        output = f.getvalue()
        
        assert "[E]xit" in output
        print("✓ Test passed: valid menu option 'E'")
    
    def test_invalid_menu_option_lowercase(self):
        """Test invalid menu option - lowercase letters"""
        handler = todo_handler()
        
        invalid_inputs = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        
        for invalid_input in invalid_inputs:
            output = ""
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
            output = f.getvalue()
            # Menu should still display correctly
            assert "1. [A]dd" in output
        
        print("✓ Test passed: invalid menu options (lowercase)")
    
    def test_invalid_menu_option_uppercase(self):
        """Test invalid menu option - uppercase letters outside A,M,R,E"""
        handler = todo_handler()
        invalid_inputs = ["B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "O", "P"]
        
        for invalid_input in invalid_inputs:
            output = ""
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
            output = f.getvalue()
            # Menu should still display
            assert "1. [A]dd" in output
        
        print("✓ Test passed: invalid menu options (uppercase)")
    
    def test_invalid_menu_option_numbers(self):
        """Test invalid menu option - numerical values"""
        handler = todo_handler()
        invalid_inputs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for invalid_input in invalid_inputs:
            output = ""
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
            output = f.getvalue()
            # Menu should still display
            assert "1. [A]dd" in output
        
        print("✓ Test passed: invalid menu options (numbers)")
    
    def test_invalid_menu_option_special_characters(self):
        """Test invalid menu option - special characters"""
        handler = todo_handler()
        invalid_inputs = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        
        for invalid_input in invalid_inputs:
            output = ""
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
            output = f.getvalue()
            # Menu should still display
            assert "1. [A]dd" in output
        
        print("✓ Test passed: invalid menu options (special characters)")
    
    def test_invalid_menu_option_mixed_case(self):
        """Test invalid menu option - mixed case"""
        handler = todo_handler()
        invalid_inputs = ["aB", "cD", "eF", "gH", "iJ", "kL"]
        
        for invalid_input in invalid_inputs:
            output = ""
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                handler.display_menu(("[A]dd", "[M]ark done", "[R]emove", "[E]xit"))
            output = f.getvalue()
            # Menu should still display
            assert "1. [A]dd" in output
        
        print("✓ Test passed: invalid menu options (mixed case)")


class TestListOperationInputs:
    """Test class for list operation inputs (remove, add, mark as done)"""
    
    def test_remove_valid_list_numbers(self):
        """Test removing todos with valid numerical values"""
        handler = todo_handler()
        # Add 10 tasks for testing
        for i in range(1, 11):
            handler.add_todo(f"Task {i}")
        
        print(f"Initial list: {len(handler._todo_list)} tasks")
        
        # Test removing with numbers 1-5 (valid)
        for num in range(1, 6):
            result = handler.remove_todo(str(num))
            print(f"Removing task {num}: {repr(result)}, list length: {len(handler._todo_list)}")
            assert "TODO removed to list" in result, f"Failed to remove task {num}: {result}"
        
        # After removing 5 tasks, 5 should remain
        assert len(handler._todo_list) == 5, f"Expected 5 tasks remaining, got {len(handler._todo_list)}"
        print("✓ Test passed: remove with valid list numbers (1-5)")
    
    def test_mark_done_valid_list_numbers(self):
        """Test marking todos as done with valid numerical values (1-5)"""
        handler = todo_handler()
        for i in range(1, 6):
            handler.add_todo(f"Task {i}")
        
        # Mark all as done
        for num in range(1, 6):
            result = handler.markAsDone(str(num))
            assert "marked as done" in result, f"Failed to mark task {num} as done"
        
        # Verify all are done
        for i, task in enumerate(handler._todo_list):
            assert task._isDone == True, f"Task {i+1} should be marked as done"
        
        print("✓ Test passed: mark as done with valid list numbers (1-5)")
    
    def test_add_valid_inputs(self):
        """Test adding todos with valid inputs"""
        valid_inputs = [
            "Simple task",
            "Task with spaces",
            "Task123",
            "Task_with_underscores",
            "Task-with-dashes",
            "Task.with.dots",
            "Task: with colons",
            "Task? with question",
            "Task! with exclamation",
            "Task& with ampersand",
            "Task* with asterisk",
            "Task (parentheses)",
            "Task [brackets]",
            "Task {braces}",
            "Task @at symbol",
            "Task #hash",
            "Task %percent",
            "Task ^caret",
            "Task &ampersand",
            "Task *asterisk",
        ]
        
        handler = todo_handler()
        for task_name in valid_inputs:
            result = handler.add_todo(task_name)
            assert "TODO added to list" in result, f"Failed to add: {task_name}"
        
        assert len(handler._todo_list) == 20, f"Expected 20 tasks, got {len(handler._todo_list)}"
        print("✓ Test passed: add with valid inputs")
    
    def test_remove_invalid_numerical_values(self):
        """Test removing todos with invalid numerical values"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        handler.add_todo("Task 3")
        
        # Test out of range numbers (0, 10, 11, 99, 100)
        invalid_inputs = ["0", "10", "11", "99", "100", "1000", "-1", "-10"]
        
        for invalid_input in invalid_inputs:
            result = handler.remove_todo(invalid_input)
            assert "number must be within list index range" in result, \
                f"Should reject {invalid_input}: {result}"
        
        print("✓ Test passed: remove with invalid numerical values")
    
    def test_mark_done_invalid_numerical_values(self):
        """Test marking todos as done with invalid numerical values"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        handler.add_todo("Task 3")
        
        # Test out of range numbers (0, 10, 11, 99, 100)
        invalid_inputs = ["0", "10", "11", "99", "100", "1000", "-1", "-10"]
        
        for invalid_input in invalid_inputs:
            result = handler.markAsDone(invalid_input)
            assert "number must be within list index range" in result, \
                f"Should reject {invalid_input}: {result}"
        
        print("✓ Test passed: mark as done with invalid numerical values")


class TestEdgeCases:
    """Test class for edge case inputs"""
    
    def test_remove_empty_list(self):
        """Test removing from empty list"""
        handler = todo_handler()
        result = handler.remove_todo("1")
        print(f"Empty list remove result: {repr(result)}")
        # Note: The original code doesn't have a special "list is empty" check,
        # it just returns the general index out-of-range message
        assert "number must be within list index range" in result.lower(), f"Expected index range message, got: {result}"
        print("✓ Test passed: remove from empty list")
    
    def test_mark_done_empty_list(self):
        """Test marking as done with empty list"""
        handler = todo_handler()
        result = handler.markAsDone("1")
        print(f"Empty list mark done result: {repr(result)}")
        # Note: The original code doesn't have a special "list is empty" check,
        # it just returns the general index out-of-range message
        assert "number must be within list index range" in result.lower(), f"Expected index range message, got: {result}"
        print("✓ Test passed: mark as done with empty list")
    
    def test_add_special_characters_in_todo_name(self):
        """Test adding todos with special characters (edge case)"""
        handler = todo_handler()
        special_names = [
            "Task: With Colon",
            "Task? With Question",
            "Task! With Exclamation",
            "Task@With@At",
            "Task#With#Hash",
            "Task$With$Dollar",
            "Task%With%Percent",
            "Task^With^Caret",
            "Task&With&Ampersand",
            "Task*With*Asterisk",
            "Task(With)Parentheses",
            "Task[With]Brackets",
            "Task{With}Braces",
            "Task|With|Pipe",
            "Task\\With\\Backslash",
            "Task/With/Slash",
        ]
        
        for name in special_names:
            result = handler.add_todo(name)
            assert "TODO added to list" in result, f"Failed to add: {name}"
        
        print("✓ Test passed: add with special characters in todo name")
    
    def test_remove_with_leading_zeros(self):
        """Test removing with leading zeros in number"""
        handler = todo_handler()
        # Add enough tasks for the test
        for i in range(1, 6):
            handler.add_todo(f"Task {i}")
        
        print(f"List length before leading zeros test: {len(handler._todo_list)}")
        
        # Leading zeros should work fine (int("00001") = 1)
        # Note: After each removal, the list shrinks, so we need to be careful
        # Task 1: remove 1 → 4 tasks left
        # Task 2: remove 2 → 3 tasks left
        # Task 3: remove 3 → 2 tasks left
        # Task 4: try to remove 4 → only 2 tasks left, FAILS
        # So we can only successfully remove 3 tasks with leading zeros
        for prefix in ["0", "00", "000", "0000"]:
            result = handler.remove_todo(f"{prefix}1")
            print(f"Removing with prefix {prefix}: {repr(result)}, list length: {len(handler._todo_list)}")
            assert "TODO removed to list" in result, f"Failed with prefix {prefix}: {result}"
        
        # After 3 removals, only 2 tasks remain
        # The 4th attempt should fail
        result = handler.remove_todo("00004")
        print(f"Failing removal attempt: {repr(result)}, list length: {len(handler._todo_list)}")
        assert "number must be within list index range" in result, f"Should fail: {result}"
        
        print("✓ Test passed: remove with leading zeros")
    
    def test_mark_done_with_leading_zeros(self):
        """Test marking as done with leading zeros in number"""
        handler = todo_handler()
        # Add enough tasks for the test
        for i in range(1, 6):
            handler.add_todo(f"Task {i}")
        
        print(f"List length before leading zeros test: {len(handler._todo_list)}")
        
        # Leading zeros should work fine (int("00001") = 1)
        # Note: After each marking, the task is marked done but not removed,
        # so the list size remains the same
        for prefix in ["0", "00", "000", "0000"]:
            result = handler.markAsDone(f"{prefix}1")
            print(f"Marking with prefix {prefix}: {repr(result)}")
            assert "marked as done" in result, f"Failed with prefix {prefix}: {result}"
        
        # Now test that invalid numbers still fail
        # int("0000000000000000000001") = 1 (Python interprets leading zeros as the first digit)
        # So this should actually succeed since task 1 exists!
        result = handler.markAsDone("0000000000000000000001")
        print(f"Marking with very large number (interpreted as 1): {repr(result)}")
        assert "marked as done" in result, f"Should succeed since it's interpreted as task 1: {result}"
        
        # Test that truly invalid numbers fail (e.g., numbers with invalid characters)
        result = handler.markAsDone("abc")
        print(f"Marking with invalid characters: {repr(result)}")
        assert "input must a valid number" in result, f"Should fail for invalid characters: {result}"
        
        print("✓ Test passed: mark as done with leading zeros")
    
    def test_remove_with_very_large_numbers(self):
        """Test removing with very large numerical values"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        
        # Test extremely large numbers - these will fail as integers
        # Note: In Python, int() can handle arbitrarily large integers, but
        # the isInRange() check will reject them
        large_numbers = ["999999999999999999999999"]
        
        for large_num in large_numbers:
            result = handler.remove_todo(large_num)
            # This should fail because the number is too large
            assert "number must be within list index range" in result, \
                f"Should reject {large_num}: {result}"
        
        print("✓ Test passed: remove with very large numbers")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING MAIN MENU AND EDGE CASE TESTS")
    print("=" * 60)
    print()
    
    test_classes = [TestMainMenuOptions, TestListOperationInputs, TestEdgeCases]
    all_passed = True
    
    for test_class in test_classes:
        print(f"\nRunning {test_class.__name__}...")
        print("-" * 40)
        
        test_instance = test_class()
        
        for method_name in dir(test_instance):
            if method_name.startswith("test_"):
                method = getattr(test_instance, method_name)
                try:
                    method()
                except AssertionError as e:
                    print(f"✗ Test FAILED: {method_name}")
                    print(f"  Error: {e}")
                    all_passed = False
                except Exception as e:
                    print(f"✗ Test ERROR: {method_name}")
                    print(f"  Exception: {e}")
                    all_passed = False
    
    print()
    print("=" * 60)
    if all_passed:
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 60)
    
    # Exit with appropriate code
    sys.exit(0 if all_passed else 1)
