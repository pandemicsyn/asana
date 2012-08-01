# Asana python api & CLI

python wrapper for the [Asana API](http://asana.com) and a sample CLI tool for 
[Asana](http://asana.com) itself.

A work in progress. Working so far:

- get_user_info
- list_users
- list_tasks
- get_task
- list_projects
- get_project
- get_project_tasks
- list_stories
- get_story
- list_workspaces
- create_task
- update_task
- create_project
- update_project*
- update_workspace*
- add_project_task
- rm_project_task
- add_story
- get_tags
- get_tag_tasks
- add_tag_task
- add_project_to_task

Todo:

- All the things!
- Especially error and response checkings.

Sample:

    import asana
    asana_api = asana.AsanaAPI('YourAsanaAPIKey', debug=True)

    # see your workspaces
    myspaces = asana_api.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]

    # create a new project
    asana_api.create_project('test project', 'notes for test project', myspaces[0]['id'])

    # create a new task
    asana_api.create_task('yetanotherapitest', myspaces[0]['id'], assignee_status='later', notes='some notes')

    # add a story to task
    asana_api.add_story(mytask, 'omgwtfbbq')

