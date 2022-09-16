
class ExceptionService(Exception):
    """
    This is a general exception, it can be used from anywhere
    just by sending the correct parameters

    Params
    ------
        - success: bool
            False if the result no is as expected
        - message: str
            Service response message
        - data: dict
            Service response data
        - status_code: int
            http status code of the service
    """

    def __init__(self, success, message, data, status_code, *args):
        super(ExceptionService, self)\
            .__init__(
            success,
            "{}".format(message),
            data,
            status_code,
            *args
        )


def exception(message, value, code):

    raise ExceptionService(
        success=False,
        message=message,
        data=value,
        status_code=code
    )

