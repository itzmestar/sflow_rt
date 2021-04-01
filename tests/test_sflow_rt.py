import pytest
from sflow_rt.sflow_rt import SFlowRT


@pytest.fixture(scope='module')
def sflow():
    return SFlowRT('127.0.0.1', 8008)


@pytest.mark.usefixtures('sflow')
class TestSFlowRT:
    """
    Test class for SFlowRT
    """

    def test_get_version(self, sflow):
        response = sflow.get_version()

        assert type(response) == str

    def test_get_analyzer_performance(self, sflow):
        assert False

    def test_get_analyzer_performance_prometheus(self, sflow):
        assert False

    def test_get_license(self, sflow):
        assert False

    def test_get_agents(self, sflow):
        assert False

    def test_get_metrics(self, sflow):
        assert False

    def test_get_agent_metrics(self, sflow):
        assert False

    def test_get_agent_metric(self, sflow):
        assert False

    def test_get_agent_metric_table(self, sflow):
        assert False

    def test_get_agent_metric_dump(self, sflow):
        assert False

    def test_get_flowkeys(self, sflow):
        assert False

    def test_get_flow(self, sflow):
        assert False
