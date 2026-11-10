from flask import jsonify
from app.api import bp


@bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})
