from flask import jsonify
from flask_restful import abort, reqparse, Resource

from data import db_session
from data.jobs import Jobs


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResorses(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id',
                  'team_leader',
                  'job',
                  'work_size',
                  'collaborators',
                  'end_date',
                  'start_date',
                  'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResourses(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id',
                  'team_leader',
                  'job',
                  'work_size',
                  'collaborators',
                  'end_date',
                  'start_date',
                  'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(**args)
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('end_date', required=True)
parser.add_argument('start_date', required=True)
parser.add_argument('is_finished', required=True, type=bool)
