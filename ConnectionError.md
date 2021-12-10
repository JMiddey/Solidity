# Solidity
Traceback (most recent call last):
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/util/connection.py", line 96, in create_connection
    raise err
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/util/connection.py", line 86, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 61] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connectionpool.py", line 394, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/http/client.py", line 1282, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/http/client.py", line 1328, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/http/client.py", line 1277, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/http/client.py", line 1037, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/http/client.py", line 975, in send
    self.connect()
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connection.py", line 205, in connect
    conn = self._new_conn()
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x1053ad5a0>: Failed to establish a new connection: [Errno 61] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/urllib3/util/retry.py", line 574, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=8545): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x1053ad5a0>: Failed to establish a new connection: [Errno 61] Connection refused'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/joe/demos/web3_py_simple_storage/deploy.py", line 63, in <module>
    nonce = w3.eth.getTransactionCount(my_address)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/module.py", line 57, in caller
    result = w3.manager.request_blocking(method_str,
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/manager.py", line 197, in request_blocking
    response = self._make_request(method, params)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/manager.py", line 150, in _make_request
    return request_func(method, params)
  File "cytoolz/functoolz.pyx", line 250, in cytoolz.functoolz.curry.__call__
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/formatting.py", line 76, in apply_formatters
    response = make_request(method, params)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/gas_price_strategy.py", line 90, in middleware
    return make_request(method, params)
  File "cytoolz/functoolz.pyx", line 250, in cytoolz.functoolz.curry.__call__
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/formatting.py", line 74, in apply_formatters
    response = make_request(method, formatted_params)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/attrdict.py", line 33, in middleware
    response = make_request(method, params)
  File "cytoolz/functoolz.pyx", line 250, in cytoolz.functoolz.curry.__call__
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/formatting.py", line 74, in apply_formatters
    response = make_request(method, formatted_params)
  File "cytoolz/functoolz.pyx", line 250, in cytoolz.functoolz.curry.__call__
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/formatting.py", line 76, in apply_formatters
    response = make_request(method, params)
  File "cytoolz/functoolz.pyx", line 250, in cytoolz.functoolz.curry.__call__
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/formatting.py", line 74, in apply_formatters
    response = make_request(method, formatted_params)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/buffered_gas_estimate.py", line 40, in middleware
    return make_request(method, params)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/middleware/exception_retry_request.py", line 105, in middleware
    return make_request(method, params)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/providers/rpc.py", line 88, in make_request
    raw_response = make_post_request(
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/web3/_utils/request.py", line 48, in make_post_request
    response = session.post(endpoint_uri, data=data, *args, **kwargs)  # type: ignore
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/requests/sessions.py", line 590, in post
    return self.request('POST', url, data=data, json=json, **kwargs)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/Users/joe/demos/web3_py_simple_storage/new-env/lib/python3.10/site-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=8545): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x1053ad5a0>: Failed to establish a new connection: [Errno 61] Connection refused'))
