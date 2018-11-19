from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core import serializers
import json


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def show_accounts(request):
    accounts = Account.objects.all()
    res = query_result_to_array(accounts)
    res_string = """<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
"""
    res_string += dict_of_dicts_to_html_table(res)
    return HttpResponse(res_string)


def dict_of_dicts_to_html_table(dict_of_dicts):
    headers = set()
    # headers.add("pk")
    for pk in dict_of_dicts:
        for field in dict_of_dicts[pk]:
            headers.add(field)
    ret = ""

    ret += "<table>\n"
    ret += "  <tr>\n"
    ret += "    <th>pk</th>\n"
    for header in headers:
        ret += "    <th>" + header + "</th>\n"
    ret += "  </tr>\n"

    for pk in dict_of_dicts:
        ret += "  <tr>\n"
        ret += "    <td>" + pk + "</td>\n"
        for key in dict_of_dicts[pk]:
            ret += "    <td>" + dict_of_dicts[pk][key] + "</td>\n"
        ret += "  </tr>\n"
    ret += "</table>\n"
    return ret


def serialise_get_object(get_object):
    data = serializers.serialize('json', [get_object, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return data


def query_result_to_array(list_object):
    '''
    Returns an object ready to be serialized with json.dumps(res)
    '''
    d = dict()
    tmp_python = serializers.serialize('python', list_object)
    for el in tmp_python:
        d[el["pk"]] = el["fields"]
    return d
