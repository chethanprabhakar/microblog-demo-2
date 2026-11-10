from app.api import bp


@bp.route('/health', methods=['GET'])
def health():
    return {'status': 'ok'}, 200
