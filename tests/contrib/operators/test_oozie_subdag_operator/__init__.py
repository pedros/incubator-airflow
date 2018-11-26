import unittest

from airflow.models import DAG
from airflow.contrib.operators.oozie_subdag_operator import OozieSubDagOperator


TASK_ID = 'oozie-subdag-operator'


class OozieSubDagOperatorTest(unittest.TestCase):
    def test_init_with_xsd_loading(self):
        """
        Test the initializer with XMLSchema loads.
        """
        op = OozieSubDagOperator(config='asd', dag=DAG())

        expected = []

        self.assertCountEqual(expected, op.schemas)
