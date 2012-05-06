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

Todo:

- All the things!
- Especially error and response checkings.

Sample:

    from asana import AsanaAPI()
    asana = AsanaAPI('YourAsanaAPIKey', debug=True)
    myspaces = asana.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]
    #create a new project
    asana.create_project('test project', 'notes for test project', myspaces[0]['id'])
    #create a new task
    asana.create_task('yetanotherapitest', myspaces[0]['id'], assignee_status='later', notes='some notes')
    #add a story to task
    asana.add_story(mytask, 'omgwtfbbq')

