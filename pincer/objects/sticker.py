# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2021 Pincer
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from pincer.objects.user import User
from pincer.utils.api_object import APIObject

class StickerType(Enum):
    STANDARD = 1
    GUILD = 2

class StickerFormatType(Enum):
    PNG = 1
    APNG = 2
    LOTTIE = 3

@dataclass
class Sticker(APIObject):
    id : int
    name : str
    description : str
    tags : str
    type : StickerType
    format_type : StickerFormatType

    pack_id : Optional[int] = None
    available : Optional[bool] = None
    guild_id : Optional[int] = None
    user : Optional[User] = None
    sort_value : Optional[int] = None