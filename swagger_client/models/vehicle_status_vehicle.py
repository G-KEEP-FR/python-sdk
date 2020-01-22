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


class VehicleStatusVehicle(object):
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
        'capacity': 'int',
        'id': 'int',
        'driver': 'VehicleStatusVehicleDriver'
    }

    attribute_map = {
        'capacity': 'capacity',
        'id': 'id',
        'driver': 'driver'
    }

    def __init__(self, capacity=None, id=None, driver=None):  # noqa: E501
        """VehicleStatusVehicle - a model defined in Swagger"""  # noqa: E501
        self._capacity = None
        self._id = None
        self._driver = None
        self.discriminator = None
        if capacity is not None:
            self.capacity = capacity
        if id is not None:
            self.id = id
        if driver is not None:
            self.driver = driver

    @property
    def capacity(self):
        """Gets the capacity of this VehicleStatusVehicle.  # noqa: E501


        :return: The capacity of this VehicleStatusVehicle.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this VehicleStatusVehicle.


        :param capacity: The capacity of this VehicleStatusVehicle.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def id(self):
        """Gets the id of this VehicleStatusVehicle.  # noqa: E501


        :return: The id of this VehicleStatusVehicle.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleStatusVehicle.


        :param id: The id of this VehicleStatusVehicle.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def driver(self):
        """Gets the driver of this VehicleStatusVehicle.  # noqa: E501


        :return: The driver of this VehicleStatusVehicle.  # noqa: E501
        :rtype: VehicleStatusVehicleDriver
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this VehicleStatusVehicle.


        :param driver: The driver of this VehicleStatusVehicle.  # noqa: E501
        :type: VehicleStatusVehicleDriver
        """

        self._driver = driver

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
        if issubclass(VehicleStatusVehicle, dict):
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
        if not isinstance(other, VehicleStatusVehicle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other