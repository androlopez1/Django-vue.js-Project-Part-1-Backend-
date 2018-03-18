from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone
from django.test import TestCase, RequestFactory
from.models import RiskType, RiskField
import datetime
from .views import RiskViewSet

class SimpleTest(TestCase):
    
    def test_was_published_recently_with_future_time(self):
        """
        was_published_recently() returns False for risk whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_time = RiskType(pub_date=time)
        self.assertIs(future_time.was_published_recently(), False)
       
    def setUp(self):
        """
        authentication
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='admin', email='admin@admin.com', password='britecore')
        
    def test_list(self):
        """
        unit test for risk list endpoint
        """
        view = RiskViewSet.as_view({'get': 'list'})
        request = self.factory.get('/risks/')
        
        request.user = self.user
        
        response = view(request)
        self.assertEqual(response.status_code,200)
        
    def test_risk(self):
        """
        unit test for single list endpoint
        """
        view = RiskViewSet.as_view({'get': 'list'})
        request = self.factory.get('/risks/1/')
        
        request.user = self.user
        
        response = view(request)
        self.assertEqual(response.status_code,200)
        


