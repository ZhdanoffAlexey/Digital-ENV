# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.achievement import Achievement  # noqa: F401,E501
from swagger_server import util


class Article(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, text: str=None, author: str=None, rate: str=None, number_views: str=None, _date: datetime=None, achievements: List[Achievement]=None):  # noqa: E501
        """Article - a model defined in Swagger

        :param id: The id of this Article.  # noqa: E501
        :type id: int
        :param text: The text of this Article.  # noqa: E501
        :type text: str
        :param author: The author of this Article.  # noqa: E501
        :type author: str
        :param rate: The rate of this Article.  # noqa: E501
        :type rate: str
        :param number_views: The number_views of this Article.  # noqa: E501
        :type number_views: str
        :param _date: The _date of this Article.  # noqa: E501
        :type _date: datetime
        :param achievements: The achievements of this Article.  # noqa: E501
        :type achievements: List[Achievement]
        """
        self.swagger_types = {
            'id': int,
            'text': str,
            'author': str,
            'rate': str,
            'number_views': str,
            '_date': datetime,
            'achievements': List[Achievement]
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'author': 'author',
            'rate': 'rate',
            'number_views': 'numberViews',
            '_date': 'date',
            'achievements': 'achievements'
        }

        self._id = id
        self._text = text
        self._author = author
        self._rate = rate
        self._number_views = number_views
        self.__date = _date
        self._achievements = achievements

    @classmethod
    def from_dict(cls, dikt) -> 'Article':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Article of this Article.  # noqa: E501
        :rtype: Article
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Article.


        :return: The id of this Article.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Article.


        :param id: The id of this Article.
        :type id: int
        """

        self._id = id

    @property
    def text(self) -> str:
        """Gets the text of this Article.


        :return: The text of this Article.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Article.


        :param text: The text of this Article.
        :type text: str
        """

        self._text = text

    @property
    def author(self) -> str:
        """Gets the author of this Article.

        login author  # noqa: E501

        :return: The author of this Article.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this Article.

        login author  # noqa: E501

        :param author: The author of this Article.
        :type author: str
        """

        self._author = author

    @property
    def rate(self) -> str:
        """Gets the rate of this Article.


        :return: The rate of this Article.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate: str):
        """Sets the rate of this Article.


        :param rate: The rate of this Article.
        :type rate: str
        """

        self._rate = rate

    @property
    def number_views(self) -> str:
        """Gets the number_views of this Article.


        :return: The number_views of this Article.
        :rtype: str
        """
        return self._number_views

    @number_views.setter
    def number_views(self, number_views: str):
        """Sets the number_views of this Article.


        :param number_views: The number_views of this Article.
        :type number_views: str
        """

        self._number_views = number_views

    @property
    def _date(self) -> datetime:
        """Gets the _date of this Article.


        :return: The _date of this Article.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date: datetime):
        """Sets the _date of this Article.


        :param _date: The _date of this Article.
        :type _date: datetime
        """

        self.__date = _date

    @property
    def achievements(self) -> List[Achievement]:
        """Gets the achievements of this Article.


        :return: The achievements of this Article.
        :rtype: List[Achievement]
        """
        return self._achievements

    @achievements.setter
    def achievements(self, achievements: List[Achievement]):
        """Sets the achievements of this Article.


        :param achievements: The achievements of this Article.
        :type achievements: List[Achievement]
        """

        self._achievements = achievements
