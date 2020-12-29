from flask import jsonify

class APIError(Exception):
    payload = None
    message = 'Unknown API Error, do not use this error directly'

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class ConnectionPoolExhausted(APIError):
    status_code = 503
    message = 'connection pool exhausted'
