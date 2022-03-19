import requests


response_get_all = requests.get("http://127.0.0.1:5000/api/jobs")
response_get_by_id = requests.get("http://127.0.0.1:5000/api/jobs/1")
bad_response_1 = requests.get("http://127.0.0.1:5000/api/jobs/123123")
bad_response_2 = requests.get("http://127.0.0.1:5000/api/jobs/asdsada")

print(response_get_all.json(), response_get_all.status_code)
print(response_get_by_id.json(), response_get_by_id.status_code)
print(bad_response_1.json(), bad_response_1.status_code)
print(bad_response_2.json(), bad_response_2.status_code)
