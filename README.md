# Asana python api & CLI

python wrapper for the [Asana API](http://asana.com)

A work in progress, but here's what's present so far:

- add_project_task
- add_story
- add_tag_task
- create_project
- create_task
- get_basic_auth
- get_project
- get_project_tasks
- get_story
- get_tags
- get_tag_tasks
- get_task
- list_projects
- list_stories
- list_tasks
- list_users
- list_workspaces
- rm_project_task
- update_project
- update_task
- update_workspace
- user_info

Todo:

- All the things!
- unittests
- Better error handling

Sample:

    import asana
    asana_api = asana.AsanaAPI('YourAsanaAPIKey', debug=True)

    # see your workspaces
    myspaces = asana_api.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]

    # create a new project
    asana_api.create_project('test project', myspaces[0]['id'])

    # create a new task
    asana_api.create_task('yetanotherapitest', myspaces[0]['id'], assignee_status='later', notes='some notes')

    # add a story to task
    asana_api.add_story(mytask, 'omgwtfbbq')

