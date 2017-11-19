from callisto_core.notification import api as notification_api
from callisto_core.notification.api import CallistoCoreNotificationApi
from callisto_core.reporting import api as reporting_api
from callisto_core.reporting.api import CallistoCoreMatchingApi


class SiteAwareNotificationApi(
    notification_api.CallistoCoreNotificationApi,
):

    @property
    def Site(_):
        from django.contrib.sites.models import Site
        return Site

    def user_site_id(self, user):
        self.Site.objects.filter(id=1).update(domain='testserver')
        return 1


class CustomNotificationApi(SiteAwareNotificationApi):

    def send_email(self):
        pass  # disable sending

    def log_action(self):
        super().log_action()
        for key, value in self.context.items():
            self._logging(**{key: value})

    def _logging(self, *args, **kwargs):
        pass  # for testing inputs


class CustomMatchingApi(
    reporting_api.CallistoCoreMatchingApi,
):
    pass
