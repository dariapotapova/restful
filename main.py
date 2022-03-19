from flask import Flask, jsonify, make_response
from flask_restful import Api

from data.db_session import global_init
from routes import jobs_blueprint, news_blueprint
from resources import NewsListResource, NewsResource
from resources.user_resourses import UsersResorses, UsersListResourses
from resources.jobs_resources import JobsResorses, JobsListResourses

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    global_init("db/blogs.db")
    app.register_blueprint(jobs_blueprint)
    app.register_blueprint(news_blueprint)
    api.add_resource(NewsResource, "/api/v2/news/<int:news_id>")
    api.add_resource(NewsListResource, "/api/v2/news")
    api.add_resource(UsersListResourses, '/api/v2/users')
    api.add_resource(UsersResorses, '/api/v2/users/<int:user_id>')
    api.add_resource(JobsListResourses, '/api/v2/jobs')
    api.add_resource(JobsResorses, '/api/v2/jobs/<int:job_id>')
    app.run()


if __name__ == '__main__':
    main()
