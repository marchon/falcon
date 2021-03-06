"""Falcon is a fast micro-framework for building cloud APIs.

Copyright 2013 by Rackspace Hosting, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

# Hoist classes and functions into the falcon namespace
from falcon.version import version
from falcon.api import API, DEFAULT_MEDIA_TYPE
from falcon.status_codes import *
from falcon.exceptions import *
from falcon.http_error import HTTPError
from falcon.util import dt_to_http
