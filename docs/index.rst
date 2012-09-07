.. asana documentation master file, created by
   sphinx-quickstart on Fri Sep  7 00:35:58 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Asana, the python wrapper for the asana api
===========================================

Basic usage::

    from asana import asana
    asana_api = asana.AsanaAPI('YourAsanaAPIKey', debug=True)

    # see your workspaces
    myspaces = asana_api.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]

    # create a new project
    asana_api.create_project('test project', myspaces[0]['id'])

    # create a new task
    asana_api.create_task('yetanotherapitest', myspaces[0]['id'], assignee_status='later', notes='some notes')

    # add a story to task
    asana_api.add_story(mytask, 'omgwtfbbq')

AsanaAPI()
==========

.. automodule:: asana.asana
    :members:
    :undoc-members:
    :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

