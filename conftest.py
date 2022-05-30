# import os
# from remote import trigger_github_actions_regression
# import pytest
# from xdist.scheduler import LoadScopeScheduling
#
#
# def pytest_addoption(parser):
#     parser.addoption('--env', action='store', default='dev', help='select environment')
#     parser.addoption('--country', action='store', default='arg', help='select country')
#     parser.addoption('--remote', action='store_true',
#                      help='if true triggers parametrized regression tests in github actions')
#     parser.addoption('--profile', action='store', default='', help='select profile')
#
#
# def pytest_configure(config):
#     os.environ["env"] = config.getoption('env')
#     os.environ["country"] = config.getoption('country')
#     os.environ["profile"] = config.getoption('profile')
#
#     if config.getoption('remote'):
#         trigger_github_actions_regression(config.known_args_namespace)
#         pytest.exit('Tests will be run remotely in GitHub Actions')
#
#
# def pytest_xdist_make_scheduler(config, log):
#     class RegressionScheduler(LoadScopeScheduling):
#         def _split_scope(self, nodeid):
#
#             if "Test/Test-JPetStore" in nodeid:
#                 return "test-j_pet_store_tests_node"
#
#     return RegressionScheduler(config, log)
