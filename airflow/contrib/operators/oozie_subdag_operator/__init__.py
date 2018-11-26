# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import glob

from airflow.operators.subdag_operator import SubDagOperator


class OozieSubDagOperator(SubDagOperator):
    """
    Parse and run an Oozie workflow as a sub dag.

    :param config: path to an Oozie job properties file.
    :type config: file.
    """

    schemas = []

    def __init__(
            self,
            config,
            *args, **kwargs):
        super(OozieSubDagOperator, self).__init__(**kwargs)
        import xmlschema
        dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'xsd', '*.xsd')
        schemas = [xmlschema.XMLSchema(f) for f in glob.glob(dir_path)]
