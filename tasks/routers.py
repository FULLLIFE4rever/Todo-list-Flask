from flask import Blueprint, jsonify, request

from exceptions.exeptions import TaskValidationError

from .models import Task
from .schemas import STasksInfo
from .services import TaskService

tasks_route = Blueprint("route", __name__, url_prefix="/tasks")


@tasks_route.errorhandler(TaskValidationError)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@tasks_route.route("", methods=["GET"])
def get_tasks():
    tasks = TaskService.find_all()
    return jsonify(STasksInfo(tasks=tasks).model_dump())


@tasks_route.route("", methods=["POST"])
def add_task():
    """Add new task"""
    data = request.get_json()
    if TaskService.is_valid(0, **data):
        raise TaskValidationError("Invalid data", 400)
    task = TaskService.add(**data)["Task"]
    return jsonify(task.to_dict()), 201


@tasks_route.route("/<int:model_id>", methods=["GET"])
def get_task_by_id(model_id: int):
    """Find task by id"""
    task = TaskService.find_by_id(model_id)

    if not task:
        return jsonify({"message": "Not found"}), 404
    return jsonify(Task(**task).to_dict()), 200


@tasks_route.route("/<int:model_id>", methods=["PUT"])
def update_task_by_id(model_id: int):
    """Update task by id"""
    data = request.get_json()
    task = TaskService.find_by_id(model_id=model_id)
    if not task:
        return jsonify({"message": "Not found"}), 404
    if TaskService.is_valid(1, **data):
        raise TaskValidationError("Invalid data", 400)
    task = TaskService.update(model_id, **data)
    return jsonify(Task(**task).to_dict()), 200


@tasks_route.route("/<int:model_id>", methods=["DELETE"])
def delete_task_by_id(model_id: int):
    """Delete task by id"""
    task = TaskService.find_by_id(model_id)
    if not task:
        raise TaskValidationError("Not found", 404)
    TaskService.delete(model_id)
    return jsonify({"message": "deleted"}), 204
