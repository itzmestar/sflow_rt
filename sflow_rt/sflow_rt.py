# -*- coding: utf-8 -*- #
"""This provides the class implementation which acts as
sFlow-RT Rest API client."""

import requests
import simplejson


class SFlowRT:
    """
    SFlowRT class to act as sFlow-RT Rest API client.
    All the requests can be made through this class.
    """

    def __init__(self, ip, port):
        """
        Initialize the object
        :param ip: IP address of sFlow-RT Rest API Host
        :param port: Port on which sFlow-RT Rest API is listening
        """
        self.base_url = f"http://{ip}:{port}"
        self.session = requests.Session()

    def _send_message(self, method, endpoint, params=None, data=None):
        """
        Send API request.
        :param method: HTTP method (get, post, delete, etc.)
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :param data: JSON-encoded string payload for POST
        :return: dict/list/String: JSON response if returned
        """
        url = self.base_url + endpoint
        response = self.session.request(method, url, params=params,
                                        data=data, timeout=30)
        try:
            data = response.json()
        except simplejson.errors.JSONDecodeError:
            data = response.text

        return data

    def _get(self, endpoint, params=None):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :return:
        """
        return self._send_message('GET', endpoint, params=params)

    # ----- Server Related ----- #
    def get_version(self):
        """
        Show software version
        :return: string
        """
        path = '/version'

        return self._get(path)

    def get_analyzer_performance(self):
        """
        sFlow analyzer performance information
        :return:
        """
        path = '/analyzer/json'

        return self._get(path)

    def get_analyzer_performance_prometheus(self):
        """
        sFlow analyzer performance information as Prometheus metrics
        :return:
        """
        path = '/prometheus/analyzer/json'

        return self._get(path)

    def get_license(self):
        """
        get License type and status
        :return:
        """
        path = '/license/json'

        return self._get(path)

    def get_agents(self, query=None):
        """
        List sFlow agents with session information
        :param query: query Used to filter agents, e.g. agent=10.0.0.1&agent=test1
                returns information on selected agents
        :return:
        """
        path = '/agents/json'

        return self._get(path)

    # ----- Metrics Related ----- #

    def get_metrics(self):
        """
        List currently active metrics and elapsed time (in mS) since last seen.
        :return:
        """
        path = '/metrics/json'

        return self._get(path)

    def get_agent_metrics(self, agent):
        """
        Retrieve metrics for agent
        :param agent: ip address or hostname of agent
        :return:
        """
        path = f'/metric/{agent}/json'

        return self._get(path)

    def get_agent_metric(self, agent, metric, query=None):
        """
        Retrieve metrics for agents with query params
        :param agent: comma separated list of agent addresses/hostnames e.g. 10.0.0.1,switch1
                the token 'ALL' represents all agents
        :param metric: ordered list of metric names, e.g. load_one,load_five -
                prefix metric with max:, min:, sum:, avg:, var:, sdev:, med:, q1:, q2:, q3:, iqr:
                or any: to specify aggregation operation, e.g. max:load_one,min:load_one.
                Default aggregation max is used if no prefix specified
        :param query: query parameters applied as filter to select agents based on metrics,
                e.g. os_name=linux&os_name=windows&cpu_num=2&host_name=*web.*
        :return:
        """
        path = f'/metric/{agent}/{metric}/json'

        return self._get(path)

    def get_agent_metric_table(self, agent, metric, query=None):
        """
        Retrieve table of metrics for agents with query params
        :param agent: comma separated list of agent addresses/hostnames e.g. 10.0.0.1,switch1
                the token 'ALL' represents all agents
        :param metric: ordered list of metric names, e.g. load_one,load_five -
                prefix metric with max:, min:, sum:, avg:, var:, sdev:, med:, q1:, q2:, q3:, iqr:
                or any: to specify aggregation operation, e.g. max:load_one,min:load_one.
                Default aggregation max is used if no prefix specified
        :param query: query parameters applied as filter to select agents based on metrics,
                e.g. os_name=linux&os_name=windows&cpu_num=2&host_name=*web.*
        :return:
        """
        path = f'/table/{agent}/{metric}/json'

        return self._get(path)

    def get_agent_metric_dump(self, agent, metric, query=None):
        """
        Dump metrics for agents with query params
        :param agent: comma separated list of agent addresses/hostnames e.g. 10.0.0.1,switch1
                the token 'ALL' represents all agents
        :param metric: list of metric names, e.g. load_one;load_five - the token ALL represents all metrics
        :param query: query parameters applied as filter to select agents based on metrics,
                e.g. os_name=linux&os_name=windows&cpu_num=2&host_name=*web.*
        :return:
        """
        path = f'/dump/{agent}/{metric}/json'

        return self._get(path)

    # ----- Flows Related ----- #

    def get_flowkeys(self):
        """
        List currently active flow keys and elapsed time (in mS) since last seen
        :return:
        """
        path = '/flowkeys/json'

        return self._get(path)

    def get_flow(self):
        """
        List flow definitions
        :return:
        """
        path = '/flow/json'

        return self._get(path)
