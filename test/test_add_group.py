

def test_add_group(app):
    old_group_list = app.group.get_group_list()
    app.group.add_new_group("new_group_name")
    new_group_list = app.group.get_group_list()
    old_group_list.append("new_group_name")
    assert sorted(old_group_list) == sorted(new_group_list)




