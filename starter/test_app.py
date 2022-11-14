import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Employee


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):

        DATABASE_URL = os.environ['DATABASE_URL']
        HR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdZVXJJUDlSc2RrSVk5aXBwaDA1WCJ9.eyJpc3MiOiJodHRwczovL2Rldi1xaHF3LXZpeS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMxYzFjNWVjMmE3MTIzMmJjOGM2NjJlIiwiYXVkIjoiZW1wbG95ZWUiLCJpYXQiOjE2NjgzOTU2NjksImV4cCI6MTY2ODQwMjg2OSwiYXpwIjoiU21XREVJemh2ZEp4eW5QdlJCWHFoa3JJSkRLcWNmaXUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTplbXBsb3llZSIsImdldDplbXBsb3llZS1kZXRhaWxzIiwiZ2V0OmVtcGxveWVlcyIsInBhdGNoOmVtcGxveWVlIiwicG9zdDplbXBsb3llZSJdfQ.aO1Q96N1D1wXn5gR9dHZTv3LM_ZCv-N8KmIULmgWVR_oob5uM__nwVy1o3ha1iSlvKWJL_3sLyTtfNezzLeJ_5Vpu2x57DuFatVwZ9SMxO-OlAR77bqPXXWDGB1Zdr-zDdwv-bzQDmUhHHkOLtDIi2M-4vxIrrq7kAvNLm-ivyx9uKJaEx-Qd3wPnwJKaP_s169Chz7sE_dvVlDK-C39bpCIg6XIBxzhu-X4idY-1euobr6thYTu5W6fBwD4Z_aSDBLG_adIoT5dZltFDLV67g1QaiMs_Amj25Una6qjww2pjv1osd1Q4RGUzGOkNQ7EJHsfrXMbxt4EJJZeZnmqmw"
        MANAGER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdZVXJJUDlSc2RrSVk5aXBwaDA1WCJ9.eyJpc3MiOiJodHRwczovL2Rldi1xaHF3LXZpeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTEzOTAyMDY5NTI4MTU2NDMzMjAiLCJhdWQiOiJlbXBsb3llZSIsImlhdCI6MTY2ODM5NTU5NSwiZXhwIjoxNjY4NDAyNzk1LCJhenAiOiJTbVdERUl6aHZkSnh5blB2UkJYcWhrcklKREtxY2ZpdSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmVtcGxveWVlLWRldGFpbHMiLCJnZXQ6ZW1wbG95ZWVzIl19.BAAqBA5fuaEios_M1SSlmoYfMqKA4QIWN9zYs7XThXMlltouemIkan2up-pN3VmiA47Z4_T7BlPzhzReO3xPwhAX14xKLPKm6e-0fjYdNziC-_s-VqwjVZocV2wyZx_VTGGpbd4KkQ17GikQ45Pap91S-Cqb5D9RKFJZnbDRBRDjSYuNyjCusSqQjgwuVVR7PS2kw_F5qG6GkQNY2hqaTqSfdIKYQBe8rYXyhvY3kNCttoFXHhm6kwf_aK26pxyCKDVtcsRdpJsCqfoqsOGqH2fgbcz-euyodS96rpiOlPUYWzcr5lEJ5ed2ArxsJL-c2DJIpR9AWUElnX7mtOBf9g"
        self.hr_auth_header = {'Authorization': 'Bearer ' + HR_TOKEN}
        self.manager_auth_header = {'Authorization': 'Bearer ' + MANAGER_TOKEN}
        self.database_path = DATABASE_URL
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, self.database_path)


# Test data set-up for all tests down under
        self.post_employee = {
            "name": "Nitin1",
            "dob": "1988-06-28",
            "designation": "Director1",
            "address": "Rani Bagh"
            }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

# Executed after reach test
    def tearDown(self):
        pass

# Get list of employees using HR role
    def test_a_list_employees_hr(self):
        res = self.client().get('/employees', headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

# Get list of employees using Manager role
    def test_b_list_employees_manager(self):
        res = self.client().get('/employees', headers=self.manager_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

# GET employee details using HR role
    def test_c_employee_details_hr(self):
        res = self.client().get('/aemployee/1', headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

# GET employee details using Manager role
    def test_d_employee_details_manager(self):
        res = self.client().get('/aemployee/1', 
                                headers=self.manager_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)        

# POST employee - HR Role
    def test_e_post_new_employee_hr(self):
        res = self.client().post('/employee', json=self.post_employee, 
                                  headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

# POST employee - Manager Role
    def test_f_post_new_employee_manager(self):
        res = self.client().post('/employee', json=self.post_employee, 
                                  headers=self.manager_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

# DELETE employee - HR Role
    def test_g_delete_employee_hr(self):
        res = self.client().post('/employee/5',
                                 headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

# DELETE employee - HR Role - Not found
    def test_h_delete_employee_hr_not_found(self):
        res = self.client().post('/employee/999',
                                 headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

# DELETE employee - Manager Role
    def test_i_delete_employee_manager(self):
        res = self.client().delete('/employee/5',
                                   headers=self.manager_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

# PATCH employee - HR Role
    def test_j_patch_employee_hr(self):
        res = self.client().patch('/employee/5',
                                  json=self.post_employee,
                                  headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        
# PATCH employee - HR role Not Found
    def test_k_patch_employee_hr_not_found(self):
        res = self.client().patch('/employee/999',
                                  json=self.post_employee,
                                  headers=self.hr_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

# PATCH employee - Manager Role
    def test_l_patch_employee_manager(self):
        res = self.client().patch('/employee/5',
                                  json=self.post_employee,
                                  headers=self.manager_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

# run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()
