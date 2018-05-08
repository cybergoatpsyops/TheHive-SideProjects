#!/usr/bin/python3
# https://github.com/cybergoatpsyops/TheHive-SideProjects

from flask import Flask, request
import json
import requests
import os


hookURL = os.environ['hookURL']  # Your Slack URL API
hiveURL = os.environ['hiveURL']  # Your Hive URL
headers = {'content-type': 'application/json'}


def case_new():  # New case created payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "New Hive Case",
            "pretext": "Case#" + (str(data['object']['caseId'])),
            "author_name": "Created by " + (str(data['object']['createdBy'])),
            "title": (str(data['details']['title'])),
            "title_link": hiveURL + "/index.html/case/" + data['objectId'] + "/details",
            "color": "danger",
            "text": "New Case Created!",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['details']['description'])),
                    "short": False
                          }
                       ]
                    }
                 ]
              }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    print("Response: " + str(r.status_code) + "," + str(r.reason))


def case_delete():  # Case deleted payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Hive Case Deleted",
            "pretext": "Case#" + (str(data['details']['caseId'])),
            "author_name": "Owner: " + (str(data['details']['owner'])),
            "title": (str(data['details']['title'])),
            "title_link": hiveURL + "/index.html#/cases",
            "color": "danger",
            "fields": [
                {
                    "title": "Description",
                    "value": "Case has been deleted",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def case_update():  # Case updated payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Hive Case Updated",
            "pretext": "New Case Update - " + (str(data['object']['title'])),
            "author_name": "Updated by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/details",
            "color": "danger",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['details']['description'])),
                    "short": False,
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def task_new():  # New case task created payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "New Case Task",
            "pretext": "New Case Task",
            "author_name": "Created by " + (str(data['object']['createdBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "New task has been created",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def task_update():  # Case task updated payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Task Update",
            "pretext": "Task Update",
            "author_name": "Updated by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been updated",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def task_delete():  # Case task deleted payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Task Canceled",
            "pretext": "Task Canceled",
            "author_name": "Canceled by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been canceled",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def task_complete():  # Case task completed payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Task Completed",
            "pretext": "Task Completed",
            "author_name": "Completed by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been completed",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def observe_new(): # New case observable created
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Observable Created",
            "pretext": "Observable Created",
            "author_name": "Created by " + (str(data['object']['createdBy'])),
            "title": "New " + (str(data['object']['dataType'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/observables",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['object']['message'])),
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def observe_update():  # Case observable updated
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Observable Updated",
            "pretext": "Observable Updated",
            "author_name": "Updated by " + (str(data['object']['updatedBy'])),
            "title": "New " + (str(data['object']['dataType'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/observables",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['object']['message'])),
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def observe_delete():  # Case obserable deleted
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Observable Deleted",
            "pretext": "Observable Deleted",
            "author_name": "Deleted by " + (str(data['object']['updatedBy'])),
            "title": "New " + (str(data['object']['dataType'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/observables",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Observable has been permanently deleted",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def find_key(obj, key):  # recursive generator
    if isinstance(obj, dict):
        yield from iter_dict(obj, key, [])
    elif isinstance(obj, list):
        yield from iter_list(obj, key, [])


def iter_dict(d, key, indices):
    for k, v in d.items():
        if k == key:
            yield indices + [k], v
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])


def iter_list(seq, key, indices):
    for k, v in enumerate(seq):
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])


app = Flask(__name__)


@app.route('/', methods=['POST'])  # Flask app route
def process():  # If logic
    data = json.loads(request.data.decode("utf-8"))  # decode json data to utf-8 string
    keys = "objectType", "operation", "status"

    for k in keys:
        keypath, val = next(find_key(data, k))
        print("{!r}: {!r}".format(k, val))
    if (data['objectType']) == 'case':
        if (data['operation']) == 'Creation':  # Case created, updated, deleted
            case_new()
        elif (data['operation']) == 'Update':
            case_update()
        elif (data['operation']) == 'Delete':
            case_delete()
    if (data['objectType']) == 'case_task': # Task created deleted, completed, updated
        if (data['operation']) == 'Creation':
            task_new()
        elif (data['object']['status']) == 'Cancel':
            task_delete()
        elif (data['object']['status']) == 'Completed':
            task_complete()
        elif (data['operation']) == 'Update':
            if (data['object']['status']) == 'InProgress':
                task_update()
    if (data['objectType']) == 'case_artifact': # Observable created, updated, deleted
        if (data['operation']) == 'Creation':
            observe_new()
        elif(data['operation']) == 'Update':
            observe_update()
        elif (data['operation']) == 'Delete':
            observe_delete()
    return 'ok'


if __name__ == '__main__':
    app.run()
