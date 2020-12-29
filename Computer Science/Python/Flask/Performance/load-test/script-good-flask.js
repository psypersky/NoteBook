import http from "k6/http";
import { Rate } from "k6/metrics";

const failedRequests = new Rate("failed_requests");

export default function () {
  const response = http.get("http://localhost:3000/users");

  failedRequests.add(response.status !== 200);
}
