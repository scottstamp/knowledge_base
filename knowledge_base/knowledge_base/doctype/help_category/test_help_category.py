# Copyright (c) 2013, Web Notes and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Help Category')

class TestHelpCategory(unittest.TestCase):
	pass
