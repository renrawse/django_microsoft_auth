from .conf import config

app_name = "microsoft_auth"

urlpatterns = []

if config.MICROSOFT_AUTH_LOGIN_ENABLED:  # pragma: no branch
    from django.conf.urls import url
    from . import views

    urlpatterns = [
        url(
            r"auth-callback/",
            views.AuthenticateCallbackView.as_view(),
            name="auth-callback",
        ),
        url(
            r"from-auth-redirect/",
            views.AuthenticateCallbackRedirect.as_view(),
            name="from-auth-redirect",
        ),
        url(
            r"to-auth-redirect/",
            views.to_ms_redirect,
            name="to-auth-redirect",
        )
    ]
