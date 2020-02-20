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


class FrameHistoryList(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'battery_level': 'int',
        'engine_started': 'bool',
        'is_moving': 'bool',
        'fuel_level': 'float',
        'msg_time': 'int'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'battery_level': 'battery_level',
        'engine_started': 'engine_started',
        'is_moving': 'is_moving',
        'fuel_level': 'fuel_level',
        'msg_time': 'msg_time'
    }

    def __init__(self, latitude=None, longitude=None, battery_level=None, engine_started=None, is_moving=None, fuel_level=None, msg_time=None):  # noqa: E501
        """FrameHistoryList - a model defined in Swagger"""  # noqa: E501
        self._latitude = None
        self._longitude = None
        self._battery_level = None
        self._engine_started = None
        self._is_moving = None
        self._fuel_level = None
        self._msg_time = None
        self.discriminator = None
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if battery_level is not None:
            self.battery_level = battery_level
        if engine_started is not None:
            self.engine_started = engine_started
        if is_moving is not None:
            self.is_moving = is_moving
        if fuel_level is not None:
            self.fuel_level = fuel_level
        if msg_time is not None:
            self.msg_time = msg_time

    @property
    def latitude(self):
        """Gets the latitude of this FrameHistoryList.  # noqa: E501


        :return: The latitude of this FrameHistoryList.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this FrameHistoryList.


        :param latitude: The latitude of this FrameHistoryList.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this FrameHistoryList.  # noqa: E501


        :return: The longitude of this FrameHistoryList.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this FrameHistoryList.


        :param longitude: The longitude of this FrameHistoryList.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def battery_level(self):
        """Gets the battery_level of this FrameHistoryList.  # noqa: E501


        :return: The battery_level of this FrameHistoryList.  # noqa: E501
        :rtype: int
        """
        return self._battery_level

    @battery_level.setter
    def battery_level(self, battery_level):
        """Sets the battery_level of this FrameHistoryList.


        :param battery_level: The battery_level of this FrameHistoryList.  # noqa: E501
        :type: int
        """

        self._battery_level = battery_level

    @property
    def engine_started(self):
        """Gets the engine_started of this FrameHistoryList.  # noqa: E501


        :return: The engine_started of this FrameHistoryList.  # noqa: E501
        :rtype: bool
        """
        return self._engine_started

    @engine_started.setter
    def engine_started(self, engine_started):
        """Sets the engine_started of this FrameHistoryList.


        :param engine_started: The engine_started of this FrameHistoryList.  # noqa: E501
        :type: bool
        """

        self._engine_started = engine_started

    @property
    def is_moving(self):
        """Gets the is_moving of this FrameHistoryList.  # noqa: E501


        :return: The is_moving of this FrameHistoryList.  # noqa: E501
        :rtype: bool
        """
        return self._is_moving

    @is_moving.setter
    def is_moving(self, is_moving):
        """Sets the is_moving of this FrameHistoryList.


        :param is_moving: The is_moving of this FrameHistoryList.  # noqa: E501
        :type: bool
        """

        self._is_moving = is_moving

    @property
    def fuel_level(self):
        """Gets the fuel_level of this FrameHistoryList.  # noqa: E501


        :return: The fuel_level of this FrameHistoryList.  # noqa: E501
        :rtype: float
        """
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, fuel_level):
        """Sets the fuel_level of this FrameHistoryList.


        :param fuel_level: The fuel_level of this FrameHistoryList.  # noqa: E501
        :type: float
        """

        self._fuel_level = fuel_level

    @property
    def msg_time(self):
        """Gets the msg_time of this FrameHistoryList.  # noqa: E501


        :return: The msg_time of this FrameHistoryList.  # noqa: E501
        :rtype: int
        """
        return self._msg_time

    @msg_time.setter
    def msg_time(self, msg_time):
        """Sets the msg_time of this FrameHistoryList.


        :param msg_time: The msg_time of this FrameHistoryList.  # noqa: E501
        :type: int
        """

        self._msg_time = msg_time

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
        if issubclass(FrameHistoryList, dict):
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
        if not isinstance(other, FrameHistoryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
