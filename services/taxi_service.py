from models.request import Request, ReqStatus
from datetime import datetime

def ride(customer_id):
    try:
        Request(customer_id).create()
    except Exception as e:
        print e
        res = {"status": "error", "message": "Couldn't submit request for this ride."}
        return res
    res = {
        "status": "success",
        "message": "Request for the ride has been submitted successfully."
    }
    return res

def get_requests():
    from models.request import Request
    requests = Request.all()
    return map(lambda r: r.as_dict(), requests)

def get_requests_by_status(status=ReqStatus.WAITING,driver_id=None):
    filter_criteria = {
        "req_status": status
    }
    if driver_id is not None:
        filter_criteria['driver_id'] = driver_id

    requests = Request.filter(filter_criteria)
    return map(lambda r: r.as_dict(), requests)

def serve_request(driver_id, request_id):
    try:
        updated_args = {
            "req_status": ReqStatus.ONGOING,
            "driver_id": driver_id,
            "picked_up": datetime.utcnow()
        }
        request = Request.filter_and_update(filter_args={"id": request_id}, updated_args=updated_args)
    except Exception as e:
        print e
        res = {"status": "error", "message": "Couldn't serve request."}
        return res
    res = {
        "status": "success",
        "message": "Accepted request successfully."
    }
    return res


