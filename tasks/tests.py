from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Task  # Import your model
from .forms import TaskForm  # Import your form


class TaskTestCase(TestCase):
    def setUp(self):
        # Create test data for the Task model
        self.task = Task.objects.create(
            aircraft_registration='Test Aircraft',
            unit_description='Test Description',
            unit_part_number='Test Part Number',
            unit_serial_number='Test Serial Number',
            reported_snag='Test Snag',
            work_done='Test Work Done'
        )

    def test_task_creation(self):
        # Test if the task was created successfully
        self.assertEqual(self.task.__str__(), 'Task for Test Aircraft')

    def test_task_form_valid(self):
        # Test if the TaskForm is valid with valid data
        form_data = {
            'aircraft_registration': 'Test Aircraft',
            'unit_description': 'Test Description',
            'unit_part_number': 'Test Part Number',
            'unit_serial_number': 'Test Serial Number',
            'reported_snag': 'Test Snag',
            'work_done': 'Test Work Done'
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        # Test if the TaskForm is invalid with missing data
        form_data = {}  # Empty data
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_detail_view(self):
        # Test the detail view of a Task
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Aircraft')
        self.assertContains(response, 'Test Description')

    def test_task_update_view(self):
        # Test updating a Task
        updated_data = {
            'aircraft_registration': 'Updated Aircraft',
            'unit_description': 'Updated Description',
        }
        response = self.client.post(
            reverse('task_update', args=[self.task.id]), data=updated_data)
        # Redirect after successful update
        self.assertEqual(response.status_code, 302)

        # Retrieve the updated task from the database
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.aircraft_registration,
                         'Updated Aircraft')
        self.assertEqual(updated_task.unit_description, 'Updated Description')

    def test_task_delete_view(self):
        # Test deleting a Task
        response = self.client.post(
            reverse('task_delete', args=[self.task.id]))
        # Redirect after successful delete
        self.assertEqual(response.status_code, 302)

        # Verify that the task has been deleted
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task.id)


"""test_task_detail_view checks if the detail view of a Task displays the expected content.

test_task_update_view tests the ability to update a Task through a view, including checking the response status and verifying that the Task's fields are updated in the database.

test_task_delete_view tests the ability to delete a Task through a view, including checking the response status and verifying that the Task has been removed from the database."""
