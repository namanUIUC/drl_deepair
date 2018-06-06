# Copyright 2018 Deep Air. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""main function"""

from utils.json_flatter import flat_json


def main():
    flat_json('flat.json', ['JSON_ep1/AvailabilityRequest.txt', 'JSON_ep1/AvailabilityResponse.txt', 'JSON_ep1/BookingPaymentEvent.txt'])


if __name__ == "__main__":
    main()
