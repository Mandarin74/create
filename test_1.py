import pytest
import yaml




with open("testdata.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)



def test_step1(site, sel_log, sel_pass, sel_button, sel_err):
    input1 = site.find_el("xpath", sel_log)
    input1.send_keys("log")
    input2 = site.find_el("xpath", sel_pass)
    input2.send_keys("pass")
    btn = site.find_el("css", sel_button)
    btn.click()
    err_label = site.find_el("xpath", sel_err)
    assert err_label.text == "401"


def test_step2(site, sel_log, sel_pass, sel_button, sel_err, prov):
    input1 = site.find_el("xpath", sel_log)
    input1.send_keys(data["log"])
    input2 = site.find_el("xpath", sel_pass)
    input2.send_keys(data["pass"])
    btn = site.find_el("css", sel_button)
    btn.click()
    ppc = site.find_el("xpath", prov)
    assert ppc.text == "About"

def test_step3(site, sel_log, sel_pass, sel_button, sel_err, sel_button2, title, description, content, sel_button3, head_s):
    input1 = site.find_el("xpath", sel_log)
    input1.send_keys(data["log"])
    input2 = site.find_el("xpath", sel_pass)
    input2.send_keys(data["pass"])
    btn = site.find_el("css", sel_button)
    btn.click()
    btn2 = site.find_el("xpath", sel_button2)
    btn2.click()
    input3 = site.find_el("xpath", title)
    input3.send_keys(data["tit"])
    input4 = site.find_el("xpath", description)
    input4.send_keys(data["des"])
    input5 = site.find_el("xpath", content)
    input5.send_keys(data["con"])
    btn3 = site.find_el("xpath", sel_button3)
    btn3.click()
    answer = site.find_el("xpath", head_s)
    assert answer.tag_name == "owbed5"
