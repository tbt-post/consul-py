# Consul agent client for python

# Usage with tornado

```
    from tornado.ioloop import PeriodicCallback
    from consul.agent import ConsulAgent, HTTPError

    agent = ConsulAgent()
    try:
        agent.check_update_with_register(
            'backend_ttl_check',
            id='backend',
            port=8081,
            checks=[
                {
                    'CheckId': 'backend_ttl_check',
                    'TTL': '15s',
                    'DeregisterCriticalServiceAfter': '5m',
                },
                {
                    'Args': ['curl', 'localhost:8081/api/v1'],
                    'Interval': '10s',
                }
            ],
        )
    except HTTPError, e:
        from tornado.log import app_log as log
        log.error("failed to heartbeat to consul:", "%s %s" % (
            e.response.status_code, e.response.content) if e.response.content else unicode(e))
```
