import http from "k6/http";
import { Rate } from "k6/metrics";
import { check } from "k6";

const failedRequests = new Rate("failed_requests");
const connectionPoolFailedRequests = new Rate("failed_request_conn_pool");

export default function () {
  const response = http.get("http://localhost:3000/users");
  let resJson;
  try {
    resJson = response.json();
  } catch (e) {}
  check(response, {
    "is status 200": (r) => r.status === 200,
  });
  check(resJson, {
    "is body correct": (r) => {
      return (
        Array.isArray(r) &&
        (r.length === 10) & (typeof r[0]["first_name"] === "string")
      );
    },
  });
  failedRequests.add(response.status !== 200);
  connectionPoolFailedRequests.add(response.status === 503);
}
