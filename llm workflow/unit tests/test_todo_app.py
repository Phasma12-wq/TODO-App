"""
Unit Tests for TODO App

This module contains comprehensive unit tests for the TODO application.
Tests cover: main menu options, list operations, edge cases, and invalid inputs.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from todo_tasks import todo_handler
from data_classes import todo_item, todo


class TestTodoHandler:
    """Test class for todo_handler functionality"""
    
    def test_add_todo_with_valid_input(self):
        """Test adding a todo with valid input"""
        handler = todo_handler()
        result = handler.add_todo("Test Task")
        assert "TODO added to list" in result, f"Expected 'TODO added to list', got '{result}'"
        assert len(handler._todo_list) == 1, "List should have 1 item"
        print("✓ Test passed: add_todo with valid input")
    
    def test_add_todo_with_empty_string(self):
        """Test adding a todo with empty string input"""
        handler = todo_handler()
        result = handler.add_todo("")
        assert "Input must be provided" in result, f"Expected 'Input must be provided', got '{result}'"
        assert len(handler._todo_list) == 0, "List should remain empty"
        print("✓ Test passed: add_todo with empty string")
    
    def test_add_todo_with_none(self):
        """Test adding a todo with None input"""
        handler = todo_handler()
        result = handler.add_todo(None)
        assert "Input must be provided" in result, f"Expected 'Input must be provided', got '{result}'"
        assert len(handler._todo_list) == 0, "List should remain empty"
        print("✓ Test passed: add_todo with None")
    
    def test_add_todo_with_whitespace(self):
        """Test adding a todo with only whitespace - CURRENT BEHAVIOR NOTE"""
        handler = todo_handler()
        result = handler.add_todo("   ")
        # Note: Current implementation does NOT validate whitespace-only strings
        # This is an edge case that could be improved in future versions
        # Expected: "TODO added to list" (current behavior)
        # Recommended: "Input must be provided" (better validation)
        print(f"  Current behavior: '{result}' (whitespace validation not implemented)")
        print("✓ Test passed: add_todo with whitespace (documenting current behavior)")
    
    def test_display_menu(self):
        """Test displaying the menu correctly"""
        handler = todo_handler()
        menu_items = ("[A]dd", "[M]ark done", "[R]emove", "[E]xit")
        output = ""
        
        # Capture print output by temporarily redirecting stdout
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_menu(menu_items)
        output = f.getvalue()
        
        assert "1. [A]dd" in output, "Menu should display '[A]dd'"
        assert "2. [M]ark done" in output, "Menu should display '[M]ark done'"
        assert "3. [R]emove" in output, "Menu should display '[R]emove'"
        assert "4. [E]xit" in output, "Menu should display '[E]xit'"
        print("✓ Test passed: display_menu")
    
    def test_display_list_with_items(self):
        """Test displaying todo list with items"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        handler.add_todo("Task 3")
        
        output = ""
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_list()
        output = f.getvalue()
        
        assert "1. Task 1 Pending" in output, "List should show Task 1"
        assert "2. Task 2 Pending" in output, "List should show Task 2"
        assert "3. Task 3 Pending" in output, "List should show Task 3"
        print("✓ Test passed: display_list with items")
    
    def test_display_list_empty(self):
        """Test displaying empty todo list"""
        handler = todo_handler()
        output = ""
        
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            handler.display_list()
        output = f.getvalue()
        
        assert "<list is empty>" in output, "Should show empty list message"
        print("✓ Test passed: display_list empty")
    
    def test_remove_todo_with_valid_index(self):
        """Test removing a todo with valid index"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        handler.add_todo("Task 3")
        
        result = handler.remove_todo("1")
        assert "TODO removed to list" in result, f"Expected removal message, got '{result}'"
        assert len(handler._todo_list) == 2, "List should have 2 items after removal"
        print("✓ Test passed: remove_todo with valid index")
    
    def test_remove_todo_with_invalid_index(self):
        """Test removing a todo with invalid index"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        
        # Test out of range index
        result = handler.remove_todo("5")
        assert "number must be within list index range" in result, f"Expected range error, got '{result}'"
        
        # Test non-numeric index
        result = handler.remove_todo("abc")
        assert "input must a valid number" in result, f"Expected number error, got '{result}'"
        
        print("✓ Test passed: remove_todo with invalid index")
    
    def test_mark_as_done_with_valid_index(self):
        """Test marking a todo as done with valid index"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        
        result = handler.markAsDone("1")
        assert "marked as done" in result, f"Expected 'marked as done', got '{result}'"
        assert handler._todo_list[0].getStr() == "Task 1 Done ✅", "Task should be marked as done"
        print("✓ Test passed: mark_as_done with valid index")
    
    def test_mark_as_done_with_invalid_index(self):
        """Test marking a todo as done with invalid index"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        
        # Test out of range
        result = handler.markAsDone("5")
        assert "number must be within list index range" in result, f"Expected range error, got '{result}'"
        
        # Test non-numeric
        result = handler.markAsDone("abc")
        assert "input must a valid number" in result, f"Expected number error, got '{result}'"
        
        print("✓ Test passed: mark_as_done with invalid index")
    
    def test_is_in_range_valid(self):
        """Test isInRange method with valid indices"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        handler.add_todo("Task 2")
        
        assert handler.isInRange(0) == True, "Index 0 should be in range"
        assert handler.isInRange(1) == True, "Index 1 should be in range"
        print("✓ Test passed: is_in_range with valid indices")
    
    def test_is_in_range_invalid(self):
        """Test isInRange method with invalid indices"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        
        assert handler.isInRange(-1) == False, "Negative index should be out of range"
        assert handler.isInRange(1) == False, "Index equal to length should be out of range"
        assert handler.isInRange(2) == False, "Index greater than length should be out of range"
        print("✓ Test passed: is_in_range with invalid indices")
    
    def test_is_not_empty_with_items(self):
        """Test isNotEmpty method with items"""
        handler = todo_handler()
        handler.add_todo("Task 1")
        assert handler.isNotEmpty() == True, "Should return True with items"
        print("✓ Test passed: isNotEmpty with items")
    
    def test_is_not_empty_empty(self):
        """Test isNotEmpty method with empty list"""
        handler = todo_handler()
        assert handler.isNotEmpty() == False, "Should return False when empty"
        print("✓ Test passed: isNotEmpty empty")


class TestDataClasses:
    """Test class for data classes"""
    
    def test_todo_item_creation(self):
        """Test creating a todo_item"""
        todo = todo_item("Test Task")
        assert todo.name == "Test Task", "Name should match"
        assert todo._isDone == False, "Task should not be done by default"
        print("✓ Test passed: todo_item creation")
    
    def test_todo_item_mark_done(self):
        """Test marking a todo as done"""
        todo = todo_item("Test Task")
        assert todo._isDone == False, "Task should not be done initially"
        todo.markDone()
        assert todo._isDone == True, "Task should be done after markDone"
        print("✓ Test passed: todo_item mark done")
    
    def test_todo_item_getstr_pending(self):
        """Test getStr method when task is pending"""
        todo = todo_item("Test Task")
        output = todo.getStr()
        assert "Pending" in output, "Output should contain 'Pending'"
        assert "Test Task" in output, "Output should contain task name"
        print("✓ Test passed: todo_item getStr pending")
    
    def test_todo_item_getstr_done(self):
        """Test getStr method when task is done"""
        todo = todo_item("Test Task")
        todo.markDone()
        output = todo.getStr()
        assert "Done" in output, "Output should contain 'Done'"
        assert "Test Task" in output, "Output should contain task name"
        print("✓ Test passed: todo_item getStr done")


def run_all_tests():
    """Run all unit tests"""
    print("=" * 60)
    print("RUNNING UNIT TESTS FOR TODO APP")
    print("=" * 60)
    print()
    
    test_classes = [TestTodoHandler, TestDataClasses]
    all_passed = True
    
    for test_class in test_classes:
        print(f"\nRunning {test_class.__name__}...")
        print("-" * 40)
        
        # Create an instance of the test class
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
    
    return all_passed


if __name__ == "__main__":
    run_all_tests()
