from flask import Blueprint

zsaxf = Blueprint('zsaxf_blue', __name__, url_prefix='/axf/')

# 测试，不用理它
@zsaxf.route('/test/')
def test():

    return 'testok'