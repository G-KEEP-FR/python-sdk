# coding: utf-8

"""
    Gkeep API

    Gkeep API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UpdateNotificationSettingsNotificationAlert9(object):
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
        'level': 'int',
        'notify_by_sms': 'int',
        'notify_by_email': 'int'
    }

    attribute_map = {
        'level': 'level',
        'notify_by_sms': 'notify_by_sms',
        'notify_by_email': 'notify_by_email'
    }

    def __init__(self, level=None, notify_by_sms=None, notify_by_email=None):  # noqa: E501
        """UpdateNotificationSettingsNotificationAlert9 - a model defined in Swagger"""  # noqa: E501
        self._level = None
        self._notify_by_sms = None
        self._notify_by_email = None
        self.discriminator = None
        if level is not None:
            self.level = level
        if notify_by_sms is not None:
            self.notify_by_sms = notify_by_sms
        if notify_by_email is not None:
            self.notify_by_email = notify_by_email

    @property
    def level(self):
        """Gets the level of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501


        :return: The level of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdateNotificationSettingsNotificationAlert9.


        :param level: The level of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def notify_by_sms(self):
        """Gets the notify_by_sms of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501


        :return: The notify_by_sms of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501
        :rtype: int
        """
        return self._notify_by_sms

    @notify_by_sms.setter
    def notify_by_sms(self, notify_by_sms):
        """Sets the notify_by_sms of this UpdateNotificationSettingsNotificationAlert9.


        :param notify_by_sms: The notify_by_sms of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501
        :type: int
        """

        self._notify_by_sms = notify_by_sms

    @property
    def notify_by_email(self):
        """Gets the notify_by_email of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501


        :return: The notify_by_email of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501
        :rtype: int
        """
        return self._notify_by_email

    @notify_by_email.setter
    def notify_by_email(self, notify_by_email):
        """Sets the notify_by_email of this UpdateNotificationSettingsNotificationAlert9.


        :param notify_by_email: The notify_by_email of this UpdateNotificationSettingsNotificationAlert9.  # noqa: E501
        :type: int
        """

        self._notify_by_email = notify_by_email

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
        if issubclass(UpdateNotificationSettingsNotificationAlert9, dict):
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
        if not isinstance(other, UpdateNotificationSettingsNotificationAlert9):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
