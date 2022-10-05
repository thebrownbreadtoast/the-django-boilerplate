from rest_framework.response import Response


class BaseResponse(Response):
    """Base Response class to be inherited by all Response classes."""

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ):
        super().__init__(
            data, status, template_name, headers, exception, content_type
        )


class Ok(BaseResponse):
    """200 OK

    Should be used to indicate nonspecific success. Must not be used to
    communicate errors in the response body.
    In most cases, 200 is the code the client hopes to see. It indicates that
    the REST API successfully carried out whatever action the client requested,
    and that no more specific code in the 2xx series is appropriate. Unlike
    the 204 status code, a 200 response should include a response body.
    """

    status_code = 200


class Created(BaseResponse):
    """201 Created

    Must be used to indicate successful resource creation.
    A REST API responds with the 201 status code whenever a collection creates,
    or a store adds, a new resource at the client's request. There may also be
    times when a new resource is created as a result of some controller action,
    in which case 201 would also be an appropriate response.
    """

    status_code = 201


class BadRequest(BaseResponse):
    """400 Bad Request

    May be used to indicate nonspecific failure.
    400 is the generic client-side error status, used when no other 4xx error
    code is appropriate.
    """

    status_code = 400


class Forbidden(BaseResponse):
    """403 Forbidden

    Should be used to forbid access regardless of authorization state.
    A 403 error response indicates that the client's request is formed
    correctly, but the REST API refuses to honor it. A 403 response is not a
    case of insufficient client credentials; that would be 401 ("Unauthorized").
    REST APIs use 403 to enforce application-level permissions. For example, a
    client may be authorized to interact with some, but not all of a REST API's
    resources. If the client attempts a resource interaction that is outside of
    its permitted scope, the REST API should respond with 403.
    """

    status_code = 403


class NotFound(BaseResponse):
    """404 Not Found

    Must be used when a client's URI cannot be mapped to a resource.
    The 404 error status code indicates that the REST API can't map the
    client's URI to a resource.
    """

    status_code = 404


class InternalServerError(BaseResponse):
    """500 Internal Server Error

    Should be used to indicate API malfunction.
    500 is the generic REST API error response. Most web frameworks
    automatically respond with this response status code whenever they execute
    some request handler code that raises an exception.
    A 500 error is never the client's fault and therefore it is reasonable for
    the client to retry the exact same request that triggered this response,
    and hope to get a different response.
    """

    status_code = 500


class NotImplemented(BaseResponse):
    """501 Not Implemented

    The server either does not recognise the request method, or it lacks the
    ability to fulfill the request.
    """

    status_code = 501
