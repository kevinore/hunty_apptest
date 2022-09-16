def response_format(response: dict):
    """
    General format for all api responses

    Params
    ------
        response: dict
            - success: bool
                True if the result is as expected
            - message: str
                Service response message
            - data: dict
                Service response data
    """
    return {
        "success": response.get('success'),
        "message": response.get('message'),
        "data": response.get('data'),
    }
