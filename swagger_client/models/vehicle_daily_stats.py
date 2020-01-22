# coding: utf-8

"""
    Gkeep API

    Gkeep API  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class VehicleDailyStats(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'engine_on_time': 'int',
        'stopped_time': 'int',
        'distance': 'int',
        'fuel_cost': 'int',
        'consumption': 'int',
        'average_consumption': 'int',
        'average_consumption_hour': 'int',
        'abnormal_consumption': 'int',
        'real_consumption': 'int',
        'objective': 'str'
    }

    attribute_map = {
        'engine_on_time': 'engine_on_time',
        'stopped_time': 'stopped_time',
        'distance': 'distance',
        'fuel_cost': 'fuel_cost',
        'consumption': 'consumption',
        'average_consumption': 'average_consumption',
        'average_consumption_hour': 'average_consumption_hour',
        'abnormal_consumption': 'abnormal_consumption',
        'real_consumption': 'real_consumption',
        'objective': 'objective'
    }

    def __init__(self, engine_on_time=None, stopped_time=None, distance=None, fuel_cost=None, consumption=None, average_consumption=None, average_consumption_hour=None, abnormal_consumption=None, real_consumption=None, objective=None):  # noqa: E501
        """VehicleDailyStats - a model defined in Swagger"""  # noqa: E501
        self._engine_on_time = None
        self._stopped_time = None
        self._distance = None
        self._fuel_cost = None
        self._consumption = None
        self._average_consumption = None
        self._average_consumption_hour = None
        self._abnormal_consumption = None
        self._real_consumption = None
        self._objective = None
        self.discriminator = None
        if engine_on_time is not None:
            self.engine_on_time = engine_on_time
        if stopped_time is not None:
            self.stopped_time = stopped_time
        if distance is not None:
            self.distance = distance
        if fuel_cost is not None:
            self.fuel_cost = fuel_cost
        if consumption is not None:
            self.consumption = consumption
        if average_consumption is not None:
            self.average_consumption = average_consumption
        if average_consumption_hour is not None:
            self.average_consumption_hour = average_consumption_hour
        if abnormal_consumption is not None:
            self.abnormal_consumption = abnormal_consumption
        if real_consumption is not None:
            self.real_consumption = real_consumption
        if objective is not None:
            self.objective = objective

    @property
    def engine_on_time(self):
        """Gets the engine_on_time of this VehicleDailyStats.  # noqa: E501


        :return: The engine_on_time of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._engine_on_time

    @engine_on_time.setter
    def engine_on_time(self, engine_on_time):
        """Sets the engine_on_time of this VehicleDailyStats.


        :param engine_on_time: The engine_on_time of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._engine_on_time = engine_on_time

    @property
    def stopped_time(self):
        """Gets the stopped_time of this VehicleDailyStats.  # noqa: E501


        :return: The stopped_time of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._stopped_time

    @stopped_time.setter
    def stopped_time(self, stopped_time):
        """Sets the stopped_time of this VehicleDailyStats.


        :param stopped_time: The stopped_time of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._stopped_time = stopped_time

    @property
    def distance(self):
        """Gets the distance of this VehicleDailyStats.  # noqa: E501


        :return: The distance of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this VehicleDailyStats.


        :param distance: The distance of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def fuel_cost(self):
        """Gets the fuel_cost of this VehicleDailyStats.  # noqa: E501


        :return: The fuel_cost of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._fuel_cost

    @fuel_cost.setter
    def fuel_cost(self, fuel_cost):
        """Sets the fuel_cost of this VehicleDailyStats.


        :param fuel_cost: The fuel_cost of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._fuel_cost = fuel_cost

    @property
    def consumption(self):
        """Gets the consumption of this VehicleDailyStats.  # noqa: E501


        :return: The consumption of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._consumption

    @consumption.setter
    def consumption(self, consumption):
        """Sets the consumption of this VehicleDailyStats.


        :param consumption: The consumption of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._consumption = consumption

    @property
    def average_consumption(self):
        """Gets the average_consumption of this VehicleDailyStats.  # noqa: E501


        :return: The average_consumption of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._average_consumption

    @average_consumption.setter
    def average_consumption(self, average_consumption):
        """Sets the average_consumption of this VehicleDailyStats.


        :param average_consumption: The average_consumption of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._average_consumption = average_consumption

    @property
    def average_consumption_hour(self):
        """Gets the average_consumption_hour of this VehicleDailyStats.  # noqa: E501


        :return: The average_consumption_hour of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._average_consumption_hour

    @average_consumption_hour.setter
    def average_consumption_hour(self, average_consumption_hour):
        """Sets the average_consumption_hour of this VehicleDailyStats.


        :param average_consumption_hour: The average_consumption_hour of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._average_consumption_hour = average_consumption_hour

    @property
    def abnormal_consumption(self):
        """Gets the abnormal_consumption of this VehicleDailyStats.  # noqa: E501


        :return: The abnormal_consumption of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._abnormal_consumption

    @abnormal_consumption.setter
    def abnormal_consumption(self, abnormal_consumption):
        """Sets the abnormal_consumption of this VehicleDailyStats.


        :param abnormal_consumption: The abnormal_consumption of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._abnormal_consumption = abnormal_consumption

    @property
    def real_consumption(self):
        """Gets the real_consumption of this VehicleDailyStats.  # noqa: E501


        :return: The real_consumption of this VehicleDailyStats.  # noqa: E501
        :rtype: int
        """
        return self._real_consumption

    @real_consumption.setter
    def real_consumption(self, real_consumption):
        """Sets the real_consumption of this VehicleDailyStats.


        :param real_consumption: The real_consumption of this VehicleDailyStats.  # noqa: E501
        :type: int
        """

        self._real_consumption = real_consumption

    @property
    def objective(self):
        """Gets the objective of this VehicleDailyStats.  # noqa: E501


        :return: The objective of this VehicleDailyStats.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this VehicleDailyStats.


        :param objective: The objective of this VehicleDailyStats.  # noqa: E501
        :type: str
        """

        self._objective = objective

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VehicleDailyStats, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VehicleDailyStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
