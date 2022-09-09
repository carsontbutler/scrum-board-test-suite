import requests
import pytest
import logging
import time

# Logging setup
timestr = time.strftime("%Y-%m-%d_%H%M%S")
log = logging.getLogger(__name__)
logging.basicConfig(filename=timestr, encoding='utf-8',
                    level=logging.DEBUG, format='%(asctime)s %(message)s')

# Configuration
# base_url = 'http://localhost:8000/api'
base_url = 'scrum-api.carsonbutler.dev'
username = 'test_user'
password = 'password321'

# Define the data for tests
organization_data = {'name': 'Test API Organization'}
board_data = {'name': 'Test Board 1', 'prefix': 'BRD1'}
column_data = [{'name': 'TestCol1', 'position': 0},
               {'name': 'TestCol2', 'position': 1},
               {'name': 'TestCol3', 'position': 2}]

ticket_data = [{'title': 'Test Ticket 1',
                'description': 'This is a description for Test Ticket 1',
                'repro_steps': 'These are the repro_steps for Test Ticket 1',
                'acceptance_criteria': 'This is the acceptance criteria for Test Ticket 1',
                'type': 'Bug',
                'priority': 'Low'},

               {'title': 'Test Ticket 2',
                'description': 'This is a description for Test Ticket 2',
                'repro_steps': 'These are the repro_steps for Test Ticket 2',
                'acceptance_criteria': 'This is the acceptance criteria for Test Ticket 2',
                'type': 'Improvement',
                'priority': 'Medium'},

               {'title': 'Test Ticket 3',
                'description': 'This is a description for Test Ticket 3',
                'repro_steps': 'These are the repro_steps for Test Ticket 3',
                'acceptance_criteria': 'This is the acceptance criteria for Test Ticket 3',
                'type': 'Task',
                'priority': 'High'}]

test_data = {'organization': organization_data,
             'board': board_data,
             'columns': column_data,
             'tickets': ticket_data}

#Updated variables
new_org_name = 'Organization New Name'
new_board_name = 'Board New Name'
new_board_prefix = 'PFX1'

@pytest.fixture(scope="class")
def token():
    r = requests.post(f'{base_url}/token/',
                        data={'username': username, 'password': password})
    _token = r.json()['access']
    yield _token

@pytest.fixture(scope="class")
def req_headers(token):
    _req_headers = {'Authorization': f'Bearer {token}'}
    yield _req_headers



class API():
    def register():
        r = requests.post(f'{base_url}/register/', data={'username': username,
                          'password': password, 'password2': password})

    def login():
        r = requests.post(f'{base_url}/token/',
                          data={'username': username, 'password': password})
        return r.json()['access']

    def create_organization(self, req_headers):
        r = requests.post(f'{base_url}/create-organization/',
                          data=test_data['organization'], headers=req_headers)
        if r.status_code == 200:
            org_id = r.json()['id']
            test_data['organization']['id'] = org_id
            test_data['board']['organization'] = org_id
            for i in range(len(test_data['tickets'])):
                test_data['tickets'][i]['organization'] = org_id
            print('create_organization ', r.status_code)
            return True
        else:
            print('create_organization ', r.status_code)
            return False

    def rename_organization(self, req_headers):
        org_id = test_data['organization']['id']
        req_data = {'name': new_org_name}
        r = requests.patch(f'{base_url}/organization/{org_id}/rename/', data=req_data, headers=req_headers)
        if r.status_code == 200:
            res = r.json()
            if res['organization']['name'] == new_org_name:
                return True
            else:
                return False
        else:
            return False

    def create_board(self, req_headers):
        r = requests.post(f'{base_url}/create-board/',
                          data=test_data['board'], headers=req_headers)
        if r.status_code == 200:
            board_id = r.json()['id']
            test_data['board']['board_id'] = board_id
            for i in range(len(test_data['columns'])):
                test_data['columns'][i]['board'] = board_id
            for i in range(len(test_data['tickets'])):
                test_data['tickets'][i]['board'] = board_id
            print('create_board ', r.status_code)
            return True
        else:
            return False

    def update_board(self, req_headers):
        board_id = test_data['board']['board_id']
        req_data = {'name': new_board_name, 'prefix': new_board_prefix}
        r = requests.patch(f'{base_url}/board/{board_id}/update/', data=req_data, headers=req_headers)
        if r.status_code == 200:
            res = r.json()
            if res['board']['name'] == new_board_name and res['board']['prefix'] == new_board_prefix:
                return True
        else:
            return False

    def create_columns(self, req_headers):
        try:
            for i in range(len(test_data['columns'])):
                r = requests.post(f'{base_url}/column/create/',
                                  data=test_data['columns'][i], headers=req_headers)
                if r.status_code == 200:
                    col_id = r.json()['id']
                    test_data['columns'][i] = r.json()
                    test_data['tickets'][i]['column'] = col_id
                    print('created column ', r.json()['id'])
            return True
        except:
            return False

    def create_tickets(self, req_headers):
        try:
            for i in range(len(test_data['tickets'])):
                r = requests.post(f'{base_url}/create-ticket/',
                                  data=test_data['tickets'][i], headers=req_headers)

                if r.status_code == 200:
                    print('created ticket ', r.json()['id'])
                    test_data['tickets'][i] = r.json()
            return True
        except:
            return False

    def cleanup(self, req_headers):
        try:
            org_id = test_data['organization']['id']
            r = requests.delete(
                f'{base_url}/organization/{org_id}/delete/', headers=req_headers)
            return True
        except:
            return False

class TestAPI():
    def test_create_organization(self, req_headers):
        assert API.create_organization(self, req_headers) == True
    def test_create_board(self, req_headers):
        assert API.create_board(self, req_headers) == True
    def test_create_columns(self, req_headers):
        assert API.create_columns(self, req_headers) == True
    def test_create_tickets(self, req_headers):
        assert API.create_tickets(self, req_headers) == True
    def test_rename_organization(self, req_headers):
        assert API.rename_organization(self, req_headers) == True
    def test_update_board(self, req_headers):
        assert API.update_board(self, req_headers) == True
    def test_cleanup(self, req_headers):
        assert API.cleanup(self, req_headers) == True
        

    # #Users
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterUserView.as_view()),

    # #Organizations
    # path('organizations/', GetOrganizations.as_view()),
    # path('organization/remove-member/', RemoveMemberView.as_view()),
    # path('organization/<str:pk>/delete/', DeleteOrganizationView.as_view()),

    # #Boards
    # path('boards/', GetBoards.as_view()),
    # path('board/<str:pk>/', GetBoard.as_view()), #! is this needed?
    # path('board/<str:pk>/tickets/', GetTickets.as_view()),

    # path('board/<str:pk>/update/', UpdateBoardView.as_view()),
    # path('board/<str:pk>/delete/', DeleteBoardView.as_view()),

    # #Columns
    # path('column/<str:pk>/delete/', DeleteColumnView.as_view()),
    # path('column/<str:pk>/update/', UpdateColumnView.as_view()),
    # path('column/create/', CreateColumnView.as_view()),

    # #Tickets
    # path('create-ticket/', CreateTicketView.as_view()),
    # path('ticket/<str:pk>/update/', UpdateTicket.as_view()),
    # path('ticket/<str:pk>/delete/', DeleteTicketView.as_view()),

    # #JoinRequests
    # path('requests/send/', SendJoinRequestView.as_view()),
    # path('requests/<str:pk>/approve/', ApproveJoinRequestView.as_view()),
    # path('requests/<str:pk>/deny/', DenyJoinRequestView.as_view()),
    # path('get-join-requests/', GetJoinRequestsView.as_view()),