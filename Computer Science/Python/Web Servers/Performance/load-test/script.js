import http from "k6/http";

export default function() {
    const response = http.get("http://localhost:3000/v2")

    if (response.status !== 200) {
        console.error(response.body)
    }
}
