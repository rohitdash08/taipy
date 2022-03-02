from taipy.gui import Gui


def test_button_md_1(gui: Gui, helpers):
    gui._bind_var_val("name", "World!")
    gui._bind_var_val("btn_id", "button1")
    md_string = "<|Hello {name}|button|id={btn_id}|>"
    expected_list = ["<Button", 'defaultLabel="Hello World!"', "label={tp_Hello_name"]
    helpers.test_control_md(gui, md_string, expected_list)


def test_button_md_2(gui: Gui, helpers):
    gui._bind_var_val("name", "World!")
    gui._bind_var_val("btn_id", "button1")
    md_string = "<|button|label=Hello {name}|id={btn_id}|>"
    expected_list = ["<Button", 'defaultLabel="Hello World!"', "label={tp_Hello_name"]
    helpers.test_control_md(gui, md_string, expected_list)


def test_button_html_1(gui: Gui, helpers):
    gui._bind_var_val("name", "World!")
    gui._bind_var_val("btn_id", "button1")
    html_string = '<taipy:button label="Hello {name}" id="{btn_id}" />'
    expected_list = ["<Button", 'defaultLabel="Hello World!"', "label={tp_Hello_name"]
    helpers.test_control_html(gui, html_string, expected_list)


def test_button_html_2(gui: Gui, helpers):
    gui._bind_var_val("name", "World!")
    gui._bind_var_val("btn_id", "button1")
    html_string = '<taipy:button id="{btn_id}">Hello {name}</taipy:button>'
    expected_list = ["<Button", 'defaultLabel="Hello World!"', "label={tp_Hello_name"]
    helpers.test_control_html(gui, html_string, expected_list)
