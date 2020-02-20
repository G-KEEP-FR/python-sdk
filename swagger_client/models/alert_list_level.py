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


class AlertListLevel(object):
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
        'id': 'int',
        'name': 'str',
        'color': 'str',
        'level': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'color': 'color',
        'level': 'level'
    }

    def __init__(self, id=None, name=None, color=None, level=None):  # noqa: E501
        """AlertListLevel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._color = None
        self._level = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
        if level is not None:
            self.level = level

    @property
    def id(self):
        """Gets the id of this AlertListLevel.  # noqa: E501


        :return: The id of this AlertListLevel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertListLevel.


        :param id: The id of this AlertListLevel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AlertListLevel.  # noqa: E501


        :return: The name of this AlertListLevel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertListLevel.


        :param name: The name of this AlertListLevel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def color(self):
        """Gets the color of this AlertListLevel.  # noqa: E501


        :return: The color of this AlertListLevel.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AlertListLevel.


        :param color: The color of this AlertListLevel.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def level(self):
        """Gets the level of this AlertListLevel.  # noqa: E501


        :return: The level of this AlertListLevel.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this AlertListLevel.


        :param level: The level of this AlertListLevel.  # noqa: E501
        :type: int
        """

        self._level = level

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
        if issubclass(AlertListLevel, dict):
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
        if not isinstance(other, AlertListLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
