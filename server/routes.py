from . import api
import controllers.sample

def add_routes():
    api.add_resource(controllers.sample.SampleController, '/')
