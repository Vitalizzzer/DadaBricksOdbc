import os

import logging

from reportportal_behave.behave_integration_service import BehaveIntegrationService

from repository.pyodbc_sqlite import open_connection


def before_all(context):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
    context.config.setup_logging()

    tags = ', '.join([tag for tags in context.config.tags.ands for tag in tags])
    rp_enable = context.config.userdata.getbool('rp_enable', False)
    step_based = context.config.userdata.getbool('step_based', True)
    context.requested_browser = context.config.userdata.get('browser', "chrome")
    rp_endpoint = os.environ.get("RP_ENDPOINT")
    rp_project = os.environ.get("RP_PROJECT")
    rp_uuid = os.environ.get("RP_UUID")
    rp_launch = os.environ.get("RP_LAUNCH")
    launch_description = "BDD Tests"
    add_screenshot = context.config.userdata.getbool('add_screenshot', False)
    context.behave_integration_service = BehaveIntegrationService(rp_endpoint=rp_endpoint,
                                                                  rp_project=rp_project,
                                                                  rp_token=rp_uuid,
                                                                  rp_launch_name=rp_launch,
                                                                  rp_launch_description=launch_description,
                                                                  rp_enable=rp_enable,
                                                                  step_based=step_based,
                                                                  add_screenshot=add_screenshot,
                                                                  verify_ssl=False)
    context.launch_id = context.behave_integration_service.launch_service(tags=tags)


def before_feature(context, feature):
    context.feature_id = context.behave_integration_service.before_feature(feature)


def before_scenario(context, scenario):
    context.connection = open_connection()
    logging.info("Connection is opened")

    context.scenario_id = context.behave_integration_service.before_scenario(scenario,
                                                                             feature_id=context.feature_id)


def before_step(context, step):
    context.step_id = context.behave_integration_service.before_step(step, scenario_id=context.scenario_id)


def after_step(context, step):
    context.behave_integration_service.after_step(step, context.step_id)


def after_scenario(context, scenario):
    context.connection.close()
    logging.info("Connection is closed")
    context.behave_integration_service.after_scenario(scenario, context.scenario_id)


def after_feature(context, feature):
    context.behave_integration_service.after_feature(feature, context.feature_id)


def after_all(context):
    context.behave_integration_service.after_all(context.launch_id)
