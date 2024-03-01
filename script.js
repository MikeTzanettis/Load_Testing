import { check } from "k6";
import http from "k6/http";
const customRate = __ENV.RATE || 3000;
const customPreAllocatedVUs = __ENV.PRE_ALLOCATED_VUS || 500;
const duration = __ENV.DURATION || '600s'

export const options = {
    scenarios: {
      constant_request_rate: {
        executor: 'constant-arrival-rate',
        rate: `${customRate}`,
        timeUnit: '1s', // 1000 iterations per second, i.e. 1000 RPS
        duration: `${duration}`,
        preAllocatedVUs: `${customPreAllocatedVUs}`, // how large the initial pool of VUs would be
      },
    },
  };

  
export default function() {
  let res = http.get("http://192.168.49.2:30006/gateway-service",{ timeout: '100s' });
  check(res, {
    "is status 200": (r) => r.status === 200
  });
};