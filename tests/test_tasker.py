import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("tasker", PROJECT_ROOT / "tasker.py")
tasker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tasker
SPEC.loader.exec_module(tasker)


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.previous_directory = Path.cwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.previous_directory)
        self.temp_dir.cleanup()

    def test_task_lifecycle(self):
        tasker.add_task("Buy groceries")
        tasker.add_task("Read book")

        tasker.complete_task(1)
        tasker.delete_task(1)

        with open("tasks.json", "r") as tasks_file:
            tasks = json.load(tasks_file)

        self.assertEqual(
            tasks,
            [
                {
                    "id": 1,
                    "description": "Read book",
                    "status": "pending",
                    "created_at": tasks[0]["created_at"],
                }
            ],
        )

    def test_list_empty_tasks(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            tasker.list_tasks()

        self.assertIn("No tasks found", output.getvalue())


if __name__ == "__main__":
    unittest.main()
