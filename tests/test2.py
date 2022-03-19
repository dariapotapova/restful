from datetime import datetime

import requests


def post_jobs(json):
    post_response = requests.post("http://127.0.0.1:5000/api/jobs", json=json)
    data = post_response.json()
    if "success" in data:
        print("Добавлен")
    else:
        print("Ошибка:", data["error"])


json_data = {"id": 15,
             "job": "Описание работы",
             "work_size": 2,
             "collaborators": "1, 2",
             "end_date": datetime.now().strftime("%y-%m-%d"),
             "start_date": datetime.now().strftime("%y-%m-%d"),
             "is_finished": True,
             "team_leader": 1}

get_response = requests.get("http://127.0.0.1:5000/api/jobs")
jobs_length = len(get_response.json()["jobs"])
print(f"Количество работ: {jobs_length}")

post_jobs(json_data)

get_response = requests.get("http://127.0.0.1:5000/api/jobs")
jobs_length = len(get_response.json()["jobs"])
print(f"Количество работ: {jobs_length}")
