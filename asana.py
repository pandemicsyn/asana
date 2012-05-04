#!/usr/bin/env python

import requests
import optparse
import getpass
try:
    import simplejson as json
except ImportError:
    import json

class AsanaAPI(object):

    def __init__(self, apikey, debug=False):
        self.debug = debug
        self.asana_url = "https://app.asana.com/api"
        self.api_version = "1.0"
        self.aurl = "/".join([self.asana_url, self.api_version])
        self.apikey = apikey
        self.bauth = self.get_basic_auth()

    def get_basic_auth(self):
        """Get basic auth creds
        :returns: the basic auth string
        """
        s = self.apikey + ":"
        return s.encode("base64").rstrip()

    def _asana(self, api_target):
        target = "/".join([self.aurl, api_target])
        if self.debug:
            print "-> Calling: %s" % target
        r = requests.get(target, auth=(self.apikey, ""))
        if self._ok_status(r.status_code) and r.status_code is not 404:
            if r.headers['content-type'] == 'application/json':
                return json.loads(r.text)
            else:
                raise Exception('Did not receive json from api')
        else:
            if self.debug:
                print "-> Got: %s" % r.status_code
                print "-> %s" % r.text
            raise Exception('Received non 2xx or 404 status code on call')

    def _ok_status(self, status_code):
        if status_code/200 is 1:
            return True
        elif status_code/400 is 1:
            if status_code is 404:
                return True
            else:
                return False
        elif status_code is 500:
            return False

    def user_info(self, user_id="me"):
        return self._asana('users/%s' % user_id)

    def list_users(self, workspace=None, filters=[]):
        if workspace:
            return "Not yet available"
        else:
            if filters:
                fkeys = [x.strip().lower() for x in filters]
                fields = ",".join(fkeys)
                return self._asana('users?opt_fields=%s' % fields)
            else:
                return self._asana('users')

    def list_tasks(self, workspace, assignee):
        target = "tasks?workspace=%s&assignee=%s" % (workspace, assignee)
        return self._asana(target)

    def list_projects(self, workspace=None):
        if workspace:
            return self._asana('workspaces/%s/projects' % workspace)
        else:
            return self._asana('projects')

    def project(self, project_id):
        return self._asana('projects/%s' % project_id)

    def project_tasks(self, project_id):
        return self._asana('projects/%s/tasks' % project_id)

    def task_stories(self, task_id):
        return self._asana('tasks/%s/stories' % task_id)

    def story(self, story_id):
        return self._asana('stories/%s' % story_id)

    def workspaces(self):
        return self._asana('workspaces')
