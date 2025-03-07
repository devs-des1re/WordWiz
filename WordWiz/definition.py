"""
The MIT License (MIT)

Copyright 2025 devs_des1re

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import requests

from .errors import *

def get_definitions(term: str):
    """
    Gets the definition of a term.

    Parameters
    ----------
    term :class:`str` : The term you want to get the definition for.

    Returns
    ----------
    A list of definitions.

    Raises
    ----------
    APIException :class:`errors.APIException`
        If no definitions have been found.
    """
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{term}")
    if response.status_code != 200:
        raise APIException("No definition found.")
    else:
        data = response.json()
        meanings = data[0]["meanings"]
        defintions = []
        for meaning in meanings:
            defintions.append([meaning["partOfSpeech"], meaning["definitions"][0]["definition"]])
        return defintions