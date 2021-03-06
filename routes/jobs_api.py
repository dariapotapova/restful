from datetime import datetime

import flask
from flask import jsonify, request

from data.db_session import create_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs',
    __name__,
    template_folder='templates',
    url_prefix="/api/jobs"
)


@blueprint.route('/')
def get_jobs():
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [job.to_dict(only=("id",
                                   "job",
                                   "work_size",
                                   "collaborators",
                                   "end_date",
                                   "start_date",
                                   "is_finished",
                                   "team_leader"))
                 for job in jobs]
        }
    )


@blueprint.route('/<int:jobs_id>', methods=['GET'])
def get_one_job(jobs_id):
    db_sess = create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': job.to_dict(only=("id",
                                      "job",
                                      "work_size",
                                      "collaborators",
                                      "end_date",
                                      "start_date",
                                      "is_finished",
                                      "team_leader"))
        }
    )


@blueprint.route('/', methods=['POST'])
def create_jobs():
    keys = ("id",
            "job",
            "work_size",
            "collaborators",
            "end_date",
            "start_date",
            "is_finished",
            "team_leader")
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in keys):
        return jsonify({'error': 'Bad request'})
    db_sess = create_session()
    exist_job = db_sess.query(Jobs).get(request.json["id"])
    if exist_job:
        return jsonify({'error': 'Id already exists'})
    data = {key: request.json[key] for key in keys}
    data["start_date"] = datetime.strptime(data["start_date"], "%y-%m-%d")
    data["end_date"] = datetime.strptime(data["end_date"], "%y-%m-%d")
    # print(data)
    jobs = Jobs(**data)
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})