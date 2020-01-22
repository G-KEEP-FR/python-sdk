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


class UserProfile(object):
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
        'email': 'str',
        'groups': 'list[UserProfileGroups]',
        'roles': 'list[str]',
        'firstname': 'str',
        'lastname': 'str',
        'phone': 'str',
        'parent_id': 'str',
        'association': 'str',
        'comment': 'str',
        'company': 'str',
        'company_short_name': 'str',
        'contract': 'str',
        'external_company': 'str',
        'nav_system_access_data': 'str',
        'id': 'int',
        'lang': 'UserProfileLang',
        'nav_system': 'str',
        'notify_by_email': 'bool',
        'notify_by_sms': 'bool',
        'notify_timezone': 'str',
        'partner_type': 'str',
        'is_terms_accepted': 'bool',
        'geo_localization_settings': 'UserProfileGeoLocalizationSettings',
        'api_token': 'str'
    }

    attribute_map = {
        'email': 'email',
        'groups': 'groups',
        'roles': 'roles',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'phone': 'phone',
        'parent_id': 'parent_id',
        'association': 'association',
        'comment': 'comment',
        'company': 'company',
        'company_short_name': 'company_short_name',
        'contract': 'contract',
        'external_company': 'external_company',
        'nav_system_access_data': 'nav_system_access_data',
        'id': 'id',
        'lang': 'lang',
        'nav_system': 'nav_system',
        'notify_by_email': 'notify_by_email',
        'notify_by_sms': 'notify_by_sms',
        'notify_timezone': 'notify_timezone',
        'partner_type': 'partner_type',
        'is_terms_accepted': 'is_terms_accepted',
        'geo_localization_settings': 'geo_localization_settings',
        'api_token': 'api_token'
    }

    def __init__(self, email=None, groups=None, roles=None, firstname=None, lastname=None, phone=None, parent_id=None, association=None, comment=None, company=None, company_short_name=None, contract=None, external_company=None, nav_system_access_data=None, id=None, lang=None, nav_system=None, notify_by_email=None, notify_by_sms=None, notify_timezone=None, partner_type=None, is_terms_accepted=None, geo_localization_settings=None, api_token=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._groups = None
        self._roles = None
        self._firstname = None
        self._lastname = None
        self._phone = None
        self._parent_id = None
        self._association = None
        self._comment = None
        self._company = None
        self._company_short_name = None
        self._contract = None
        self._external_company = None
        self._nav_system_access_data = None
        self._id = None
        self._lang = None
        self._nav_system = None
        self._notify_by_email = None
        self._notify_by_sms = None
        self._notify_timezone = None
        self._partner_type = None
        self._is_terms_accepted = None
        self._geo_localization_settings = None
        self._api_token = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if groups is not None:
            self.groups = groups
        if roles is not None:
            self.roles = roles
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if phone is not None:
            self.phone = phone
        if parent_id is not None:
            self.parent_id = parent_id
        if association is not None:
            self.association = association
        if comment is not None:
            self.comment = comment
        if company is not None:
            self.company = company
        if company_short_name is not None:
            self.company_short_name = company_short_name
        if contract is not None:
            self.contract = contract
        if external_company is not None:
            self.external_company = external_company
        if nav_system_access_data is not None:
            self.nav_system_access_data = nav_system_access_data
        if id is not None:
            self.id = id
        if lang is not None:
            self.lang = lang
        if nav_system is not None:
            self.nav_system = nav_system
        if notify_by_email is not None:
            self.notify_by_email = notify_by_email
        if notify_by_sms is not None:
            self.notify_by_sms = notify_by_sms
        if notify_timezone is not None:
            self.notify_timezone = notify_timezone
        if partner_type is not None:
            self.partner_type = partner_type
        if is_terms_accepted is not None:
            self.is_terms_accepted = is_terms_accepted
        if geo_localization_settings is not None:
            self.geo_localization_settings = geo_localization_settings
        if api_token is not None:
            self.api_token = api_token

    @property
    def email(self):
        """Gets the email of this UserProfile.  # noqa: E501


        :return: The email of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfile.


        :param email: The email of this UserProfile.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def groups(self):
        """Gets the groups of this UserProfile.  # noqa: E501


        :return: The groups of this UserProfile.  # noqa: E501
        :rtype: list[UserProfileGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserProfile.


        :param groups: The groups of this UserProfile.  # noqa: E501
        :type: list[UserProfileGroups]
        """

        self._groups = groups

    @property
    def roles(self):
        """Gets the roles of this UserProfile.  # noqa: E501


        :return: The roles of this UserProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserProfile.


        :param roles: The roles of this UserProfile.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def firstname(self):
        """Gets the firstname of this UserProfile.  # noqa: E501


        :return: The firstname of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserProfile.


        :param firstname: The firstname of this UserProfile.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserProfile.  # noqa: E501


        :return: The lastname of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserProfile.


        :param lastname: The lastname of this UserProfile.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def phone(self):
        """Gets the phone of this UserProfile.  # noqa: E501


        :return: The phone of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserProfile.


        :param phone: The phone of this UserProfile.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def parent_id(self):
        """Gets the parent_id of this UserProfile.  # noqa: E501


        :return: The parent_id of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this UserProfile.


        :param parent_id: The parent_id of this UserProfile.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def association(self):
        """Gets the association of this UserProfile.  # noqa: E501


        :return: The association of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this UserProfile.


        :param association: The association of this UserProfile.  # noqa: E501
        :type: str
        """

        self._association = association

    @property
    def comment(self):
        """Gets the comment of this UserProfile.  # noqa: E501


        :return: The comment of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserProfile.


        :param comment: The comment of this UserProfile.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def company(self):
        """Gets the company of this UserProfile.  # noqa: E501


        :return: The company of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UserProfile.


        :param company: The company of this UserProfile.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def company_short_name(self):
        """Gets the company_short_name of this UserProfile.  # noqa: E501


        :return: The company_short_name of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._company_short_name

    @company_short_name.setter
    def company_short_name(self, company_short_name):
        """Sets the company_short_name of this UserProfile.


        :param company_short_name: The company_short_name of this UserProfile.  # noqa: E501
        :type: str
        """

        self._company_short_name = company_short_name

    @property
    def contract(self):
        """Gets the contract of this UserProfile.  # noqa: E501


        :return: The contract of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this UserProfile.


        :param contract: The contract of this UserProfile.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def external_company(self):
        """Gets the external_company of this UserProfile.  # noqa: E501


        :return: The external_company of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._external_company

    @external_company.setter
    def external_company(self, external_company):
        """Sets the external_company of this UserProfile.


        :param external_company: The external_company of this UserProfile.  # noqa: E501
        :type: str
        """

        self._external_company = external_company

    @property
    def nav_system_access_data(self):
        """Gets the nav_system_access_data of this UserProfile.  # noqa: E501


        :return: The nav_system_access_data of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._nav_system_access_data

    @nav_system_access_data.setter
    def nav_system_access_data(self, nav_system_access_data):
        """Sets the nav_system_access_data of this UserProfile.


        :param nav_system_access_data: The nav_system_access_data of this UserProfile.  # noqa: E501
        :type: str
        """

        self._nav_system_access_data = nav_system_access_data

    @property
    def id(self):
        """Gets the id of this UserProfile.  # noqa: E501


        :return: The id of this UserProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserProfile.


        :param id: The id of this UserProfile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lang(self):
        """Gets the lang of this UserProfile.  # noqa: E501


        :return: The lang of this UserProfile.  # noqa: E501
        :rtype: UserProfileLang
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this UserProfile.


        :param lang: The lang of this UserProfile.  # noqa: E501
        :type: UserProfileLang
        """

        self._lang = lang

    @property
    def nav_system(self):
        """Gets the nav_system of this UserProfile.  # noqa: E501


        :return: The nav_system of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._nav_system

    @nav_system.setter
    def nav_system(self, nav_system):
        """Sets the nav_system of this UserProfile.


        :param nav_system: The nav_system of this UserProfile.  # noqa: E501
        :type: str
        """

        self._nav_system = nav_system

    @property
    def notify_by_email(self):
        """Gets the notify_by_email of this UserProfile.  # noqa: E501


        :return: The notify_by_email of this UserProfile.  # noqa: E501
        :rtype: bool
        """
        return self._notify_by_email

    @notify_by_email.setter
    def notify_by_email(self, notify_by_email):
        """Sets the notify_by_email of this UserProfile.


        :param notify_by_email: The notify_by_email of this UserProfile.  # noqa: E501
        :type: bool
        """

        self._notify_by_email = notify_by_email

    @property
    def notify_by_sms(self):
        """Gets the notify_by_sms of this UserProfile.  # noqa: E501


        :return: The notify_by_sms of this UserProfile.  # noqa: E501
        :rtype: bool
        """
        return self._notify_by_sms

    @notify_by_sms.setter
    def notify_by_sms(self, notify_by_sms):
        """Sets the notify_by_sms of this UserProfile.


        :param notify_by_sms: The notify_by_sms of this UserProfile.  # noqa: E501
        :type: bool
        """

        self._notify_by_sms = notify_by_sms

    @property
    def notify_timezone(self):
        """Gets the notify_timezone of this UserProfile.  # noqa: E501


        :return: The notify_timezone of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._notify_timezone

    @notify_timezone.setter
    def notify_timezone(self, notify_timezone):
        """Sets the notify_timezone of this UserProfile.


        :param notify_timezone: The notify_timezone of this UserProfile.  # noqa: E501
        :type: str
        """

        self._notify_timezone = notify_timezone

    @property
    def partner_type(self):
        """Gets the partner_type of this UserProfile.  # noqa: E501


        :return: The partner_type of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._partner_type

    @partner_type.setter
    def partner_type(self, partner_type):
        """Sets the partner_type of this UserProfile.


        :param partner_type: The partner_type of this UserProfile.  # noqa: E501
        :type: str
        """

        self._partner_type = partner_type

    @property
    def is_terms_accepted(self):
        """Gets the is_terms_accepted of this UserProfile.  # noqa: E501


        :return: The is_terms_accepted of this UserProfile.  # noqa: E501
        :rtype: bool
        """
        return self._is_terms_accepted

    @is_terms_accepted.setter
    def is_terms_accepted(self, is_terms_accepted):
        """Sets the is_terms_accepted of this UserProfile.


        :param is_terms_accepted: The is_terms_accepted of this UserProfile.  # noqa: E501
        :type: bool
        """

        self._is_terms_accepted = is_terms_accepted

    @property
    def geo_localization_settings(self):
        """Gets the geo_localization_settings of this UserProfile.  # noqa: E501


        :return: The geo_localization_settings of this UserProfile.  # noqa: E501
        :rtype: UserProfileGeoLocalizationSettings
        """
        return self._geo_localization_settings

    @geo_localization_settings.setter
    def geo_localization_settings(self, geo_localization_settings):
        """Sets the geo_localization_settings of this UserProfile.


        :param geo_localization_settings: The geo_localization_settings of this UserProfile.  # noqa: E501
        :type: UserProfileGeoLocalizationSettings
        """

        self._geo_localization_settings = geo_localization_settings

    @property
    def api_token(self):
        """Gets the api_token of this UserProfile.  # noqa: E501


        :return: The api_token of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this UserProfile.


        :param api_token: The api_token of this UserProfile.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other