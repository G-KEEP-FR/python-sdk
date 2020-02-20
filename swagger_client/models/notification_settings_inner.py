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


class NotificationSettingsInner(object):
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
        'id': 'str',
        'notify_by_email': 'bool',
        'notify_by_sms': 'bool',
        'level': 'object',
        'code': 'object'
    }

    attribute_map = {
        'id': 'id',
        'notify_by_email': 'notify_by_email',
        'notify_by_sms': 'notify_by_sms',
        'level': 'level',
        'code': 'code'
    }

    def __init__(self, id=None, notify_by_email=None, notify_by_sms=None, level=None, code=None):  # noqa: E501
        """NotificationSettingsInner - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._notify_by_email = None
        self._notify_by_sms = None
        self._level = None
        self._code = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if notify_by_email is not None:
            self.notify_by_email = notify_by_email
        if notify_by_sms is not None:
            self.notify_by_sms = notify_by_sms
        if level is not None:
            self.level = level
        if code is not None:
            self.code = code

    @property
    def id(self):
        """Gets the id of this NotificationSettingsInner.  # noqa: E501


        :return: The id of this NotificationSettingsInner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationSettingsInner.


        :param id: The id of this NotificationSettingsInner.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def notify_by_email(self):
        """Gets the notify_by_email of this NotificationSettingsInner.  # noqa: E501


        :return: The notify_by_email of this NotificationSettingsInner.  # noqa: E501
        :rtype: bool
        """
        return self._notify_by_email

    @notify_by_email.setter
    def notify_by_email(self, notify_by_email):
        """Sets the notify_by_email of this NotificationSettingsInner.


        :param notify_by_email: The notify_by_email of this NotificationSettingsInner.  # noqa: E501
        :type: bool
        """

        self._notify_by_email = notify_by_email

    @property
    def notify_by_sms(self):
        """Gets the notify_by_sms of this NotificationSettingsInner.  # noqa: E501


        :return: The notify_by_sms of this NotificationSettingsInner.  # noqa: E501
        :rtype: bool
        """
        return self._notify_by_sms

    @notify_by_sms.setter
    def notify_by_sms(self, notify_by_sms):
        """Sets the notify_by_sms of this NotificationSettingsInner.


        :param notify_by_sms: The notify_by_sms of this NotificationSettingsInner.  # noqa: E501
        :type: bool
        """

        self._notify_by_sms = notify_by_sms

    @property
    def level(self):
        """Gets the level of this NotificationSettingsInner.  # noqa: E501


        :return: The level of this NotificationSettingsInner.  # noqa: E501
        :rtype: object
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this NotificationSettingsInner.


        :param level: The level of this NotificationSettingsInner.  # noqa: E501
        :type: object
        """

        self._level = level

    @property
    def code(self):
        """Gets the code of this NotificationSettingsInner.  # noqa: E501


        :return: The code of this NotificationSettingsInner.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this NotificationSettingsInner.


        :param code: The code of this NotificationSettingsInner.  # noqa: E501
        :type: object
        """

        self._code = code

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
        if issubclass(NotificationSettingsInner, dict):
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
        if not isinstance(other, NotificationSettingsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other