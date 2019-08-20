from flask import Blueprint

blueprint = Blueprint('{{ identifier }}', __name__,
                      url_prefix='/{{ identifier }}',
                      template_folder='templates')


@blueprint.route('/some/url')
def some_endpoint():
    return 'not implemented'
