from flask import Blueprint, jsonify

bp = Blueprint("api", __name__)

@bp.get("/health")
def health():
    return jsonify(status="ok"), 200

@bp.get("/items")
def items():
    return jsonify(items=[{"id": 1, "name": "widget"}])

