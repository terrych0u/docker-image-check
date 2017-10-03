#!/usr/bin/env python

import docker
import sys
import json
import requests


def check_remote_digest(repo, tags):
    login = "https://auth.docker.io/token?service=registry.docker.io&scope=repository:{repository}:pull"    
    get_manifest = "https://registry.hub.docker.com/v2/{repository}/manifests/{tag}"

    if "/" not in repo:
        repo = "library/"+repo

    try:
        response = requests.get(login.format(repository=repo), json=True,timeout=3)
    except requests.exceptions.Timeout:
        print "Login timeout"
        sys.exit(1)
    
    response_json = response.json()
    token = response_json["token"]

    try:
        response = requests.get(get_manifest.format(repository=repo, tag=tags,timeout=3),
            headers={"Authorization": "Bearer {}".format(token) ,"Accept": "application/vnd.docker.distribution.manifest.v2+json"},
            json=True
        )
    except requests.exceptions.Timeout :
        print "Request timeout"
        sys.exit(1)

    if 'Docker-Content-Digest' in response.headers:
         manifest = response.headers['Docker-Content-Digest'].split(":")[1]
    else:
        manifest = "-1"

    return manifest


if __name__ == '__main__':
    
    client = docker.from_env()
    responded = client.containers.list()

    print'{0}{1:^18}{2}'.format('CONTAINER ID','TAG','UP TO DATE?')

    for i in responded:
        container = client.containers.get(i.short_id)
        raw_repo = container.attrs['Config']['Image']
        repo = raw_repo.split(":")[0]

        if not i.image.attrs['RepoDigests']:
            continue

        local_digest = i.image.attrs['RepoDigests'][0].split(":")[1]

        try :
            tags = raw_repo.split(":")[1]
        except:
            tags = "latest"

        remote_digest = check_remote_digest(repo, tags)

        if remote_digest == "-1":
            update = "Not Found in Docker Hub"
        elif local_digest != remote_digest:
            update = "true"
        else:
            update = "false"

        print'{0}{1:^22}{2}'.format(i.short_id, tags, update)
