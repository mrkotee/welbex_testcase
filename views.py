import flask
from base.models import Resource
from base.connector import create_session
from config import user, password, dbname, host, port


dbname = "psgr_dev"
user = "psgr_user"
password = "psgr_pswrd"


app = flask.Flask(__name__, static_folder='static/')


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return flask.render_template("index.html")


@app.route('/', methods=['POST'])
def get_table():
    page = int(flask.request.get_json()['page'])
    per_page = int(flask.request.get_json()['per_page'])
    session = create_session(user, password, dbname, host, port)
    resources = session.query(Resource).all()
    pages = len(resources) / per_page
    pages = round(pages + (0.5 if pages % 1 > 0 else 0))
    resources = resources[(page - 1) * per_page:page * per_page]
    res_dict = {'pages': pages, 'resources': [{'date': res.date.strftime("%Y-%m-%d"),
                                               'name': res.name,
                                               'amount': res.amount,
                                               'distance': res.distance} for res in resources]}
    session.close()
    return flask.jsonify(res_dict)


@app.route('/table', methods=['POST'])
def update_table():
    request = flask.request.get_json()['request']

    session = create_session(user, password, dbname, host, port)

    page = int(flask.request.get_json()['page'])
    per_page = int(flask.request.get_json()['per_page'])

    resources = session.query(Resource)
    if request == "sort":
        sort_field = flask.request.get_json()['sort_field']
        reverse = flask.request.get_json()['reverse']

        if sort_field == 'name':
            resources = set_query_order(resources, Resource.name, reverse)
        elif sort_field == 'amount':
            resources = set_query_order(resources, Resource.amount, reverse)
        elif sort_field == 'distance':
            resources = set_query_order(resources, Resource.distance, reverse)

    elif request == "search":
        page = 1
        search_field = flask.request.get_json()['search_field']
        search_opt = flask.request.get_json()['search_opt']
        search = flask.request.get_json()['search']

        if search_field == 'name':
            resources = set_filter_query(resources, Resource.name, search, search_opt)
        elif search_field == 'amount':
            resources = set_filter_query(resources, Resource.amount, search, search_opt)
        elif search_field == 'distance':
            resources = set_filter_query(resources, Resource.distance, search, search_opt)
        elif search_field == 'date':
            resources = set_filter_query(resources, Resource.date, search, search_opt)

    resources = resources.all()
    pages = len(resources) / per_page
    pages = round(pages + (0.5 if pages % 1 > 0 else 0))
    resources = resources[(page - 1) * per_page:page * per_page]
    res_dict = {'pages': pages, 'resources': [{'date': res.date.strftime("%Y-%m-%d"),
                                               'name': res.name,
                                               'amount': res.amount,
                                               'distance': res.distance} for res in resources]}
    session.close()
    return flask.jsonify(res_dict)


def set_query_order(query, instance, reverse):
    if reverse:
        return query.order_by(instance.desc())
    else:
        return query.order_by(instance.asc())


def set_filter_query(query, instance, search, operator):
    if operator == 'equals':
        return query.filter(instance == search)
    elif operator == 'into':
        return query.filter(instance.like(f'%{search}%'))
    elif operator == 'larger':
        return query.filter(instance > search)
    elif operator == 'less':
        return query.filter(instance < search)
