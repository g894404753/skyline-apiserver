# Copyright 2021 99cloud
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ALGORITHM = "HS256"

KEYSTONE_API_VERSION = "3.13"
NOVA_API_VERSION = "2.79"
GLANCE_API_VERSION = "2"
CINDER_API_VERSION = "3.59"
NEUTRON_API_VERSION = "2.0"
PLACEMENT_API_VERSION = "1.36"

# request_id middleware will set this into openstack.global_request_id environ
INBOUND_HEADER = "X-Openstack-Request-Id"
INBOUND_HEADER_REGEX = "^req-\\w{8}(-\\w{4}){3}-\\w{12}"

ERR_MSG_TOKEN_REVOKED = "The token has revoked."
ERR_MSG_TOKEN_EXPIRED = "The token has expired."
ERR_MSG_TOKEN_NOTFOUND = "Token not found."

# prometheus
PROMETHEUS_QUERY_API = "/api/v1/query"
PROMETHEUS_QUERY_RANGE_API = "/api/v1/query_range"

# RESTful API
# neutron
NEUTRON_PORTS_API = "/v2.0/ports"

EXTENSION_API_LIMIT_GT = 0

ID_UUID_RANGE_STEP = 100

SETTINGS_HIDDEN_SET = set()
SETTINGS_RESTART_SET = set()

DEFAULT_TIMEOUT = 30
